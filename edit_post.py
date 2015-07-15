import webapp2
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb
import db_defs

class EditPost(blobstore_handlers.BlobstoreUploadHandler):
    def allRequiredFields(self):
        if (self.request.get('username') and self.request.get('user_email')):
            return True
        else:
            return False    

    def updateValues(self, post):
        post.username = self.request.get('username')
        post.user_email = self.request.get('user_email')
        post.subject = self.request.get('subject')
        post.message = self.request.get('message')
        post.city = self.request.get('city')
        post.state = self.request.get('state')
        post.zipcode = int(self.request.get('zipcode'))
        if self.request.get('importance') == "Urgent":
            post.importance_flag = True
        else:
            post.importance_flag = False
        if self.request.get('update') == 'updated':
            update = self.request.get('update')

    def post(self):
        post_key = ndb.Key(urlsafe=self.request.get('key'))
        post = post_key.get()
        if self.allRequiredFields():
            self.updateValues(post)
            if self.request.get('image-action') == 'remove':
                post.icon = None
            elif self.request.get('image-action') == 'change':
                upload_files = self.get_uploads('icon')
                if upload_files != []:
                    blob_info = upload_files[0]
                    post.icon = blob_info.key()
        post.languages = [ndb.Key(urlsafe=x) for x in self.request.get_all('languages[]')]
        post.put()
        self.redirect('/edit?key=' + post_key.urlsafe() + '&type=post&confirmation=yes')

class DeletePost(EditPost):
    def get(self):
        post_key = ndb.Key(urlsafe=self.request.get('key'))
        post_key.delete()
        self.redirect('/')
        self.response.write("The post has been deleted.")