.. _front-page:

.. Scrape documentation master file, created by
   sphinx-quickstart on Tue Dec  4 12:54:57 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: __scrape_logo.rst

===========================
|Shdr| - the Documentation
===========================



|SP| is a tool developed to help researchers extract
selective data from web publications.
It is particularly useful for serial web publications
which have similar structure over many issues.
You interactively develop a selection and extraction
set of commands, and run them across a series of
issues, generating output (JSON or CSV).



.. toctree::
   :hidden:

   overview
   installation
   tutorials/contents
   LICENSE


:doc:`Overview <overview>`
============================
   What's involved, required knowledge,  and the basic modes of operation.

:doc:`Installation <installation>`
===================================

   Software and browser requirements.

:doc:`Tutorials <tutorials/contents>`
=======================================

   Get started with a concrete examples.


Alternatives
============

Examples of just some of the alternatives to |s| include:

 - scrapy_
 - twill_
 - dryscrape_
 - django-dynamic-scraper_

.. _django-dynamic-scraper: http://django-dynamic-scraper.readthedocs.org

.. _dryscrape: http://dryscrape.readthedocs.org

.. _scrapy: http://doc.scrapy.org

.. _twill: http://twill.idyll.org

You can also look through the *notable tools* section on
`Wikipedia <http://www.wikipedia.org/wiki/Web_scraping>`_.

Many of these are either not interactive,
or are programmers libraries or toolkits.
|S| is an interactive script development tool
which, with a modicum of knowledge, is both powerful and simple.
|S| scripts use |s| commands, shell commands, and commands
provided by extensions.


:doc:`LICENSE`
==============

  This license applies to the program, |iS|, and its documentation.


Work in Progress
=================

This document is currently a work-in-progress.
Here are a list of known items left to do:

.. todolist::

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

