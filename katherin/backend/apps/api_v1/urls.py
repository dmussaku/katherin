"""
APIv1 views mapping to url endpoints
"""
from django.conf import settings
from django.conf.urls import url
from .views import *


urlpatterns = [
    #### news api ####
    url(r'^auth/$', AuthIndex.as_view()),
    ##################
    ]
    