
from django.urls import path
from .views import ArticleAPIView, ArticleDetailsAPIView

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('article/<int:id>/', ArticleDetailsAPIView.as_view()),

]
