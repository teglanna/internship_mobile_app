from rest_framework import viewsets
from .serializers import MessageSerializer, StuffSerializer
from .models import Message, Stuff


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
