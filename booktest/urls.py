from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^static_test/$', views.static_test),

]