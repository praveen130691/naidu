"""samyu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from samyuapp import views
from django.conf.urls import url


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home),
    url(r'regi', views.regi),
    url(r'login', views.login),
    url(r'sanjeev', views.sanjeev),
    url(r'saroja', views.saroja),
    url(r'input',views.input),
    url(r'grand',views.grand),
    url(r'gra1',views.gra1),
    url(r'parent',views.parent),
    url(r'praveen', views.praveen),
    url(r'sibling',views.sibling),
    url(r'naveen', views.naveen),
    url(r'nick',views.nick),
    url(r'apple',views.apple),
    url(r'edu',views.edu),
    url(r'psn',views.psn),
]
