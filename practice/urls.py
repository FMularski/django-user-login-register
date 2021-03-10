from django.urls import path
from . import views

app_name = 'practice'

urlpatterns = [
    path('register/', views.register, name='register')
]