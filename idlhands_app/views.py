from django.template import Context, loader
from idlhands_app.models import UserProfile, Project, Image
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

def home(request):
    if request.user.is_authenticated():
        session_id = request.session.get('member_id')
        session_user = User.objects.get(id=session_id)
        return render_to_response('home.html',{'session_username':session_user.username})
    return render_to_response('home.html')

def user_profile(request,username):
    user = User.objects.get(username=username)
    id = user.id
    user_profile = user.get_profile()
    username = user.username
    info = user_profile.info
    website = user_profile.website
    trendsetter = user_profile.trendsetter
    gallery = user_profile.trendsetter
    avatar = user_profile.avatar
    location = user_profile.location

    session_id = request.session.get('member_id')
    session_user = User.objects.get(id=session_id)
    if session_user.is_authenticated():
        return render_to_response('profile.html',
                {'session_username':session_user.username,'username':username,\
                'info':info, 'website':website, 'trendsetter':trendsetter,'gallery':gallery,\
                'avatar':avatar, 'location':location})
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

def new_user(request, username, email, password):
    banned = ['admin', 'login','logout','profiles', 'images', 'portfolios', 'new']
    if username in banned:
        pass
    user = User.objects.create_user(username, email, password)
    user.save()
    pass

@csrf_exempt
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['member_id'] = user.id
                return render_to_response('home.html')
        else:
            # Return an 'invalid login' error message.
            return render_to_response('login.html', {'invalid':True})
    else:
        return render_to_response('login.html', {'invalid':False})

def logout_page(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    logout(request)
    return render_to_response('logged_out.html')