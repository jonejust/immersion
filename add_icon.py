import webapp2
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
import add_post

class AddPost(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        upload_files = self.get_uploads('icon')
        if upload_files != []:
            blob_info = upload_files[0]
            return add_post.AddPostMain(self.request, self.response).post(icon_key=blob_info.key())
        else:
            return add_post.AddPostMain(self.request, self.response).post()
