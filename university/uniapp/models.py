from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Application(models.Model):

    name = models.CharField(max_length=70)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    university = models.CharField(max_length=70)
    program = models.CharField(max_length=70)
    studyType = models.TextChoices("Online", "Offline")
    study_mode = models.CharField(choices=studyType, max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    leave_reason = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.name
