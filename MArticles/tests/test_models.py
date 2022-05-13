from django.contrib.auth import get_user_model
from django.test import TestCase
from EHub.models import Profile
from MArticles.models import Article


class TestArticleModel(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        self.profile = Profile.objects.get(username__username__contains="testuser")

    def test_should_create_article(self):
        article_obj = Article.objects.create(
            title="Deploy Django",
            description="fdsdf",
            author=self.profile,
        )

        # check for equlity between string representation of obj with "Deploy Django"
        self.assertEqual(str(article_obj), "Deploy Django")
