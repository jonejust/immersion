import webapp2
import base_page
from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.ext import blobstore
import db_defs

class Edit(base_page.BaseHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}
        self.template_values['edit_url'] = blobstore.create_upload_url('/edit/post')

    def get(self):
        if self.request.get('type') == 'post':
            post_key = ndb.Key(urlsafe=self.request.get('key'))
            post = post_key.get()
            self.setTemplateValues(post)
            #self.template_values['username'] = post.username
            if post.icon:
                self.template_values['img_url'] = images.get_serving_url(post.icon, crop=True, size=64)
            self.template_values['post'] = post
            languages = db_defs.Language.query(ancestor=ndb.Key(db_defs.Language, self.app.config.get('default-group')))
            language_boxes = []
            for l in languages:
                if l.key in post.languages:
                    language_boxes.append({'language':l.language, 'key':l.key.urlsafe(), 'checked':True})
                else:
                    language_boxes.append({'language':l.language, 'key':l.key.urlsafe(), 'checked':False})
        self.template_values['languages'] = language_boxes
        self.render('edit.html', self.template_values)

class DeleteLanguage(base_page.BaseHandler):
    def get(self):
        if self.request.get('type') == 'language':
            language_key = ndb.Key(urlsafe=self.request.get('key'))
            language_key.delete()
            self.redirect('/view/languages')