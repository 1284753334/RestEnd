from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from sendemail.tasks import add, send_email


def index(request):
    result = add(5,6)
    return HttpResponse(result)


def asyn(request):
    result = add.delay(6, 8)
    return HttpResponse(result)


def email(request):
    mail_address= request.GET.get('address')
    sen_result=send_email.delay(mail_address)
    return HttpResponse(sen_result)


def home(request):
    return HttpResponse('我很厉害')