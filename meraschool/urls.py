"""meraschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from apiapps.api import WorkList,QualList,TypeList
from student.api import Infolist
from register.views import RegisterAPI




urlpatterns = [
    path('admin/', admin.site.urls),
    path('guardian/qualification',QualList.as_view(),name='qualification'),
    path('guardian/workprofile',WorkList.as_view(),name='workprofile'),
    path('guardian/type',TypeList.as_view(),name='type'),
    path('student/info',Infolist.as_view(),name='info'),
    path('register',RegisterAPI.as_view(),name='register'),

  
]
