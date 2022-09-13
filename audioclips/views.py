from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import AudioClip
# from .permissions import IsUserOrReadOnly
from .serializers import AudioClipSerializer, CreateAudioClipSerializer


class AudioClipViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = AudioClip.objects.all()
    serializer_class = AudioClipSerializer
    permission_classes = (AllowAny,)


class AudioClipCreateViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = AudioClip.objects.all()
    serializer_class = CreateAudioClipSerializer
    permission_classes = (AllowAny,)
