from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()

router.register('v1/groups', GroupViewSet)
router.register('v1/posts', PostViewSet)
router.register('v1/follow', FollowViewSet, basename='follow')
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='Comment'
)


urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls)),

]
