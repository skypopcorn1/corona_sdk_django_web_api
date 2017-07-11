from rest_framework.serializers import(
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField
	)
from myapp.models import Person

url = HyperlinkedIdentityField(
		view_name = 'api:retrieve',
		lookup_field = 'pk'
		)
delete_url = HyperlinkedIdentityField(
		view_name = 'api:delete',
		lookup_field = 'pk'
		)
update_url = HyperlinkedIdentityField(
		view_name = 'api:update',
		lookup_field = 'pk'
		)

class MyAppUpdateSerializer(ModelSerializer):
	class Meta:
		model = Person
		fields = "__all__"

class MyAppListSerializer(ModelSerializer):
	detail = url
	first_name = SerializerMethodField()
	class Meta:
		model = Person
		fields = [
			'detail',
		    'first_name',
		    'last_name',
		    'create_at',
		]	

	def get_first_name(self, obj):
		return str(obj.first_name)

class MyAppRetrieveSerializer(ModelSerializer):
	class Meta:
		model = Person
		fields = [
			'id',
		    'first_name',
		    'last_name',
		    'create_at',
		]	