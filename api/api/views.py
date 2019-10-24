from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.
header = {"Content-type": "application/json"}

def index(request):
    return render(request,'index.html',{"context":"some error occured"})


def get_view(request):
    if request.method=='POST':
        url=request.POST['_method']
        print(url)
        r = requests.get(url, headers=header)
        print(r.text)
        return render(request,'showresult.html',{"context":r.text})
    else:
        return render(request,'showresult.html',{"context":"some error occured"})


def put_view(request):
    if request.method=='POST':
        url=request.POST['_method']
        data=request.POST['data']
        data=json.loads(data)
        print(url)
        print(data)
        r = requests.put(url, data=json.dumps(data), headers=header)
        return render(request,'showresult.html',{"context":"requested data is updated at api server"})
    else:
        return render(request,'showresult.html',{"context":"some error occured"})

def delete_view(request):
    if request.method=='POST':
        url=request.POST['_method']
        print(url)
        r = requests.delete(url, headers=header)
        print(r.text,r.content)
        return render(request,'showresult.html',{"context":"requested data will be deleted from the api server"})
    else:
        return render(request,'showresult.html',{"context":"some error occured"})

def post_view(request):
    if request.method=='POST':
        url=request.POST['_method']
        data=request.POST['data']
        data=json.loads(data)
        print(type(data))
        print(url,"==",data)
        r = requests.post(url, data=json.dumps(data), headers=header)
        print(r.text)
        return render(request,'showresult.html',{"context":"data send to api and will be saved at api server"})
    else:
        return render(request,'showresult.html',{"context":"some error occured"})
