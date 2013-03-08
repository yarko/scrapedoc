.. include:: __scrape_logo.rst

.. _installation:

====================
|Shdr| Installation
====================

|iSP| requires the following:

 - a recent version of python_ 2.7
 - a recent version of Firefox_ [#browser]_

Installing |s| will install or upgrade the following python libraries:

 - argparse
 - lxml
 - cssselect
 - PyYAML
 - selenium
 - |s|'s version of envoy
 - a |s| plugin library

Installation requires you have a compiler on your machine.

For Linux systems, this should already be the case.

For Macintosh OS/X systems, downloaded Xcode
free from the `Mac App Store`_ (also install the command line tools).
Alternatively, you may be able to install just the command-line tools
(see https://github.com/kennethreitz/osx-gcc-installer - we have not tried this).

For Windows platforms, this is not a straightforward process.
See the ``MS Windows`` section at http://lxml.de/installation.html.


.. _Mac App Store: https://itunes.apple.com/us/app/xcode/id497799835



Installing |iSP|
----------------

.. sidebar:: Prerequisites:

   - python_ 2.7
   - a recent version of Firefox_

   **Recommended:**

   - virtualenv_
   - pip_


.. _python: http://python.org/download/releases/

.. _Firefox: http://www.mozilla.org/firefox

.. _pip: http://www.pip-installer.org/


I suggest you use python's  ``virtualenv``, particularly your first
time with |s|
(see  virtualenv_).

.. _virtualenv: https://pypi.python.org/pypi/virtualenv

This will ensure you have an isolated, clean python install
of |s| to start.
Once you have this working, you may consider installing this
your system's python site-libraries.


To properly use ``virtualenv``, you'll need ``pip``.
Ensure you have ``pip`` installed::

  $ which pip

If you don't have pip installed, then install it::

  $ easy_install pip

If you do have pip, be sure it's up-to-date::

  $ pip install --upgrade pip



..  $ pip install http://someplace/scrape-vesion.tar.gz


.. todo::
   Have yet to debug the scrape.gz install file (installation does not mirror setup.py).


.. You can also install scrape from the sources (currently, the preferred method)::

Now, install the current version of |s|.
Currently, you must do this from sources.
Clone a copy of |s| and run setup.py::

  $ hg clone ssh://hg@bitbucket.org/yarko/scrape
  $ cd scrape
  $ python setup.py install


.. _chrome-webdriver: https://code.google.com/p/chromedriver/

.. _Chrome: http://www.google.com/chrome

----

.. rubric:: Footnotes

.. [#browser]  Firefox is the only browser officially supported for |s|.  As an alternative,
        you may try a current version of Chrome_, but note that you will need to
        download a chrome-webdriver_.  For some combinations of versions of Chrome,
        chrome-webdriver and selenium, timeouts didn't properly work.
        For some medical journal sites with continuous stream advertising,
        Chrome would not respond (would never return when called from scrape).

