from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login_page', views.login_page),
    path('register_page', views.register_page),
    path('register', views.create_user),
    path('login', views.login),
    path('logout', views.logout),
    path('home', views.home_page),
    path('creation', views.creation),
    path('create_char', views. create_character),
    path('user_profile/<int:id>', views.profile),
    path('creator_profile/<int:id>', views.creator_profile),
    path('created_character/<int:id>', views.image_view_page),
    path('unsave_art/<int:art_id>', views.unsave_art),
    path('delete/<int:char_id>', views.delete),
    path('save_art/<int:art_id>', views.save_art),
    path('saved_art', views.view_saved),
    path('edit', views.edit),
    path('profile/<int:profile_id>/edit', views.edit_profile),
    path('pic_update', views.pic_update),
]