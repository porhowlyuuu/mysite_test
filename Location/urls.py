"""Location URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from HarmonicSourceLocation import views 
urlpatterns = [
    path('topo2Matrix/',views.Topo2Matrix.as_view(),name='topo2Matrix'),
    path('HarSouLocation/',views.HarSouLocation.as_view(),name='HarSouLocation'),
    path('MultiHarSouLocation/',views.MultiHarSouLocation.as_view(),name='MultiHarSouLocation'),
    path('connect2SQL/',views.Connect2SQL.as_view(),name='connect2SQL'),
    path('index/',views.Index.as_view(),name='index'),
    path('test/',views.Test.as_view(),name="test"),
    path('', views.Start.as_view(),name='start')
    # path("admin/", admin.site.urls),
]
