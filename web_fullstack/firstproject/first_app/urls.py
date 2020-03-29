from django.urls import path
from first_app import views

app_name = 'first_app'
urlpatterns = [
    path('first_app/', views.index, name='index'),
    path('', views.homepage, name='home'),
]
