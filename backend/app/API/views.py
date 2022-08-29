from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from producst.models import Product
from rest_framework .response import Response
from rest_framework.decorators import api_view
from producst.serializers import ProductSerializer


@api_view(['POST'])
def apiHome(request, *args,**kwargs):
    # instance = Product.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #   #  data = model_to_dict(instance,fields=['id','title'])
    #     #serialization
    #     data = ProductSerializer(instance).data
    #data = request.data
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
      #instance = serializer.save()
     # print(instance)
      data = serializer.data
      print(data)
      
      
      return Response(data)
