from django.urls import path
from .views import ProductListAPI, ProductFormView, ProductListView

urlpatterns = [
    path('api/', ProductListAPI.as_view(), name='list_product_api'),
    path('', ProductListView.as_view(), name='list_product'),
    path('add/', ProductFormView.as_view(), name='add_product'),
]