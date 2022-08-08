from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="johndoe",
            email="johndoe.example.com",
            password="secret",
        )

        self.post = Post.objects.create(
            title="A good title",
            body="Nice Body content",
            author=self.user,
        )

    """
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="abc123"
        )
        testuser1.save()

        # Create a blog post
        test_post = Post.objects.create(
            author=testuser1, title="Blog title", body="Body content..."
        )
        test_post.save()
    """

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "johndoe")
        self.assertEqual(title, "A good title")
        self.assertEqual(body, "Nice Body content")

    def test__str__(self):
        post = Post.objects.get(id=1)
        assert post.__str__() == post.title
        assert str(post) == post.title
