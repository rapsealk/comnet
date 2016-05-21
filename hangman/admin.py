from django.contrib import admin
from hangman.models import User
from hangman.models import Question

# Register your models here.

admin.site.register(User)
admin.site.register(Question)
