from rest_framework import serializers
from .models import Villain

class VillainSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    
    class Meta:
        model = Villain
        fields = ('id', 'name', 'age', 'origin', 'image_url', 'image_screen_large_url', 'description', 'character_enemies','powers','weaknesses')