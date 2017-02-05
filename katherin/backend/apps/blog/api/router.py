
from rest_framework import routers

from .article.api import ArticleViewSet


router = routers.SimpleRouter()
router.register(r'blog/articles', ArticleViewSet, base_name='articles')
