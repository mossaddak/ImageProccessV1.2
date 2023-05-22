from django.contrib import admin
from django.urls import path
from .views import (
    StripePaymentView,
    VerifyPayment
)

urlpatterns = [
    path('get-payment-intent/', StripePaymentView.as_view(), name='get-payment-intent'),
    path('verify-payment/', VerifyPayment.as_view(), name='verify-payment')
]