from django.urls import path

from .apis import AudioClipListApi


urlpatterns = [
    path('', AudioClipListApi.as_view(), name='list')
]