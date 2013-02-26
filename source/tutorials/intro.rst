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


We'll start by making sure you have |s| installed.

Activate_ the virtual environment you have installed |s|.


.. _Activate: https://pypi.python.org/pypi/virtualenv


Now run ``scrape``::

  $ scrape http://scrape.readthedocs.org

This should start |s| and open its documentation.

 - your Firefox should have "WebDriver" displayed in the lower-right;

   - this indicates that this Firefox can be controlled from |s|.

 - you should see a log of the plugins registered (scrape comes distributed with one - ``affiliations``);

   - if you don't see ``scrape: INFO - ...registering plugins:`` in your |s| shell, then likely something is incomplete in your installation.  You can continue with the exercises, but you will need to install plugins when you need them.

At the ``[S]crape >>>`` prompt type the following:;

  [S]crape >>> help

|SP| gives you access to an HTML file or web page.
It does this by parsing your web page
into a *tree* of HTML *nodes*.
You then traverse the tree of nodes,
scraping the information you want from a selected node.

|S| starts by setting the active node to the ``<body>`` of your HTML page[#]_.

Let's show the contents of the current node::

  [S]crape >>> show node 

You should see the source for the ``<body>`` of the |s| document page.

The general starategy for using |s| is:

  - select a scrape target (a web page);
  - declare a tablename (someplace to collect output);
  - declare a variable to collect information;
  - navigate the web page's tree;
  - capture the desired information;
  - repeat as desired;
  - save a table (a set of variables) to a file;

To develop a script, we save select commands.

Let's save the headers to develop an outline for this page.

First, declare a table name and a variable to collect output.
Setting ``var my_name`` will select a variable to collect data
(a data catcher).
The variable does not need to exist (it will be created). ::

  [S]crape >>> table outline
  [S]crape >>> var topics

Our table is called ``outline``.
Should you decide to save the output, it will be saved in a file ``outline.csv``.
So far, this table has one column - one variable - called ``topics``.

|S| starts by providing a simplified interface to the libxml2 library,
so that most of the information you will find about ``xpath`` selectors
and ``cssselectors`` will work as you expect in |s|.
Additionally, scrape combines and extends these tools
for interactive use.
For example, ``find_by_text`` will search
nodes selected by an xpath expression for a string.

You may want to
open http://www.w3schools.com/xpath/xpath_syntax.asp in another browser
window for reference.

Let's find the subheadings on our target page, and see if this
will satisfy our needs for a page outline::

  [S]crape >>> findall .//h2
  [S]crape >>> show node

This should find all the ``<H2>`` nodes under the current node.
More than one node is found.
``Show`` displays all of them.
|S| variables are lists of values.

The text of these nodes seems like it would serve nicely as an outline, so lets capture those.
To see what the various variables of a table currently have, we ``show out``,
which shows the current table's contents.
The form of the display is *YAML*.
Varible names are shown with a colon (``my_var:``),
and their values are shown as a list of items, each preceded by a '-'.

The ``text`` command of |s| will collect the text contents of the currently
selected ``HTML`` nodes;  the current variable will catch them.
::

  [S]crape >>> show out
  [S]crape >>> text
  [S]crape >>> show out


There was no output pending prior to the ``text`` command.
After, ``header`` contains a list of four strings.
If you wanted to save this now, the ``table`` command (without a name)
will output the current table name to a ``csv`` table (if one already exsits,
it will not be overridden; the name will have a number added to it).

If you wanted to continue to develop your script later, look
at your history.
Only scrape commands which act on pages are saved to history.
You can choose which parts of history you save.
::

  [S]crape >>> history
  [S]crape >>> help save

If you'd like, you can save your script now.
To exit |s|, see ``help EOF``.

Now it's time to pick a tutorial track from the menu on the right.

Have fun |is| ing!


----

.. [#]  You can also start at the root of the document - see ``help doc`` and ``help body``.

.. [#] Be sure you've installed |s| and a current Firefox browser.
