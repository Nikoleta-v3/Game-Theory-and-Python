# Game-Theory-and-Python

This is a repository created to run a workshop on Game Theory using
the programming language [Python](https://www.python.org/) and more specifically
an open source software called the [Axelrod Python library](https://github.com/Axelrod-Python/Axelrod).

The topics that this workshop cover are the following:

1. An introduction to Game theory and the iterated prisoner's dilemma (IPD)
2. Creating matches and tournaments using the Axelrod library
3. Writing strategies and contributing to the Axelrod library
4. Playing against strategies of the IPD

# Installing Python

There are various distributions of Python. I recommend using [Anaconda](www.continuum.io/downloads)
which comes packaged with a variety of tools, such as Jupyter Notebooks.

This tutorial is written in [Jupyter Notebooks](http://jupyter.org/).

# Virtual Environment

This repository comes with an `environment.yml` file. The `environment.yml` file
will allow you to create an Anaconda environment. To do that use the terminal or
an anaconda prompt and after you have navigated to the repository just type:

```
$ conda env create -f environment.yml
```

The environment can be activated by typing:

```
$ conda activate game-python
```

and notebooks can also run in it. To do that you will have to select (from within
a running notebook) `Kernel` and under `Change Kernel` select the environment
`game-python`.

# Contributions

All contributions are welcome! This may include communicating ideas for new sections,
letting us know about bugs, and code contributions.
