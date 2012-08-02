from django.contrib import admin
from idlhands_app.models import User, Image, Project, Vote, Date, Show

class ProjectInline(admin.StackedInline):
    model = Project

class ImageInline(admin.StackedInline):
    model = Image

class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'password','info', 'email', 'website', 'location','trendsetter', 'gallery', 'avatar']
    inlines = [ProjectInline]
#    list_display = (['username', 'user_since'])

admin.site.register(User, UserAdmin)

class ProjectAdmin(admin.ModelAdmin):
    fields = ['title', 'artist']
    inlines = [ImageInline]

admin.site.register(Project, ProjectAdmin)

class ImageAdmin(admin.ModelAdmin):
    fields = ['title', 'artist', 'project','tags', 'media', 'url']

admin.site.register(Image, ImageAdmin)


# TODO: fields that didn't work with admin

# User: user_since
# Project: pub_date, update
# Image: pub_date