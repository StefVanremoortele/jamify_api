from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from jamify_api.utils.pagination import get_paginated_response, LimitOffsetPagination
from jamify_api.audioclips.models import AudioClip
from jamify_api.audioclips.selectors import audioclip_list
from jamify_api.audioclips.services import create_audioclip



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