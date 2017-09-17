=====
Usage
=====

To use django-n3-templateplugins in a project, add it to your `INSTALLED_APPS`:

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
