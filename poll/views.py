from django.shortcuts import render
from django.shortcuts import redirect
from .forms import CreatePollForm

def home(request):
    context = {}
    return render(request, 'home.html', context)

def create(request):
    form = CreatePollForm()  # Initialize form here

    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect inside the if block

    context = {'form': form}
    return render(request, 'create.html', context)

def results(request):
    context = {}
    return render(request, 'results.html', context)

def vote(request):
    context = {}
    return render(request, 'vote.html', context)
