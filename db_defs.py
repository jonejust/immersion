from google.appengine.ext import ndb

"""
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
    """

class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    user_email = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)
    city = ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    zipcode = ndb.IntegerProperty(required=True)

class Post(ndb.Model):
    subject = ndb.StringProperty(required=True)
    message = ndb.StringProperty(required=True)
    date = ndb.DateTimeProperty(auto_now_add=True)
    user_key = ndb.KeyProperty(required=True)
    replies = ndb.KeyProperty(repeated=True)
    city = ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    zipcode = ndb.IntegerProperty(required=True)
    languages = ndb.KeyProperty(repeated=True)
    icon = ndb.BlobKeyProperty()

    def to_dict(self):
        d = super(Post, self).to_dict()
        d['replies'] = [r.id() for r in d['replies']]
        d['languages'] = [l.id() for l in d['languages']]
        d['user_key'] = user_key.id()
        delete d['icon'] 
        return d

class Reply(ndb.Model):
    post = ndb.KeyProperty(required=True)
    user_key = ndb.KeyProperty(required=True)
    city = ndb.StringProperty(required=True)
    state = ndb.StringProperty(required=True)
    zipcode = ndb.IntegerProperty(required=True)
    icon = ndb.BlobKeyProperty()
    message = ndb.StringProperty(required=True)

    def to_dict(self):
        d = super(Reply, self).to_dict()
        d['post'] = post.id()
        d['user_key'] = user_key.id()
        delete d['icon']

class Language(ndb.Model):
    language = ndb.StringProperty(required=True)