from rest_framework import serializers
from app.part_details.models import PartsType,PartsName,PartsDetail


class PartsTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = PartsType
		fields = ('id','equipment','built','make','name','title','description','is_deleted','created_at','updated_at')
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
		fields = ('id','parts_type','equipment','built','make','name','title','description','is_deleted','created_at','updated_at')
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
		fields = ('id','equipment','built','make','parts_type','parts_name','name','title','description','ref','code','part','slp','qty','spec','remarks','serial','date','fuel','engine','image','is_deleted','created_at','updated_at')
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
