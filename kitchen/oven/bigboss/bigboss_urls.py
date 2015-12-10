__author__ = 'hieutran'

from django.conf.urls import patterns, url
from oven.bigboss import bigboss_views

urlpatterns = patterns(
    '',
    url(r'^create', bigboss_views.AssignmentView.as_view()),
    url(r'^assignment/(?P<id>[0-9]+)$', bigboss_views.AssignmentDetailView.as_view()),
    url(r'^assignment', bigboss_views.AssignmentAllView.as_view()),
    url(r'^feedback', bigboss_views.FeedbackRequestView.as_view()),
)
