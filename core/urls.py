from django.urls import path

from .  import views


urlpatterns = [
    path("", views.index, name="index"),
    path('create-task/', views.create_task, name='create_task'),
    path('update-task/<str:pk>/', views.update_task, name="update_task"),
    path('delete-task/<str:pk>/', views.delete_task, name="delete_task"),
    path("close-modal/", views.close_modal, name="close_modal"),
]
