__author__ = 'hieutran'

from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from oven.models import Assignment, Contractor, Component
from oven.bigboss.bigboss_serializers import AssignmentRegSerializer


class AssignmentView(APIView):
    def __init__(self):
        object.__init__(self)
        self.data_response = {}

    def post(self, request):
        self.data_response = {}
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
        assignment.component = data['component']
        assignment.deadline = deadline
        assignment.requirement = requirement
        assignment.rating = 0
        assignment.save()
        self.data_response = {
            'success': True,
            'data' : {
                'id': assignment.id,
                'name': assignment.name,
                'contractor': assignment.contractor,
                'deadline': assignment.deadline,
                'requirement': assignment.requirement,
                'rating': assignment.rating
            }
        }
        return Response(self.data_response, status=status.HTTP_200_OK)

    def get(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class AssignmentDetailView(APIView):
    def __init__(self):
        object.__init__(self)
        self.data_response = {}

    def post(self, request):
        pass

    ### Get one assignment's detail ###
    def get(self, request, id):
        assignment = Assignment.objects.get(pk=id)
        component = Component.objects.get(pk=assignment.component)
        contractor = Contractor.objects.get(pk=assignment.contractor)
        return_data = {
            'id'        : assignment.id,
            'name'      : assignment.name,
            'requirement': assignment.requirement,
            'deadline'  : assignment.deadline,
            'contractor': contractor.name,
            'component' : component.name,
            'rating'    : assignment.rating
        }
        self.data_response = {
            'success'   : True,
            'data'      : return_data
        }
        return Response(self.data_response, status=status.HTTP_200_OK)

    def put(self, request):
        self.data_response = {}
        if 'id' not in request.data and 'rating' not in request.data:
            self.data_response = {
                'success': False,
                'data': {}
            }
            return Response(self.data_response, status=status.HTTP_200_OK)
        assignment = Assignment.objects.get(pk=request.data['assignment_id'])
        assignment.rating = request.data['rating']
        assignment.save()
        self.data_response = {
            'success': True,
            'data': {
                'id': assignment.id,
                'name': assignment.name,
                'contractor': assignment.contractor,
                'deadline': assignment.deadline,
                'requirement': assignment.requirement,
                'rating': assignment.rating
            }
        }
        return Response(self.data_response, status=status.HTTP_200_OK)

    def delete(self, request):
        pass


class AssignmentAllView(APIView):
    def __init__(self):
        object.__init__(self)
        self.data_response = {}

    def post(self, request):
        pass

    ### Get all set assignments ###
    def get(self, request):
        self.data_response = {}
        assignments = Assignment.objects.all()
        all_data = []
        for assignment in assignments:
            assignment_data = {
                'id'    : assignment.id,
                'name'  : assignment.name
            }
            all_data.append(assignment_data)
        self.data_response = {
            'success': True,
            'data' : all_data
        }
        return Response(self.data_response, status=status.HTTP_200_OK)

    def put(self, request):
        pass

    def delete(self, request):
        pass
