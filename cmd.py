#!/usr/bin/env python
# coding=utf-8
"""
Filename:       setting.py
Last modified:  2016-10-01 19:13

Description:

"""

from setting import CMD, TIMEOUT
import time
from subprocess32 import STDOUT, check_output


def run_th(input_image, model, save_path):
    cmd = CMD % (input_image, model, save_path)
    try:
        start_time = time.time()
        output = check_output(cmd, stderr=STDOUT, timeout=TIMEOUT)
        end_time = time.time()
        print 'run %s in (%d) s : result %s ' % (cmd, int(end_time - start_time), output)
        return {'code': 0}
    except Exception, e:
        print 'run_th error', str(e)
        return {'code': -2, 'msg': str(e)}
