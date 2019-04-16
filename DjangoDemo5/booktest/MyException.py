from django.http import HttpResponse


class MyException():
    # @staticmethod
    def process_exception(response, exception):
        return HttpResponse('sorry哦 , ' + exception.message)
