import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import sys
import caffe

caffe.set_mode_cpu()
net = caffe.Net('examples/mnist/lenet.prototxt', 
				'examples/mnist/lenet_iter_500.caffemodel',
				caffe.TEST)

# # params: 
# # ['conv1', 'conv2', 'ip1', 'ip2']
# # print net.params.keys()
# cur_data = net.params['conv2'][0].data
# num_to_plot = 36

# row = int(np.sqrt(num_to_plot))
# col = int(np.ceil(num_to_plot*1./row))
# for i in xrange(num_to_plot):
# 	ax = plt.subplot(row,col,i+1)
# 	ax.yaxis.set_visible(False)
# 	ax.xaxis.set_visible(False)
# 	plt.imshow(cur_data[i,0])
# plt.show()

# blobs:
# print net.blobs.keys()
# ['data', 'conv1', 'pool1', 'conv2', 'pool2', 'ip1', 'ip2', 'prob']
# load an imag
img_id = 'data/mnist/sample_data/sample2.jpg'
layer = net.blobs.keys()[1]
im2 = caffe.io.load_image(img_id, color=False) #(360, 480, 3)
im = im2[:,:,0:1]
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,1,0))
transformer.set_raw_scale('data', 255.0)
net.blobs['data'].data[...] = transformer.preprocess('data', im)
out = net.forward()
feature = net.blobs[layer].data
num_to_plot = 36
row = int(np.sqrt(num_to_plot))
col = int(np.ceil(num_to_plot*1./row))
for i in xrange(num_to_plot):
	ax = plt.subplot(row, col, i+1)
	ax.yaxis.set_visible(False)
	ax.xaxis.set_visible(False)
	plt.imshow(feature[i/col, i%col].T)
plt.show()


