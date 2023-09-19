from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    return render(request, 'main/index.html')


def shop(request):
    return render(request, 'main/shop.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была введена не правильно'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
