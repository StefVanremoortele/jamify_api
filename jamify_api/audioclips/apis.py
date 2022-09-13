# import json
# from ast import Try
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

from jamify_api.utils.pagination import get_paginated_response, LimitOffsetPagination
from jamify_api.audioclips.models import AudioClip, Comment
from jamify_api.audioclips.selectors import audioclip_comments_list, audioclip_list
from jamify_api.audioclips.services import create_audioclip, create_audioclip_comment
from jamify_api.users.models import User


# TODO: When JWT is resolved, add authenticated version
class AudioClipApi(APIView):
    permission_classes = [AllowAny]

    class Pagination(LimitOffsetPagination):
        default_limit = 10             

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        filename = serializers.CharField(required=False)

    class InputSerializer(serializers.Serializer):
        filename = serializers.CharField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = AudioClip
            fields = (
                'id',
                'filename',
            )

    def get(self, request):
        # Make sure the filters are valid, if passed
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        audioclips = audioclip_list(filters=filters_serializer.validated_data)

        return get_paginated_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=audioclips,
            request=request,
            view=self
        )

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        audioclip = create_audioclip(filename=serializer.data['filename'])

        return Response(self.OutputSerializer(audioclip).data)


class AudioClipCommentApi(APIView):
    permission_classes = [AllowAny]
    lookup_url_kwarg = 'id'

    class Pagination(LimitOffsetPagination):
        default_limit = 10 

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        text = serializers.CharField(required=False)

    class InputSerializer(serializers.Serializer):
        text = serializers.CharField()

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = (
                'id',
                'text',
            )

    def get(self, request, *args, **kwargs):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        try:
            comments = audioclip_comments_list(
                audioclip_id=self.kwargs.get(self.lookup_url_kwarg),
                filters=filters_serializer.validated_data
            )
            return get_paginated_response(
                pagination_class=self.Pagination,
                serializer_class=self.OutputSerializer,
                queryset=comments,
                request=request,
                view=self
            )
        except Exception as ex:
            if isinstance(ex, ObjectDoesNotExist):
                return Response('Comment matching query does not exist')
            return Response('something went wrong')

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        u = User.objects.get(name='stef')
        ac = AudioClip.objects.get(filename='test')
        print(u)
        print(ac)
        comment = create_audioclip_comment(text=serializer.data['text'], user=u, audioclip=ac)

        return Response(self.OutputSerializer(comment).data)
