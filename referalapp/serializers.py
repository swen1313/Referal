from rest_framework import serializers

from referalapp.models import Refer


class ReferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refer
        fields = '__all__'