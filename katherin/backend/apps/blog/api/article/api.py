
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from apps.blog.models import Article, Comment
from .serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @detail_route(methods=['post'], url_path='add_comment')
    def add_comment(self, request, pk=None):
        user = request.user
        comment_content = request.data.get('content', '')
        comment_status = request.data.get('comment_status', Comment.DRAFT)

        article = Article.objects.get(pk=pk)

        comment = article.add_comment(comment_content, user, comment_status)

        return Response(comment)

    @detail_route(methods=['post'], url_path='add_activity')
    def add_activity(self, request, pk=None):
        user = request.user
        activity_type = request.data.get('activity_type', '')

        article = Article.objects.get(pk=pk)

        activity = article.add_activity(activity_type, user)

        return Response(activity)
