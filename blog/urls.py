from django.urls import path

from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='post_list_url'),
    path('post/', PostCreate.as_view(), name='post_create_url')
]
