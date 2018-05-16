from django.conf.urls import url
from app.users import views
app_name='users'

urlpatterns = [
	url(r'user$',views.User.as_view()),
	url(r'search-1$',views.SearchTemplate.as_view()),
	url(r'search-2$',views.Search2Template.as_view()),
	url(r'details$',views.ShowDetailsTemplate.as_view()),
	
]