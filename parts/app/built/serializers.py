from rest_framework import serializers
from app.built.models import Built

class BuiltSerializer(serializers.ModelSerializer):
	class Meta:
		model =  Built
		fields = ('id','make','name','title','description','is_deleted','created_at','updated_at')
		extra_kwargs = {
			'make': {
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
