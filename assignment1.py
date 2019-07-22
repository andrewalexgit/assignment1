from flask import Flask, render_template
import json
import urllib
import webbrowser

# Request JSON Object from NASA
target = 'https://api.nasa.gov/planetary/apod?api_key='
key = 'DEMO_KEY'

apod_raw = urllib.request.urlopen(target + key)
apod_raw = apod_raw.read()
apod_obj = json.loads(apod_raw.decode('utf-8'))

app = Flask(__name__)


@app.route('/')
def init():

	# Grab picture of the day
	picture_of_the_day = apod_obj['url']

	# Initialize Page
	return render_template('pod.html', picture_of_the_day = picture_of_the_day)



