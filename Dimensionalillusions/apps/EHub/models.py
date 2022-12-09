from django.contrib.auth.models import User
from django.core.checks import messages
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.timezone import now


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(username=instance, email=instance.email)
        profile.save()


from django.core.validators import (
    FileExtensionValidator,
    MaxValueValidator,
    MinValueValidator,
)


def user_image_path():
    return "Profiles/"


class Media(models.Model):
    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to="images/", blank=True)


# Create your models here.
class Profile(models.Model):
    Gender_Choices = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]
    username = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.SlugField(max_length=10, null=True)
    second_name = models.CharField(max_length=10, null=True)

    email = models.EmailField(max_length=140, null=True, blank=True)
    image = models.URLField(
        blank=True,
        null=True,
    )
    gender = models.CharField(choices=Gender_Choices, null=True, max_length=50)
    date_joined = models.DateTimeField(auto_now_add=True)  # datetimefield responds to timezone
    auth_token = models.CharField(max_length=100, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse("profileinfo", kwargs={"pk": self.id})


class Contact(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=140, null=True)
    message = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Message from " + str(self.name)


class EmailSubscription(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)
