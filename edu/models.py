from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save


class ContactUs(models.Model):
    title = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    text = models.TextField(max_length=250, null=True)


class UserProfile(models.Model):
    # This field is required.
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)


class Course(models.Model):
    DAY_CHOICES = [
        (0, 'shanbe'),
        (1, 'yeshanbe'),
        (2, 'doshanbe'),
        (3, 'seshanbe'),
        (4, 'charshanbe'),
    ]

    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course_number = models.IntegerField(unique=True)
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    first_day = models.IntegerField(choices=DAY_CHOICES)
    second_day = models.IntegerField(choices=DAY_CHOICES)
