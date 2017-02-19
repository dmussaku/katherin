
from rest_framework import serializers

from apps.blog.models import Article
from apps.blog.api.activity.serializers import ActivitySerializer
from apps.blog.api.comment.serializers import CommentSerializer


class ArticleSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()
    activities = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = (serializers.ALL_FIELDS)

    def get_comments(self, obj):
        return CommentSerializer(obj.comments.all(), many=True).data

    def get_activities(self, obj):
        return ActivitySerializer(obj.activities.all(), many=True).data
