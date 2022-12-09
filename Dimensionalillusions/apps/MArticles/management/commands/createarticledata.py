import random,string
from random import seed, choice, randint

import faker.providers
from django.core.management.base import BaseCommand
from faker import Faker
from MArticles.models import *
from django.contrib.auth.models import User
"""Faker doesn't provide categories so we will make custom using faker.providers"""


CATEGORIES = [
    "WebDevelopment",
    "AndroidDevelopment",
    "Technology",
    "HowTo?",
    "Desigining",
    "Dev-Ops",
    "Frontend",
    "Deployment",
]
SITEVIEWERS= [
    "quora.com",
    "google.com",
    "edx.org",
    "coursera.org",
    "sameershahithakuti111.com.np",
    "learningsansar.com",
    "onlinekhabar.com",
    "meronepal.com",
    "meroshare.com",
]
ARTICLES = [
    "C++ Program to multiply two numbers",
    "DocKer Guide",
    "Assembly Program to multiply two 8 bit numbers",
    "C Program to find fibonacci series",
    "Github Guide",
    "Django Mode lCheatsheet",
    "Django Forms Cheatsheet",
]

"""adding list to fake.provides.BaseProvider"""
class Provider(faker.providers.BaseProvider):
    def article_category(self):
        return self.random_element(CATEGORIES)

    def ipmodels(self):
        return self.random_element(SITEVIEWERS)

    def article_models(self):
        return self.random_element(ARTICLES)

category_queryset=Category.objects.all()

class Command(BaseCommand):
    help = "Command information"

    def handle(self, *args, **kwargs):

        fake = Faker(["en_US"])
        fake.add_provider(Provider)  #adding data to provider
        
        def flip_coin():
            """Returns True or False with equal probability"""
            return choice([True, False])        
        
        def rand_alphanumeric(n):
            """Returns random string of alphanumeric characters of length n"""
            r = ''.join(random.choice(string.ascii_uppercase + string.digits)
                        for _ in range(n))
            return r
        for _ in range(3):
            categories=choice(category_queryset),#get certain category
            description=fake.paragraph(),
            email = fake.email(domain='gmail.com')
            license_plate=rand_alphanumeric(6);
            username = fake.unique.first_name();
            image=fake.image_url(width=1000, height=920)
            password =str(fake.unique.first_name()+fake.currency_code()+fake.unique.date(pattern='%Y'));
            password2 = fake.password(length=7, special_chars=False)
            print(username,'\n',password2,image,'\n')
            print(categories);
            print(license_plate);
            print(email)

'''
    
        for _ in range(7):
            d = fake.unique.article_category();
            category_obj = Category.objects.create(name=d)
            print(category_obj," created!")

        for _ in range(100):
            d = fake.ipmodels();
            ipmodel_obj = IpModel.objects.create(ip=d)
            print("\n",ipmodel_obj," created!")

        for _ in range(15):
            title = fake.text(max_nb_chars=100)
            categoryid = random.randint(1, 7)
            articleid = random.randint(1, 15)
            publishedtime=fake.date()
            updatedtime=fake.date()            
            Article.objects.create(
                product_type_id=articleid,
                category_id=categoryid,
                title=title,
                description=fake.text(max_nb_chars=800),
                published_date=publishedtime,
                last_updated = updatedtime,
                #discount_price=(round(random.uniform(10.99, 49.99), 2)),
            )


        check_category = Category.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of categories: {check_category}"))
'''