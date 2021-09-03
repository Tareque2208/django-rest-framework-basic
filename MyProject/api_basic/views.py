from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer

# Create your views here.
@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        perdata = JSONParser().parse(request)
        serializer = ArticleSerializer(data=perdata)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status = 400)


