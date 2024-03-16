from django.urls import path
from . import views
app_name='movieapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/',views.home,name='home'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('add/', views.add_movie, name='add_movie'),
    path('add/home/',views.home,name='home'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('search/', views.search, name='search'),
    path('all_movie_cat/', views.category, name='category'),
    path('<slug:c_slug>/', views.category , name='category'),
    path('movie/<int:movie_id>/post_review',views.post_review,name='post_review'),
    path('movie/<int:movie_id>/post_rating', views.post_rating, name='post_rating'),


]
