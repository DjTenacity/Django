import time
from celery import task

@task
def sayhello():
    print('hello ...')
    time.sleep(5)
    print('world ...')