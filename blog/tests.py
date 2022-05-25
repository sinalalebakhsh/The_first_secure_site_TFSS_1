from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post


class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user1')
        self.post1 = Post.objects.create(
            title='Post1',
            text='This is the description of Post1',
            status=Post.STATUS_CHOICES[0],
            author=self.user,
        )
