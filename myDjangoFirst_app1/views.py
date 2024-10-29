
from django.shortcuts import HttpResponse,render
from .models import Student
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("Welcome to Django Training at CareerBridge")

def index(request):
    our_dict={'insert_myDjangoFirst':"welcome to Django training institute in kphb"}
    return render(request,'myDjangoFirst_app1/index.html',context=our_dict)

def student_table(request):
    Students=Student.objects.all()
    return render((request,'myDjangoFirst_app1/student_table.html'),{'students':Students})