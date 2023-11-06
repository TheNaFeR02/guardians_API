from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Hero, Fight, Sponsor, Blacklist
from .serializers import HeroSerializer, FightSerializer, SponsorSerializer, BlacklistSerializer


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FightViewSet(viewsets.ModelViewSet):
    queryset = Fight.objects.all()
    serializer_class = FightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]        


class BlacklistViewSet(viewsets.ModelViewSet):
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]