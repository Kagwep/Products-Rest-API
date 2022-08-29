from rest_framework.response import Response
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        #serializer.save(user = self.request.user)
        print(serializer.validated_data)
        title = serializer.validate_data.get('title')
        content = serializer.validate_data.get('content')
 
        serializer.save()

class ProductDetailapiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    
    # lookup_field = 'pk' 
class ProductListApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
@api_view(['POST','GET'])
def product_alt_view(request,pk=None,*args,**kwargs):
    method = request.method
    
    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj,many = False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data)
    if method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validate_data.get('title')
            content = serializer.validate_data.get('content') or None
            if content is None:
                content = title 
                
        serializer.save(content=content)

        
        return Response({'invalid':'Please check your data'},status =400)