from rest_framework import serializers
from .models import AudioClip


class AudioClipSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioClip
        fields = ('id', 'filename', )
        # read_only_fields = ()


class CreateAudioClipSerializer(serializers.ModelSerializer):

    # def create(self, validated_data):
    #     # call create_user on user object. Without this
    #     # the password will be stored in plain text.
    #     # user = AudioClip.objects.create_audioclip(**validated_data)
    #     return user

    class Meta:
        model = AudioClip
        fields = ('id', 'filename', )
        read_only_fields = ()
