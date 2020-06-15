from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),                                  # 1
    path('shows/create', views.create_show),                # 2
    path('shows/<int:show_id>', views.show_info),           # 3

    path('shows', views.all_shows),                         # 4
    path('shows/<int:show_id>/edit', views.edit_show),      # 5
    path('shows/<int:show_id>/delete', views.delete_show),  # 6

    path('shows/<int:show_id>/update', views.update_show),  # 7
    path('shows/new', views.new_show)                       # 8
]