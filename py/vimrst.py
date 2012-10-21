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

def cjk_width(text):
    return len(text.decode(ENC,'replace').encode("GBK"))

def cjk_width(text):
    width = 0
    if not isinstance(text, unicode):
        text = text.decode(ENC)
    for char in text:
        if east_asian_width(char) in  ['Na', 'H']:
            width += 1
        else:
            width += 2
    return width
 

def _formatit(body):
    L1, L2, L3 = '','',''

    Z = len(body)
    for i in xrange(Z):
        L2, L3 = L1, L2
        L1 = body[i].rstrip()
        if XDEBUG:
            print L1
        # current line must be underline and title line cannot be blank
        if not (L1 and L2 and (L1[0] in AD_CHARS) and L1.lstrip(L1[0])==''):
            continue
        # underline must be as long as headline text
        if len(L1) < 2:
            continue
        # there is no overline; L3 must be blank line; L2 must be not inset
        if not L3 and len(L2)==len(L2.lstrip()):
            #if len(L1) < len(L2.decode(ENC,'replace')): continue
            gotHead = True
            ad = L1[0]
            if XDEBUG:
                print L2, len(L2), cjk_width(L2)
            vim.current.buffer[i] = ad * cjk_width(L2)
            #vim.current.buffer[i] = 'xxxxx'
            head = L2.strip()
        # there is overline -- bnode is lnum of overline!
        elif L3==L1:
            #if len(L1) < len(L2.decode(ENC,'replace')): continue
            gotHead = True
            ad = L1[0]*2
            head = L2.strip()

@bridged
def format_section_title():
    _formatit(vim.current.buffer)

#format_section_title()


