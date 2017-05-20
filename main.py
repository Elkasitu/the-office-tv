from flask import request, Flask, render_template
from os import walk

app = Flask(__name__)

@app.route('/')
def index():
    files = []
    # walk the content folder recursively and add all
    # filenames to the files list
    for (dirpath, dirnames, filenames) in walk('static/'):
        files.extend(filenames)
    return render_template('index.html', files=files)
