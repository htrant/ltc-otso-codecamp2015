__author__ = 'hieutran'

from django.conf.urls import patterns, url
from oven.customer import customer_views

urlpatterns = patterns(
    '',
    url(r'^feedback/answer', customer_views.FeedbackAnswerView.as_view()),
)
