from django.urls import path, include

urlpatterns = [
    path('', include('show_time_app.urls'))
]
