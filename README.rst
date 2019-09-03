Game-Theory-and-Python
----------------------

.. image:: https://travis-ci.org/Nikoleta-v3/Game-Theory-and-Python.svg?branch=master
    :target: https://travis-ci.org/Nikoleta-v3/Game-Theory-and-Python
.. image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square
    :target: http://makeapullrequest.com

This is a repository created to run a workshop on Game Theory using
the programming language `Python <https://www.python.org/>`_ and more specifically
an open source software called the `Axelrod Python library <https://github.com/Axelrod-Python/Axelrod>`_.

The topics being covered in this workshop are the following:

1. `An introduction to Game theory and the iterated prisoner's dilemma <https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/1.%20Introduction.ipynb>`_
2. `Creating matches and tournaments using the Axelrod library <https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/2.%20Matches%20and%20Tournaments.ipynb>`_
3. `Writing strategies and contributing to the Axelrod library <https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/3.%20Writing%20a%20Strategy.ipynb>`_
4. `Playing against strategies of the iterated prisoner's dilemma <https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/4.%20Human%20Strategy.ipynb>`_

Installing Python
-----------------

There are various distributions of Python. I recommend using `Anaconda <www.continuum.io/downloads>`_
which comes packaged with a variety of tools, such as Jupyter Notebooks.

This tutorial is written in `Jupyter Notebooks <http://jupyter.org/>`_.

Virtual Environment
-------------------

This repository comes with an `environment.yml` file. The `environment.yml` file
will allow you to create an Anaconda environment. To do that use the terminal or
an anaconda prompt and after you have navigated to the repository just type::

$ conda env create -f environment.yml


The environment can be activated by typing::

$ conda activate game-python


and notebooks can also run in it. To do that you will have to select (from within
a running notebook) `Kernel` and under `Change Kernel` select the environment
`game-python`.

Contributions
-------------

All contributions are welcome! This may include communicating ideas for new sections,
letting us know about bugs, and code contributions.

Events
------

This tutorial has been used in the following events:

- `PyCon Namibia 2017 <https://na.pycon.org/pycon-namibia-2017/>`_

Have you used this tutorial in an event you hosted or participated? Please do let
me know by either contacting `me <https://nikoleta-v3.github.io/>`_ or feel free to
open a `pr` adding your event to this list.

License
-------

The code in this repository, including all code samples in the notebooks listed above,
is released under the `MIT license <https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/LICENSE.txt>`_.