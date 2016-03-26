from django.conf.urls import url
from .views import add_hasta,hasta_list, view_hasta, edit_hasta, \
    create_olay, view_olay

urlpatterns = [
    url(r'^$',hasta_list,name="hasta_list"),
    url(r'^add$',add_hasta,name="add_hasta"),
    url(r'^(?P<pk>[0-9]+)$',view_hasta,name="view_hasta"),
    url(r'^(?P<pk>[0-9]+)/edit$',edit_hasta,name="edit_hasta"),
    url(r'^kateter/(?P<kateter_id>[0-9]+)/olay/add$',create_olay,name="create_olay"),
    url(r'^olay/(?P<olay_id>[0-9]+)$',view_olay,name="view_olay"),
]
