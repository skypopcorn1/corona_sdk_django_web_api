from rest_framework.serializers import ModelSerializer
from myapp.models import Person

class MyAppListSerializer(ModelSerializer):
	class Meta:
		model = Person
		fields = [
		    'first_name',
		    'last_name',
		    'create_at',
		]	

class MyAppRetrieveSerializer(ModelSerializer):
	class Meta:
		model = Person
		fields = [
			'id',
		    'first_name',
		    'last_name',
		    'create_at',
		]	