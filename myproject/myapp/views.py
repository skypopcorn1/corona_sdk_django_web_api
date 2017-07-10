from rest_framework.generics import (
	DestroyAPIView,
	ListAPIView, 
	RetrieveAPIView,
	UpdateAPIView
	)
from .models import Person
from .serializers import MyAppListSerializer, MyAppRetrieveSerializer

class MyAppDeleteAPIView(DestroyAPIView):
	queryset = Person.objects.all()
	serializer_class = MyAppRetrieveSerializer

class MyAppListAPIView(ListAPIView):
	queryset = Person.objects.all()
	serializer_class = MyAppListSerializer
		
class MyAppRetrieveAPIView(RetrieveAPIView):
	queryset = Person.objects.all()
	serializer_class = MyAppRetrieveSerializer

class MyAppUpdateAPIView(UpdateAPIView):
	queryset = Person.objects.all()
	serializer_class = MyAppRetrieveSerializer