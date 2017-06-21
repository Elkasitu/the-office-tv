from flask import Flask, render_template
from os import walk, listdir

app = Flask(__name__)
SRC_PATH = 'static/'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/shows')
def tv_shows():
    shows_path = SRC_PATH + 'content/'
    thumb_path = SRC_PATH + 'thumbnails/'
    folders = listdir(shows_path)
    return render_template('shows.html', shows=folders, path=thumb_path)


@app.route('/shows/<showname>')
def tv_show(showname):
    path = SRC_PATH + 'content/' + showname + '/'
    files = []
    # walk the content folder recursively and add all
    # filenames to the files list
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)

    enum = enumerate(files)
    return render_template('show.html', files=enum, path=path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
