from boto.s3.connection import S3Connection
from boto.s3.key import Key
from boto_cred import access_id, secret_key
from django.contrib.auth.models import User, Image

def upload_boto(uid, image):
    # Establish S3 connection
    access_id = access_id()
    secret_key = secret_key()
    conn = S3Connection(access_id, secret_key)

    # S3 index is username concatenated with the number of images a user has + 1

    num = len(Image.objects.filter(artist=uid)) + 1
    user = User.objects.get(id=uid)
    username = user.username
    title = image.title
    filename = username + str(num)

    # TODO: Change this to search with regex
    location = ('/idlhands_app/static/' + image.id + ".jpg")

    #  Upload image to 'idlhands' S3 bucket

    buckets = conn.get_all_buckets()
    k = Key(buckets[0])
    k.key = filename
    k.set_contents_from_filename(location)
    k.set_acl('public-read')
