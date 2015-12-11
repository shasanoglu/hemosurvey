from django.conf.urls import url
from .views import add_hasta

urlpatterns = [
    url(r'^add$',add_hasta,name="add_hasta"),
]
