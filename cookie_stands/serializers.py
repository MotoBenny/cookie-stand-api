from rest_framework import serializers
from .models import CookieStand


class StandSerializer(serializers.ModelSerializer): # TODO: may need to change this name
    class Meta:
        model = CookieStand
        fields = "__all__"
