from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication
# import local data
from .serializers import GeeksSerializer
from .models import A1, A2, A3, A4, A5, A6

@permission_classes((IsAuthenticated,))
# create a viewset
#class GeeksViewSet(viewsets.ModelViewSet):
class GeeksViewSet(viewsets.ReadOnlyModelViewSet):
    # define queryset
    queryset = A1.objects.all()
    # specify serializer to be used
    serializer_class = GeeksSerializer

class GeeksViewSet2(viewsets.ReadOnlyModelViewSet):
    # define queryset
    queryset = A2.objects.all()
    # specify serializer to be used
    serializer_class = GeeksSerializer

class GeeksViewSet3(viewsets.ReadOnlyModelViewSet):
    # define queryset
    queryset = A3.objects.all()
    # specify serializer to be used
    serializer_class = GeeksSerializer

class GeeksViewSet4(viewsets.ReadOnlyModelViewSet):
    # define queryset
    queryset = A4.objects.all()
    # specify serializer to be used
    serializer_class = GeeksSerializer

class GeeksViewSet5(viewsets.ReadOnlyModelViewSet):
    # define queryset
    queryset = A5.objects.all()
    # specify serializer to be used
    serializer_class = GeeksSerializer

class GeeksViewSet6(viewsets.ReadOnlyModelViewSet):
    # define queryset
    queryset = A6.objects.all()
    # specify serializer to be used
    serializer_class = GeeksSerializer

