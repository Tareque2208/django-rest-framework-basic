from rest_framework import serializers
from .models import Article

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
