from rest_framework import viewsets
from .serializers import MessageSerializer
from .models import Message


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'pk'