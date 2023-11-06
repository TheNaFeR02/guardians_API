from rest_framework import serializers
from .models import Hero, Fight, Sponsor, Blacklist


class HeroSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Hero
        fields = ['id', 'name', 'age', 'image_url',
                  'description', 'character_friends', 'powers','sponsors']


class FightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fight
        fields = ['id', 'hero', 'villain', 'result']


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['id', 'name', 'amount']


class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blacklist
        fields = ['id', 'sponsor_name']
