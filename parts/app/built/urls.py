from django.conf.urls import url
from app.built import views

app_name='built'

urlpatterns = [
	url(r'built$',views.AddBuilt.as_view()),
	url(r'built/(?P<built_id>\d+)$',views.AddBuilt.as_view()),
	url(r'builttemplate$',views.BuiltTemplate.as_view()),
	
]