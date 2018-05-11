from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from lib.response import ApiResponse
from django.views.generic import TemplateView
from app.equipment.serializers import EquipmentSerializer
from app.equipment.models import Equipment


# Create your views here.
class AddEquipment(APIView):
	def post(self,request):
		try:
			print(request.data)
			equipment_data = EquipmentSerializer(data=request.data)
			if not(equipment_data.is_valid()):
				return ApiResponse().error("Error", 400)
			equipment_data.save()
			return ApiResponse().success("Successfully inserted", 201)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in inserting Equipment", 400)

	def get(self,request):
		try:
			get_equipment = Equipment.objects.filter(is_deleted=False)
			equipment_data = EquipmentSerializer(get_equipment,many=True)
			return ApiResponse().success(equipment_data.data, 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in Getting Equipment", 400)

	def delete(self,request,equipment_id):
		try:
			Equipment.objects.filter(pk=equipment_id).update(is_deleted=True)
			return ApiResponse().success("Successfully Deleted", 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Please send valid id", 400)

class EquipmentTemplate(TemplateView):
	def get(self,request):
		return render(request,'admin/equipment.html')