"""textUtility URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from . import views
from . import pipLine

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pipLine.index,name="index"),
    path('textAnylized',pipLine.analyze,name="Check String"),
    # path('upperCase', pipLine.upperCase, name="upperCase"),
    # path('capitlize',pipLine.capital,name="capitialize"),
    # path('newline',pipLine.newline,name="newline"),
    # path('spaceremove',pipLine.spaceremove,name="spaceremove"),
    # path('charcount',pipLine.charcount,name="charcount"),
    #
    # path('about',views.about,name="about"),
    # path('table',views.table,name="table"),
    path('website',views.website,name="website")
]
