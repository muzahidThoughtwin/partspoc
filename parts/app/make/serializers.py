from rest_framework import serializers
from app.make.models import Make

class MakeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Make
		fields = ('id','equipment','make_type','name','title','description','is_deleted','created_at','updated_at')
		extra_kwargs = {
			'make_type': {
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