from rest_framework import generics

from .models import Client, Bill, Product
from .serializers import ClientSerializer, BillSerializer, ProductSerializer


class CreateClient(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientList(generics.ListAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CreateBill(generics.CreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillList(generics.ListAPIView):

    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class BillDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Bill.objects.all()
    serializer_class = BillSerializer


class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
