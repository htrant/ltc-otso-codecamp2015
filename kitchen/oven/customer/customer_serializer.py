__author__ = 'hieutran'

from rest_framework import serializers
from oven.models import CustomerFeedback


class CustomerFeedbackAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFeedback
        fields = ('name', 'email', 'phone', 'address', 'social_number', 'component', 'problem', 'rate')
