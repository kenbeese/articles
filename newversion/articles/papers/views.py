from django.shortcuts import render

# Create your views here.
def toppage(request):
    d={}
    return render(request, "top.html", d)
