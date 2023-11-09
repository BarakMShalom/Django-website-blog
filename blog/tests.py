from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post


class BlogTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test post
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post content.',
            author=self.user
        )

    def test_blog_home_view(self):
        """
        Test the blog home view.
        """
        response = self.client.get(reverse('blog-home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        """
        Test the post detail view.
        """
        response = self.client.get(reverse('post-detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_create_view_authenticated(self):
        """
        Test the post create view when the user is authenticated.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post-create'), {'title': 'New Post', 'content': 'New Post Content'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='New Post').exists())

    def test_post_create_view_not_authenticated(self):
        """
        Test the post create view when the user is not authenticated.
        """
        response = self.client.post(reverse('post-create'), {'title': 'New Post', 'content': 'New Post Content'})
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(title='New Post').exists())

    def test_post_update_view_authenticated(self):
        """
        Test the post update view when the user is the author.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post-update', args=[self.post.id]),
                                    {'title': 'Updated Post', 'content': 'Updated Post Content'})
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')

    def test_post_update_view_not_authenticated(self):
        """
        Test the post update view when the user is not the author.
        """
        # Create another user
        another_user = User.objects.create_user(username='anotheruser', password='anotherpassword')

        # Login with the new user
        self.client.login(username='anotheruser', password='anotherpassword')

        response = self.client.post(reverse('post-update', args=[self.post.id]),
                                    {'title': 'Updated Post', 'content': 'Updated Post Content'})
        self.assertEqual(response.status_code, 403)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Test Post')

    def test_post_delete_view_authenticated(self):
        """
        Test the post delete view when the user is the author.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('post-delete', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Post.objects.filter(title='Test Post').exists())

    def test_post_delete_view_not_authenticated(self):
        """
        Test the post delete view when the user is not the author.
        """
        # Create another user
        another_user = User.objects.create_user(username='anotheruser', password='anotherpassword')

        # Login with the new user
        self.client.login(username='anotheruser', password='anotherpassword')

        response = self.client.post(reverse('post-delete', args=[self.post.id]))
        self.assertEqual(response.status_code, 403)
        self.assertTrue(Post.objects.filter(title='Test Post').exists())
