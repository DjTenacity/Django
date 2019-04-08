##HttpReqeust对象
* 服务器接收到http协议的请求后，会根据报文创建HttpRequest对象
* 视图函数的第一个参数是HttpRequest对象
* 在django.http模块中定义了HttpRequest对象的API
###属性
* 下面除非特别说明，*属性都是只读的*
* path：一个字符串，表示请求的页面的完整路径，不包含域名
* method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'
* encoding：一个字符串，表示提交的数据的编码方式
    * 如果为None则表示使用浏览器的默认设置，一般为utf-8
    * 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值
* GET：一个类似于字典的对象，包含get请求方式的所有参数
* POST：一个类似于字典的对象，包含post请求方式的所有参数
* FILES：一个类似于字典的对象，包含所有的上传文件
* COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串
* session：一个既可读又可写的类似于字典的对象，表示当前的会话，只有当Django 启用会话的支持时才可用，详细内容见“状态保持”
###方法
* is_ajax()：如果请求是通过XMLHttpRequest发起的，则返回True

##QueryDict对象
* 定义在django.http.QueryDict
* request对象的属性GET、POST都是QueryDict类型的对象
* 与python字典不同，QueryDict类型的对象用来处理 _同一个键带有多个值_ 的情况
* 方法get()：根据键获取值
    * 只能获取键的一个值
    * 如果一个键同时拥有多个值，获取最后一个值
`dict.get('键',default)
或简写为
dict['键']`
* 方法getlist()：根据键获取值
    * 将键的值以列表返回，可以获取一个键的多个值
`dict.getlist('键',default)`