from rest_framework import serializers
from .models import Charge

class VerifyPaymentSerializer(serializers.Serializer):
    client_secret = serializers.CharField()
