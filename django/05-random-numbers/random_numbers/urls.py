from django.urls import path, include
urlpatterns = [
    path('', include('random_numbers_app.urls')),
]
