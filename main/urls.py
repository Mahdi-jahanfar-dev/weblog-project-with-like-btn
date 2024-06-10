from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index_view'),
    path('contactus', views.ContactUserView.as_view(), name='contactus')
]