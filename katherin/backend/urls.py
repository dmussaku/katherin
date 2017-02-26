"""
Definition of all URL endpoints that katherin backend supports
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from apps.api_v1.router import router as api_v1_router

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(api_v1_router.urls)),
]
