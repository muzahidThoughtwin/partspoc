from django.db import models

# Create your models here.
class Role(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(null=True,blank=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		managed = True
		db_table = 'role'

