__author__ = 'hieutran'

from django.conf.urls import patterns, url
from oven.sub import sub_views

urlpatterns = patterns(
    '',
    url(r'^component', sub_views.ComponentView.as_view()),
)
