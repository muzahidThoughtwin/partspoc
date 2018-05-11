from django.shortcuts import render
from rest_framework.views import APIView
from lib.response import ApiResponse
from django.views.generic import TemplateView
from app.built.serializers import BuiltSerializer
from app.built.models import Built


# Create your views here.
class AddBuilt(APIView):
	def get(self,request,built_id=None):
		try:
			if(built_id):
				get_built = Built.objects.filter(is_deleted=False,pk=built_id)[0]
				built_data = BuiltSerializer(get_built)
			else:
				get_built = Built.objects.filter(is_deleted=False)
				built_data = BuiltSerializer(get_built,many=True)
			return ApiResponse().success(built_data.data, 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in Getting Built", 400)
		return ApiResponse().success("Built Successfully Got", 201)

	def post(self,request):
		try:
			print(request.data)
			built_data = BuiltSerializer(data=request.data)
			if not(built_data.is_valid()):
				return ApiResponse().error("Error", 400)
			built_data.save()
			return ApiResponse().success("Built Successfully inserted", 201)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in inserting Built", 400)

	def put(self,request,built_id):
		try:
			built_data = Built.objects.get(pk=built_id)
			update_data = BuiltSerializer(built_data,data=request.data)
			print(request.data)
			if update_data.is_valid():
				update_data.save()
				return ApiResponse().success("Successfully Updated", 200)
			else:
				return ApiResponse().error("Please send valid id", 400)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in Updating Built", 400)
			
	def delete(self,request,built_id):
		try:
			Built.objects.filter(pk=built_id).update(is_deleted=True)
			return ApiResponse().success("Successfully Deleted", 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Please send valid id", 400)


class BuiltTemplate(TemplateView):
	def get(self,request):
		return render(request,'admin/built.html')