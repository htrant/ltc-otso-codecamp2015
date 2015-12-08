__author__ = 'hieutran'

from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from oven.models import Component
from oven.sub.sub_serializers import ComponentSerializer


class ComponentView(APIView):
    def __init__(self):
        object.__init__(self)
        self.data_response = {}

    def post(self, request):
        pass

    ### Get all available components ####
    def get(self, request):
        components = Component.objects.all()
        all_data = []
        for component in components:
            all_data.append(ComponentSerializer(component).data)
        self.data_response = {
            'success': True,
            'data' : all_data
        }
        return Response(self.data_response, status=status.HTTP_200_OK)

    def put(self, request):
        pass

    def delete(self, request):
        pass
