from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
  return render(request,"home.html")
def about(request):
  return HttpResponse("Hello Iam About Page")
def contact(request):
  return render(request,"contact.html")
def details(request):
  return HttpResponse("hello Iam Detail Page")
def thanx(request):
  return render(request,"thanx.html")