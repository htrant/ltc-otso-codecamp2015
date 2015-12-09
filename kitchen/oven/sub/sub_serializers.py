__author__ = 'hieutran'

from rest_framework import serializers
from oven.models import Component

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('name', 'note')
