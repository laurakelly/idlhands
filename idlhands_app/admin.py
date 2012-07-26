from django.contrib import admin
from idlhands_app.models import User, Image, Project, Vote, Date, Show

class ProjectInline(admin.StackedInline):
    model = Project

class ImageInline(admin.StackedInline):
    model = Image

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'password', 'user_since','info', 'email', 'website', 'trendsetter', 'gallery', 'avatar']
    inlines = [ProjectInline]
    list_display = ('username', )

admin.site.register(User, UserAdmin)

class ProjectAdmin(admin.ModelAdmin):
    fields = ['title','pub_date', 'update', 'artist']
    inlines = [ImageInline]

admin.site.register(Project, ProjectAdmin)

class ImageAdmin(admin.ModelAdmin):
    fields = ['title', 'artist', 'pub_date', 'project','tags', 'media', 'url']

admin.site.register(Image, ImageAdmin)


# TODO: fields that didn't work with admin

# User: user_since
# Project: pub_date, update
# Image: pub_date