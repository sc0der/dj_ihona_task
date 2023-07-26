from django.shortcuts import render

# Create your views here.

# views.py

from rest_framework import viewsets
from .models import Tag, Post, Question, UserQAProfile, Image
from .serializers import TagSerializer, PostSerializer, QuestionSerializer, UserQAProfileSerializer, ImageSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class UserQAProfileViewSet(viewsets.ModelViewSet):
    queryset = UserQAProfile.objects.all()
    serializer_class = UserQAProfileSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer