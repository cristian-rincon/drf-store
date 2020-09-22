from rest_framework import serializers

from . import models
from users.models import User

class BillSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'client_id', 'company_name', 'nit', 'code')
        model = models.Bill


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name', 'description', 'attribute')
        model = models.Product


class UploadUsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('id', 'username', 'document', 'email', 'is_client')
        model = User