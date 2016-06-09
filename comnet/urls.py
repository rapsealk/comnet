"""comnet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import patterns, url, include
from django.contrib import admin
from hangman import views

#url(regex, view, kwargs=None, name=None, prefix='')
#regex: URL regular expression
#view: call view, parameter
#kwargs: python dictionary parameter
#name: url name
#prefix: view prefix
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^wait/$', views.wait, name='wait'),
    url(r'^game/$', views.game, name='game'),
    url(r'^rank/$', views.rank, name='rank'),
]