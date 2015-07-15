import webapp2

config = {'default-group': 'base-data'}

app = webapp2.WSGIApplication([
  ('/edit/post', 'edit_post.EditPost'),
  ('/edit', 'edit.Edit'),
  ('/delete/post', 'edit_post.DeletePost'),
  ('/delete/language', 'edit.DeleteLanguage'),
  ('/add_icon', 'add_icon.AddPost'),
  ('/add_language', 'add_post.AddPostMain'),
  ('/view/languages', 'lang.Language'),
  ('/add_post', 'add_post.AddPostMain'),
  ('/view', 'view.ViewPost'),
  ('/', 'view.ViewAll')
  ], debug=True, config=config)


#from google.appengine.api import users


"""
class MainPage(webapp2.RequestHandler):
    def get(self):
        #check for active Google account session
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/html; charset=utf-8'
            self.response.write(user.nickname() + ' is logged in.')

        else:
            self.redirect(users.create_login_url(self.request.uri))    
"""