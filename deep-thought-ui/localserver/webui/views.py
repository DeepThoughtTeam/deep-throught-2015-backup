from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from models import *
from .forms import DocumentForm
import os, subprocess


def home(request):
    # return render(request, 'homepage.html')
    return render(request, 'beautiful_page.html')


@csrf_exempt
def caffe_train_result(request):
    if request.method == 'POST':
        try:
            json_object = json.loads(request.body)
        except ValueError, e:
            return HttpResponse('Json parse failed')
        with open('caffe_train_result.json', 'wb+') as destination:
            destination.write(request.body)
        return HttpResponse(request.body)
    if request.method == 'GET':
        with open('caffe_train_result.json', 'r') as myfile:
            data = json.load(myfile)
        return JsonResponse(data)


@csrf_exempt
def caffe_test_result(request):
    if request.method == 'POST':
        try:
            json_object = json.loads(request.body)
        except ValueError, e:
            return HttpResponse('Json parse failed')
        with open('caffe_test_result.json', 'wb+') as destination:
            destination.write(request.body)
        return HttpResponse(request.body)
    if request.method == 'GET':
        with open('caffe_test_result.json', 'r') as myfile:
            data = json.load(myfile)
        return JsonResponse(data)


def show_train_result(request):
    if request.method == 'GET':
        return render(request, 'display-train-result.html')


def show_test_result(request):
    if request.method == 'GET':
        return render(request, 'display-test-result.html')

@csrf_exempt
def net_description(request):
    if request.method == 'GET':
        with open('upload/' + 'mlp_train_test.json', 'r') as myfile:
            data = json.load(myfile)
        return JsonResponse(data)
    if request.method == 'POST':
        try:
            json_object = json.loads(request.body)
        except ValueError, e:
            return HttpResponse('Json parse failed')
        with open('upload/' + 'mlp_train_test.json', 'wb+') as destination:
            destination.write(request.body)
        return HttpResponse(request.body)


@csrf_exempt
def upload_file(request):
    if request.method == 'GET':
        return render(request, 'checkbox.html')

    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")

    return HttpResponse("Failed")


def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    subprocess.call(['python','/Users/Wei/caffe/run2out.py', '-m', 'prepare', '-j', '/Users/Wei/workspace/deep-thought-ui/localserver/upload/mlp_train_test.json'])
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


def display_net(request):
    if request.method == 'GET':
        return render(request, 'friday.html')


def beautiful_home(request):
    return render(request, 'beautiful_page.html')


def train(request):
    p = subprocess.Popen(['python', '/Users/Wei/caffe/run2out.py', '-m', 'train', '-j', '/Users/Wei/workspace/deep-thought-ui/localserver/upload/mlp_solver.json', '-r', '5000'])
    while subprocess.Popen.poll(p) == None:
        subprocess.Popen.wait(p)
    return HttpResponse("Successful")

def test(request):
    # Function for test
    p = subprocess.Popen(['python', '/Users/Wei/caffe/run2out.py', '-m', 'test', '-j', '/Users/Wei/workspace/deep-thought-ui/localserver/upload/mlp_train_test.json', '-r', '/Users/Wei/caffe/json_parser/mlp_models/mlp_iter_5000.caffemodel'])
    return HttpResponse("Successful")

