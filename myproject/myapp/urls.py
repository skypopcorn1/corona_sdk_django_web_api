from django.conf.urls import url
from .views import (
	MyAppDeleteAPIView,
	MyAppListAPIView,
	MyAppRetrieveAPIView,
	MyAppUpdateAPIView
)

urlpatterns = [
    url(r'^$', MyAppListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', MyAppRetrieveAPIView.as_view(), name='retrieve'),
    url(r'^(?P<pk>\d+)/edit/$', MyAppUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', MyAppDeleteAPIView.as_view(), name='delete'),
]