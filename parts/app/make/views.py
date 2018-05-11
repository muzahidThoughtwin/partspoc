from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from lib.response import ApiResponse
from django.views.generic import TemplateView
from app.make.serializers import MakeSerializer
from app.make.models import Make

# Create your views here.
class AddMake(APIView):
	def get(self,request):
		try:
			get_make = Make.objects.filter(is_deleted=False)
			make_data = MakeSerializer(get_make,many=True)
			return ApiResponse().success(make_data.data, 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in Getting Equipment", 400)
		return ApiResponse().success("Successfully inserted", 201)

	def post(self,request):
		try:
			make_data = MakeSerializer(data=request.data)
			if not(make_data.is_valid()):
				return ApiResponse().error("Error", 400)
			make_data.save()
			return ApiResponse().success("Successfully inserted", 201)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in inserting Equipment", 400)
		return ApiResponse().success("Successfully inserted", 201)

	def delete(self,request,make_id):
		try:
			Make.objects.filter(pk=make_id).update(is_deleted=True)
			return ApiResponse().success("Successfully Deleted", 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Please send valid id", 400)

class MakeTemplate(TemplateView):
	def get(self,request):
		return render(request,'admin/make.html')