from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name = 'home'),
    path ('publish', views.publish, name = 'publish'),
    path ('subscribe',views.subscribe, name = 'subscribe' ),
]