"""
Definition of all URL endpoints that katherin backend supports
"""
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from django.contrib import admin

from apps.blog.api.router import router as blog_router


router = DefaultRouter()
router.registry.extend(blog_router.registry)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include('apps.api_v1.urls', namespace='api')),
]
