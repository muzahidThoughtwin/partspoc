from django.conf.urls import url
from app.equipment import views
app_name='equipment'

urlpatterns = [
	url(r'create/equipment$',views.EquipmentTemplate.as_view()),
	url(r'^equipment/(?P<equipment_id>\d+)$',views.AddEquipment.as_view()),
	url(r'equipment$',views.AddEquipment.as_view()),
	
	
]