__author__ = 'hieutran'

from rest_framework import serializers
from oven.models import Assignment

class AssignmentRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ('name', 'contractor', 'deadline')