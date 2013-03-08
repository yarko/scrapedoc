.. _tutorials:

.. include:: ../__scrape_logo.rst


==================
Tutorials
==================


Select the tutorials which are appropriate for what you want to do.

To start, I recommend you follow the installation checkout and tutorial on this page,
followed by the example PyCon project.
These brief tutorials will introduce the concepts and strategies
for using scrape, as well as give an overview of some of the most useful commands.

.. graphviz::
   :alt: [S]crape tutorials

   digraph g{
     graph [nodesep="0.7", margin="0.6,0.15"];
     node [fontname="verdana", shape=box, fillcolor=snow, style="rounded,filled"];

     "Getting Started" -> "First Project"
   }


.. toctree::
   :maxdepth: 2
   :hidden:

   intro
   pycon



:doc:`Introduction to [S]crape <intro>`
----------------------------------------

   The :doc:`"Getting Started" Tutorial <intro>`
   will help you confirm your installation, and
   introduce the basic |is| concepts.


:doc:`Developing a Project <pycon>`
-------------------------------------

   In this :doc:`Intermediate Tutorial <pycon>`,
   we'll look at using |is| to report on volunteers
   signed up for running talks at a national conference.
   In the process, will look at the different groups
   of commands in |is| and introduce some
   useful patterns for developing scripts.

