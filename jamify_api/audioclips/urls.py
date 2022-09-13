from django.urls import path

from .apis import AudioClipApi, AudioClipCommentApi


urlpatterns = [
    path('', AudioClipApi.as_view(), name='list'),
    path('<uuid:id>/comments', AudioClipCommentApi.as_view(), name='list-comments'),
]