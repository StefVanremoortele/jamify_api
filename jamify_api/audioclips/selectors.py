from django.db.models.query import QuerySet

from jamify_api.audioclips.models import AudioClip
from jamify_api.audioclips.filters import AudioClipFilter




def audioclip_list(*, filters=None) -> QuerySet[AudioClip]:
    filters = filters or {}
    qs = AudioClip.objects.all()
    return AudioClipFilter(filters, qs).qs