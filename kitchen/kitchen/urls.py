__author__ = 'hieutran'

from django.conf import settings
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^api/bigboss/', include("oven.bigboss.bigboss_urls")),
    url(r'^api/sub/', include("oven.sub.sub_urls")),
    url(r'^api/customer', include("oven.customer.customer_urls")),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
