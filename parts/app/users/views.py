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

