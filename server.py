#!/usr/bin/env python
# coding=utf-8
"""
Filename:       server.py
Last modified:  2016-09-18 16:31

Description:

"""

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from flask import Flask,jsonify
app = Flask(__name__)

from cmd import run_th


@app.route('/th_image', methods=['POST'])
def th_image():
    output = run_th()
    return output

if __name__ == '__main__':
    app.run()
