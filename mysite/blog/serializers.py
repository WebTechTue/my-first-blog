from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
#    author = serializers.CharField
#    title = serializers.CharField
#    text = serializers.CharField
#    created_date = serializers.DateTimeField
#    published_date = serializers.DateTimeField
    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'created_date','published_date')
