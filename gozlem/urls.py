from django.conf.urls import url
from .views import create_gozlem, view_gozlem, gozlem_list, delete_gozlem

urlpatterns = [
    url(r'^create$',create_gozlem,name="create_gozlem"),
    url(r'^(?P<id>[0-9]+)$',view_gozlem,name="view_gozlem"),
    url(r'^$',gozlem_list,name="gozlem_list"),
    url(r'^(?P<id>[0-9]+)/delete$', delete_gozlem, name="delete_gozlem"),
]