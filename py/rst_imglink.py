#!/usr/bin/env python
#coding: utf-8
#file   : vimrst.py
#author : ning
#date   : 2012-10-20 21:29:37


import vim
from vim_bridge import bridged

AD_CHARS = """  ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~  """
AD_CHARS = AD_CHARS.split()

ENC = 'utf-8'

# diagram of Body lines when a headline is detected
# trailing whitespace always removed with rstrip()
# a b c
# ------ L3, blines[i-2] -- an overline or blank line
#  head  L2, blines[i-1] -- title line, not blank, <= than underline, can be inset only if overline
# ------ L1, blines[i]   -- current line, always underline
# x y z

XDEBUG = 0


from unicodedata import east_asian_width

import urllib, urllib2
import os, sys
import re, time
from urlparse import urlparse
import cStringIO
from PIL import Image
import imghdr

save_path = '/home/ning/idning/blog_and_notes/imgs/'

def down_and_gen_link(url, filename):
    data = urllib2.urlopen(url).read()
    
    img = Image.open(cStringIO.StringIO(data))

    ext = '.' + imghdr.what(cStringIO.StringIO(data))

    if not filename:
        filename = os.path.basename(urlparse(url).path)
        filename = filename.lower().replace('[^a-z0-9]+', '_')

    if not filename.endswith(ext):
        filename = filename + ext
    if os.path.exists(save_path + filename):
        DATESTR = time.strftime( '_%Y-%m-%d', time.localtime() )
        filename = filename + DATESTR + ext

    path = save_path + filename
    f = open(path, 'w')
    f.write(data)
    f.close()

    width, height = img.size
    if width > 500 or height > 200:
        width = width/2
        height = height/2

    r = '''
.. image:: imgs/%s
    :width: %dpx
    :height: %dpx
''' % (filename, width, height) 
    return r.strip()

@bridged
def rst_insert_img_link(url, filename=''):
    url = url.replace('"', '').replace("'", '')
    lines = down_and_gen_link(url, filename)
    lines = lines.split('\n')
    (row, col) = vim.current.window.cursor

    vim.current.buffer.append(lines, row)

#format_section_title()


