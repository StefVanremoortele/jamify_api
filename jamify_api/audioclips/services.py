
from jamify_api.audioclips.models import AudioClip



def create_audioclip(*, filename: str) -> AudioClip:
    audioclip = AudioClip(filename=filename)
    audioclip.save()
    return audioclip