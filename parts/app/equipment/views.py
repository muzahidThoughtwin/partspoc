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

	def get(self,request,equipment_id=None):
		try:
			if(equipment_id):
				get_equipment = Equipment.objects.filter(is_deleted=False,pk=equipment_id)[0]
				equipment_data = EquipmentSerializer(get_equipment)
			else:
				get_equipment = Equipment.objects.filter(is_deleted=False)
				equipment_data = EquipmentSerializer(get_equipment, many=True)
			return ApiResponse().success(equipment_data.data, 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Please send valid id", 400)

	def put(self,request,equipment_id):
		try:
			equipment_data = Equipment.objects.get(pk=equipment_id)
			update_data = EquipmentSerializer(equipment_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return ApiResponse().success("Successfully Updated", 200)
			else:
				return ApiResponse().error("Please send valid id", 400)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in Updating Equipment", 400)
			

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