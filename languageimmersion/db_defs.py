from google.appengine.ext import ndb

class Post(ndb.Model):
    username = ndb.StringProperty(required=True)
    user_email = ndb.StringProperty(required=True)
    subject = ndb.StringProperty(required=True)
    message = ndb.StringProperty(required=True)
    city = ndb.StringProperty(required=False)
    state = ndb.StringProperty(required=False)
    zipcode = ndb.IntegerProperty(required=True)
    languages = ndb.KeyProperty(repeated=True)
    importance_flag = ndb.BooleanProperty(required=True)
    icon = ndb.BlobKeyProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


class Language(ndb.Model):
    language = ndb.StringProperty(required=True)