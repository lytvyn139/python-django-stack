from django.urls import path, include
urlpatterns = [
    path('', include('session_app.urls')),
]
