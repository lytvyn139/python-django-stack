from django.urls import path, include

urlpatterns = [
        path('', include('templates_app.urls')),
]
