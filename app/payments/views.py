import stripe
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView


stripe.api_key = settings.STRIPE_SECRET_KEY


class ChargeAPI(APIView):
    def post(self, request, format=None):
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description=request.data['movie'],
            source=request.data['token']
        )
        response_object = {
            'status': 'success',
            'charge': charge
        }
        return Response(response_object)
