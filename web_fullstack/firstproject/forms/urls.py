from django.urls import path
from . import views

app_name = 'forms'
urlpatterns = [
    path('', views.form_name_view, name='forms')
]
