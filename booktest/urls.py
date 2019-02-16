from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^static_test/$', views.static_test),
    url(r'^show_upload/$', views.show_upload),
    url(r'^upload_handle$', views.upload_handle),
    url(r'^show_area/$', views.show_area)

]