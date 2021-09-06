from rest_framework.serializers import Serializer
from .models import Article, ArticleRating, Tag
from .serializers import ArticleSerializer, ArticleRatingSerializer

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.


class ArticleViewSet(viewsets.ModelViewSet):

    # Look up is used for which field he is going to compare !
    lookup_field = 'id'
    authentication_classes = [SessionAuthentication,
                              TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
# Overriding create method because of one to one relation in article-articleRating

    def create(self, request, *args, **kwargs):
        article_data = request.data
        if article_data['rating'] :
            new_rating = ArticleRating.objects.create(
            likes=article_data['rating']['likes'], 
            dislikes=article_data['rating']['dislikes'],)
        else:
            new_rating = ArticleRating.objects.create(likes =0, dislikes=0)
            
        new_rating.save()

        # tags = Tag.objects.get(id=article_data['tag'])
        # if article_data['tag'] :
        #     new_rating = Tag.objects.create(
        #     title=article_data['tag']['title'], 
        #     desc=article_data['tag']['desc'],)
        # else:
        #     new_rating = ArticleRating.objects.create(title =0, dislikes=0)
            
        # new_rating.save()



        new_article = Article.objects.create(
            title = article_data['title'],
            author = article_data['author'],
            email = article_data['email'],
            rating = new_rating )
        new_article.save()
        serializer = ArticleSerializer(new_article)
        return Response(serializer.data)


class ArticleRatingViewSet(viewsets.ModelViewSet):

   
    authentication_classes = [SessionAuthentication,
                              TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = ArticleRating.objects.all()
    serializer_class = ArticleRatingSerializer
