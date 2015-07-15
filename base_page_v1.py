import webapp2
import os
import jinja2

#The design and code layout of base page taken from CS496 OSU lectures
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + 
        '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
    )

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

