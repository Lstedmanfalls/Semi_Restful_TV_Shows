from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), #GET request redirecting to shows route
    path('shows', views.shows), #GET request to display all objects' info starting at a different root
    path('shows/new_show', views.add_show), #GET request to display form to create an object
    path('shows/create_show', views.create_show), #POST request to create an object
    path('shows/<int:show_id>', views.view_show), #GET request to display a specific object's info
    path('shows/<int:show_id>/edit', views.edit_show), #GET request to display form to update a specific object
    path('shows/<int:show_id>/update', views.update_show), #POST request to update a specific object
    path('shows/<int:show_id>/destroy', views.delete_show), #POST request to delete a specific object
]