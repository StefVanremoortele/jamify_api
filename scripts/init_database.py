from jamify_api.users.models import User
from jamify_api.users.services import create_user, create_super_user
from jamify_api.audioclips.models import AudioClip
from jamify_api.audioclips.services import create_audioclip, create_audioclip_comment


def generate_user():
    create_user()


def generate_super_user():
    create_super_user()


def generate_audioclips():
    create_audioclip(filename='test')


def generate_audioclip_comment():
    u = User.objects.first()
    ac = AudioClip.objects.first()
    create_audioclip_comment(text='something', owner=u, audioclip=ac)


def run():
    generate_user()
    generate_super_user()
    generate_audioclips()
    generate_audioclip_comment()