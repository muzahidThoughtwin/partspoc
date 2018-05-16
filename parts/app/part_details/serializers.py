from rest_framework import serializers
from app.part_details.models import PartsType,PartsName,PartsDetail


class PartsTypeSerializer(serializers.ModelSerializer):
	parts_name = serializers.SerializerMethodField("getPartsName")
	def getPartsName(self,obj):
		try:
			return PartsNameSerializer(PartsName.objects.filter(parts_type=obj.id, is_deleted=False), many=True).data
		except Exception as e:
			print(e)
			return None


	class Meta:
		model = PartsType
		fields = ('id','equipment','parts_name','built','make','name','title','description','is_deleted','created_at','updated_at')
		# extra_kwargs = {
		# 	'make_type': {
		# 		'required':True,
		# 		'error_messages':{
		# 		'required':"Please fill this field",
		# 		}
		# 	},
		# 	'name': {
		# 		'required':True,
		# 		'error_messages':{
		# 		'required':"name is required",
		# 		}
		# 	},
		# 	'title': {
		# 		'required':True,
		# 		'error_messages':{
		# 		'required':"title is required",
		# 		}
		# 	},
			
		# }	
class PartsNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = PartsName
		fields = ('id','equipment','parts_type','built','make','name','title','description','is_deleted','created_at','updated_at')
		# extra_kwargs = {
		# 	'make_type': {
		# 		'required':True,
		# 		'error_messages':{
		# 		'required':"Please fill this field",
		# 		}
		# 	},
		# 	'name': {
		# 		'required':True,
		# 		'error_messages':{
		# 		'required':"name is required",
		# 		}
		# 	},
		# 	'title': {
		# 		'required':True,
		# 		'error_messages':{
		# 		'required':"title is required",
		# 		}
		# 	},
			
		# }	
class PartsDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = PartsDetail
		fields = ('id','equipment','built','make','price','parts_type','parts_name','name','title','description','ref','code','part','slp','qty','spec','remarks','serial','date','fuel','engine','image','is_deleted','created_at','updated_at')
		# extra_kwargs = {
		# 	'make_type': {
		# 		'required':True,
		# 		'error_messages':{
		# 		'required':"Please fill this field",
		# 		}
		# 	},
		# 	'name': {
		# 		'required':True,
		# 		'error_messages':{
		# 		'required':"name is required",
		# 		}
		# 	},
		# 	'title': {
		# 		'required':True,
		# 		'error_messages':{
		# 		'required':"title is required",
		# 		}
		# 	},
			
		# }	
