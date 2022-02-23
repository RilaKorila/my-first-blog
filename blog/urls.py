from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login'),
    path('', include('blog.urls')),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.draft_list, name='draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:pk>/approve/', views.approve_comment, name='approve_comment'),
    
    ]
# <int:pk>: Django expects an int value and 
# will transfer it to a view as a variable called pk(Primary Key)