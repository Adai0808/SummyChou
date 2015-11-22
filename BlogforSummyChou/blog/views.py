from django.shortcuts import render

# Create your views here.


def blog_content(request):
    return render(request, "blog_content.html")
