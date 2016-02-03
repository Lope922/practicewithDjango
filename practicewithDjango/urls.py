"""practicewithDjango URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from learningbasicDjango.views import post_list

#urls and paths will be stored here.
urlpatterns = [
    # this regular expression means that for every URL that starts with admin/ include in the site urls
    url(r'^admin/', admin.site.urls),

    #same here for start. Now Django should redirect everything that comes to 127.0.0.1:8000 to the start page
    url(r'^$', 'practicewithDjango.learningbasicDjango.views', name='start'),

    # searches for start, a loads post_list method/function
    url(r'^start/', post_list)


]

