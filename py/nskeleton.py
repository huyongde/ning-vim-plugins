#!/usr/bin/env python
#coding: utf-8
#file   : nskeleton.py
#author : ning
#date   : 2013-11-19 16:57:32


import vim
from vim_bridge import bridged

import re
import os, sys
import time
from datetime import datetime

PWD = os.path.dirname(os.path.realpath(__file__))

SKELETONS_PATH = PWD+'/../skeletons'

def format_time(timestamp=None, fmt='%Y-%m-%d %H:%M:%S'):
    if not timestamp:
        timestamp = time.time()
    t = datetime.fromtimestamp(float(timestamp))
    return t.strftime(fmt)

@bridged
def load_skeleton():
    cb = vim.current.buffer     # gets the current buffer

    def replace(body):
        path = cb.name
        filename = os.path.basename(path)
        base, ext = os.path.splitext(filename)
        ext = ext[1:]
        dirname = os.path.basename(os.path.dirname(path))

        body = body.replace('<+DATE+>', format_time())
        body = body.replace('<+FILE_NAME+>', filename)
        body = body.replace('<+FILE_NAME_BASE+>', base)
        body = body.replace('<+FILE_NAME_U+>', base.upper())
        body = body.replace('<+DIR_NAME+>', dirname)
        return body

    filetype = cb.name.split('.')[-1]
    skeleton_file_path =  '%s/%s.skeleton' % (SKELETONS_PATH, filetype)
    #print skeleton_file_path

    if not os.path.exists(skeleton_file_path):
        return
    body = replace(file(skeleton_file_path).read()) 
    lines = body.split('\n')
    cb.append(lines, 0)


