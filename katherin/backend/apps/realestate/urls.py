from django.conf.urls import url

from .views import (
    CityFormView,
    CityListView,
)


urlpatterns = [
    url(r'^city/$', CityListView.as_view(), name='city-list'),
    url(r'^city/create/$', CityFormView.as_view(), name='city-create'),
]
