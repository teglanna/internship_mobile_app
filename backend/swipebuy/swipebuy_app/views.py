from rest_framework import viewsets
from .serializers import MessageSerializer, StuffSerializer, ImageSerializer, ActionSerializer
from .models import Message, Stuff, Image, SwipeAction


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'pk'


class StuffViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
    lookup_field = 'pk'


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'pk'

class ActionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SwipeAction.objects.all()
    serializer_class = ActionSerializer
    lookup_field = 'pk'    