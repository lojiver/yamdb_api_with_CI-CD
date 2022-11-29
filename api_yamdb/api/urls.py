from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .v1.views import (CategoryViewSet, CommentsViewSet, GenreViewSet,
                       ReviewsViewSet, TitleViewSet, UserViewSet, create,
                       get_token)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'titles', TitleViewSet)
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewsViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet
)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/token/', get_token),
    path('v1/auth/signup/', create),
]
