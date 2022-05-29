from django.contrib.auth.models import User
from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User

class PostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user1')
        self.post1 = Post.objects.create(
            title='Post1',
            text='This is description',
            status=Post.STATUS_CHOICES[0][0],
            author=self.user,
        )

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

