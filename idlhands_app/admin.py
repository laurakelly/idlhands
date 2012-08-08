from django.contrib import admin
from idlhands_app.models import UserProfile, User, Image, Project, Vote, Date, Show

class ProjectInline(admin.StackedInline):
    model = Project

class ImageInline(admin.StackedInline):
    model = Image

class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user','info', 'website', 'location','trendsetter', 'gallery', 'avatar']

admin.site.register(UserProfile, UserProfileAdmin)

class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'artist', 'media', 'tags']
    inlines = [ImageInline]

admin.site.register(Project, ProjectAdmin)

class ImageAdmin(admin.ModelAdmin):
    fields = ['title', 'artist', 'project','tags', 'image']

admin.site.register(Image, ImageAdmin)


# TODO: fields that didn't work with admin

# User: user_since
# Project: pub_date, update
# Image: pub_date