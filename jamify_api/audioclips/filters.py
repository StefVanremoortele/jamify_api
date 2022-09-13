import django_filters

from jamify_api.audioclips.models import AudioClip


class AudioClipFilter(django_filters.FilterSet):
    class Meta:
        model = AudioClip
        fields = ('id', 'filename')
