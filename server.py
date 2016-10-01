#!/usr/bin/env python
# coding=utf-8
"""
Filename:       server.py
Last modified:  2016-10-01 19:45

Description:

"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


from os import listdir
from os.path import isfile, join

from flask import Flask, jsonify, request
from setting import MODEL_DIR, IMAGE_DIR, HOST, PORT
import uuid
from werkzeug import secure_filename


app = Flask(__name__)

from cmd import run_th


ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/image/models', methods=['GET'])
def get_avaible_models():
    """
    """
    models = [f for f in listdir(MODEL_DIR) if isfile(
        join(MODEL_DIR, f)) and f.endswith('.t7')]
    return jsonify({"models": models})


@app.route('/image/convert/<string:model>', methods=['POST'])
def convert(model):
    file = request.files['image']
    if file and allowed_file(file.filename):
        uid = str(uuid.uuid4())
        filename = secure_filename(file.filename)
        intput_filename = join(IMAGE_DIR, '%s_%s_%s' % (uid, 'in', filename))
        file.save(filename)
    else:
        return jsonify({'code': -1, 'msg': 'save file error'})
    output_filename = join(IMAGE_DIR, '%s_%s_%s' % (uid, 'out', filename))
    result = run_th(intput_filename, model, output_filename)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
