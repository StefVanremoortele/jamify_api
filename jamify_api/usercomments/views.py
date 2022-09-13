from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import UserComment
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserCommentSerializer, UserCommentSerializer


class UserCommentViewSet(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    """
    Updates and retrieves user accounts
    """
    queryset = UserComment.objects.all()
    serializer_class = UserCommentSerializer
    permission_classes = (AllowAny,)


class UserCommentCreateViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates user accounts
    """
    queryset = UserComment.objects.all()
    serializer_class = CreateUserCommentSerializer
    permission_classes = (AllowAny,)
