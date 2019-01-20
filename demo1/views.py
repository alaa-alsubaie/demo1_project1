from django.shortcuts import render
from .models import Resturant
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.generics import ListAPIView,RetrieveUpdateAPIView,DestroyAPIView,RetrieveAPIView
from .serializers import ListSerializer,DetailSerializer



# Create your views here.

def resturant_info(request):
	res = Resturant.objects.all()

	return HttpResponse("HEEEEElllo")



class ListApiView(ListAPIView):
	queryset = Resturant.objects.all()
	serializer_class = ListSerializer
	


class DetailApiView(RetrieveAPIView):
	queryset = Resturant.objects.all()
	serializer_class = DetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'x'



class UpdateApiView(RetrieveUpdateAPIView):
	queryset = Resturant.objects.all()
	serializer_class = ListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'x'



class DeleteView(DestroyAPIView):
	queryset = Resturant.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'x'

    

