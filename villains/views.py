from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser 
from .models import Villain
from .serializers import VillainSerializer

# Create your views here.
class VillainViewSet(viewsets.ModelViewSet):
    queryset = Villain.objects.all()
    serializer_class = VillainSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


 




