
from rest_framework import routers

from .api import ArticleViewSet, PostViewSet


router = routers.SimpleRouter()
router.register(r'blog/articles', ArticleViewSet, base_name='articles')
router.register(r'blog/posts', PostViewSet, base_name='posts')
