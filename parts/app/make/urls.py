from django.conf.urls import url
from app.make import views
app_name='make'

urlpatterns = [

	url(r'make$',views.MakeTemplate.as_view()),
	url(r'make/(?P<make_id>\d+)$',views.MakeViewset.as_view()),
	url(r'make$',views.MakeViewset.as_view()),

]