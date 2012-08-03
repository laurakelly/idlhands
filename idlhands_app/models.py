from django.db import models

class User(models.Model):
    # Represent User objects as usernames when called in the shell
    def __unicode__(self):
        return self.username

    password = models.CharField(max_length=64)
    info = models.TextField(max_length=200)
    username = models.CharField(unique=True, max_length=64)
    email = models.CharField(max_length=320)
    website = models.URLField()
    trendsetter = models.NullBooleanField()
    gallery = models.BooleanField()
    avatar = models.URLField(max_length=200)
    user_since = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=200)
#    fav_users = models.ManyToManyField('User')

class Project(models.Model):
    # Represent Project objects as titles when called in the shell
    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=140)
    artist = models.ForeignKey('User')
    pub_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    media = models.CharField(max_length=140)
    tags = models.CharField(max_length=140)


class Image(models.Model):
    # Represent Image objects as titles when called in the shell
    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=140)
    artist = models.ForeignKey('User')
    project = models.ForeignKey('Project')
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=140)
    url = models.URLField()

# TODO: Add votes after Projects feature is working

class Vote(models.Model):
    user = models.ForeignKey('User')
    image = models.ForeignKey('Image')
    date = models.DateTimeField(auto_now_add=True)

# TODO: Add Calendar Feature After Votes Are Working

class Date(models.Model):
    date = models.DateTimeField()

class Show(models.Model):
    exhibition = models.BooleanField()
    opening_date = models.ForeignKey('Date')
    opening_start = models.DateTimeField()
    opening_end = models.DateTimeField()
    exhibition_start = models.DateTimeField(null=True)### only if exhibition is true
    exhibition_end = models.DateTimeField(null=True)### only if exhibition is true
    creator = models.ForeignKey('User')
    description = models.TextField(max_length=1000)
    location_name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=64)
    country = models.CharField(max_length=200)
