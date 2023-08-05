from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

from users.models import User
from articles.models import Article

class ArticleTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.faker = Faker()
        cls.user_data = {'email':'test@test.com','password':'testpass'}
        cls.user = User.objects.create_user('test@test.com','testpass')
        
        cls.article_data = {'title':cls.faker.sentence(),'content': cls.faker.text()}
        for _ in range(5):
            Article.objects.create(
                author=cls.user,
                title = cls.faker.sentence(),
                content = cls.faker.text())
        
    def setUp(self) ->None:
        url = reverse('login')
        res = self.client.post(url,self.user_data)
        self.access_token = res.data['access']
    
    def test_create_article(self):
        url = reverse('article')
        
        res = self.client.post(
            path=url,
            data=self.article_data,
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data['title'], self.article_data['title'])
        
    def test_get_articles(self):
        url = reverse('article')

        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data['results']), 5)
        