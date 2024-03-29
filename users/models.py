from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, name, date_of_birth, gender, country, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            name = name,
            date_of_birth = date_of_birth,
            gender = gender,
            country = country,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, date_of_birth, gender, country, password, **extra_fields):
        return self._create_user(email,name, date_of_birth, gender, country, password, False, False, **extra_fields)

    def create_superuser(self,  email, name, date_of_birth, gender, country, password, **extra_fields):
        user = self._create_user( email, name, date_of_birth, gender, country,password, True, True, **extra_fields)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    date_of_birth = models.CharField(max_length=13,null=True, blank=True)
    gender = models.CharField(max_length=50,null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name','date_of_birth','gender','country']

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)

    def get_user_type(self):
        return self.email

'''
class A1(models.Model):
    category = models.CharField(max_length=100, null=True)
    text = models.TextField(blank=True, null=True)

    REQUIRED_FIELDS = ['category', 'text']

    def __str__(self):
        return '%s  %s' % (self.category, self.text)

class A2(models.Model):
    category = models.CharField(max_length=100, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s  %s' % (self.category, self.text)

class A3 (models.Model):
    category = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s  %s' % (self.category, self.text)

class A4 (models.Model):
    category = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s  %s' % (self.category, self.text)

class A5 (models.Model):
    category = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s  %s' % (self.category, self.text)

class A6 (models.Model):
    category = models.CharField(max_length=100)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return '%s  %s' % (self.category, self.text)

class Counter(models.Model):
    language = models.CharField(max_length=100)
    languagetwo = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    a1 = models.CharField(max_length=100)
    a2 = models.CharField(max_length=100)
    a3 = models.CharField(max_length=100)
    a4 = models.CharField(max_length=100)
    a5 = models.CharField(max_length=100)
    a6 = models.CharField(max_length=100)

    def __str__(self):
        return '%s  %s %s  %s  %s  %s  %s  %s  %s ' % (self.language, self.languagetwo, self.email, self.a1, self.a2, self.a3, self.a4, self.a5, self.a6)

'''