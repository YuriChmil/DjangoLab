from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class HomeTests(TestCase):

    def test_home_url(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_list_url(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_category_list_url(self):
        url = reverse('articles-category-list', args=['test-category'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

