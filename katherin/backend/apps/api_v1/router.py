
from rest_framework.routers import DefaultRouter

from .auth.router import router as auth_router
from .blog.router import router as blog_router


router = DefaultRouter()
router.registry.extend(auth_router.registry)
router.registry.extend(blog_router.registry)
