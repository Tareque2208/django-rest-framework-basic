from django.db import models

# Create your models here.

class ArticleRating(models.Model):
    likes=models.BigIntegerField(default=0)
    dislikes=models.BigIntegerField(default=0)

    def __int__(self):
        return self.likes

class Tag(models.Model):
    title=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Course(models.Model):
    title=models.CharField(max_length=100)
    teacher=models.CharField(max_length=100)
    tag=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.courseTitle

class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    #One to one
    rating = models.OneToOneField(ArticleRating, on_delete=models.CASCADE, null=True)
    #One to many
    tags = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.title

