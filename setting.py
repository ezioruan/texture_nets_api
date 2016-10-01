#!/usr/bin/env python
# coding=utf-8
"""
Filename:       setting.py
Last modified:  2016-10-01 15:57

Description:

"""

import os

HERE = os.path.abspath(os.path.dirname(__file__))
TEXTURE_NETS_PATH = "/home/ubuntu/texture_nets"
MODEL_DIR = "/home/ubuntu/texture_nets"
IMAGE_DIR = os.path.join(HERE,"images")
if not os.path.exists(IMAGE_DIR):
    os.mkdir(IMAGE_DIR)


CMD = "th test.lua --input_image %s -model_t7 %s -save_path %s -cpu"
# will cancel after timeout (seconds)
TIMEOUT = 15
