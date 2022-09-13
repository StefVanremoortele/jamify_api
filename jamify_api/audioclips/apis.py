from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import AllowAny

from jamify_api.utils.pagination import get_paginated_response, LimitOffsetPagination

from jamify_api.audioclips.models import AudioClip
from jamify_api.audioclips.selectors import audioclip_list



# TODO: When JWT is resolved, add authenticated version
class AudioClipListApi(APIView):
    permission_classes = [AllowAny]

    class Pagination(LimitOffsetPagination):
        default_limit = 1

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        filename = serializers.CharField(required=False)
        # Important: If we use BooleanField, it will default to False
        # is_admin = serializers.NullBooleanField(required=False)
        # email = serializers.EmailField(required=False)

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