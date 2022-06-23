from unicodedata import category
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from item.models import Category, Item
from item.serializers import ItemSerializers

# Create your views here.


class ItemView(APIView):
    def get(self, request):
        # items = Item.objects.all()
        items_serializer = ItemSerializers().data
        return Response(items_serializer, status=status.HTTP_200_OK)
