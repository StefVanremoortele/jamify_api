
from jamify_api.audioclips.models import AudioClip, Comment
from jamify_api.users.models import User


def create_audioclip(*, filename: str) -> AudioClip:
    audioclip = AudioClip(filename=filename)
    audioclip.save()
    return audioclip


def create_audioclip_comment(*, text: str, owner: User, audioclip=AudioClip) -> Comment:
    comment = Comment(text=text, owner=owner, audioclip=audioclip)
    comment.save()
    return comment
