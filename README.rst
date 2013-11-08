1.rst_format_title
==================


auto format reStructuredText section title when you save::

    vimrst
    ===

will change to ::

    vimrst
    ======


2.rst_imglink
=============

::

    RstInsertImg http://datavlab.org/wp-content/uploads/2011/12/map.jpg 

will generate a image with a auto-generated filename::

    .. image:: imgs/map.jpg.jpeg
        :width: 350px
        :height: 210px

::

    RstInsertImg http://datavlab.org/wp-content/uploads/2011/12/map.jpg my-map
 
will generate::

    .. image:: imgs/my-map.jpeg
        :width: 350px
        :height: 210px


3.nskeleton
===========

auto skeleton

put files in ~/.vim/skeletons/::

    $ tree skeletons/
    skeletons/
    |-- cpp.skeleton
    |-- c.skeleton
    |-- h.skeleton
    |-- mkd.skeleton
    |-- php.skeleton
    |-- processing.skeleton
    |-- python.skeleton
    |-- README_tskeleton.txt
    |-- rst.skeleton
    `-- sh.skeleton

    $ cat rst.skeleton 
    <+FILE_NAME_BASE+>
    #################################

    :slug: <+FILE_NAME_BASE+>
    :date: <+DATE+>
    :author: ning
    :Last modified: 2013-03-06 14:20:04

    .. contents:: Table of Contents

auto modify lastmodify on save::

    :Last modified: 2013-11-08 15:53:08

4.keyword_check
===============

check keyword before saving


