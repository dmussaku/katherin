
from rest_framework import serializers

from apps.blog.models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (serializers.ALL_FIELDS)
