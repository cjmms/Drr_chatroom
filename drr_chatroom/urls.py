"""drr_chatroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def signin(request):
    print("i am heer")
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return render(request, 'chat/index.html', {})
        else:
            # Return a 'disabled account' error message
            print("fuck")
    else:
        # Return an 'invalid login' error message.
        print("fuck2")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('signup.urls')),
    path('index/', include('django.contrib.auth.urls')),
    path('test/',TemplateView.as_view(template_name='index.html'), name='test'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('chat/', include('chat.urls')),
    path('index/login/my_view', signin),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

