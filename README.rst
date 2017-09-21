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

Features
--------

If you want to build an extensible platform, you may find the need to allow the developers that use your app to alter
or add on to the functionality that you provide.  This django package attempts to add 'plugin' functionality to
your django app.

How it works:

End-Users of your app create a 'plugin', which is just a Python Class which inherits from django-n3-template's
TemplatePlugin.  This class requires two methods to be created:

.get_context_data():  Which is how their plugin adds extra data to your Views/Templates

.render_html(): Which uses their context (and any provided by your view) to return HTML code (Full Django Template
syntax is allowed here!)

You then use the provided decorator @load_plugins to decorate your views like this:
.. code-block:: python

    # views.py
    @load_plugins
    class SomeView(DetailView):
        ...

This decorator will set a class property called self.plugins which is a dictionary.  You then use this at any point
in your code and make sure it gets into your template context.


In your template you use django-n3-templateplugins provided templatetag to render the plugin's html, which looks
something like this:

.. code-block:: python

    # some_template.html
    {% load render_plugin %}
    {% for k, v in plugins.items %}
        {% render_plugin v.plugin_pbject %}
    {% endfor %}

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
