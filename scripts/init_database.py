
import json

from jamify_api.audioclips.models import AudioClip
from jamify_api.audioclips.services import list_audioclips, create_audioclip


def create_audioclips():
    create_audioclip(filename='test-file')



def run():
    create_audioclips()