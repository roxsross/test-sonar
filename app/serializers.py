from rest_framework import serializers
from .models import Task, Car, Product

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'


class CarSerializer(serializers.ModelSerilzer):
	class Meta:
		model = Car
		fields = '__all__'

class ProductSerilizer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = '__all__'

