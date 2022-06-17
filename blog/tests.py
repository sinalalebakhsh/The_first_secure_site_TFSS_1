from django.contrib.auth.models import User
from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='user1')
        cls.post1 = Post.objects.create(
            title='Post1',
            text='This is description',
            status=Post.STATUS_CHOICES[0][0],
            author=user,
        )
        cls.post2 = Post.objects.create(
            title='Post2',
            text='This is for Post2',
            status=Post.STATUS_CHOICES[1][0],
            author=user,
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
        response = self.client.get(reverse('post detail', args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_in_posts_list(self):
        response = self.client.get(reverse('post list view'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_post_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'Post1')
        self.assertEqual(self.post1.text, 'This is description')


