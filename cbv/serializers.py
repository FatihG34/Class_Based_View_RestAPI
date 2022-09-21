from rest_framework import serializers
from .models import People, Country
from datetime import date


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name"]


class PeopleSerializer(serializers.ModelSerializer):
    country = serializers.StringRelatedField()
    country_id = serializers.IntegerField()

    def get_age(self, obj):
        today = date.today()
        age = today.year - obj.birth_date.year
        if today.month < obj.birth_date.month or today.month == obj.birth_date.month and today.day < obj.birth_date.day:
            age -= 1
        return age

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    class Meta:
        model = People
        fields = ("id", "first_name", "last_name",
                  "age", "country", "country_id")
