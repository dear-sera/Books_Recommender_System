from rest_framework import serializers
from api.models.best import Bestseller


class BestsellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bestseller
        fields = "__all__"
