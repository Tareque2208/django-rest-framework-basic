
from django.db import router
from django.urls import path
from django.urls.conf import include
# from .views import GenericArticleAPIView, ArticleViewSet
from .views import ArticleViewSet, ArticleRatingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router.register('article-ratings', ArticleRatingViewSet, basename='article-ratings')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    # path('generic/article/', GenericArticleAPIView.as_view()),
    # path('generic/article/<int:id>', GenericArticleAPIView.as_view()),

]
