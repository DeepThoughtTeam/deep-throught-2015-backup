# pipe command line output of run_test.sh to file and send to server as json
import subprocess
import sys, getopt, os
import json
import requests
import output_util as util

def main(argv):
	mode = ''
	jsonf = ''
	prototxtf = ''
	more = ''
	dic = {}
	TEMP_TXT = 'temp.txt'
	TRAIN_TEST_PTXT = '/Users/Wei/caffe/json_parser/mlp_train_test.prototxt'
	SOLVER_PTXT = '/Users/Wei/caffe/json_parser/mlp_solver.prototxt'

	try:
		opts, args = getopt.getopt(argv,"hm:o:j:p:r:",["mode=","output=","jsonf=","more="])
	except getopt.GetoptError:
		print 'run2out.py -m <mode> -j <jsonf> -r <more>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'run2out.py -m <mode> -j <jsonf> -r <more>'
			sys.exit()
		elif opt in ("-m","-mode"):
			mode = arg
		elif opt in ("-j", "--jsonf"):
			jsonf = arg
		elif opt in ("-r", "--more"):
			more = arg
	
	if mode == 'prepare':
		prototxtf = TRAIN_TEST_PTXT
		subprocess.call(['/bin/sh','/Users/Wei/caffe/run_test.sh', 'prepare', jsonf, prototxtf])
	else:
		if mode == 'train': 
			prototxtf = SOLVER_PTXT
			with open(TEMP_TXT, 'w') as f:
				p = subprocess.Popen(['/bin/sh','/Users/Wei/caffe/run_test.sh', 'train', jsonf, prototxtf, more], stdout=f, stderr=f)
			while subprocess.Popen.poll(p) == None:
				subprocess.Popen.wait(p)
			util.trainToJson(TEMP_TXT, dic)
		else:
			prototxtf = TRAIN_TEST_PTXT
			with open(TEMP_TXT, 'w') as f:
				p = subprocess.Popen(['/bin/sh','/Users/Wei/caffe/run_test.sh', 'test', jsonf, prototxtf, more], stdout=f, stderr=f)
			while subprocess.Popen.poll(p) == None:
				subprocess.Popen.wait(p)
			util.testToJson(TEMP_TXT, dic)

	if mode == 'prepare':
		with open(jsonf) as f:
			net_data = json.load(f)
		r = requests.post("http://127.0.0.1:8000/webui/net-description/", json = net_data)
		
	else:
		# os.remove(TEMP_TXT)
		if mode == 'train':
			r = requests.post("http://127.0.0.1:8000/webui/caffe-train-result/", json = dic)

		if mode == 'test':
			r = requests.post("http://127.0.0.1:8000/webui/caffe-test-result/", json = dic)


if __name__ == "__main__":
	main(sys.argv[1:])
