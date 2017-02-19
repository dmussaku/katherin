
from rest_framework import serializers

from apps.blog.models import Activity


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = ('__all__')
