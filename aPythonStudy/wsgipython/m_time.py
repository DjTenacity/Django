# coding:utf-8
import time


def say_time():
    return time.ctime()


def fun_a():
    pass


def application(env, start_response):
    status = "200 OK"
    header = [
        ("Content-Type", "text/plain")
    ]

    start_response(status, header)
    return time.ctime()
