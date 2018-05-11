from django.db import models
from app.equipment.models import Equipment

# Create your models here.
class Make(models.Model):
	equipment = models.ForeignKey(Equipment)
	make_type = models.CharField(max_length=255)
	name = models.CharField(max_length=255)
	title = models.CharField(max_length=255)
	description = models.TextField(null=True,blank=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		managed = True
		db_table = 'make'

