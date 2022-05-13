from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from EHub.models import Profile
from MArticles.models import Article


class TestArticleModel(TestCase):

    # We define here variables that are useful for test.This method runs before all the test functions
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="test@email.com", password="secret"
        )
        self.profile = Profile.objects.get(username__username__contains="testuser")
        self.article = Article.objects.create(
            title="Deploy Django",
            description="Nice body content",
            author=self.profile,
        )

    # Every function must start with test except setUp
    def test_article_page_status_code(self):
        # Issue a GET request.
        response = self.client.get("/articles/")  # reverese doesn't work

        # assertEqual:checks the resonse code equal to 200?
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Articles/article.html")

    def test_article_detail_page(self):
        no_response = self.client.get("articledetail/3423/1gdfgfdvd/")
        print(no_response.status_code)
        response = self.client.get("article_detail/" + str(self.article.id) + "/" + self.article.slug)

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(no_response.status_code, 404)
        # self.assertTemplateUsed(response, "Articles/articledetail.html")


"""


    def test_article_detail_page(self):
        self.user = {
            "username": "dswehjdwe",
            "email": "ad1hj23@gmail.com",
            "passsword1": "sdcsd",
            "passsword2": "sdcsd",
        }
        response = self.client.post("account/sign-up/", self.user)
        self.assertEquals(response.status_code, 302)
        
    def test_articledetail_page_status_code(self):
        response = self.client.get("/articles/detail/2")  
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "Articles/articledetail.html")
"""


"""
client¶
The test client is a Python class that acts as a dummy web browser, allowing you to test your views and interact with your Django-powered application programmatically.
"""


"""

    def setUp(Self):
        scds
    
    def test_article_creation(self):
        user_obj = User.objects.create_user(username="ihukhM", email="asdin@gmail.com")
        user_obj.set_password("password123")
        user_obj.save()
        profile_obj = Profile.objects.create(username=user_obj)
        profile_obj.save()
        article_obj = Article.objects.create(author=profile_obj, title="Deploy Django")
        article_obj.save()
        self.assertEqual(str(article_obj), "Deploy Django")
        
"""
