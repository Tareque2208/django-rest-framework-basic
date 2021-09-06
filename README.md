# Django REST Framework Basics

### project-setup branch, 
````python
# installing django REST framework
pip install djangorestframework
# Markdown support for the browsable API.
pip install markdown
# Filtering support.
pip install django-filter
# Create the project directory.
mkdir django-rest-framework-basic
# accessing the directory.
cd django-rest-framework-basic
# Create my project.
django-admin startproject MyProject
# accessing the directory.
cd MyProject
# Creating migration.
python manage.py migrate
# Checking the project is running or not.
python manage.py runserver
# Cancel.
Ctrl+c
# Creating application for my project.
python manage.py startapp api_basic
# Creating Super User. and giving new email and pass
python manage.py createsuperuser
# Access admin panel with http://127.0.0.1:8000/admin
#username-ahmedtareque
#password-123

add 'rest_framework', 'api_basic' in INSTALLED_APPS from MyProject/settings.py

````

### serializer-basics branch, 
````python
# Before sending data to clients we need to serialize it to JSON format. Ap API's end result is always JSON format. An api communicate with multiple technologies which receives JSON format data. Let's create a model serializer -
# Make an Article Class Model with their fields in MyProject/models.py
class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# Now, make migration and then, migrate
cd MyProject
python manage.py makemigrations
python manage.py migrate

#Adding the migration to the admin panel in admin.py
admin.site.register(Article)

# Now, It's time for Serializer Class to serialize out models in api_basic/serializers.py
# We are going user create and update method with validated_date and instance where needed

class ArticleSerializer(serializers.Serializer):
    title=serializers.CharField(max_length=100)
    author=serializers.CharField(max_length=100)
    email=serializers.CharField(max_length=100)
    date=serializers.DateTimeField()


    def create(self, validated_date):
        return Article.objets.create(validated_date)

    def update(self, instance, validated_date):
        instance.title = validated_date.get('title', instance.title)
        instance.author = validated_date.get('author', instance.author)
        instance.email = validated_date.get('email', instance.email)
        instance.date = validated_date.get('date', instance.date)
        instance.save()
        return instance
        

# Now, It's time to use django shell

python manage.py shell
->
from api_basic.models import Article
from api_basic.serializers import ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# Now create an instance of Article Model and save

a= Article( title = 'First Title', author = 'First Author', email = 'First Email')
a.save()

#Seralizer data showing
serializer = ArticleSerializer(a)
serializer.data
serializer = ArticleSerializer(Article.objects.all(),many=True)
serializer.data
````

### model-serializer branch, 
````python
#That was pretty basic of serialization but We can do better with ModelSerializer

    class Meta:
        model = Article
        fields = ['id', 'title', 'author']

````

###  function-based-api branch, 
````python
#function base api is one way to represent api views with routing, http request & response

1. In view.py of my project, we are going to use article_list function to check for GET method -> get objects.all() - ArticleSerializer(articles) - return JsonResponse(serializer.data).

2. or check for POST method -> JSONParser().parse(request) - ArticleSerializer(data=perdata) - ArticleSerializer - check serializer.is_valid() - do save and return JsonResponse(serializer.data) - or return JsonResponse(serializer.errors)

3. by the way, Must user @csrf_exempt before every function for local testing on POSTMAN as because we want to be able to POST this request to view from clients that will not have a CSRF token, we need to mark the view as csrf_exempt. This is not something that you would normally want to do, and REST framework views actually use more sensible behavior than this, but it will do for our testing purposes right now.

4. For details of each product, try -> Article.objects.get(pk=pk) - except Article.DoesNotExist -> return HttpResponse(status=404)

5.Now, repeatation of checking method GET -> ArticleSerializer(article) - return JsonResponse(serializer.data)

6.Again, repeatation for PUT method -> JSONParser().parse(request) - ArticleSerializer(article, data=perdata) - ArticleSerializer - check serializer.is_valid() - do save and return JsonResponse(serializer.data) - or return JsonResponse(serializer.errors)

````



###  api-view branch, 
````python
#We are just going to use django rest framework browseable api, we can easily play with our data here

1. replace  @csrf_exempt with @api_view(['GET','POST','PUT','DELETE']) according to the methods which are used in the function
2. replace  JsonResponse,HttpResponse with Response
3. We don not need to parse the request data so delete that and serialize, ArticleSerializer(data=request.data)
4. replace status with status.HTTP_400_BAD_REQUEST or whatever that is
5. change fields in ArticleSerializer to '__all__'

````


###  class-based-api branch, 
````python
# Class base api is another way to represent api views with routing, http request & response we just need to define both classes against functions

1. from rest_framework.views import APIView

2. define ArticleAPIView(APIView) & ArticleDetailsAPIView(APIView) and then define the function name as methods name and just replace previous logics within the functions. Boom !

3. even define a function to get the object/article with article id and call it everytime to get the article details - article = self.get_article(id).

4. change the urls with the classnames.as_view() - path('article/<int:id>/', ArticleDetailsAPIView.as_view())

````

###  generic-mixin-based-api branch, 
````python
# Generic base api is the easiest way to represent api views with routing, http request & response we just need to define both classes against functions import mixins - generics.GenericAPIView,RetrieveModel, ListModel, DestroyModel, CreateModel, UpdateModel

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
# Look up is used for which field he is going to compare !
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)

````


###  session-token-base-auth branch, 
````python
# Session based authentication indicates that you got to be using username, password while token base authentication can be done with Token {token-key} using postman.

1. Add 'rest_framework.authtoken' in settings.py and python manag.py migrate
2. from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
3. lookup_field = 'id'
4. authentication_classes = [SessionAuthentication, BasicAuthentication]
5. permission_classes = [IsAuthenticated]

````


###  viewset branch, 
````python
# Viewset is amazingly easy. You need to define list, create. retrieve, update, destroy

just place all code from generic api view and replace -
1. article = Article.objects.get(pk=pk)
2. update the router with DefaultRouter
3. router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

````


###  generic-viewset branch, 
````python
# Generic-Viewset is the easiest way ever. LOL

#In Views -
from rest_framework import mixins
from rest_framework import viewsets

from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


#In Router -
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
]

````


###  model-viewset branch, 
````python
# This one the ground breaking. Lol

class ArticleViewSet(viewsets.ModelViewSet):

queryset = Article.objects.all()
    serializer_class = ArticleSerializer

#That's it ! Nothing else needs to change
````
