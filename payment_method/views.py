import stripe
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import(
    Charge
)
from account.models import(
    User
)
from .serializer import(
    ChargeSerializer
)
from django.conf import settings
from rest_framework.permissions import (
    IsAuthenticated
)
from rest_framework_simplejwt.authentication import (
    JWTAuthentication
)


# Create your views here.

#my stripe
stripe.api_key = 'sk_test_51Mei6tA4Xf1XOr7ROyXtE7oBA3CUKjMg3jhpbjcc9EgCzFENvPxQfRxe0caqLIvHokpUNwLEazVeJMmkeHgW6G1y00fHxP7I11'

#client stripe
#stripe.api_key = 'pk_live_51KH8ijFQRvmRrSikRd1spAjHsW9D18eN8Sx8XpvolnHWbtiajBHT4klGOSLUdgEfHazQIHBTgw5IxnznGcWMIw8R00kwdrZrEk'

class StripePaymentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        try:
            user_email = request.user.email
            user = User.objects.get(email=user_email)
            user.is_subscribed = True
            user.save()


            # Create a charge on Stripe
            amount = request.data['amount']
            charge = stripe.Charge.create(
                amount=int(amount * 100),
                currency='usd',
                source=request.data['token']
            )

            # Create a charge in the database
            charge_obj = Charge.objects.create(
                amount=amount,
                stripe_charge_id=charge.id,
                user=request.user
            )

            # Serialize and return the charge
            serializer = ChargeSerializer(charge_obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)


