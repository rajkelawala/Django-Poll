from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'home.html', context)

def create(request):
    context = {}
    return render(request, 'create.html', context)

def results(request):
    context = {}
    return render(request, 'results.html', context)

def vote(request):
    context = {}
    return render(request, 'vote.html', context)
