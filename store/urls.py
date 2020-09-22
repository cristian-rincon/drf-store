from django.urls import path

from . import views

urlpatterns = [
    path('bills/', views.BillList.as_view()),
    path('bills/new/', views.CreateBill.as_view()),
    path('bill/<int:pk>', views.BillDetail.as_view()),
    path('products/', views.ProductList.as_view()),
    path('products/new/', views.CreateProduct.as_view()),
    path('product/<int:pk>', views.ProductDetail.as_view()),
]
