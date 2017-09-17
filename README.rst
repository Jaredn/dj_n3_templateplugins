=============================
django-n3-templateplugins
=============================

.. image:: https://badge.fury.io/py/dj-n3-templateplugins.svg
    :target: https://badge.fury.io/py/dj-n3-templateplugins

.. image:: https://travis-ci.org/Jaredn/dj-n3-templateplugins.svg?branch=master
    :target: https://travis-ci.org/Jaredn/dj-n3-templateplugins

.. image:: https://codecov.io/gh/Jaredn/dj-n3-templateplugins/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/Jaredn/dj-n3-templateplugins

Extensible Template Plugins for Django

Documentation
-------------

The full documentation is at https://dj-n3-templateplugins.readthedocs.io.

Quickstart
----------

Install django-n3-templateplugins::

    pip install dj-n3-templateplugins

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'dj_n3_templateplugins.apps.DjN3TemplatepluginsConfig',
        ...
    )

Add django-n3-templateplugins's URL patterns:

.. code-block:: python

    from dj_n3_templateplugins import urls as dj_n3_templateplugins_urls


    urlpatterns = [
        ...
        url(r'^', include(dj_n3_templateplugins_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
