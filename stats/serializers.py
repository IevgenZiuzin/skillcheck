from rest_framework import serializers
from .models import Completion


class CompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Completion
        fields = '__all__'
