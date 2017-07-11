from django.db.models import Q
from django.shortcuts import render

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView, 
	RetrieveAPIView,
	RetrieveUpdateAPIView,
	UpdateAPIView
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly
	)

from .models import Person
from .serializers import (
	MyAppUpdateSerializer, 
	MyAppListSerializer, 
	MyAppRetrieveSerializer
	)
class MyAppCreateAPIView(CreateAPIView):
	queryset = Person.objects.all()
	serializer_class = MyAppRetrieveSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


class MyAppDeleteAPIView(DestroyAPIView):
	queryset = Person.objects.all()
	serializer_class = MyAppRetrieveSerializer

class MyAppListAPIView(ListAPIView):
	
	serializer_class = MyAppListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['first_name', 'last_name', 'create_at' ]

	def get_queryset(self, *args, **kwargs):
		queryset_list = Person.objects.all()
		query = self.request.GET.get("q")

		if query:
			queryset_list = queryset_list.filter(
				Q(first_name__contains=query)|
				Q(last_name__contains=query)
				)
		return queryset_list
		
class MyAppRetrieveAPIView(RetrieveAPIView):
	queryset = Person.objects.all()
	serializer_class = MyAppRetrieveSerializer

class MyAppUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Person.objects.all()
	serializer_class = MyAppUpdateSerializer

	def put(self, request, *args, **kwargs):
		return self.partial_update(request, *args, **kwargs)

def index(request):
	return render(request, 'index.html')