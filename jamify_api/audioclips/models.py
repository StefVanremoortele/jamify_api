import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

from jamify_api.common.models import BaseModel
from jamify_api.users.models import User


class AudioClip(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filename = models.CharField(max_length=150)

    def __str__(self):
        return self.filename


class Comment(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    audioclip = models.ForeignKey(AudioClip, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
