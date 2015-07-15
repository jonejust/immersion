import webapp2
import os
import jinja2
import db_defs
from google.appengine.ext import ndb

class BaseHandler(webapp2.RequestHandler):
    template_values = {}

    @webapp2.cached_property
    def jinja2(self):
        return jinja2.Environment(
            loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + 
                '/templates'),
            extensions=['jinja2.ext.autoescape'],
            autoescape=True
            )

    def render(self, template, template_variables={}):
        template = self.jinja2.get_template(template)
        self.response.write(template.render(template_variables))

    def setTemplateValues(self, post):
        self.template_values['username'] = post.username
        self.template_values['user_email'] = post.user_email
        self.template_values['subject'] = post.subject
        self.template_values['message'] = post.message
        self.template_values['city'] = post.city
        self.template_values['state'] = post.state
        self.template_values['zipcode'] = post.zipcode
        self.template_values['importance'] = post.importance_flag 

class RenderPostInfo(BaseHandler):
    def render(self, page):
        self.template_values['languages'] = [{'language':x.language, 'key':x.key.urlsafe()} for x in db_defs.Language.query(ancestor=ndb.Key(db_defs.Language, self.app.config.get('default-group'))).fetch()]
        self.template_values['posts'] = [{'subject':x.subject, 'key':x.key.urlsafe()} for x in db_defs.Post.query(ancestor=ndb.Key(db_defs.Post, self.app.config.get('default-group'))).fetch()]
        BaseHandler.render(self, page, self.template_values)        