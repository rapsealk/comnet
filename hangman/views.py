from django.shortcuts import render
from hangman.models import User
from hangman.models import Question

# Create your views here.

def index(request):
    return render(request, 'index.html')

def wait(request):
    return render(request, 'waiting.html')

def game(request):
    return render(request, 'game.html')

def rank(request):
    ranker = User.objects.all().order_by('-score')[:5]
    context = {'ranker' : ranker}
    return render(request, 'rank.html', context)
