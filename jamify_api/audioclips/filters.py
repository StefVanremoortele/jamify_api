import django_filters

from jamify_api.audioclips.models import AudioClip, Comment


class AudioClipFilter(django_filters.FilterSet):
    class Meta:
        model = AudioClip
        fields = ('id', 'filename')


class AudioClipCommentFilter(django_filters.FilterSet):
    class Meta:
        model = Comment
        fields = ('id', 'text')
