from django.contrib import admin
from hangman.models import User
from hangman.models import Question
from hangman.models import Counting
from hangman.models import Quiz

# Register your models here.

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Counting)
admin.site.register(Quiz)
