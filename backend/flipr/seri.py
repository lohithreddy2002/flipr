from rest_framework import serializers

from .models import title


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = title
        fields = '__all__'