import base_page

class Language(base_page.RenderPostInfo):
    def get(self):
        self.render('language_list.html')