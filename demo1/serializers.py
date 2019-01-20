from rest_framework import serializers

from .models import Resturant


class ListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Resturant
		fields = ['id','title',]




class DetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Resturant
		fields = '__all__'