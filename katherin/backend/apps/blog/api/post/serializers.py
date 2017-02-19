
from rest_framework import serializers

from apps.blog.models import Post
from apps.blog.api.activity.serializers import ActivitySerializer
from apps.blog.api.comment.serializers import CommentSerializer


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    activities = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('__all__')

    def get_comments(self, obj):
        return CommentSerializer(obj.comments.all(), many=True)

    def get_activities(self, obj):
        return ActivitySerializer(obj.activity.all(), many=True)
