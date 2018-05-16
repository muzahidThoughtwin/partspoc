from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from lib.response import ApiResponse
from django.views.generic import TemplateView
from app.equipment.serializers import EquipmentSerializer
from app.equipment.models import Equipment
from app.part_details.models import PartsType,PartsName,PartsDetail
from app.part_details.serializers import PartsTypeSerializer,PartsNameSerializer,PartsDetailSerializer

# Create your views here.
class PartsTypeViewset(APIView):
	def get(self,request,parts_type_id=None):
		try:
			if(parts_type_id):
				get_parts_type = PartsType.objects.filter(is_deleted=False,pk=parts_type_id)[0]
				parts_type_data = PartsTypeSerializer(get_parts_type)
			else:
				get_parts_type = PartsType.objects.filter(is_deleted=False)
				parts_type_data = PartsTypeSerializer(get_parts_type, many=True)
			return ApiResponse().success(parts_type_data.data, 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Please send valid id", 400)

	def post(self,request):
		try:
			print(request.data)
			parts_type_data = PartsTypeSerializer(data=request.data)
			if not(parts_type_data.is_valid()):
				return ApiResponse().error("Error", 400)
			parts_type_data.save()
			return ApiResponse().success("Successfully inserted", 201)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in inserting Add Parts", 400)


	def put(self,request,parts_type_id):
		try:
			parts_type_data = PartsType.objects.get(pk=parts_type_id)
			update_data = PartsTypeSerializer(parts_type_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return ApiResponse().success("Successfully Updated", 200)
			else:
				return ApiResponse().error("Please send valid id", 400)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in Updating Parts Type", 400)
			

	def delete(self,request,parts_type_id):
		try:
			PartsType.objects.filter(pk=parts_type_id).update(is_deleted=True)
			return ApiResponse().success("Successfully Deleted", 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Please send valid id", 400)

class PartsTypeTemplate(TemplateView):
	def get(self,request):
		return render(request,'admin/partstype.html')

class PartsNameViewset(APIView):
	def get(self,request,parts_name_id=None):
		try:
			if(parts_name_id):
				parts_name_name = PartsName.objects.filter(is_deleted=False,pk=parts_name_id)[0]
				parts_name_data = PartsNameSerializer(parts_name_name)
			else:
				parts_name_name = PartsName.objects.filter(is_deleted=False)
				parts_name_data = PartsNameSerializer(parts_name_name, many=True)
			return ApiResponse().success(parts_name_data.data, 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Please send valid id", 400)

	def post(self,request):
		try:
			print(request.data)
			parts_name_data = PartsNameSerializer(data=request.data)
			if not(parts_name_data.is_valid()):
				return ApiResponse().error("Error", 400)
			parts_name_data.save()
			return ApiResponse().success("Successfully inserted", 201)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in inserting Add Parts", 400)


	def put(self,request,parts_name_id):
		try:
			parts_name_data = PartsName.objects.get(pk=parts_name_id)
			update_data = PartsNameSerializer(parts_name_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return ApiResponse().success("Successfully Updated", 200)
			else:
				return ApiResponse().error("Please send valid id", 400)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in Updating Parts Type", 400)
			

	def delete(self,request,parts_name_id):
		try:
			PartsName.objects.filter(pk=parts_name_id).update(is_deleted=True)
			return ApiResponse().success("Successfully Deleted", 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Please send valid id", 400)

class PartsNameTemplate(TemplateView):
	def get(self,request):
		return render(request,'admin/partsname.html')

class PartsDetailViewset(APIView):
	def get(self,request,parts_detail_id=None):
		try:
			if(request.GET.get('parts_name')):
				# get_parts_detail = PartsDetail.objects.filter(is_deleted=False,parts_name=request.GET.get('parts_name'))
				# get_parts_detail_data = PartsDetailSerializer(get_parts_detail,many=True)


				get_parts_detail_data = PartsDetailSerializer(PartsDetail.objects.filter(is_deleted=False,parts_name=request.GET.get('parts_name')), many=True)
				return ApiResponse().success(get_parts_detail_data.data, 200)
			elif(parts_detail_id):
				get_parts_detail = PartsDetail.objects.filter(is_deleted=False,pk=parts_detail_id)[0]
				get_parts_detail_data = PartsDetailSerializer(get_parts_detail)
				return ApiResponse().success(get_parts_detail_data.data, 200)
			else:
				get_parts_detail = PartsDetail.objects.filter(is_deleted=False)
				get_parts_detail_data = PartsDetailSerializer(get_parts_detail, many=True)
				return ApiResponse().success(get_parts_detail_data.data, 200)
		except Exception as err:
			print(err)
			return ApiResponse().error(get_parts_detail_data.errors, 400)

	def post(self,request):
		try:
			# print(request.data)
			parts_detail_data = PartsDetailSerializer(data=request.data)

			if not(parts_detail_data.is_valid()):
				print("here")
				return ApiResponse().error(parts_detail_data.errors, 400)

			parts_detail_data.save()
			return ApiResponse().success("Successfully inserted", 201)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in inserting Add Parts", 400)


	def put(self,request,parts_detail_id):
		try:
			parts_detail_data = PartsDetail.objects.get(pk=parts_detail_id)
			update_data = PartsDetailSerializer(parts_detail_data,data=request.data)
			if update_data.is_valid():
				update_data.save()
				return ApiResponse().success("Successfully Updated", 200)
			else:
				return ApiResponse().error("Please send valid id", 400)
		except Exception as err:
			print(err)
			return ApiResponse().error("Error in Updating Parts Type", 400)
			

	def delete(self,request,parts_detail_id):
		try:
			PartsDetail.objects.filter(pk=parts_detail_id).update(is_deleted=True)
			return ApiResponse().success("Successfully Deleted", 200)
		except Exception as err:
			print(err)
			return ApiResponse().error("Please send valid id", 400)

class PartsDetailTemplate(TemplateView):
	def get(self,request):
		return render(request,'admin/partsdetail.html')

class PartsAllDetailTemplate(TemplateView):
	def get(self,request,parts_detail_id):
		return render(request,'admin/partsalldetail.html')
