#!/bin/bash
# 1. run json_decoder
# 2. runt caffe test / train
# 3. parse test / train output
# 4. send request

if [ "$1" == "prepare" ]; then
	echo "preparing model"
	python /Users/Wei/caffe/json_parser/JSONDecoder.py -c test -i $2 -o $3

elif [ "$1" == "train" ]; then
	echo "training"
	python /Users/Wei/caffe/json_parser/JSONDecoder.py -c $1 -i $2 -o $3 -t $4
	/Users/Wei/caffe/build/tools/caffe $1 --solver=$3
else
	echo "testing"
	python /Users/Wei/caffe/json_parser/JSONDecoder.py -c $1 -i $2 -o $3
	/Users/Wei/caffe/build/tools/caffe $1 -model $3 -weights $4 
fi