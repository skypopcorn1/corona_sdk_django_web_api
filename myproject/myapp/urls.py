from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from .views import (
	MyAppCreateAPIView,
	MyAppDeleteAPIView,
	MyAppListAPIView,
	MyAppRetrieveAPIView,
	MyAppUpdateAPIView
)

urlpatterns = [
    url(r'^$', MyAppListAPIView.as_view(), name='list'),
    url(r'^create/$', MyAppCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', MyAppRetrieveAPIView.as_view(), name='retrieve'),
    url(r'^(?P<pk>\d+)/edit/$', MyAppUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', MyAppDeleteAPIView.as_view(), name='delete'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]