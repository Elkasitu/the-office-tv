from flask import request, Flask, render_template
from os import walk

app = Flask(__name__)
SRC_PATH = 'static/content/'

@app.route('/')
def index():
    files = []
    # walk the content folder recursively and add all
    # filenames to the files list
    for (dirpath, dirnames, filenames) in walk(SRC_PATH):
        files.extend(filenames)

    enum = enumerate(files)

    return render_template('index.html', files=enum, path=SRC_PATH)
