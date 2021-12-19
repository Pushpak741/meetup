from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meetup/login',views.login,name='login'),
    path('meetup/signup',views.signup,name='signup'),
    path('meetup/dashboard',views.login,name='login'),
    path('meetup/home',views.home,name='home'),
    path('meetup/home1',views.home1,name='home1'),
    path('meetup/home2',views.home2,name='home2'),
    path('meetup/home3',views.home3,name='home3'),
    path('<str:room>/', views.room, name='room'),
    path('meetup/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]