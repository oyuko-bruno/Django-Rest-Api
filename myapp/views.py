from rest_framework import  viewsets

from .models import  Items
from .serializers import ItemSerializer

class ItemViewSets(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer