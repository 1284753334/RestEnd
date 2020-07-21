from time import sleep

from App.celerymy import Celery

app = Celery('tasks',broker='redis://localhost:6379/1',
             backend='redis://localhost:6379/1',
             )

@app.task
def add(a,b):
    #  模拟程序需要很长的时间
    sleep(5)
    return a + b

if __name__ == '__main__':
    # print(add(2,3))
    print(add.delay(4,6))









