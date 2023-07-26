from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Post(models.Model):
    title = models.CharField(max_length=255)
    images = models.ManyToManyField('Image', blank=True, related_name="post_images")
    content = models.TextField()
    modification_date = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
    image = models.ImageField(upload_to='posts/images/')
    post = models.ForeignKey(Post, related_name='image_post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    post = models.ForeignKey(Post, related_name='polls', on_delete=models.CASCADE)
    question_text = models.TextField()
    choice_1 = models.CharField(max_length=255)
    choice_2 = models.CharField(max_length=255)
    choice_3 = models.CharField(max_length=255)
    choice_4 = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class UserQAProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    answered_questions = models.ManyToManyField(Question, through='UserResponse')
    created_at = models.DateTimeField(auto_now_add=True)

class UserResponse(models.Model):
    profile = models.ForeignKey(UserQAProfile, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)