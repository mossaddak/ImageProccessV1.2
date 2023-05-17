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
# stripe.api_key = 'sk_test_51Mei6tA4Xf1XOr7ROyXtE7oBA3CUKjMg3jhpbjcc9EgCzFENvPxQfRxe0caqLIvHokpUNwLEazVeJMmkeHgW6G1y00fHxP7I11'
stripe.api_key = 'sk_test_51N1vtNHYlHkFMKo7V6bmTauoRX6XnUlORpScFJN4XwFwnGXXMc9y0QJtyzVyetlEFRCIrA0d0QzDwPej59sp4hGQ00x8yH7Vg1'

#client stripe
#stripe.api_key = 'pk_live_51KH8ijFQRvmRrSikRd1spAjHsW9D18eN8Sx8XpvolnHWbtiajBHT4klGOSLUdgEfHazQIHBTgw5IxnznGcWMIw8R00kwdrZrEk'

class StripePaymentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def post(self, request):
        try:

            user_email = request.user.email
            user = User.objects.get(email=user_email)
            number = request.data['number']
            exp_month = request.data['exp_month']
            exp_year = request.data['exp_year']
            cvc = request.data['cvc']
            

            if user.is_subscribed == False:

                print("Card Number===========================================", number)
                # Create a test card token
                token = stripe.Token.create(
                    card={
                        'number': number,
                        'exp_month': exp_month,
                        'exp_year': exp_year,
                        'cvc': cvc
                    }
                )

                # Use the generated token for testing
                source_token = token.id

                # Create a charge on Stripe
                amount = 200
                charge_obj = stripe.Charge.create(
                    amount=int(amount * 100),
                    currency='usd',
                    source=source_token
                )

                # Create a charge in the database
                charge_obj = Charge.objects.create(
                    amount=amount,
                    stripe_charge_id=charge_obj.id,
                    user=request.user,
                    currency='usd',
                    number=number,
                    exp_month=exp_month,
                    exp_year=exp_year,
                    cvc=cvc
                )
                
                user.is_subscribed = True
                user.save()

                return Response(
                    {
                        "amount":charge_obj.amount,
                        "created":charge_obj.created,
                        "stripe_charge_id":charge_obj.stripe_charge_id
                    },
                    status=status.HTTP_201_CREATED
                )
            
            else:
                return Response(
                    {
                        'message':"You all ready subscribed"
                    },status=status.HTTP_403_FORBIDDEN
                )

        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

