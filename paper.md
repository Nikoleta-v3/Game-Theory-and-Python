---
title: "Game Theory and Python: An educational tutorial to game theory and repeated games using Python"
tags:
  - game theory
  - repeated games
  - prisoner's dilemma
  - axelrod python
authors:
  - name: Nikoleta E. Glynatsi
    orcid: 0000-0002-2943-3622
    affiliation: 1
  - name: Vincent A. Knight
    orcid: 0000-0002-4245-0638
    affiliation: 1
affiliations:
  - name: Department of Mathematics, Cardiff University, Senghennydd Rd, Cardiff CF24 4AG
    index: 1
date: 5 December 2019
bibliography: paper.bib
---

# Summary

These materials are an open source educational tutorial aimed at introducing
participants to game theory and more specifically to repeated games. The
tutorial uses the open source library called
`Axelrod-Python` and [Jupyter
Notebooks](https://jupyter.org) making this an open source, reproducible and
interactive tutorial.

# Statement of Need

We are mathematicians and Python programmers with interests in game theory and
pedagogy. This tutorial was created as a resource for computer workshops and for
introducing mathematicians to programming. As a result, this tutorial is aimed
at two groups of individuals:

- those familiar with Python (programmers) who want to start to learn game theory,
- mathematicians with little or no programming knowledge as a pathway to programming through the interesting
subject that is game theory

Game theory is a field of applied mathematics interested in strategic
interactions. Game theory itself has a number of sub fields and the one
considered in this tutorial is the area of repeated games. Repeated games have
been the subject of research [@Axelrod1981] but have also been used extensively
as an entry to the subject for students at undergraduate level courses
[@Brokaw2004], [@Knight2015]. This tutorial focuses on the Iterated Prisoner's
Dilemma. The advantage of studying the Iterated Prisoner's Dilemma is that it
models situations in which self-interest clashes with collective interest, thus
it provides a framework for illustrating the usage of mathematics in real life
decision making.

# Content

These materials consist of four tutorials that focus on the Iterated Prisoner's
Dilemma, the notion of strategies and computer tournaments whilst using
`Axelrod-Python` [@axelrodproject].

In 1980, a political scientist called Robert Axelrod ran a computer
tournament of the Iterated Prisoner’s Dilemma where strategies written in
computer code would repeatedly choose between self and collective interest. The
strategies would decide on their next action using the history of previous
interactions and the winner was decided based on the average score. The open source
package `Axelrod-Python` was created in order to reproduce Axelrod's original work
but to also serve as an educational and research tool.

Following the tutorial, participants will be able to reproduce Axelrod's
tournament but also create their own unique tournaments from a selection of more
than 200 strategies. Furthermore, participants will be able to progress their
comprehension of the topic by producing strategies and implement them using
Python code. The new strategies then can be placed in different tournaments in
order to access their success and weakness. This progression of the tutorial
fits within a constructive framework of learning [@Weir2009] and, by the nature
of participants actively writing the required software, an active learning
setting [@Freeman2014]. Participants with a knowledge of Python will benefit from
an understanding of game theory and participants with no knowledge of Python
will also be introduced to basic programming concepts through the tangible ideas
of the Prisoner's Dilemma.

# Usage

The tutorial `Game Theory and Python` can be used in a workshop environment or
through independent learning.

- **Workshop:** The material has been designed for a 2 hour workshop. A suggested
timetable is:
    - 0:00 - 0:15  Installation (guidelines are given in the
  [README](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/README.rst))
    - 0:15 - 0:30  [An introduction to game theory and the Iterated Prisoner's
  Dilemma](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/1.%20Introduction.ipynb)
    - 0:30 - 0:55  [Creating matches and
  tournaments using Axelrod-Python](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/2.%20Matches%20and%20Tournaments.ipynb)
    - 0:55 - 1:20  [Writing strategies and contributing to Axelrod-Python](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/3.%20Writing%20a%20Strategy.ipynb>)
    - 1:20 - 1:50  [Playing against strategies of the Iterated Prisoner's Dilemma](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/4.%20Human%20Strategy.ipynb)
    - 1:50 - 2:00  Closing remarks and wrapping up
  
  In a workshop environment we suggest that the instructor has familiarized
  themselves with the written parts of the tutorial beforehand. The written parts
  of each notebook include an introduction to the topic being covered. It is
  advised that the instructor discusses the introduction to the topic 
  followed by them typing out/running the material while the participants
  follow using their own machines. The instructor should encourage the participants
  to try the exercises of each notebook alone or with other participants. Before
  moving to the next notebook the instructor should encourage a discussion
  amongst everyone regarding the results of the exercises each had
  and their interpretation.
- **Independent Learning**: An independent learner should aim to spend the same
  amount of time on the material, approximately 2 hours. A suggested
timetable is:
    - 0:00 - 0:15  Installation (guidelines are given in the
  [README](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/README.rst))
    - 0:15 - 0:30  [An introduction to game theory and the Iterated Prisoner's
  Dilemma](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/1.%20Introduction.ipynb)
    - 0:30 - 1:00  [Creating matches and
  tournaments using Axelrod-Python](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/2.%20Matches%20and%20Tournaments.ipynb)
    - 1:00 - 1:30  [Writing strategies and contributing to Axelrod-Python](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/3.%20Writing%20a%20Strategy.ipynb>)
    - 1:30 - 2:00  [Playing against strategies of the Iterated Prisoner's Dilemma](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/4.%20Human%20Strategy.ipynb)
  
  If the tutorial is being followed by an individual learner, we suggest that
  the learner reads the written parts of each notebook followed by running the
  tutorial and completing the exercises. The individual should take some time to
  reflect on the results of each notebook and their interpretation.

These instructions can also be found in the [README](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/README.rst).

# Recent Uses

This tutorial was originally formulated to run a game theory workshop at [PyCon
Namibia 2017](https://na.pycon.org/pycon-namibia-2017/). It has attracted
the attention of the community ever since and has been used in various others
events.

# Acknowledgements

The tutorial has been made possible due to the existence of the open source package
[Axelrod-Python](https://github.com/Axelrod-Python/Axelrod). We would like to
express our appreciation to the maintainers of the package as well as
anyone that has ever contributed to it.

# References
