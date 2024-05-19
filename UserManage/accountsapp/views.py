from django.shortcuts import render
from django.http import HttpResponse



def hello(request):
    return HttpResponse("hai")

def user_login(request):
    return render(request,'userlogin.html')


def user_signup(request):
    return render(request,'usersignup.html')