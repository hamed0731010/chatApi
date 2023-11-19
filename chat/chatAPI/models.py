from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):

    def create_user(self, username, first_name, last_name, password=None, email=None, is_active=True):
        if not username:
            raise ValueError('Users must have a username')
        username = self.normalize_email(username)
        user = self.model(username=username, first_name=first_name, last_name=last_name, 
                          str_password=password, email=email, is_active=is_active)
        user.set_password(password)
        return user


    def create_superuser(self, username, first_name, last_name, password, is_superuser=True):
        user = self.create_user(username, first_name, last_name, password)
        user.is_active = True
        user.is_superuser = is_superuser
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=128, unique=True)
    email = models.EmailField(null=True, blank=True)
    first_name = models.CharField(max_length=128, default='', blank=True)
    last_name = models.CharField(max_length=128, default='', blank=True)
    is_staff = models.BooleanField(default=False)
    last_sent_msg = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name']



class Message(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')        
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')        
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)