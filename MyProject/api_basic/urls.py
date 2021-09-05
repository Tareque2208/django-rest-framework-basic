
from django.urls import path
from .views import GenericArticleAPIView

urlpatterns = [

    path('generic/article/', GenericArticleAPIView.as_view()),
    path('generic/article/<int:id>', GenericArticleAPIView.as_view()),

]
