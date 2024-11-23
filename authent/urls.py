from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('edit/<int:task_id>', views.edit, name="edit"), 
    path('delete/<int:task_id>', views.Delete, name='delete'), 
    path('logout', views.logout, name="logout"),
    path('invite/', views.invite_user, name="invite_user"), 
    path('register/', views.register, name="register"), 
    path('profile/', views.profilepage, name="profilepage")
]