from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'enrol/home.html')

def about(request):
    return render(request,'enrol/about.html')

def site(request):
    return render(request,'enrol/site.html')