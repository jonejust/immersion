import webapp2
import base_page
import db_defs
from google.appengine.ext import ndb
from google.appengine.ext import blobstore

class AddPostMain(base_page.RenderPostInfo):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}
        self.template_values['upload_url'] = blobstore.create_upload_url('/add_icon')

#    def render(self, page):
#        self.template_values['languages'] = [{'language':x.language, 'key':x.key.urlsafe()} for x in db_defs.Language.query(ancestor=ndb.Key(db_defs.Language, self.app.config.get('default-group'))).fetch()]
#        self.template_values['posts'] = [{'subject':x.subject, 'key':x.key.urlsafe()} for x in db_defs.Post.query(ancestor=ndb.Key(db_defs.Post, self.app.config.get('default-group'))).fetch()]
#        base_page.BaseHandler.render(self, page, self.template_values)

    def get(self):
        self.render('add_post.html')

    def post(self, icon_key=None):
        action = self.request.get('action')
        if action == 'add_post':
            k = ndb.Key(db_defs.Post, self.app.config.get('default-group'))
            p = db_defs.Post(parent=k)
            p.username = self.request.get('username')
            p.user_email = self.request.get('user_email')
            p.subject = self.request.get('subject')
            p.message = self.request.get('message')
            p.city = self.request.get('city')
            p.state = self.request.get('state')
            p.zipcode = int(self.request.get('zipcode'))
            p.languages = [ndb.Key(urlsafe=x) for x in self.request.get_all('languages[]')]
            p.icon = icon_key
            if self.request.get('importance') == 'Important':
                p.importance_flag = True
            else:
                p.importance_flag = False
            p.put()
            self.template_values['confirmation_message'] = 'Your message with subject ' + p.subject + ' was posted!'
        elif action == 'add_language':
            k = ndb.Key(db_defs.Language, self.app.config.get('default-group'))
            l = db_defs.Language(parent=k)
            l.language = self.request.get('language')

            #Check to make sure that the language is unique
            add = True
            for x in db_defs.Language.query(ancestor=ndb.Key(db_defs.Language, self.app.config.get('default-group'))).fetch():
                if x.language == l.language:
                    add = False
                    self.template_values['confirmation_message'] = 'Your language ' + l.language + ' is already in the database. It has not been added to the database again.'
            if add == True:
                l.put()
                self.template_values['confirmation_message'] = 'Your language ' + l.language + ' has been added.'
        else:
            self.template_values['confirmation_message'] = 'Action ' + action + ' is unknown.'
        self.template_values['languages'] = db_defs.Language.query(
            ancestor=ndb.Key(db_defs.Language, self.app.config.get('default-group'))).fetch
        self.render('add_post.html')



"""

    template_variables = {'post_email': 'jonejust@onid.oregonstate.edu',
            'post_language': 'Mandarin'}

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('add_post.html')
        self.response.write(template.render(self.template_variables))
        """