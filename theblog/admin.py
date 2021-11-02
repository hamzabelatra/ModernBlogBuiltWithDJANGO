from django.contrib import admin

# Register your models here.
from .models import Post, Category,Profile

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Category)