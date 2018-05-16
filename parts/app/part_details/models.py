from django.db import models
from app.equipment.models import Equipment
from app.built.models import Built
from app.make.models import Make
import datetime
# Create your models here.
class PartsType(models.Model):
	equipment = models.ForeignKey(Equipment,null=True,blank=True)
	built = models.ForeignKey(Built, blank=True, null=True)
	make = models.ForeignKey(Make, blank=True, null=True)
	name = models.CharField(max_length=255,null=True,blank=True)
	title = models.CharField(max_length=255,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		managed = True
		db_table = 'parts_type'

class PartsName(models.Model):
	equipment = models.ForeignKey(Equipment,null=True,blank=True)
	parts_type = models.ForeignKey(PartsType)
	built = models.ForeignKey(Built, blank=True, null=True)
	make = models.ForeignKey(Make, blank=True, null=True)
	name = models.CharField(max_length=255,null=True,blank=True)
	title = models.CharField(max_length=255, null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		managed = True
		db_table = 'parts_name'

class PartsDetail(models.Model):
	equipment = models.ForeignKey(Equipment,null=True,blank=True)
	built = models.ForeignKey(Built, blank=True, null=True)
	make = models.ForeignKey(Make, blank=True, null=True)
	parts_type = models.ForeignKey(PartsType)
	parts_name = models.ForeignKey(PartsName)
	name = models.CharField(max_length=255,null=True,blank=True)
	title = models.CharField(max_length=255,null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	ref = models.IntegerField()
	code = models.CharField(max_length=255)
	price = models.CharField(max_length=255,null=True,blank=True)
	part = models.CharField(max_length=255)
	slp = models.CharField(max_length=255)
	qty	= models.IntegerField()
	spec = models.CharField(max_length=255)
	remarks	= models.TextField(max_length=255)
	serial = models.CharField(max_length=255)
	date = models.DateField(default=datetime.date)	
	fuel = models.CharField(max_length=255)
	engine = models.CharField(max_length=255)
	image =  models.ImageField(upload_to = 'pic_folder/', default ='pic_folder/no-img.jpg')
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, blank=True)
	updated_at = models.DateTimeField(auto_now_add=True, blank=True)

	class Meta:
		managed = True
		db_table = 'parts_detail'

