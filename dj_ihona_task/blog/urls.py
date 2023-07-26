# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TagViewSet, PostViewSet, QuestionViewSet, UserQAProfileViewSet

router = DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'userprofiles', UserQAProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
