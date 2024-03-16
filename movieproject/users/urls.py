from django.urls import path
from . import views
app_name='users'

urlpatterns=[
    path('register', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/',views.view_profile,name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/edit/view_profile/', views.view_profile, name='view_profile'),
    path('logout', views.logout, name='logout'),
]