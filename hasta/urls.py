from django.conf.urls import url
from .views import add_hasta,hasta_list

urlpatterns = [
    url(r'^$',hasta_list,name="hasta_list"),
    url(r'^add$',add_hasta,name="add_hasta"),
]
