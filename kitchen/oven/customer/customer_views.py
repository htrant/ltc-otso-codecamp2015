__author__ = 'hieutran'

from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from oven.models import CustomerFeedback
from oven.customer.customer_serializer import CustomerFeedbackAnswerSerializer


class FeedbackAnswerView(APIView):
    def __init__(self):
        object.__init__(self)
        self.data_response = {}

    def post(self, request):
        # self.data_response = {}
        # serializer = CustomerFeedbackAnswerSerializer(data=request.data)
        # if not serializer.is_valid():
        #     self.data_response = {
        #         'success': False,
        #         'data': {}
        #     }
        #     return Response(self.data_response, status=status.HTTP_200_OK)
        # data = request.data
        # customer_feedback = CustomerFeedback.objects.create()
        # customer_feedback.name = data['name']
        # customer_feedback.phone = data['phone']
        # customer_feedback.email = data['email']
        # customer_feedback.social_number = data['social_number']
        # customer_feedback.address = data['address']
        # customer_feedback.component = data['component']
        # customer_feedback.problem = data['problem']
        # customer_feedback.rating = data['rating']
        # customer_feedback.save()
        # self.data_response = {
        #     'success': True,
        #     'data' : {
        #         'id': customer_feedback.id,
        #         'name': .customer_feedback.name,
        #         'phone': customer_feedback.phone,
        #         'email': customer_feedback.email,
        #         'address': customer_feedback.address,
        #         'social_number': customer_feedback.social_number,
        #         'problem': customer_feedback.problem,
        #         'rating': customer_feedback.rating
        #     }
        # }
        return Response(self.data_response, status=status.HTTP_200_OK)

    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass