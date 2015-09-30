from django.conf.urls import url

from . import views
urlpatterns = [
        url(r'^t2/', views.t2),
        url(r'^$', views.index),
]