========
Includer
========

.. image:: https://api.travis-ci.org/zzzsochi/includer.svg
  :target:  https://secure.travis-ci.org/zzzsochi/includer
  :align: center

.. image:: https://coveralls.io/repos/zzzsochi/includer/badge.svg
  :target:  https://coveralls.io/r/zzzsochi/includer
  :align: center

-----
Usage
-----

`some_module.py`:

.. code:: python

    def some_func(arg='World'):
        print('Hello {}'.format(arg))


`some_else_module.py`:

.. code:: python

    from includer import include

    include('some_module.some_func', arg='ZZZ')

-------------
IncluderMixin
-------------

Mix `include` method for objects.
Behavior like as `Configurator.include <http://docs.pylonsproject.org/projects/pyramid/en/1.5-branch/api/config.html#pyramid.config.Configurator.include>`_. See tests for understood it.

This is very usefull for imperative application configuration.

-----
Tests
-----

.. code:: shell

    $ pip install pytest
    $ py.test tests -v
