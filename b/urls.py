from django.urls import path
from b import views

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.registerview,name='register'),
    path('login',views.loginview,name='login'),
]
