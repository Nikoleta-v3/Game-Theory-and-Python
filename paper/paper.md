---
title: "Game Theory and Python: An educational tutorial to game theory and
repeated games using Python"
tags:
- game theory
- repeated games
- prisoner's dilemma
- axelrod python
authors:
- name: Nikoleta E. Glynatsi
  ORCID: 
  affiliation: 1 affiliations:
- name: Department of Mathematics, Cardiff University, Senghennydd Rd, Cardiff CF24 4AG
  index: 1 
date: some date in 2019
bibliography: paper.bib
---

# Summary

Game Theory and Python is an open source, educational tutorial aimed to
introduce readers to game theory and more specifically to repeated games. The
tutorial uses the open source library called [Axelrod-Python](https://github.com/Axelrod-Python/Axelrod)
integrated with Jupyter Notebooks, making this an open source, reproducible and
interactive tutorial.

# Statement of Need

Game theory is a field of applied mathematics and an essential tool for
understanding the outcome of situations where agents with different behaviours
interact. A real life example of such situation is people choosing between being
selfish or selfless when they interact with others.

In 1950, this very interaction was formulated in a two players game known as the
prisoner's dilemma (PD). The repeated form of the game is called the iterated
prisoner's dilemma (IPD) and in 1980 it attracted the attention of the scientific
community. A political scientist called R. Axelrod decided to run a computer tournament
of the IPD where strategies (written in computer code) would repeatedly choose between
selfish and selfless actions. The strategies would decide on their next action using
the history of the previous interactions. Axelrod's tournament was a success.
His work spawn to life a new research field which in 2018 achieved more than 150
publications.
An open source packaged the Axelrod-Python was created in order to reproduce
Axelrod's original work as well as other ongoing research work on the topic. Axelrod-Python
is an exceptional open source package which follows best practices and has created
a large active community.

This tutorial serves as an introduction to the IPD and the notion of strategies
whilst using Axelrod-Python. Following the tutorial, readers will be able to
reproduce  Axelrod's original tournaments but also create their own unique
tournaments from a selection of strategies, exceeding 200. Furthermore, readers
can compose their own ideas of strategies and implement them using Python code.
The new strategies then can be placed in different tournaments in order to
access their success and weakness.

The overall aim of the tutorial is not only to introduce readers to a unique and
essential field of applied mathematics. It is also to allow them to construct
their very own ideas using their Python skills and participate in a
tournament such as that run by Axelrod back in the 1980. The PD, and
subsequently this tutorial, allows readers to try and tackle a frequently
asked question since Darwin's time; how can you be the dominant
player in world where you interact with others?

# Recent Uses

This tutorial was originally formulated to run a game theory workshop at
[PyCon Namibia 2017](https://na.pycon.org/pycon-namibia-2017/).
It has attracted attention of the community ever since and has been used to various
others events.

# Acknowledgements

The tutorial has been made possible due the existence of the open source package
[Axelrod-Python](https://github.com/Axelrod-Python/Axelrod).
I would like to express my appreciation to the main contributors of
the package as well as anyone that has ever contributed to it.
I would also like to thank my PhD advisor, Dr Vincent Knight, for double checking
the material and for running the workshop with me.

# References
