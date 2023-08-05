from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from articles.serializers import ArticleSerializer

class ArticleView(APIView):
    def post(self, request):
        article_serializer = ArticleSerializer(data=request.data)
        if article_serializer.is_valid():
            article_serializer.save(author=request.user)
            return Response(article_serializer.data, status=status.HTTP_201_CREATED)
        return Response(article_serializer.errors,status=status.HTTP_400_BAD_REQUEST)