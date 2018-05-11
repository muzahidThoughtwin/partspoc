from django.db import models
from app.make.models import Make


# Create your models here.
class Built(models.Model):
	make = models.ForeignKey(Make)
	name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	description = models.TextField(null=True,blank=True)
	parent_id = models.IntegerField(blank=True, null=True)
	is_last = models.BooleanField(default=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		managed = True
		db_table = 'built'