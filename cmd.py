#!/usr/bin/env python
# coding=utf-8
"""
Filename:       setting.py
Last modified:  2016-10-02 09:32

Description:

"""

from setting import CMD, TIMEOUT, TEXTURE_NETS_PATH, HOSTNAME
import time
from subprocess32 import STDOUT, check_output


def run_th(input_image, model, save_path):
    cmd = CMD % (input_image, model, save_path)
    try:
        start_time = time.time()
        output = check_output(cmd, cwd=TEXTURE_NETS_PATH,
                              stderr=STDOUT, timeout=TIMEOUT, shell=True)
        end_time = time.time()
        print 'run %s in (%d) s : result %s ' % (cmd, int(end_time - start_time), output)
        return {'code': 0, 'url': '%s/images/%s' % (HOSTNAME, save_path)}
    except Exception, e:
        print 'run_th error', str(e)
        return {'code': -2, 'msg': str(e)}
