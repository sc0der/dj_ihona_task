from django.contrib import admin

# Register your models here.
from .models import Tag, Post, Image, Question, UserQAProfile, UserResponse

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Image)
admin.site.register(Question)
admin.site.register(UserResponse)

class UserResponseInline(admin.TabularInline):  # or admin.StackedInline if you prefer that style
    model = UserResponse
    extra = 0  # This means no empty forms will be shown; you can adjust as necessary
    readonly_fields = ['question', 'selected_answer'] 

class UserQAProfileAdmin(admin.ModelAdmin):
    inlines = [UserResponseInline]

admin.site.register(UserQAProfile, UserQAProfileAdmin)