from rest_framework.views import APIView
from app.lib.response import ApiResponse
from app.users.views import UserProfile


class AccessUserObj:

	def fromToken(self,request):
		token = request.META['HTTP_AUTHORIZATION'].replace("Token","")	
		return Token.objects.get(key=str(token).strip())


class RequestOverwrite(UpdateView):

	def overWriteUserId(self, request, dic):
		try:
			if request.POST._mutable is False:
				request.POST._mutable = True
			
			for key,value in dic.items():
				request.POST[key] = value
		except Exception as err:
			print(err)
			return False

	def overWrite(self, request, dic):
		try:
			try:
				if request.data._mutable is False:
					request.data._mutable = True
			except:
				pass
			for key,value in dic.items():
				request.data[key] = value
		except Exception as err:
			print(err)
			return False

class CheckExistance():
	def isExists(self,Object,filter):
		obj = Object.objects.filter(**filter)

		if obj.exists():
			return True
		return False			


