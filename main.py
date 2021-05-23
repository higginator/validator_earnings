from flask import Flask, json
from flask_cors import CORS
import requests
from thousand_validators import *

app = Flask(__name__)
CORS(app)

"""
    Endpoint returns a JSON string of the validators in the Polkadot Thousand Validators Programme.
"""
@app.route('/validators/polkadot')
def polkadot_validators():
    validators = get_polkadot_validators()
    return json.dumps(validators)

"""
    Endpoint returns a JSON string of the validators in the Kusama Thousand Validators Programme.
"""
@app.route('/validators/kusama')
def kusama_validators():
    validators = get_kusama_validators()
    return json.dumps(validators)


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
