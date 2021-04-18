from django.shortcuts import render
from django.http import HttpResponse

# Create your views her
def dummy(request):
    akhil = ({'num1':100,'num2':200})
    return render(request,'dummy.html',akhil)