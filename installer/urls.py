from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'transactions', TransactionViewSet, basename='transaction')


urlpatterns = [
    path('', TaskAPIView.as_view(), name='task-list'),
    path('products/', ProductListView.as_view(), name='product-view'),
    path('transactions/', TransactionAPIView.as_view(), name='transaction-list'),
    path('payments/', PaymentAPIView.as_view(), name='payment-list')
]