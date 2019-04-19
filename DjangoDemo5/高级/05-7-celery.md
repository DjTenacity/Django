###celery
* [官方网站](http://www.celeryproject.org/)
* [中文文档](http://docs.jinkan.org/docs/celery/)
* 示例一：用户发起request，并等待response返回。在本些views中，可能需要执行一段耗时的程序，那么用户就会等待很长时间，造成不好的用户体验
* 示例二：网站每小时需要同步一次天气预报信息，但是http是请求触发的，难道要一小时请求一次吗？
* 使用celery后，情况就不一样了
* 示例一的解决：将耗时的程序放到celery中执行
* 示例二的解决：使用celery定时执行
####名词
* 任务task：就是一个Python函数
* 队列queue：将需要执行的任务加入到队列中
* 工人worker：在一个新进程中，负责执行队列中的任务
* 代理人broker：负责调度，在布置环境中使用redis
####使用
* 安装包
```celery==3.1.25
celery-with-redis==3.0
django-celery==3.1.17
```
* 配置settings
```INSTALLED_APPS = (
  ...
  'djcelery',
}

...

import djcelery
djcelery.setup_loader()
BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_IMPORTS = ('应用名称.task')
在应用目录下创建task.py文件
import time
from celery import task

@task
def sayhello():
    print('hello ...')
    time.sleep(2)
    print('world ...')
```
* 迁移，生成celery需要的数据表
`python manage.py migrate`
* 启动Redis
`sudo redis-server /etc/redis/redis.conf`
* 启动worker
`python manage.py celery worker --loglevel=info`
* 调用语法
`function.delay(parameters)`
* 使用代码
```#from task import *

def sayhello(request):
    print('hello ...')
    import time
    time.sleep(10)
    print('world ...')

    # sayhello.delay()

    return HttpResponse("hello world")
```