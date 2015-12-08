__author__ = 'hieutran'

from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from oven.models import Assignment
from oven.bigboss.bigboss_serializers import AssignmentRegSerializer


class AssignmentRegView(APIView):
    def __init__(self):
        object.__init__(self)
        self.data_response = {}

    def post(self, request):
        serializer = AssignmentRegSerializer(data=request.data)
        if not serializer.is_valid():
            self.data_response = {
                'success': False,
                'data': {}
            }
            return Response(self.data_response, status=status.HTTP_200_OK)
        data = request.data
        name = data['name']
        contractor = data['contractor']
        deadline = data['deadline']
        requirement = data['requirement']
        assignment = Assignment.objects.create(name=name)
        assignment.contractor = contractor
        assignment.deadline = deadline
        assignment.requirement = requirement
        assignment.save()
        self.data_response = {
            'success': True,
            'data' : {
                'id': assignment.id,
                'name': assignment.name,
                'contractor': assignment.contractor,
                'deadline': assignment.deadline,
                'requirement': assignment.requirement
            }
        }
        return Response(self.data_response, status=status.HTTP_200_OK)

    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
