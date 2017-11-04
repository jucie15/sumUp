from django.conf.urls import url
from beacon import views

urlpatterns = [
    url(r'^$', views.signal_list),
]
