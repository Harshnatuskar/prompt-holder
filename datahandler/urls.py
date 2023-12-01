from django.urls import path
from .views import upload_json, data_list

urlpatterns = [
    path('upload/', upload_json, name ='upload_json'),
    path('data_list/', data_list, name='data_list'),
]