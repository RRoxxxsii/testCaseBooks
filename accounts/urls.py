from django.urls import path

from accounts import views

urlpatterns = [
    path('', views.RegisterUser.as_view(), name='register')
]
