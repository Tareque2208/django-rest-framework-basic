from rest_framework import fields, serializers
from .models import Article, ArticleRating, Course, Tag

# one article can have multiple tags
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        depth = 1

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

#Each course has multiple articles [one-to-many]
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class ArticleRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleRating
        fields = ['id','likes', 'dislikes']


# #Each course has multiple articles [one-to-many]
# class CourseSerializer(serializers.ModelSerializer):
#     #nesting multiple models
#     articles = ArticleSerializer(many=True)

#     class Meta:
#         model = Course
#         fields = '__all__'

#     def create(self, validated_data):
#         articles_data = validated_data.pop('articles')
#         course = Course.objects.create(**validated_data)
#         for article_data in articles_data:
#             Article.objects.create(course=course, **article_data)
#         return course