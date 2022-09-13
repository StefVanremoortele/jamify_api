from django.db.models.query import QuerySet

from jamify_api.audioclips.models import AudioClip, Comment
from jamify_api.audioclips.filters import AudioClipFilter, AudioClipCommentFilter




def audioclip_list(*, filters=None) -> QuerySet[AudioClip]:
    filters = filters or {}
    qs = AudioClip.objects.all()
    return AudioClipFilter(filters, qs).qs


def audioclip_comments_list(*, audioclip_id: str, filters=None) -> QuerySet[Comment]:
    filters = filters or {}
    qs = Comment.objects.filter(audioclip_id=audioclip_id)
    return AudioClipCommentFilter(filters, qs).qs
