__author__ = 'hieutran'

from rest_framework import serializers
from oven.models import Component, Contractor


class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = ('name', 'note')


class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ('name', 'note', 'location')
