
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from apps.blog.models import Post, Comment
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @detail_route(methods=['post'], url_path='add_comment')
    def add_comment(self, request, pk=None):
        user = request.user
        comment_content = request.data.get('content', '')
        comment_status = request.data.get('comment_status', Comment.DRAFT)

        post = Post.objects.get(pk=pk)

        comment = post.add_comment(comment_content, user, comment_status)

        return Response(comment)

    @detail_route(methods=['post'], url_path='add_activity')
    def add_activity(self, request, pk=None):
        user = request.user
        activity_type = request.data.get('activity_type', '')

        post = Post.objects.get(pk=pk)

        activity = post.add_activity(activity_type, user)

        return Response(activity)
