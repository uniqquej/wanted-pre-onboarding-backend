from rest_framework import serializers

from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields=['id','author','title','content']
        read_only_fields=['id','author']
        