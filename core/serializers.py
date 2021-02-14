from rest_framework import serializers
from core.models import *


class ItemCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemCategory
        fields = ("categoryName",)


class ItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Items
        fields = ("itemCategory","itemName",)