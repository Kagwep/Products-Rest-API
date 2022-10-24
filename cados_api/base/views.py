from inspect import CO_ASYNC_GENERATOR
from urllib import response
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from .serializers import AdvocateSerializer,CompanySerializer


from django.http import JsonResponse

from base.models import Advocate,Company



@api_view(['GET'])
def endPoints(request):
    data = ["/advocates","advocates/:username","Companies","Companies/:name"]
    return Response(data)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def advocate_list(request):
    #data =['Dennis','Tadas','Max']
    if request.method == "GET":
        query = request.GET.get('query')

        if query == None:
            query=''
        
        
        advoctes =  Advocate.objects.filter(Q(username__icontains= query) | Q(bio__icontains =query))
        serializer = AdvocateSerializer(advoctes, many=True)
    #  data = {'advocates':advoctes}
        return Response(serializer.data)
    if request.method == "POST":
        advocate = Advocate.objects.create(
            username= request.data['username'],
            bio = request.data['bio']
        )

        serializer = AdvocateSerializer(advocate, many=False)

        return Response(request.data)

# @api_view(['GET','PUT','DELETE'])
# def advocate_detail(request, username):
#     advocate = Advocate.objects.get(username=username)

#     if request.method == "GET":
        
#         serializer = AdvocateSerializer(advocate,many=False)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         advocate.username = request.data['username']
#         advocate.bio = request.data['bio']

#         advocate.save()

#         serializer = AdvocateSerializer(advocate,many=False)
#         return Response(serializer.data)

#     if request.method == 'DELETE': 

#         advocate.delete()

#         return Response('advocate deleted')



class Advocate_detail(APIView):
    
    def get(self,request,username):
        advocate = Advocate.objects.get(username=username)
        serializer = AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)

    def put(self,request,username):
        advocate = Advocate.objects.get(username=username)
        advocate.username = request.data['username']
        advocate.bio = request.data['bio']
        advocate.save()
        serializer = AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)
    def delete(self,request,username):
        advocate = Advocate.objects.get(username=username)
        advocate.delete()
        return Response('advocate deleted')




@api_view(['GET','POST'])
def companies_list(request):
    #data =['Dennis','Tadas','Max']
    if request.method == "GET":
        query = request.GET.get('query')

        if query == None:
            query=''
        
        
        companies =  Company.objects.filter(Q(name__icontains= query) | Q(bio__icontains =query))
        serializer = CompanySerializer(companies, many=True)
    #  data = {'advocates':advoctes}
        return Response(serializer.data)
    if request.method == "POST":
        company = Company.objects.create(
            name= request.data['name'],
            bio = request.data['bio']
        )

        serializer = CompanySerializer(company, many=False)

        return Response(request.data)


class Company_detail(APIView):
    
    def get(self,request,name):
        company = Company.objects.get(name=name)
        serializer = CompanySerializer(company,many=False)
        return Response(serializer.data)

    def put(self,request,name):
        company = Company.objects.get(name=name)
        company.name = request.data['name']
        company.bio = request.data['bio']
        company.save()
        serializer = CompanySerializer(company,many=False)
        return Response(serializer.data)
    def delete(self,request,name):
        company = CompanySerializer.objects.get(name=name)
        company.delete()
        return Response('company deleted')