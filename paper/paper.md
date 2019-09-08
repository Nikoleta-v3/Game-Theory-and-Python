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
- name: Dr Vincent A. Knight
  ORCID: 
  affiliation: 1 affiliations:
- name: Department of Mathematics, Cardiff University, Senghennydd Rd, Cardiff CF24 4AG
  index: 1, 2
date: some date in 2019
bibliography: paper.bib
---

# Summary

Game Theory and Python is an open source, educational tutorial aimed to
introduce readers to game theory and more specifically to repeated games. The
tutorial uses the open source library called
[Axelrod-Python](https://github.com/Axelrod-Python/Axelrod) and [Jupyter
Notebooks](https://jupyter.org), making this an open source, reproducible and
interactive tutorial.

# Statement of Need

Game theory is a field of applied mathematics and an exceptional tool for
introducing students to the field. Students can start off by playing games, then
conceptualizing strategies, and before long using equations to formulate the
interactions between players.

Repeated games are a set of games that are particularly popular in educational
game theory, and, a specific game that has gain much attention in both research
(Axelrod1980) and teaching (reference) is the Prisoner's Dilemma. The advantage
of studying the Prisoner's Dilemma is that it models situations in which
self-interest clashes with collective interest, thus it provides a powerful
framework for illustrating the usage of mathematics in real life decision
making.

% TODO a good reference that the PD is heavily used in education.

# Content

The four notebooks of this tutorial focus on the iterated version of the
Prisoner's Dilemma, the Iterated Prisoner's Dilemma, the notion of strategies
and computer tournaments whilst using Axelrod-Python.

In 1980, a political scientist called Robert Axelrod decided to run a computer
tournament of the Iterated Prisoner’s Dilemma where strategies written in
computer code would repeatedly choose between self and collective interest. The
strategies would decide on their next action using the history of previous
interactions and the winner was decided on the average score. The open source
package Axelrod-Python was created in order to reproduce Axelrod's original work
but to also serve as an educational and research tool.

Following the tutorial, participants will be able to reproduce Axelrod's
tournament but also create their own unique tournaments from a selection of
strategies, exceeding 200. Furthermore, participants will be able to progress
their comprehension of the topic by producing strategies and implement them
using Python code. The new strategies then can be placed in different
tournaments in order to access their success and weakness. This progression
of the tutorial is based on constructive framework. Participants
start by following instructions given to them, followed by the participants
producing their own strategies and tournament. This will allow them to fully
the consequences of their decision making in a setting where they interact
with others.

%TODO references

# Usage

The tutorial can be used in any of the two ways; in a workshop environment or
at home.

- In a workshop environment we suggest that the instructor has familiarized
  themselves with the written parts of the tutorial beforehand. For each
  notebook it is advised that the instructor gives a mini presentation to the
  topic followed by them typing out/running the material while the participants
  follow in their own machines. The instructor should encourage the participants
  to try the exercises of each notebook alone or with other participants. Before
  moving to the next notebook the instructor should encourage a discussion
  amongst everyone regarding the results of the exercises each had
  and their interpretation.
- If the tutorial is being followed at home the written parts of each notebook
  should be read followed by running the tutorial and completing the exercises.

# Recent Uses

This tutorial was originally formulated to run a game theory workshop at [PyCon
Namibia 2017](https://na.pycon.org/pycon-namibia-2017/). It has attracted
attention of the community ever since and has been used in various others
events.

# Acknowledgements

The tutorial has been made possible due to the existence of the open source package
[Axelrod-Python](https://github.com/Axelrod-Python/Axelrod). We would like to
express our appreciation to the main contributors of the package as well as
anyone that has ever contributed to it.

# References
