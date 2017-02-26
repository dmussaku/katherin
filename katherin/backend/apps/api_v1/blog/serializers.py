
from rest_framework import serializers

from apps.blog.models import Activity, Article, Comment, Post


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (serializers.ALL_FIELDS)


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
