from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Review(models.Model):
    user = models.CharField(max_length=255)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    comment = models.TextField(default="")
    rating = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
