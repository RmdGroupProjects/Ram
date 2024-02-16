"""
URL configuration for Rmd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import urlpatterns

from app import views

urlpatterns+= staticfiles_urlpatterns()
from Rmd import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",views.home),
    path("index/",views.index),
    path("send/",views.send),
    path("login/",views.login),
    path("log/",views.log),
    path("logout_out/",views.logout_out),
    path("password/",views.password),
    path("getpass/",views.getpass),
    #path("total/",views.total),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
