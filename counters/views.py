from django.shortcuts import render
from rest_framework import viewsets, views
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import CountersSerializer
from .models import Position

# Create your views here.
@permission_classes((IsAuthenticated,))
class CounterViewSet(viewsets.ModelViewSet):
#class GeeksViewSet(viewsets.ReadOnlyModelViewSet):
    # define queryset
    queryset = Position.objects.all()
    #queryset = Position.objects.filter(email='david123@david123.com')

    def get_queryset(self):
        user = self.request.user
        return Position.objects.filter(email=user.email)
        # specify serializer to be used
    serializer_class = CountersSerializer

