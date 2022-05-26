from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post
from django.shortcuts import reverse

class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user1')
        self.post1 = Post.objects.create(
            title='Post1',
            text='This is the description of Post1',
            status=Post.STATUS_CHOICES[0][0],
            author=self.user,
        )
        self.post2 = Post.objects.create(
            title='Post2',
            text='This is for Post2',
            status=Post.STATUS_CHOICES[1][0],
        )

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('post list view'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('post list view'))
        self.assertContains(response, self.post1.title)

    def test_post_detail_url(self):
        response = self.client.get(reverse('post detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_blog_detail_page(self):
        response = self.client.get(reverse('post detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_status_404_if_post_id_not_exist(self):
        response = self.client.get(reverse('post detail', args=[(self.post1.id)+1]))
        self.assertEqual(response.status_code, 404)
