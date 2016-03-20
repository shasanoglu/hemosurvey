from django.conf.urls import url
from .views import add_hasta,hasta_list, view_hasta, EditHasta

urlpatterns = [
    url(r'^$',hasta_list,name="hasta_list"),
    url(r'^add$',add_hasta,name="add_hasta"),
    url(r'^(?P<pk>[0-9]+)$',view_hasta,name="view_hasta"),
    url(r'^(?P<pk>[0-9]+)/edit$',EditHasta.as_view(),name="edit_hasta"),
]
