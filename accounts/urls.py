# daccounts/urls.py
from django.conf.urls import url
from accounts import views
# SET THE NAMESPACE!
app_name = 'accounts'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^special/',views.special,name='special'),
    url(r'^logout/$', views.user_logout, name='logout'),
]