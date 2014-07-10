# flask-server
# author: Ondrej Sika, http://ondrejsika.com, dev@ondrejsika.com

import os
from flask import render_template
from normpath import normpath


def errorhandlers(app, app_root):
    if os.path.exists(normpath(app_root, "templates", "404.html")):
        @app.errorhandler(404)
        def not_found(error):
            return render_template('404.html'), 404
    return app
