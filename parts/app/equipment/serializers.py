from rest_framework import serializers
from app.equipment.models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
	class Meta:
		model =  Equipment
		fields = ('id','equip_type','name','title','description','is_deleted','created_at','updated_at')
		extra_kwargs = {
			'equip_type': {
				'required':True,
				'error_messages':{
				'required':"Please fill this field",
				}
			},
			'name': {
				'required':True,
				'error_messages':{
				'required':"name is required",
				}
			},
			'title': {
				'required':True,
				'error_messages':{
				'required':"title is required",
				}
			},
			
		}
