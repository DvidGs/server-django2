from rest_framework import serializers
from counters.models import Position

# Create a model serializer
class CountersSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Position
        fields = ('id', 'language_1', 'language_2', 'email', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6')
        #read_only_fields = ('id', 'language_1', 'language_2', 'email', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6')

