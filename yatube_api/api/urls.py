from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_api_router = DefaultRouter()

v1_api_router.register('posts', PostViewSet, basename='posts')
v1_api_router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
v1_api_router.register('groups', GroupViewSet, basename='groups')
v1_api_router.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(v1_api_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
    # Очень странно, тест не дает сделать ссылку вида v1/auth/,
    # поэтому оставил просто v1/
]
