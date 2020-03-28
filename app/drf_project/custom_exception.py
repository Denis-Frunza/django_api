from django.http import Http404
from movies.views import SingleMovieAPiView, SingleReviewAPiView
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException, NotAuthenticated, MethodNotAllowed


class ServiceUnavailable(APIException):
    status_code = 500
    default_detail = 'Service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(context['view'], SingleMovieAPiView):
        if isinstance(exc, Http404):
            response.data = "That Movie doesn't exist.Enter a different movie"
            return response
    elif isinstance(context['view'], SingleReviewAPiView):
        if isinstance(exc, Http404):
            response.data = "That review doesn't exist.Enter a different review"
            return response
    elif isinstance(exc, NotAuthenticated):
        response.data = 'please login to leave a review'
        return response

    # response = Response(status=500)
    # if hasattr(exc, 'strerror'):
    #     response.data = {'message': exc.strerror}
    # else:
    #     response.data = {'message': 'Server error'}
    # return response
