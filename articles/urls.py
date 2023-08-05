from django.urls import path

from articles import views

urlpatterns = [
    path('',views.ArticleView.as_view(), name='article'),
    path('<int:article_id>/',views.ArticleDetailView.as_view(), name='article-detail'),
]
