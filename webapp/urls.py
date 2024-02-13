"""
URL configuration for mainproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
import webapp.views as view
urlpatterns = [
    path('', view.home,name='home'),
    path('auth/', view.auth_view,name='auth_view'),
    path('register_view/', view.register_view,name='register_view'),
    path('login_view/', view.login_view,name='login_view'),
    path('image_upload/', view.image_upload,name='image_upload'),
    path('logout_view/', view.logout_view,name='logout_view'),
    
]