.. include:: __scrape_logo.rst

.. _overview:

================
|Shdr| Overview
================


Context
-------


|iSP| operates within the following environment:


.. graphviz::
   :alt: [S]crape Context

   digraph g {
     graph [nodesep=0.7, margin="0.6,0.15"];
     edge [dir=both];
     node [fontname="verdana", shape=box, fillcolor=snow, style="rounded,filled"];

     subgraph {
       rank = same; "[S]crape"; scripts; plugins;
       "[S]crape" [fontname="Chalkduster"];
     }
     browser -> "[S]crape";
     shell -> "[S]crape";

     scripts -> "[S]crape";

     edge [dir=forward];
     plugins -> "[S]crape";
     "[S]crape" -> output;

   }

Modes of Operation
-------------------

You operate |s| in one of two ways:

 - interactively;
 - batch;

|SP| starts and controls a browser [#]_, and gets
it's data from that browser.

You can interactively highlight sections
in the browser and scrape will give you
unambiguous code to select that data.
As with a *Google* search,
skill will help make the search term (xpath or css selector)
more general, yet sepecific enough to return your desired result.

Inspect results as you work
interactively until you 
are satisfied and then save a range
of commands from your history
to develop your script.

At anytime you can load and run
scripts.  Thus you build up a complete
script incrementally.  In batch mode, you can automatically
run it over a pattern or list of targets.

Knowledge You Should Have
-------------------------

You should have a general understanding of *HTML* and *CSS* structure
and form.  You don't need to know much, but you should
be able to understand and recognize what you are looking at
when looking at small portions of web page source, and have
an understandging of what type of thing you are trying to extract,
i.e. path, attribute, or text.

You will need some basic understanding of XPATH_ syntax and `CSS Selectors`_
as you will be using these to descrivbe what you are looking for.
When manually highliting something in your browser,
|s| will return an *XPATH*.  Often  a *CSS selector* is both shorter
and more accurately selective.   |S| allows you to view context near
your selection.  This makes it easy to pick a different form of selector
and test it before saving it to your script.


.. _XPATH: http://www.w3schools.com/xpath/xpath_syntax.asp

.. _CSS Selectors: http://www.w3schools.com/cssref/css_selectors.asp


|iSP| Shell
------------

In interactive use, |s| is similar to a typical command shell,
such as ``sh`` or ``bash``, or ``cmd`` on Windows.
In command interpreters, there are typically builtin commands
and a way to execute external commands.
Shells also provide variables, and some sort of program control.

|SP| has a rich set of builtin commands, and allows callig
external commands through your system's shell.
You can also add builtin commands
by writing extensions in Python.

Since |s| outputs tables [#tables]_, variable names are table column
names.
This means every variable is |s| a list (you can think of them as arrays).
There are other important kinds of variables in |s|.

:output: Output variables are the normal variables, and are used to
         specify output table column names.

:local:  Local variables are similar to output variables, only they are omitted from tables.
         These are used for intermediate results.  Local variables
         have scope per output table.

:global: These variables persist accross output table
         changes.



|SP| is least like shells in that there is no familiar loop control.
For traversing an *HTML* tree and extracting data
this simplifies use.
Instead of looping, you set starting locations in the XPATH tree of the input.
We call these XPATH locations *nodes*.
Typical |s| operation involves traversing a document's HTML tree,
extracting some content from a node,
then continuing from the current location, or setting a new node as a starting point
and extracting more.
In place of program control, you control which nodes you search from.
Some general control mechanisms |s| provides are:

:root:  Normally, navigation through the document is incremental.
       This resets the current node to the start of the ``<html>`` tag.

:body: This resets the current node to the start of the ``<body>`` tag.

:grab: |S| opens a browser when it starts, and communicates with it.
       ``grab`` gets a highlited region from the page currently displayed
       in your browser, and shows some context to help you write an XPATH
       phrase to select this location, or similarly located nodes.

A majority of |s| commands involve selecting a node
using an xpath selector, a css-selector, or a combination of path and text search.
The remaining commands deal with interactive use (history, view variables, run
scripts, save or load scripts), and outputing results (tables).


Installing |iSP|
----------------

Now that you have a good overview, let's show how to develop and
run a useful |s| script.

First, be sure you have python_ 2.7 installed for your platform.
Also, be sure you have installed a recent version of Firefox_ [#browsers]_.

.. _python: http://python.org/download/releases/2.7.3/

.. _Firefox: http://www.mozilla.org/firefox

Next, ensure you have ``pip`` installed::

  $ which pip

If you don't have pip installed, then install it::

  $ easy_install pip

If you do have pip, be sure it's up-to-date::

  $ pip install -U pip


Now, install the current version of |s|::

  $ pip install ./downloads/scrape.gz

(use the path where you've saved `scrape.gz <./scrape.gz>`_).
Alternately, you can install directly from this website::

  $ pip install http://this_current_scrape_URL/scrape.gz


.. todo::
   Have yet to create the scrape.gz install file.


-----

.. [#] |S| uses a Selenium_ Client Driver to run your browser.
       At this time |s| only supports Firefox.

.. _Selenium: http://seleniumhg.org

.. [#tables] |S| was initially designed to output CSV, but this is a bit too restricting.
             For one thing, to change the view of the data (the order of way the
             data is populated into columns, the number and contents of tables)
             one would need to re-scrape the source.
             A better choice would have been saving variables in an intermediate form, such
             as JSON.
             Then, you could rebuild, re-shape your tables from your stored data source.
             This may be a worthy modification for a future version.

.. [#browsers] Firefox is the only browser officially supported for |s|.  As an alternative,
               you may try a current version of Chrome_, but note that you will need to
               download a chrome-webdriver_.  For some combinations of versions of Chrome,
               chrome-webdriver and selenium, timeouts didn't properly work.
               For some medical journal sites with continuous stream advertising, Chrome would not
               respond (would never return when called from scrape).


.. _chrome-webdriver: https://code.google.com/p/chromedriver/

.. _Chrome: http://www.google.com/chrome

