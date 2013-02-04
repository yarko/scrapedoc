.. scrape_logo.rst - a utility file

.. use |shdr| for top-level header
   scrape_logo2.png is 619 × 156 pixels
   40% 156 = 62px
   20% 156 = 31px
   15% 156 = 23px
   To get a proportional image, we scale height in abs,
   and let the width be 100%;


.. NOTE: with the "only::" directive, epub has html
   builder as true (nothing for epub or ebook, etc. )
   so if you want separate, you need to:
   - add a tag to the build command in the makefile;
   - specify html and not <the tag>
   e.g.:
   sphinx-build -t epub ...
   then:  .. only:: html and not epub

.. showstopper:  can't have aliases in
   only blocks! (it doesn't work);
   ...not even in includes...

.. |Shdr| image:: /_static/scrape_logo2.png
   :height: 58px
   :alt: [S]crape
   :align: top


.. use |sp| at the start of a paragraph

.. |iSP| image:: /_static/scrape_logo2.png
   :height: 28px
   :alt: [S]crape
   :align: top

.. for text versions of this, see
   http://docutils.sourceforge.net/docs/ref/rst/roles.html#subscript

.. |SP| replace:: [S]\ :sup:`crape`

.. eventually, lookup the way to specify the target
   font for latex (Apple's  Chalkduster)

.. |iS| image:: /_static/scrape_logo2.png
   :height: 20px
   :alt: [S]crape
   :align: top

.. |S| replace:: [S]\ :sup:`crape`

.. use |s| within text

.. |is| image:: /_static/scrape_logo2.png
   :height: 20px
   :alt: [S]crape
   :align: top

.. |s| replace:: [S]\ :sup:`crape`

