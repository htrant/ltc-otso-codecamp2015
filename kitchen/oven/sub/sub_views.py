__author__ = 'hieutran'

from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from oven.models import Component, Contractor
from oven.sub.sub_serializers import ComponentSerializer, ContractorSerializer


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
            component_data = ComponentSerializer(component).data
            component_data['id'] = component.id
            all_data.append(component_data)
        self.data_response = {
            'success': True,
            'data' : all_data
        }
        return Response(self.data_response, status=status.HTTP_200_OK)

    def put(self, request):
        pass

    def delete(self, request):
        pass


class ContractorView(APIView):
    def __init__(self):
        object.__init__(self)
        self.data_response ={}

    def post(self, request):
        pass

    ### Get all available contractors ####
    def get(self, request):
        contractors = Contractor.objects.all()
        all_data = []
        for contractor in contractors:
            contractor_data = ContractorSerializer(contractor).data
            contractor_data['id'] = contractor.id
            #contractor_data['component'] = contractor.component
            all_data.append(contractor_data)
        self.data_response = {
            'success': True,
            'data' : all_data
        }
        return Response(self.data_response, status=status.HTTP_200_OK)

    def put(self, request):
        pass

    def delete(self, request):
        pass
