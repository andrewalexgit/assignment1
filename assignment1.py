from flask import Flask, render_template
import json
import requests
import webbrowser
import requests_toolbelt.adapters.appengine

requests_toolbelt.adapters.appengine.monkeypatch()

# Request JSON Object from NASA
target = 'https://api.nasa.gov/planetary/apod?api_key='
key = 'DEMO_KEY'

apod_raw = requests.get(target + key)
apod_raw = apod_raw.content
apod_obj = json.loads(apod_raw.decode('utf-8'))

app = Flask(__name__)


@app.route('/')
def init():

	# Grab picture of the day
	picture_of_the_day = apod_obj['url']

	# Initialize Page
	return render_template('pod.html', picture_of_the_day = picture_of_the_day)



