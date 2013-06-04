# flask-server
# author: Ondrej Sika, http://ondrejsika.com, dev@ondrejsika.com

from flask import Flask

from normpath import normpath
from libserver import get_file_tree, add_view
from errorhandlers import errorhandlers

def FlaskServer(import_name, app_root):
    app = Flask(import_name)
    for path in get_file_tree(app_root, "templates"):
        add_view(app_root, path, app)
    app = errorhandlers(app, app_root)
    return app
