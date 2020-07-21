from time import sleep

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def add(a,b):
    print('不在状态')
    sleep(5)

    return a + b


@shared_task
def send_email(receiver):
    subject = '关于公司人事调动的决定'
    message = '是的'
    from_email = '1284753334@qq.com'
    recipient_list = [receiver]
    send_mail(subject,from_email,message,recipient_list)




