__author__ = 'hieutran'

from django.conf.urls import patterns, url
from oven.bigboss import bigboss_views

urlpatterns = patterns(
    '',
    url(r'^create', bigboss_views.AssignmentRegView.as_view()),
)
