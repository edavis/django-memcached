django-memcached2
=================

django-memcached2 is a lightweight, resuable Django app that displays
statistics about your currently running memcached instances.

It is a fork of Eric Florenzano's django-memcached_ that works with the
CACHES settings introduced in Django 1.3.

.. _django-memcached: https://github.com/ericflo/django-memcached

Installing django-memcached2
----------------------------

1. Either download the tarball and run ``python setup.py install``, or simply
   use easy_install or pip like so ``easy_install django-memcached2``.


2. Add django_memcached to your ``INSTALLED_APPS`` setting::

       INSTALLED_APPS = (
           # ...
           'django_memcached',
       )


3. Add the urls to your url configuration::

       urlpatterns = patterns('',
           # ...
           (r'^cache/', include('django_memcached.urls')),
       )


4. If you want to restrict these urls to only staff members, just add this
   setting to your settings file::
   
       DJANGO_MEMCACHED_REQUIRE_STAFF = True


That's it.  Hopefully this app gives you a little insight into how your
memcached servers are being utilized.
