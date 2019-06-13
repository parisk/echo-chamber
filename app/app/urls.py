from django.urls import path

from echo import views as echo_views



urlpatterns = [
    path('', echo_views.home),
]
