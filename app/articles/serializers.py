from rest_framework import serializers

from articles.models import Article


class ArticleAllSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(required=False, format='%d.%m.%y - %H:%M')
    updated_at = serializers.DateTimeField(required=False, format='%d.%m.%y - %H:%M')

    class Meta:
        model = Article
        fields = 'pk', 'title', 'description', 'created_at', 'updated_at'
