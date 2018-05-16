from django.conf.urls import url
from app.part_details import views
app_name='part_details'

urlpatterns = [
	url(r'partstype/(?P<parts_type_id>\d+)$',views.PartsTypeViewset.as_view()),
	url(r'partstype/name/(?P<parts_name_id>\d+)$',views.PartsTypeViewset.as_view()),
	url(r'partsname/(?P<parts_name_id>\d+)$',views.PartsNameViewset.as_view()),
	url(r'partsdetail/view/(?P<parts_detail_id>\d+)$',views.PartsAllDetailTemplate.as_view()),
	url(r'partsdetail/(?P<parts_detail_id>\d+)$',views.PartsDetailViewset.as_view()),
	url(r'create/partstype$',views.PartsTypeTemplate.as_view()),
	url(r'create/partsname$',views.PartsNameTemplate.as_view()),
	url(r'create/partsdetail$',views.PartsDetailTemplate.as_view()),
	url(r'partstype$',views.PartsTypeViewset.as_view()),
	url(r'partsname$',views.PartsNameViewset.as_view()),
	url(r'partsdetail$',views.PartsDetailViewset.as_view()),
	
]