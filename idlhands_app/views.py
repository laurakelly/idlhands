from django.template import Context, loader
from idlhands_app.models import UserProfile, Project, Image#, ImageForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django import forms

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

    if request.user.is_authenticated():
        return render_to_response('profile.html',
                {'session_username':request.user.username,'username':username,\
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
    banned = ['admin', 'login','logout','profiles', 'images', 'portfolios', 'portfolio' 'new','upload', 'about',\
              'series','signup', 'home', 'profile']
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
                return render_to_response('home.html', {'session_username':user.username})
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

def project(request):
    pass

def users(request):
    pass

def portfolio(request):
    if request.user.is_authenticated():
        user = request.user
        user_profile = user.get_profile()
        username = user.username
        info = user_profile.info
        website = user_profile.website
        trendsetter = user_profile.trendsetter
        gallery = user_profile.trendsetter
        avatar = user_profile.avatar
        location = user_profile.location
        projects = Project.objects.filter(user=user.id)
        return render_to_response('portfolio.html',
                {'session_username':request.user.username,'username':username,\
                'info':info, 'website':website, 'trendsetter':trendsetter,'gallery':gallery,\
                'avatar':avatar, 'location':location})
    else:
        return render_to_response('login.html', {'portfolio':True})

def new_project(request):
    if request.user.is_authenticated():
        if request.method == "POST":
#            form = ImageForm(request.POST, request.user)
            return HttpResponseRedirect('/success')
        else:
            return render_to_response('new_project.html')
    else:
        return render_to_response('login.html', {'project':True})

def signup(request):
    if request.method == "POST":
#        form = SignupForm(request.POST, request.user)
        return render_to_response('signup_success.html')
    else:
        return render_to_response('signup.html')


#def upload(request):
#    if request.user.is_authenticated():
#        if request.method == 'POST':
#            form = ImageForm(request.POST, request.user)
#            return HttpResponseRedirect('/success')
#        else:
#            return render_to_response('upload.html')
#    else:
#        return render_to_response('login.html', {'log_in':True})

def success(request):
    pass



#class ImageForm(forms.Form):
#    title = forms.CharField(max_length=140)
#    project = forms.ModelChoiceField(queryset=Project.objects.all(user=user))
#    artist =