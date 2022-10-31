from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from .models import book


# Create your views here.
def index(request):
     return HttpResponse("My Index")

def indexdb(request):
      Books = book.objects.all()
      return render(request, "MyPage/index.html", {"Books" : Books})

def book_detail(request):
     Books = book.objects.all()
     return render(request, "MyPage/book_detail.html", {"Books" : Books})

def task(request):
     task_path = f"<li> <a href = \"/taskDetails\">My Task</a></li>"
     return HttpResponse(task_path)

def taskDetails(request):
     return HttpResponse("Learn Django for 20 mins every day!")