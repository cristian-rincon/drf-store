from django.db import models

from utils.models import StoreModel

class Profile(StoreModel):
    """
    Simple public user model.

    """
    
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
