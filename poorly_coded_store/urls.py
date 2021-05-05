from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout/', views.checkout),
    path('login', views.login),
    path('create', views.create),
    path('signin', views.signin),
    path('success/<str:id>', views.success),
    path('logout', views.logout),
    path('message/<str:id>/create', views.createmessage),
    path('message/<str:id>/comment', views.createcomment),
]
