from django.urls import path, re_path
from resell import views


urlpatterns = [
    path('', views.index, name='index'),

    
]