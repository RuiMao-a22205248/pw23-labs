from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('home/', views.index_view, name="home")
]
