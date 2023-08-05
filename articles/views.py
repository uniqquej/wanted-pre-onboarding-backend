from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from articles.models import Article
from articles.serializers import ArticleSerializer
from articles.pagination import PaginationHandlerMixin

class ArticlePagination(PageNumberPagination):
    page_size=10
    
class ArticleView(APIView,PaginationHandlerMixin):
    pagination_class = ArticlePagination
    serializer_class = ArticleSerializer
    
    def get(self, request):
        articles = Article.objects.all()
        
        page = self.paginate_queryset(articles)
        if page is not None:
            article_serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            article_serializer = self.get_paginated_response(articles, many=True)

        return Response(article_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        article_serializer = ArticleSerializer(data=request.data)
        if article_serializer.is_valid():
            article_serializer.save(author=request.user)
            return Response(article_serializer.data, status=status.HTTP_201_CREATED)
        return Response(article_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ArticleDetailView(APIView):
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        article_serializer = ArticleSerializer(article)
        return Response(article_serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.author:
            article_serializer = ArticleSerializer(article, data=request.data, partial=True)
            if article_serializer.is_valid():
                article_serializer.save(author=request.user)
                return Response(article_serializer.data, status=status.HTTP_200_OK)
            return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response('권한이 없습니다.',status=status.HTTP_401_UNAUTHORIZED)
    
    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.author:
            article.delete()
            return Response('삭제가 완료되었습니다.', status=status.HTTP_204_NO_CONTENT)
        return Response('권한이 없습니다.',status=status.HTTP_401_UNAUTHORIZED)