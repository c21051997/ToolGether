from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
import random
import os

# Create your models here.

# To automatically create one to one objects
from django.db.models.signals import post_save
from django.dispatch import receiver

class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email must be provided")
        if not password:
            raise ValueError("The password must be provided")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True, null=False)

    is_staff=models.BooleanField(
        gettext_lazy('Staff Status'), default=False,
        help_text=gettext_lazy('Designates whether the user can login the site')
        )
    
    is_active=models.BooleanField(
        gettext_lazy('active'), default=True,
        help_text=gettext_lazy('Designates whether this user should be treated as active')
        )
    
    USERNAME_FIELD = 'email'
    objects=MyUserManager()

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    firstname = models.CharField(max_length=264, blank=True, default="John")
    lastname = models.CharField(max_length=264, blank=True, default="Smith")
    address = models.TextField(max_length=300, blank=True, default="000")
    postcode = models.CharField(max_length=10, blank=True, default="000")
    phone = models.CharField(max_length=20, blank=True, default="000")
    date_joined = models.DateTimeField(auto_now_add=True)

    def imageFolder():
        same = True
        while same == True:
            imageFolder = random.randint(100000000, 999999999)
            if os.path.exists("media/profile_img/" + str(imageFolder)):
                same = True
            else:
                same = False
        return str(imageFolder)
    
    a = imageFolder()
    profile_picture = models.ImageField(upload_to='media/profile_img/{}'.format(a), blank=True, default="media\pg.png")

    def __str__(self):
        return self.firstname + "'s Profile"
    
    def is_fully_filled(self):
        fields_name = [f.name for f in self._meta.get_fields()]
        for fields_name in fields_name:
            value = getattr(self, fields_name)
            if value is None or value == '':
                return False
        return True


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


