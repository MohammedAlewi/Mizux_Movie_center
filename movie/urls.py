from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list_categories/<str:category>/', views.list_categories, name='list_categories'),
    path('add_categories/', views.add_categories, name='add'),
    path('add_categories/post/', views.post_categories, name='post'),
    path('add_movies/', views.add_movies, name='add'),
    path('add_movies/post/', views.post_movies, name='post'),
    path('delete_category/<str:category>/post/', views.del_categories, name='post'),
    path('edit_categories/post/', views.post_edit_categories, name='post'),
    path('edit_category/<str:category>/', views.edit_categories, name='post'),

    path('edit_movie/post/', views.post_edit_movies, name='post'),
    path('edit_movie/<str:movie>/<str:category>', views.edit_movie, name='post'),
    path('delete_movie/<str:movie>/<str:category>', views.del_movie, name='post'),
]
