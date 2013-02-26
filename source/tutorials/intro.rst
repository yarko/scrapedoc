.. _tutorial:

.. include:: ../__scrape_logo.rst 

================
Tutorial
================

.. toctree::
   :maxdepth: 2
   :hidden:


Getting Started
================

.. |JAMA| replace:: *The Journal of the American Medical Association*

.. |jama| replace:: *JAMA*

.. _Activate: https://pypi.python.org/pypi/virtualenv


We'll start by making sure you have |s| installed.

Activate_ the virtual environment where you have installed |s|,
and run ``scrape``::

  $ scrape http://scrape.readthedocs.org

This should start |s| and open its documentation in Firefox.

 - your Firefox should have "WebDriver" displayed in the lower-right;

   - this indicates that this Firefox is being controlled from |s|.

 - you should see a log of the plugins registered (scrape comes distributed with one - ``affiliations``);

   - if you don't see ``scrape: INFO - ...registering plugins:`` in your |s| shell, then likely something is incomplete in your installation.  You can continue with the exercises, but you will need to install plugins when you need them.

At the ``[S]crape >>>`` prompt type the following::

  [S]crape >>> help

|SP| gives you access to an HTML file or web page.
It does this by parsing your web page
into a *tree* of HTML *nodes*.
You then traverse the tree of nodes,
scraping the information you want from a selected node.

|S| starts by setting the active node to the ``<body>`` of your HTML page [#]_.

Let's show the contents of the current node::

  [S]crape >>> show node 

You should see the source for the ``<body>`` of the |s| document page.

The general starategy for using |s| is:

  - select a scrape target (a web page);
  - declare a table name (someplace to collect output);
  - declare a variable to collect information;
  - navigate the web page's tree;
  - capture the desired information;
  - repeat as desired;
  - save a table (a set of variables) to a file;
  - lastly, save your interactive commands to a script to run later.

Let's save the headers to develop an outline for this page.

First, declare a table name and a variable to collect output.
Setting ``var my_name`` will select a variable to collect data.
The variable does not need to exist (it will be created).
The same holds for a table.
If you change tables before you've saved their output,
they are stored so you can later add to their variables (and output).
::

  [S]crape >>> table outline
  [S]crape >>> var topics

When you save the output from this table, it will be saved in a file ``outline.csv``.
Once you save a table, its values are emptied.
So far, this table has one column - one variable.

One thing |s| does is provide a simplified interface to the libxml2 library,
so that most of the information you will find about ``xpath`` selectors
and ``cssselectors`` will work as you expect.
|S| also combines, extends and adds to these tools
for interactive use.
For example, ``find_by_text`` will search
nodes selected by an xpath expression for a string.

You might like to
open http://www.w3schools.com/xpath/xpath_syntax.asp in another browser
window for reference during this tutorial.

Let's find the subheadings on our target page to see if this
will satisfy our needs for a page outline::

  [S]crape >>> findall .//h2
  [S]crape >>> show node

This should find all the ``<H2>`` nodes under the current node.
More than one node is found - ``show`` displays all of them.

The text of these nodes seems like it would serve nicely as an outline, so lets capture those.
To see what the various variables of a table currently have,
we issue the ``show out`` command
to show pending output (the current table's contents).
|S| variables are lists of values.
Varible names are shown with a colon (``my_var:``),
and their values are shown preceded by a '-'.

The ``text`` command will collect text contents of the currently
selected ``HTML`` nodes into the current variable.
::

  [S]crape >>> show out
  [S]crape >>> text
  [S]crape >>> show out


There was no output pending prior to the ``text`` command.
If you wanted to save this now, the ``table`` command (with no argument)
will output the current table to a ``csv`` file with the same name
(if one already exsits, it will not be overwritten;
the name will be numerically extended).

If you want to save your script for later, look
at your history.
Only scrape commands which act on pages are saved in history.
You can choose which parts of history you save to a script file.
::

  [S]crape >>> history
  [S]crape >>> help save

If you'd like, save your script now.
You can edit saved |s| scripts with a text editor.
You can add comments, which begin with '#' and extend to the end of the line.

There is an alternate form for selecting tables and variables,
which may help the commands in your script (and what they apply to)
stand out.   If you'd like, in place of::

   table outline
   var topics

you can equivalently write::

    [ outline ]
    < topics >

To exit |s|, see ``help EOF``.

After our brief interactive session with |s|, here's what our script looks like::

   ##
   # [S]crape script to get outline of a page
   #
   # - gets the text of <h2> headings;
   #
   [ outline ]
   < topics >
   findall .//h2
   text
   table   # save outline.csv


That's all there is to it!

Please consider continuing to a more detailed tutorial.

Happy |is| ing!


----

.. [#]  You can easily point to the root of the document at any time - see
       ``help doc`` and ``help body``.

.. [#] Be sure you've installed |s| and a current Firefox browser.
