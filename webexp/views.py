from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    n = 'oleg'
    return render(request, 'blog/index.html', context ={'name':n})
