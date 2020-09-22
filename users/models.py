from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from utils.models import StoreModel

class User(StoreModel, AbstractUser):
    

    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )

    phone_number = models.CharField(max_length=17, blank=True)

    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default = True,
        help_text=(
            'Help to distinguish users and perform queries'
        )

    )

    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='Set to tue when the user have verified its email address.'
    )

    def __str__(self):
        """Return username"""
        return self.username

    def get_short_name(self):
        return self.username