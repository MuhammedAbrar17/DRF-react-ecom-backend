from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .products import Products
from .models import Products
from .serializer import ProductsSerializer
# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    return Response('hello abu')

@api_view(['GET'])
def getProduct(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products,many=True)
    return Response(serializer.data)
    