#!/usr/bin/env python
# coding=utf-8
"""
Filename:       setting.py
Last modified:  2016-09-18 16:08

Description:

"""

from setting import CMD, TIMEOUT
from subprocess32 import STDOUT, check_output


def run_th(args):
    th_cmd = '%s %s' % (cmd,args)
    try:
        output = check_output(th_cmd, stderr=STDOUT, timeout=TIMEOUT)
    except Exection, e:
        pass
