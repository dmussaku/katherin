
from rest_framework import routers

from .article.api import ArticleViewSet
from .post.api import PostViewSet


router = routers.SimpleRouter()
router.register(r'blog/articles', ArticleViewSet, base_name='articles')
router.register(r'blog/posts', PostViewSet, base_name='posts')
