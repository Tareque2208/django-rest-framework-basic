
from django.urls import path
from .views import article_list, article_details

urlpatterns = [
    path('article/', article_list),
    path('article/<int:pk>/', article_details),
    # path('article/', article_list),
]
