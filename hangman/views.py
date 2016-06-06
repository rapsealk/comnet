from django.shortcuts import render
from django.db.models import F
from hangman.models import User
from hangman.models import Question
from hangman.models import Counting
from hangman.models import Quiz
from random import randint
from django.http import HttpResponse 
import django.middleware.csrf#.CsrfViewMiddleware

# Create your views here.

def index(request):
    return render(request, 'index.html')

def wait(request):
    Counting.objects.filter(name='Player').update(count=F('count')+1)
    return render(request, 'waiting.html')

#def bridge(request):
#    Counting.objects.filter(name='Player').update(count=F('count')-1)
#    player = Counting.objects.all()
#    player = player[0]
#    word = Question.objects.all().order_by('key')
#    word = word[randint(0, len(word)-1)]
#    context = {'player' : player, 'word' : word}
#    return render(request, 'game.html', context)

def game(request):
    answer = request.POST.get('answer', '')
    player = request.POST.get('player', 0)

    if Counting.objects.filter(name='Init')[0].count == 1:
        Counting.objects.filter(name='Player').update(count=F('count')-1)
        player = Counting.objects.all()
        player = player[0].count
        word = Question.objects.all().order_by('key')
        word = word[randint(0, len(word)-1)]
        Counting.objects.filter(name='Init').update(count=0)
        temp = ''
        for i in range(word.length):
            temp += '_'
        Quiz.objects.filter(key='prob').update(answer=word.word, current=temp)
    else:
        word = Quiz.objects.all()[0].answer
    #if answer and word and player and current:
    #    context = {'answer':answer, 'word':word, 'player':player+1, 'current':current}
    #else:
    #    context = {'answer':answer, 'word':word, 'player':player, 'current':current}
    cur = Quiz.objects.all()[0].current

    #context = {'player' : player, 'word' : word, 'answer' : current}

    end = False
    if len(answer)==1:
        for i in range(len(word)):
            if word[i] == answer:
                cur = cur[:i]+answer+cur[i+1:]
    elif len(answer)>1:        
        if answer == word:
            cur = word + "\n" + "You win!"
            end = True

    Quiz.objects.filter(key='prob').update(current=cur)

    context = {'player' : player, 'word' : word, 'answer' : cur, 'end' : end}
    return render(request, 'game.html', context)

def rank(request):
    user = request.POST.get('id', "default")
    if User.objects.filter(name=user):
        User.objects.filter(name=user).update(score=F('score')+100)
    else:
        rank = User(name=user, score=100)
        rank.save()
    ranker = User.objects.all().order_by('-score')[:5]
    context = {'ranker' : ranker}
    return render(request, 'rank.html', context)

#def aaaaa(request):
#   t = get_template('index.html')
#   k = request.GET
#   ttt = k['va']
#   html = t.render(Context({'va' : ttt}))
#   return HttpResponse(html)







