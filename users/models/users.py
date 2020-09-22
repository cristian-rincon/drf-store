from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

from utils.models import StoreModel

class User(StoreModel, AbstractUser):
    

    document = models.PositiveIntegerField(default=0)
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        }
    )




    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    is_client = models.BooleanField(
        'client status',
        default = True,
        help_text=(
            'Help to distinguish users and perform queries'
        )

    )


    def __str__(self):
        """Return username"""
        return self.username

    def get_short_name(self):
        return self.username