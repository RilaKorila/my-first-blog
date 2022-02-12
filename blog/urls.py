from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    ]
# <int:pk>: Django expects an int value and 
# will transfer it to a view as a variable called pk(Primary Key)