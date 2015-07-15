import webapp2
import os
import jinja2

class Begin(webapp2.RequestHandler):
    template_variables = {'post_email': 'jonejust@onid.oregonstate.edu',
            'post_language': 'Mandarin'}

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('add_post.html')
        self.response.write(template.render(self.template_variables))

    def post(self):
        self.template_variables['form_content'] = {}
        template = JINJA_ENVIRONMENT.get_template('add_post.html')
        for i in self.request.arguments():
            self.template_variables['form_content'][i] = self.request.get(i)
        self.response.write(template.render(self.template_variables))