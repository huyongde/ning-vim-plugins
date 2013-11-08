#!/usr/bin/env python
#coding: utf-8
#file   : vimrst.py
#author : ning
#date   : 2012-10-20 21:29:37

import vim
from vim_bridge import bridged

import re
import os, sys
PWD = os.path.dirname(os.path.realpath(__file__))


keywords = file(PWD+'/../keyword').readlines()
keywords = [k.strip() for k in keywords]
#print keywords

PATTERN = re.compile('|'.join(keywords))
CHECKPATH = '/home/ning/idning/blog_and_notes/'

def _keyword_check(body):
    Z = len(body)
    for i in xrange(Z):
        line = body[i].rstrip()
        m = re.search(PATTERN, line) 
        if m:
            sensitive = m.group(0)
            lineno = i
            print '%s in line %s' % (sensitive, lineno)  # tell us what's sensitive

        #vim.current.buffer[i] = xxxxx

@bridged
def keyword_check():
    cb = vim.current.buffer     # gets the current buffer
    if cb.name.find(CHECKPATH) >= 0:
        _keyword_check(vim.current.buffer)

