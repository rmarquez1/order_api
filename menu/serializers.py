from rest_framework import serializers
from menu.models import Menu

class MenuSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    description = serializers.CharField(required=True, max_length=100)
    price = serializers.FloatField()
    active = serializers.BooleanField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `menu` instance, given the validated data.
        """
        return Menu.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Menu` instance, given the validated data.
        """
        instance.title = validated_data.get('description', instance.description)
        instance.code = validated_data.get('price', instance.price)
        instance.linenos = validated_data.get('active', instance.active)
        instance.save()
        return instance
    