from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^amadon$', views.index),
    url(r'^amadon/buy$', views.create_purchase),
    url(r'^amadon/checkout$', views.display_purchase)
]
