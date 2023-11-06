from django.urls import path, include
from rest_framework import routers
from .views import VillainViewSet

router = routers.DefaultRouter()
router.register(r'villains', VillainViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
