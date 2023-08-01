from django.db import models

from users.models import User

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='게시글 작성자')
    title = models.CharField(max_length=100, verbose_name='게시글 제목')
    content = models.TextField(verbose_name='게시글 내용')