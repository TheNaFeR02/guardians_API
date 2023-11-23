from django.urls import path, include
from rest_framework import routers
from .views import HeroViewSet, FightViewSet, SponsorViewSet, BlacklistViewSet, ScheduleViewSet
from rest_framework.generics import ListAPIView
from .serializers import HeroNameSerializer
from .models import Hero

router = routers.DefaultRouter()
router.register(r'heroes', HeroViewSet)
router.register(r'fights', FightViewSet)
router.register(r'sponsors', SponsorViewSet)
router.register(r'blacklist', BlacklistViewSet)
router.register(r'schedules', ScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('names/', ListAPIView.as_view(queryset=Hero.objects.all(), serializer_class=HeroNameSerializer), name='user-list')


]
