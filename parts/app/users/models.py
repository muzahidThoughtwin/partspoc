from django.db import models
from django.contrib.auth.models import User
from app.master.models import Role


# Create your models here.
class UserProfile(models.Model):
	user = models.ForeignKey(User)
	role = models.ForeignKey(Role)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	mobile = models.CharField(max_length=10,blank=True)
	status = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		managed = True
		db_table = 'user'
