from django.db import models

class User(models.Model):
    password = models.CharField(max_length=200)
    info = models.CharField()###### fill in max length later
    username = models.CharField()###### fill in max length later
    website =
    trendsetter = models.Boolean()#####
    gallery = models.Boolean()######
    avatar = models.CharField(max_length=200)

class Project(models.Model):
    title = models.CharField(max_length=200
    artist = ForeignKey(User)
    pub_date = models.DateTimeField('date published')


class Image(models.Model):
    title = models.CharField(max_length=200)
    artist = ForeignKey(User)
    pub_date = models.DateTimeField('date published')
    votes = models.IntegerField()#### don't know how this will work
    tags = models.CharField(max_length=200)
    media = models.CharField(max_length=200)
    url = models.CharField(max_length=200)

class Vote(models.Model):
    user = ForeignKey(User)
    image = ForeignKey(Image)
    date = models.DateTimeField('date of vote')

class Date(models.Model):
    date = models.DateTimeField('date')

class Show(models.Model):
    exhibition = models.Boolean()###### boolean?
    opening_date = models.ForeignKey(Date)
    opening_start = models.DateTimeField('start date')
    opening_end = models.DateTimeField('end date')
    exhibition_start = models.DateTimeField('exhibition start')### only if exhibition is true
    exhibition_end = models.DateTimeField('exhibition end')### only if exhibition is true
    creator = models.ForeignKey(User)
    description = models.CharField()### max length?
    location = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)#### is there a location/address field?
    state = models.CharField(max_length=200)### will be a drop-down
    country = models.CharField(max_length=200)#### will be drop-down
