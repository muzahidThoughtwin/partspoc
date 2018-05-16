from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.views.generic import TemplateView
# Create your views here.
class User(APIView):
	def get(self,request):
		return Response("Users demo test")

	def post(self,request):
		return Response("Post")

class SearchTemplate(TemplateView):
	def get(self,request):
		return render(request,'user/search.html')

class Search2Template(TemplateView):
	def get(self,request):
		return render(request,'user/search2.html')

class ShowDetailsTemplate(TemplateView):
	def get(self,request):
		return render(request,'user/details.html')