#!/usr/bin/python3
"""Flask server (variable app)
"""


from flask import Flask, jsonify
from models import storage
from flask_cors import CORS
from os import getenv
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False

# enable CORS and allow for origins:
CORS(app, resources={r'/api/v1/*': {'origins': '0.0.0.0'}})


@app.teardown_appcontext
def downtear(self):
    '''Status of your API'''
    storage.close()

# Error handlers for expected app behaviour
@app.errorhandler(404)
def page_not_found(error):
    '''return render_template'''
    return jsonify(error='Not found'), 404


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
