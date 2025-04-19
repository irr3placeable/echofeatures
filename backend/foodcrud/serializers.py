from rest_framework import serializers
from .models import RecipeRequest

class RecipeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeRequest
        exclude = ['approvalStatus']  
