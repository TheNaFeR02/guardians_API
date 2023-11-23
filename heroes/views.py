from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Hero, Fight, Sponsor, Blacklist, Schedule
from .serializers import HeroSerializer, FightSerializer, SponsorSerializer, BlacklistSerializer, ScheduleSerializer, HeroNameSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HeroNameView(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroNameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class FightViewSet(viewsets.ModelViewSet):
    queryset = Fight.objects.all()
    serializer_class = FightSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlacklistViewSet(viewsets.ModelViewSet):
    queryset = Blacklist.objects.all()
    serializer_class = BlacklistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hero']
