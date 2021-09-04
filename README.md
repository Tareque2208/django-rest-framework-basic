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
#function base api is one way to represnt api views with routing, http request & response

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
