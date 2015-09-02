from rest_framework import serializers
from .models import Message, Stuff, Image, SwipeAction


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'stuff', 'author', 'text', 'recipient', 'bid')


class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = ('id', 'user', 'location', 'description', 'pickup', 'delivery', 'price', 'main_img', 'active')


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Image
		fields = ('id', 'stuff', 'image')

class ActionSerializer(serializers.ModelSerializer):
	class Meta:
		model = SwipeAction
		fields = ('id', 'user', 'stuff', 'action')

