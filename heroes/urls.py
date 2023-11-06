from django.urls import path, include
from rest_framework import routers
from .views import HeroViewSet, FightViewSet, SponsorViewSet, BlacklistViewSet

router = routers.DefaultRouter()
router.register(r'heroes', HeroViewSet)
router.register(r'fights', FightViewSet)
router.register(r'sponsors', SponsorViewSet)
router.register(r'blacklist', BlacklistViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
