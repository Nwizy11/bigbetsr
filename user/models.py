from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractUser, PermissionsMixin)
from django.urls import reverse
# Create your models here.

'''BaseManager'''
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('No email provided')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        return user
    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

'''Custom user'''
class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, verbose_name='Full name')
    reciept = models.ImageField(upload_to='images')
    plan = models.BooleanField(max_length=400, null=True)
    is_active = models.BooleanField(default=True)
    is_confirm = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_level):
        return True
    @property
    def is_staff(self):
        return self.is_admin
    def __str__(self):
        return self.email
    def get_absolute_url(self):
        return reverse('home')