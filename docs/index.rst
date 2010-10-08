Performance Tools
=================

This app is a collection of tools that can improve the performance of GLAM-style websites. 

.. rubric:: This is part of the GLAMkit Project. For more information, please visit http://glamkit.org.


At the moment it contains one utility - the `mediahash` templatetag.

Planned future inclusions:

* CSS and Javascript optimisation tools (for now, we recommend `django-farstyle <http://code.google.com/p/django-farstyle/>`_.)
* Cache monitoring tools

The Mediahash template tag
--------------------------

Philosophy
^^^^^^^^^^

Mediahash deals with a common performance bottleneck found in media-rich websites. Most browsers have a numerical limit to the number of connections they will allow with any one hostname - commonly 2, 4 or 6 connections. This results in a staggered download of the page's contents. Consider a common scenario found on GLAM websites: a page listing collection items - each with a small thumbnail. Since each thumbnail requires its own http connection to download, the thumbnails cannot all download simultaneously. This connection limiting is a holdover from the early pre-broadband days of the web where connections could easily get saturated. It seldom applies today.

A common solution is to spread your media files across several hostnames. If you've ever looked at the source code for a page of thumbnails served from Google or Flickr or some other major website that invests serious time and money into optimising site speed, you will have noticed that the images are served from a cluster of hostnames (eg. t0.gstatic.com, t1.gstatic.com, t2.gstatic.com and so on). This effectively overrides the browser's multiple connection limit and allows for a lot more simultaneous connections. Taking this approach will have a different effect depending on the nature of your website, but overall speed boosts in the order of 20-40% are not uncommon. The impact is tangible - not just tweaking at the edge of performance!

Of course, each separate hostname requires a DNS lookup which adds a delay into the equation (commonly around 500ms). Using too many hostnames will require too many lookups, and you'll lose the advantage of parallel media delivery. It's a matter of finding the sweet spot between maximum parallelisation and minimum DNS lookups. Fortunately mediahash makes it very easy to test and tweak your settings without having to laboriously re-allocate media files to different hosts. See configuration 

.. seealso::

    `Google page speed <http://code.google.com/speed/page-speed/docs/rtt.html#ParallelizeDownloads>`_
    `Optimizing Page Load Time <http://www.die.net/musings/page_load_time/>`_


What does it do?
^^^^^^^^^^^^^^^^
Mediahash is a simple templatetag that takes one string argument - the media file's path (relative to settings.MEDIA_ROOT), like so::

    {% mediahash 'images/collection/paintings/mona_lisa.jpg' %}
    
Mediahash will take the filepath string and run it through an md5 hash 


Installation
^^^^^^^^^^^^
Mediahash requires that you serve your media files from a separate subdomain. For example:



Configuration
-------------

Generally we find that sites in the GLAM sector benefit from a figure of ``3`` or ``4``.

