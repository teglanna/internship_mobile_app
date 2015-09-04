from rest_framework import serializers
from .models import Message, Stuff, Image, SwipeAction


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'stuff', 'author', 'text', 'recipient', 'bid', 'created')


class StuffSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    distance = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField('get_comments_count')
    views = serializers.SerializerMethodField()
    main_img = serializers.SerializerMethodField('get_image')

    class Meta:
        model = Stuff
        fields = ('id', 'user', 'created', 'full_name', 'location', 'description', 'pickup', 'delivery', 'price',
                  'main_img', 'distance', 'active', 'comments', 'comment_count', 'views')

    @staticmethod
    def get_distance(obj):
        return obj.distance.standard

    @staticmethod
    def get_image(obj):
        return 'img/stuff/1.jpg'

    @staticmethod
    def get_comments(obj):
        return 1

    @staticmethod
    def get_comments_count(obj):
        return 1

    @staticmethod
    def get_views(obj):
        return 1

    @staticmethod
    def get_full_name(obj):
        return obj.user.get_full_name()


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'stuff', 'image')


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SwipeAction
        fields = ('id', 'user', 'stuff', 'action')
