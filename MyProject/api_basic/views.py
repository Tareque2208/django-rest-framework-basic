from .models import Article
from .serializers import ArticleSerializer

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

from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.

class ArticleViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):

    # Look up is used for which field he is going to compare !
    lookup_field = 'id'
    authentication_classes=[SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


    #Overriding modelviewset like as I want to add my logic on post, so 
    #if uid exists then update, else create... as well other processing.
    #Again I want to retrieve custom response

    class ArticleViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    # """
    # API endpoint for adding and processing new client (by uid) Article
    # """
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer
        permission_classes = [IsAuthenticated]

        def create(self, request):
            if "uid" in request.POST:
                try:
                    instance = Article.objects.get(pk=request.POST['uid'])
                    serializer = ArticleSerializer(
                        instance=instance,
                        data=request.data
                    )
                except Article.DoesNotExist:
                    serializer = ArticleSerializer(data=request.data)
            else:
                serializer = ArticleSerializer(data=request.data)

            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
    
    #Retrieveing Custom Response
        def retrieve(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = ArticleSerializer(instance=instance)
            return Response(serializer.data)
    
    
    
    
    # def list(self, request):
    #     articles = Article.objects.all()
    #     serializer = ArticleSerializer(articles, many=True)
    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer = ArticleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     queryset = Article.objects.all()
    #     article = get_object_or_404(queryset,pk =pk)
    #     serializer = ArticleSerializer(article)
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     article = Article.objects.get(pk=pk)
    #     serializer = ArticleSerializer(article, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


    # def destroy(self, reques, pk=None):
    #     article = Article.objects.get(pk=pk)
    #     article.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# class GenericArticleAPIView(generics.GenericAPIView,mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
# # Look up is used for which field he is going to compare !
#     lookup_field = 'id'
#     # authentication_classes=[SessionAuthentication, BasicAuthentication]
#     authentication_classes=[TokenAuthentication]

#     permission_classes = [IsAuthenticated]

#     def get(self, request, id=None):
#         if id:
#             return self.retrieve(request)
#         else:
#             return self.list(request)

#     def post(self,request):
#         return self.create(request)

#     def put(self, request, id=None):
#         return self.update(request, id)

#     def delete(self, request, id=None):
#         return self.destroy(request, id)



# class ArticleAPIView(APIView):
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# class ArticleDetailsAPIView(APIView):
#     def get_object(self, id):
#         try:
#             return Article.objects.get(id=id)

#         except Article.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)

#     def put(self, request, id):
#         article = self.get_object(id)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     def delete(self,request, id):
#         article = self.get_object(id)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

