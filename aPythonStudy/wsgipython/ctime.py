# coding:utf-8

import time

# "/ctime.py?timezone=e8"
# "/ctime.py?timezone=e1"


def application(env, start_response):

    # env.get("Method")
    # env.get("PATH_INFO")
    # env.get("QUERY_STRING")

    status = "200 OK"

    headers = [
        ("Content-Type", "text/plain")
    ]

    start_response(status, headers)

    return time.ctime()







