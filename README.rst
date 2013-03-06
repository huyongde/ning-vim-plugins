1.vimrst
========


auto format reStructuredText section title on write::

    vimrst
    ===

will became ::

    vimrst
    ======


2.nskeleton
===========


auto sckleton

3.rst_insert_img_link
=====================

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


