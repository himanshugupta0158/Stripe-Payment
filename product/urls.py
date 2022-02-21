from django.urls import path
from .views import (
    CreateCheckoutSessionView,
    CancelView,
    Products,
    Buy_Product,
    Order_Product
)

app_name = "payment"

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', Products.as_view(), name='product'),
    path('buy/<int:pk>', Buy_Product.as_view(), name='buy'),
    path('order/', Order_Product.as_view(), name='order'),
]
