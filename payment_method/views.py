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
    VerifyPaymentSerializer
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
            
            if user.is_subscribed == False:
                c_amount = 1
                intent = stripe.PaymentIntent.create(
                    amount=100*c_amount,
                    currency='usd',
                    payment_method_types=['card'],
                )

                Charge.objects.create(
                    user=request.user,
                    amount = c_amount,
                    client_secret = intent['client_secret'],
                    payment_id = intent['id']
                )

                return Response(
                    {
                        "message": "Payment intent created successfully",
                        "amount": c_amount,
                        "payment_id":intent['id'],
                        "client_secret":intent['client_secret'],
                        "publish_key":"pk_test_51N1vtNHYlHkFMKo7k8hRgsZ2oAjE6pfllmeRZJfau9OVZHmPB5gF5xmAFBiAxUQ2zMguR9n86BnBhW3Sey6plAlO00QrEq8Rgm",
                        "profile_picture" : []

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
    

class VerifyPayment(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        try:
            
            data = request.data
            serializer = VerifyPaymentSerializer(data=data)

            if serializer.is_valid():
                payment_id = serializer.data["payment_id"]
                charge = Charge.objects.get(payment_id=payment_id)

                # user_serializer = UserSerializer(data=charge.user)
                # print("user serilizer=======================>", user_serializer)

                if charge.user.is_subscribed == False:
                    charge.user.is_subscribed = True
                    charge.user.save()
                    print(charge.user.email)
                    return Response(
                        {
                            "message":"You successfully subscribed",
                            "data":{
                               "id":charge.user.id,
                                "username": charge.user.username,
                                "first_name": charge.user.first_name,
                                "last_name": charge.user.last_name,
                                "email": charge.user.email,
                                "profile_picture":[],
                                "is_superuser": charge.user.is_superuser,
                                "is_subscribed": charge.user.is_subscribed,
                                "is_verified": charge.user.is_verified
                            }
                        },
                        status=status.HTTP_201_CREATED
                    )
                else:
                    return Response(
                        {
                            "message":"You already subscribed"
                        },
                        status=status.HTTP_201_CREATED
                    )


        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

