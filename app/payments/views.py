import stripe
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context

    @staticmethod
    def charge(request):
        if request.method == 'POST':
            charge = stripe.Charge.create(
                amount=500,
                currency='usd',
                description='A Django charge',
                source=request.POST['stripeToken']
            )
        return render(request, 'charge.html')

# class ChargeAPI(APIView):
#
#     def post(self, request, format=None):
#         stripe.Charge.create(
#             amount=500,
#             currency='usd',
#             description='A Django charge',
#         )