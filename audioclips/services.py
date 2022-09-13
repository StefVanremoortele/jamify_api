
from jamify_api.audioclips.models import AudioClip


def list_audioclips() -> AudioClip:
    return AudioClip.objects.all()


def create_audioclip(*, filename: str) -> AudioClip:
    audioclip = AudioClip(filename=filename)
    audioclip.save()
    return audioclip