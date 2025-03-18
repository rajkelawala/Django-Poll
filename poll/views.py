from django.shortcuts import render, redirect
from .forms import CreatePollForm
from .models import Poll
from django.http import HttpResponse


def home(request):
    polls = Poll.objects.all()
    context = {'polls': polls}
    return render(request, 'home.html', context)


def create(request):
    form = CreatePollForm()
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'create.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {'poll': poll}
    return render(request, 'results.html', context)  # ✅ Fixed infinite redirect


def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':
        selected_option = request.POST.get('poll')  # ✅ Fix KeyError issue
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse("Invalid form option", status=400)  # ✅ Fix error handling

        poll.save()
        return redirect('results', poll_id=poll.id)  # ✅ Redirect to results page after voting

    return render(request, 'vote.html', {'poll': poll})
