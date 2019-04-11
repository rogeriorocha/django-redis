# cache/urls.py

from django.conf.urls import url
from .views import view_produtos, view_cached_produtos

 from django.views.decorators.cache import cache_page

urlpatterns = [
    url(r'^$', view_produtos),
    url(r'^cached/', cache_page(600) view_cached_produtos)
]