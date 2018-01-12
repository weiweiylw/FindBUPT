__author__ = 'xiaoyue'
from rest_framework import serializers
from models import Department,Tag,Location


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card

