from django.template import Context, loader
from idlhands_app.models import UserProfile, Project, Image
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    return render_to_response('home.html')

def user_profile(request,username):
    user = User.objects.get(username=username)
    id = user.id
    user_profile = UserProfile.objects.filter(user=id)

    username = user_profile.username
    info = user_profile.info
    website = user_profile.website
    trendsetter = user_profile.trendsetter
    gallery = user_profile.trendsetter
    avatar = user_profile.avatar
    location = user_profile.location
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