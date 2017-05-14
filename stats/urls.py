from django.conf.urls import url
from .views import stat

urlpatterns = [
    url(r'^$',stat,name="stat"),
]
