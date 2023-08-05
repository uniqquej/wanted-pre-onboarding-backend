from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from articles.models import Article
from articles.serializers import ArticleSerializer

class ArticleView(APIView):
    def post(self, request):
        article_serializer = ArticleSerializer(data=request.data)
        if article_serializer.is_valid():
            article_serializer.save(author=request.user)
            return Response(article_serializer.data, status=status.HTTP_201_CREATED)
        return Response(article_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        articles = Article.objects.all()
        
        if len(articles)==0:
            return Response('게시글이 없습니다.', status=status.HTTP_200_OK)
        article_serializer = ArticleSerializer(articles, many=True)
        return Response(article_serializer.data, status=status.HTTP_200_OK)