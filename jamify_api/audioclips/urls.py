from django.urls import path

from .apis import AudioClipApi


urlpatterns = [
    path('', AudioClipApi.as_view(), name='list')
]