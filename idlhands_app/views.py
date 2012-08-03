from django.template import Context, loader
from idlhands_app.models import User, Project, Image
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html')

def user(request,username):
    user = User.objects.get(username=username)
    username = user.username
    info = user.info
    website = user.website
    trendsetter = user.trendsetter
    gallery = user.trendsetter
    avatar = user.avatar
    location = user.location
    return render_to_response('profile.html',
            {'username':username, 'info':info, 'website':website, \
            'trendsetter':trendsetter,'gallery':gallery,\
            'avatar':avatar, 'location':location})

def project(request,username,id):
    project = Project.objects.get(id=id)
    title = project.title
    images = Image.objects.filter(project=id)
    media = project.media
    tags = project.tags
    return render_to_response('project.html',{'title':title, \
            'images':images, 'artist':username, 'tags':tags, 'media':media})