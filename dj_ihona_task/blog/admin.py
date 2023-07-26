from django.contrib import admin

# Register your models here.
from .models import Tag, Post, Image, Question, UserQAProfile, UserResponse

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Question)
admin.site.register(UserQAProfile)
admin.site.register(UserResponse)