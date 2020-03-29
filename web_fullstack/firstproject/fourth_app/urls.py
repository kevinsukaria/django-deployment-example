from . import views
from django.urls import path

app_name = 'fourth_app'
urlpatterns = [
    path('', views.fork, name='fork'),
    path('path1/', views.path1, name='path1'),
    path('path2/', views.path2, name='path2'),
]
