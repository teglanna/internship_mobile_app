from rest_framework import serializers
from .models import Message, Stuff


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'stuff', 'author', 'text', 'recipient', 'bid')


class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = ('id', 'user', 'location', 'description', 'pickup', 'delivery', 'price', 'main_img', 'active')
