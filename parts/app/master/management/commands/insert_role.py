from django.core.management.base import BaseCommand
from app.master.models import Role
from app.users.models import UserProfile
from django.contrib.auth.models import User


class Command(BaseCommand):
	args ='';
	help='For insert data in role model'

	def insertData(self):
		try:
			if(Role.objects.all().count() > 0):
				return "Data has already exists in db"
		except:
			pass		

		role = [];
		role.append(Role(name="Super Admin"))
		role.append(Role(name="Sub Admin"))
		role.append(Role(name="Users"))
		Role.objects.bulk_create(role)

	
	def insertDataMasterUser(self):
		try:
			if(userProfile.objects.all().count() > 0):
				return "Data has already exists in db"
		except:
			pass		
		email = "admin@admin.com"
		user = User.objects.create_user(username=email,email=email,password=12345678,is_staff=True)
		userProfile = UserProfile(first_name="Super",role=Role.objects.get(id=1),last_name="Admin",mobile="1234567890",status=True,user= user)
		userProfile.save()


	def handle(self,*args,**options):
		self.insertData()		
		self.insertDataMasterUser()	
		print ('data inserted')
