from rest_framework import serializers
from .models import Charge

class VerifyPaymentSerializer(serializers.Serializer):
    payment_id = serializers.CharField()
