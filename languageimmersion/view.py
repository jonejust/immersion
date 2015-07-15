import webapp2
import add_post
import base_page
from google.appengine.ext import ndb
from google.appengine.api import images
import edit
import db_defs

class ViewAll(add_post.AddPostMain):
    def get(self):
        self.render('view_posts.html')

class ViewPost(base_page.RenderPostInfo):
    def get(self):
        post_key = ndb.Key(urlsafe=self.request.get('key'))
        post = post_key.get()
        self.setTemplateValues(post)
        if post.icon:
                self.template_values['img_url'] = images.get_serving_url(post.icon, crop=True, size=64)
        self.template_values['key'] = self.request.get('key')
        self.render('view_post.html')
