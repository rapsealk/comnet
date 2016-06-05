from django.shortcuts import render
from django.db.models import F
from hangman.models import User
from hangman.models import Question
from hangman.models import Counting
from random import randint
from django.http import HttpResponse 
import django.middleware.csrf#.CsrfViewMiddleware

# Create your views here.

def index(request):
    return render(request, 'index.html')

def wait(request):
    Counting.objects.filter(name='Player').update(count=F('count')+1)
    return render(request, 'waiting.html')

def bridge(request):
    Counting.objects.filter(name='Player').update(count=F('count')-1)
    player = Counting.objects.all()
    player = player[0]
    word = Question.objects.all().order_by('key')
    word = word[randint(0, len(word)-1)]
    context = {'player' : player, 'word' : word}
    return render(request, 'game.html', context)

def game(request):
    answer = request.POST.get('answer', '')
    length = request.POST.get('length', 0)
    word = request.POST.get('word', '')
    player = request.POST.get('player', 0)
    current = request.POST.get('current', '')
    
    if length:
        for i in range(length):
            if answer == word[i]:
                current[i] = answer
    #Counting.objects.filter(name='Player').update(count=F('count')-1)
    #player = Counting.objects.all()
    #player = player[0]
    #word = Question.objects.all().order_by('key')
    #word = word[randint(0, len(word)-1)]
    if answer and word and player and current:
        context = {'answer':answer, 'word':word, 'player':player+1, 'current':current}
    else:
        context = {'answer':answer, 'word':word, 'player':player, 'current':current}
    #context = {'player' : player, 'word' : word, 'answer' : answer}
    return render(request, 'game.html', context)

def rank(request):
    ranker = User.objects.all().order_by('-score')[:5]
    context = {'ranker' : ranker}
    return render(request, 'rank.html', context)

#def aaaaa(request):
#   t = get_template('index.html')
#   k = request.GET
#   ttt = k['va']
#   html = t.render(Context({'va' : ttt}))
#   return HttpResponse(html)







