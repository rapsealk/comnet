from django.shortcuts import render
from django.db.models import F
from hangman.models import User
from hangman.models import Question
from hangman.models import Counting
from hangman.models import Quiz
from hangman.models import Player
from random import randint
from django.http import HttpResponse 
import django.middleware.csrf#.CsrfViewMiddleware
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.

def index(request):
    back = request.POST.get('back', '')
    if back == 'back':
        Counting.objects.filter(name='Player').update(count=F('count')-1)
    return render(request, 'index.html')


def wait(request):
    new = request.POST.get('new', '')
    key = request.POST.get('key', '')
    if new == 'new':
        Counting.objects.filter(name='Player').update(count=F('count')+1)
    player = Counting.objects.filter(name='Player')
    player = player[0].count
    if key == '':
        key = player
    context = {'player' : player, 'key' : key}
    return render(request, 'waiting.html', context)


def game(request):
    answer = request.POST.get('answer', '')
    word = request.POST.get('word', '')
    new = request.POST.get('new', '')
    key = request.POST.get('key', 0)
    if new == 'new':
        Counting.objects.filter(name='Player').update(count=F('count')-1)
    if Player.objects.filter(name='Player'+str(key))[0].init == 1:        
        Player.objects.filter(name='Player'+str(key)).update(init=0)
    if Counting.objects.filter(name='Init')[0].count == 1:
        word = Question.objects.all().order_by('key')
        word = word[randint(0, len(word)-1)]
        Counting.objects.filter(name='Init').update(count=0)
        temp = ''
        for i in range(word.length):
            temp += '_'
        Quiz.objects.filter(key='prob').update(answer=word.word, current=temp, lives=8)
    else:
        word = Quiz.objects.all()[0].answer
        
    p1 = Player.objects.filter(name='Player1')
    p2 = Player.objects.filter(name='Player2')
    p3 = Player.objects.filter(name='Player3')
    p4 = Player.objects.filter(name='Player4')
    plist = [p1, p2, p3, p4]
    
    for p in plist:
        if p[0].done:
            if p[0].win:
                for i in range(4):
                    if plist[i] == p:
                        continue
                    plist[i].update(done=1, lose=1)
                break

    cur = Quiz.objects.all()[0].current    
    end = False
    
    if p1[0].done or p2[0].done or p3[0].done or p4[0].done:
        end = True
        cur = word
    
    found = 0
    if answer != "#refresh#":
        if len(answer)==1:
            for i in range(len(word)):
                if word[i] == answer:
                    cur = cur[:i]+answer+cur[i+1:]
                    found += 1
            if cur == word:
                cur += "\n"# + "You win!"
                Player.objects.filter(name='Player'+str(key)).update(done=1, win=1)
                end = True
        elif len(answer)>1:
            if answer == word:
                cur = word + "\n"# + "You win!"
                Player.objects.filter(name='Player'+str(key)).update(done=1, win=1)
                end = True
                found += 1

        if found == 0:
            Player.objects.filter(name='Player'+str(key)).update(lives=F('lives')-1)
    lives = Player.objects.filter(name='Player'+str(key))[0].lives
    if lives == 0:
        Player.objects.filter(name='Player'+str(key)).update(done=1, lose=1)
        end = True

    lose = Player.objects.filter(name='Player'+str(key))[0].lose
    Quiz.objects.filter(key='prob').update(current=cur)
    context = {'key' : key, 'word' : word, 'answer' : cur, 'lives': lives, 'lose' : lose, 'end' : end}
    return render(request, 'game.html', context)


def rank(request):
    key = request.POST.get('key', '')
    Counting.objects.filter(name='Init').update(count=1)
    user = request.POST.get('id', "default")
    result = request.POST.get('result', "lose")
    if key != '':
        Player.objects.filter(name='Player'+str(key)).update(init=1, lives=8, done=0, win=0, lose=0)
    if result == "win":
        if User.objects.filter(name=user):
            User.objects.filter(name=user).update(score=F('score')+100)
        else:
            rank = User(name=user, score=100)
            rank.save()
    ranker = User.objects.all().order_by('-score')[:5]
    context = {'ranker' : ranker}
    return render(request, 'rank.html', context)