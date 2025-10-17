from django.shortcuts import render,HttpResponse

# Create your views here.


def students(request):

    students = [
        {'id':1, 'name':'pratts','age':'20'}
    ]

    
    return HttpResponse (students)