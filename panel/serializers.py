# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from panel.models import A1, A2, A3, A4, A5, A6

# Create a model serializer
class GeeksSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = A1
        fields = ('id', 'category', 'text')
        read_only_fields = ('id', 'category', 'text')

    class Meta2:
        model = A2
        fields = ('id', 'category', 'text')
        read_only_fields = ('id', 'category', 'text')

    class Meta3:
        model = A3
        fields = ('id', 'category', 'text')
        read_only_fields = ('id', 'category', 'text')

    class Meta4:
        model = A4
        fields = ('id', 'category', 'text')
        read_only_fields = ('id', 'category', 'text')

    class Meta5:
        model = A5
        fields = ('id', 'category', 'text')
        read_only_fields = ('id', 'category', 'text')

    class Meta6:
        model = A6
        fields = ('id', 'category', 'text')
        read_only_fields = ('id', 'category', 'text')


