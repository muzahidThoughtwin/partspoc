from django.conf.urls import url
from app.users import views
app_name='users'

urlpatterns = [
	url(r'user$',views.User.as_view()),
	
	
]