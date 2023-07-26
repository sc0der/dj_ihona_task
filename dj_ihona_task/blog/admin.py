from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Tag, Post, Image, Question, UserQAProfile, UserResponse

# unregistered group
admin.site.unregister(Group)


# customizing user profile
class UserResponseInline(admin.TabularInline):  # or admin.StackedInline if you prefer that style
    model = UserResponse
    extra = 0  # This means no empty forms will be shown; you can adjust as necessary
    readonly_fields = ['question', 'selected_answer'] 

class UserQAProfileAdmin(admin.ModelAdmin):
    inlines = [UserResponseInline]


# registration of models
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Question)
admin.site.register(UserResponse)
admin.site.register(UserQAProfile, UserQAProfileAdmin)

