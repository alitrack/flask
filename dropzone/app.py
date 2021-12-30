# -*- coding: utf-8 -*-
"""
    :author: Steven Lee <rocsky@gmail.com>
    :copyright: (c) 2017 by Steven Lee.
    :license: MIT, see LICENSE for more details.
"""
import os

from flask import Flask, render_template, request

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
)


@app.route('/', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        file_path = os.path.join(app.config['UPLOADED_PATH'], f.filename)
        f.save(file_path)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
