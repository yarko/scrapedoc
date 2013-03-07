.. _pycon:

.. include:: ../__scrape_logo.rst 


=====================
Developing a Project
=====================

This is the second tutorial in a series.

From the introductory tutorial, we saw how
to select a destination (file or URL).
Initially, it's also beneficial to 
view the destination's source along with the
browser window.
You can either search for what interests you
in the source window, or use ``inspect element`` to
get to the item that interests you.

Once you've quickly found the item
of interest, you can start trying various
tree traversal commands to get to related items
in |s|, view the nodes found, and save some part of
their content in |s| variables for output.
You can also save your script activity into a script,
which you can edit and run later in scrape.

In this tutorial we'll see how to backtrack and make
corrections.
We'll also see how the various scrape commands behave when
applied to multiple nodes.

.. Note:: *A word about* |s| ing *public sites*

   Good citizenship is in order:

   - avoid repeatedly hitting a site, and loading its servers;
   - always check for copyright, and observe fair use doctrines.


PyCon Volunteer Reporting
==========================

Here's our project:  the US PyCon 2013 Conference is coming up.
PyCon is a community conference and depends heavily on voluneers.
We want to track how many volunteers we still need for session staff [#sessstaff]_.

The conference site lists the sessions and staff on http://us.pycon.org/2013/schedule/sessions.
Since this will likely change dynamically, we'll use a snapshot version we saved,
just as you would when first developing a script (in order to spare repeatedly hitting a site's servers).
Having a static copy will also make it easier to follow along with the tutorial:

  - download :download:`tutorial2.zip </_static/tutorial2.zip>`.


Getting oriented with the source
---------------------------------

Let's review what we've learned so far.
|S| commands are divided into commands which
navigate the source tree, and commands which
capture content into variables.
There are also commands to manipulate |s| variables,
and to save collected content.
There are also commands to inspect command history,
and save commands as scripts, so you may later
develop or run them.


Finding objects of interest
----------------------------

A starting strategy
--------------------

Adjusting course
-----------------


Saving output
--------------


Running another day
--------------------



.. |JAMA| replace:: *The Journal of the American Medical Association*

.. |jama| replace:: *JAMA*

.. _Activate: https://pypi.python.org/pypi/virtualenv


----

.. rubric:: Footnotes

.. [#sessstaff]  Session staff consist of chairs and runners.
        Chairs introduce speakers, manage questions and keep
        track of time.
        Runners get speakers to their talk on time and
        ensure they have everything they need.
        A typical session consists of 3 talks.
        Sessions run simultaneously in multiple rooms.

