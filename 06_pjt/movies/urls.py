from django.urls import path
from . import views 

app_name = 'movies'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/comments/', views.comments, name='comments'),
    path('<int:movie_pk>/comments/>int:comments_pk>/delete', views.comment_delete, name='comment_delete'),
    
]
