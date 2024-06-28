from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('generate_snippet_form/', views.generate_snippet_form, name='generate_snippet_form'),
    path('generate_snippet/', views.generate_snippet, name='generate_snippet'),
]
