# urls.py

from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import TagViewSet, PostViewSet, QuestionViewSet, UserQAProfileViewSet

router = DefaultRouter()

router.register(r'tags', TagViewSet)
router.register(r'posts', PostViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'userprofiles', UserQAProfileViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]