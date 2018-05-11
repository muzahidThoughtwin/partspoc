from django.core.paginator import Paginator
from apps.lib.response import ApiResponse
class ApiPagination:

	lim = 10

	def init(self,request,obj,serializer, unview=None):
		try:
			
			ser,obj = ApiPagination().common(request,obj,serializer)
			return  ApiResponse().paginationSuccess(ser.data,200,obj.count(), unview)
		except Exception as err:
			print(err)
			return ApiResponse().success([],200)

	def rawPagination(request,obj,serializer):
		try:
			
			ser,obj = ApiPagination().common(request,obj,serializer)
			return  ser.data,obj.count()
		except Exception as err:
			print(err)
			print("Error in raw pagination ")
			return [],obj.count()

	def common(self,request,obj,serializer):

		lim = ApiPagination().lim
		if not request.GET.get("pageSize") is None:
			lim = request.GET.get("pageSize")

		if int(lim)<0:
			ser = serializer(obj,many=True,context={'request':request})
			return ser,obj


		paginator = Paginator(obj, lim)
		page =1 
		if not request.GET.get("pageNumber") is None:
			page = request.GET.get('pageNumber')
		ser = serializer(paginator.page(page),many=True,context={'request':request})
		return 	ser,obj		
			
	def paging(request,array,mul=1):
		try:
			lim = ApiPagination().lim
			if not request.GET.get("pageSize") is None:
				lim = request.GET.get("pageSize")

			paginator = Paginator(array,int(lim)*int(mul))
			page =1 
			if not request.GET.get("pageNumber") is None:
				page = request.GET.get('pageNumber')
			result = []
			objects = paginator.page(page)	
			
			for i in objects:
				result.append(i)
			return result
		except Exception as err:
			return []			
