from django.conf.urls import url
from app.make import views
app_name='make'

urlpatterns = [
	url(r'make$',views.AddMake.as_view()),
	url(r'make/(?P<make_id>\d+)$',views.AddMake.as_view()),
	url(r'maketemplate$',views.MakeTemplate.as_view()),
	
]