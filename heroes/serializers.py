from rest_framework import serializers
from .models import Hero, Fight, Sponsor, Blacklist, Schedule


class HeroSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    image_screen_large_url = serializers.ImageField(required=False)

    class Meta:
        model = Hero
        fields = ['id', 'name', 'age', 'image_url', 'image_screen_large_url',
                  'description', 'character_friends', 'powers', 'sponsors']


class HeroNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id', 'name']


class FightSerializer(serializers.ModelSerializer):
    hero_name = serializers.SerializerMethodField()
    villain_name = serializers.SerializerMethodField()
  
    class Meta:
        model = Fight
        fields = ['id', 'hero', 'villain', 'result', 'hero_name', 'villain_name']

    def get_hero_name(self, obj):
        return obj.hero.name if obj.hero else None

    def get_villain_name(self, obj):
        return obj.villain.name if obj.villain else None


class SponsorSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)

    class Meta:
        model = Sponsor
        fields = ['id', 'name', 'amount', 'image_url']


class BlacklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blacklist
        fields = ['id', 'sponsor_name']


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'hero', 'title', 'start', 'end', 'color']
