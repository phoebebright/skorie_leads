from rest_framework import serializers
from .models import Lead, Interaction, InteractionTemplate


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'

class InteractionTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteractionTemplate
        fields = '__all__'
