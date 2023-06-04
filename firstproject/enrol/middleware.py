from django.shortcuts import HttpResponse,render
class My_middleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        response = render(request,'enrol/site.html')
        return response