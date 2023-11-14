from django.shortcuts import render, redirect


def home(request):
    return render(request, 'base/home.html')

def base(request):
    return render(request, 'base/base.html')