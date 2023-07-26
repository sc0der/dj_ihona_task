from django.shortcuts import render

# Create your views here.

# views.py

from rest_framework import viewsets
from .models import Tag, Post, Question, UserQAProfile
from .serializers import TagSerializer, PostSerializer, QuestionSerializer, UserQAProfileSerializer

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
