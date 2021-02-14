from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import APIView
from rest_framework.response import Response
import json
from core.serializers import *
from rest_framework.permissions import AllowAny
from rest_framework import status
from core.models import ItemCategory, Items
# Create your views here.


class ItemCategoryView(APIView):
    """
        create Item Category
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        if "categoryName" not in request.data:
            return Response({"sucess" : False, "error" : {"code" : 404, "message" : "categoryName not present in request data" }})

        serializer = ItemCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"sucess" : False, "error" : {"code" : 400, "message" : serializer.errors }})



class ItemView(APIView):
    """
        Add Items to the category and Get total items
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        if "itemName" not in request.data:
            return Response({"sucess" : False, "error" : {"code" : 404, "message" : "itemName not present in request data" }})
        if "categoryName" not in request.data:
            return Response({"sucess" : False, "error" : {"code" : 404, "message" : "categoryName not present in request data" }})

        try:
            category = ItemCategory.objects.get(categoryName=request.data["categoryName"])
        except Exception as e:
            return Response({"sucess" : False, "error" : {"code" : 404, "message" : repr(e) }})
        serializer = ItemsSerializer(data={"itemName" : request.data["itemName"], "itemCategory" : category.id})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"sucess" : False, "error" : {"code" : 400, "message" : serializer.errors }})

    def get(self, request):
        items_count = Items.objects.all().count()
        return Response({"items_count" : items_count}, status=status.HTTP_201_CREATED)

