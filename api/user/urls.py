from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from user import views

urlpatterns = [
    url(r'^$', views.signup),
    url(r'^login/$', obtain_jwt_token),
]
