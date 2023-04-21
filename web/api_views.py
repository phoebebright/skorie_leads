from rest_framework import generics
from .models import Lead, Interaction, InteractionTemplate
from .serializers import LeadSerializer, InteractionSerializer, InteractionTemplateSerializer


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class LeadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class InteractionListCreate(generics.ListCreateAPIView):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer

class InteractionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer


class InteractionTemplateRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = InteractionTemplate.objects.all()
    serializer_class = InteractionTemplateSerializer
