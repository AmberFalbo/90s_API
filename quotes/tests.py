from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Quotes

class QuoteTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_post = Quotes.objects.create(
            author = testuser1,
            quote = 'Family Matters',
            body = 'Did I do that? - Family Matters'
        )
        test_post.save()

    def test_blog_content(self):
        post = Quotes.objects.get(id=1)
        actual_author = str(post.author)
        actual_quote = str(post.quote)
        actual_body = str(post.body)
        self.assertEqual(actual_author, 'testuser1')
        self.assertEqual(actual_quote, 'Family Matters')
        self.assertEqual(actual_body, 'Did I do that? - Family Matters')