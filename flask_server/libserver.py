# flask-server
# author: Ondrej Sika, http://ondrejsika.com, dev@ondrejsika.com

import os

from flask import render_template
from flask.views import View

from normpath import normpath

class BaseView(View):
    def __init__(self, template_name):
        self.template_name = template_name
    def dispatch_request(self):
        return render_template(self.template_name)

def add_view(app_root, file_path, app):
    path = file_path.replace(normpath(app_root, "templates"), "")[1:]
    if path[-5:] == ".html":
        url = path.replace(".html", "")
        if url[-5:] == "index": url = url[:-5]
        if url[-4:] == "home": url = url[:-4]
    else:
        url = path
    app.add_url_rule('/'+url, view_func=BaseView.as_view(path, template_name=path))

def get_file_tree(*args):
    for path, dirs, files in os.walk(normpath(*args)):
        for filename in files:
            yield os.path.join(path, filename)