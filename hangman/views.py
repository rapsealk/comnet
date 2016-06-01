from django.shortcuts import render
from django.db.models import F
from hangman.models import User
from hangman.models import Question
from hangman.models import Counting
from random import randint

# Create your views here.

def index(request):
    return render(request, 'index.html')

def wait(request):
    Counting.objects.filter(name='Player').update(count=F('count')+1)
    return render(request, 'waiting.html')

def game(request):
    Counting.objects.filter(name='Player').update(count=F('count')-1)
    word = Question.objects.all().order_by('key')
    word = word[randint(0, len(word)-1)]
    context = {'word' : word}
    return render(request, 'game.html', context)

def rank(request):
    ranker = User.objects.all().order_by('-score')[:5]
    context = {'ranker' : ranker}
    return render(request, 'rank.html', context)