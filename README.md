# Game-Theory-and-Python

[![status](https://jose.theoj.org/papers/10.21105/jose.00078/status.svg)](https://doi.org/10.21105/jose.00078)
[![license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Nikoleta-v3/Game-Theory-and-Python/master/LICENSE)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
![CI](https://img.shields.io/github/workflow/status/Nikoleta-v3/Game-Theory-and-Python/ci)

This repository was created to support a workshop on Game Theory using the
programming language [Python](https://www.python.org/) and, more specifically,
the open-source [Axelrod Python
library](https://github.com/Axelrod-Python/Axelrod).

## Workshop Topics

1. [An introduction to game theory and the Iterated Prisoner's Dilemma](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/1.%20Introduction.ipynb)
2. [Creating matches and tournaments using Axelrod-Python](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/2.%20Matches%20and%20Tournaments.ipynb)
3. [Writing strategies and contributing to Axelrod-Python](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/3.%20Writing%20a%20Strategy.ipynb)
4. [Playing against strategies of the Iterated Prisoner's Dilemma](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/4.%20Human%20Strategy.ipynb)

## Installing Python

There are various Python distributions. We recommend using
[Anaconda](https://www.anaconda.com/download), which comes bundled with tools
like Jupyter Notebooks.

This tutorial is written using [Jupyter Notebooks](http://jupyter.org/).

## Virtual Environment

This repository includes an `environment.yml` file to help you set up an
Anaconda environment.

To create the environment, navigate to the repository folder and run:

```bash
conda env create -f environment.yml
```

Activate the environment with:

```bash
conda activate game-python
```

You can now run notebooks in this environment. In Jupyter, go to `Kernel > Change Kernel` and select `game-python`.

### Using python `venv` instead of Conda

If you prefer Python `venv` instead of Conda, you can create a virtual environment using the following commands:

```bash
python3 -m venv game-python
```

Then, activate the virtual environment and install the required packages:
source game-python/bin/activate
pip install -r requirements.txt
```

### Virtual Environment in Jupyter

If your environment does not appear in Jupyter, run the following command while the environment is activated:

```bash
python -m ipykernel install --user --name=game-python
```

## Usage

The tutorial **Game Theory and Python** can be used in a workshop setting or for independent learning.

### Workshop

This material is designed for a 2-hour workshop. Suggested schedule:

| Time      | Topic                                                                                          |
| --------- | ---------------------------------------------------------------------------------------------- |
| 0:00–0:15 | Installation (see above)                                                                       |
| 0:15–0:30 | [Intro to game theory and the Iterated Prisoner's Dilemma](1.%20Introduction.ipynb)            |
| 0:30–0:55 | [Creating matches and tournaments with Axelrod-Python](2.%20Matches%20and%20Tournaments.ipynb) |
| 0:55–1:20 | [Writing strategies and contributing](3.%20Writing%20a%20Strategy.ipynb)                       |
| 1:20–1:50 | [Playing against IPD strategies](4.%20Human%20Strategy.ipynb)                                  |
| 1:50–2:00 | Closing remarks                                                                                |

**Instructor tips:**

Instructors should familiarize themselves with the content ahead of time. For
each notebook, start with a short explanation or demo, then guide participants
through the material. Encourage individual or group exploration of the
exercises, and discuss the outcomes before moving on.

### Independent Learning

If you're using this material on your own, you should aim to spend around 2 hours.

Suggested self-study timeline:

| Time      | Topic                                                                               |
| --------- | ----------------------------------------------------------------------------------- |
| 0:00–0:15 | Installation                                                                        |
| 0:15–0:30 | [Intro to game theory and the Iterated Prisoner's Dilemma](1.%20Introduction.ipynb) |
| 0:30–1:00 | [Creating matches and tournaments](2.%20Matches%20and%20Tournaments.ipynb)          |
| 1:00–1:30 | [Writing strategies](3.%20Writing%20a%20Strategy.ipynb)                             |
| 1:30–2:00 | [Playing against IPD strategies](4.%20Human%20Strategy.ipynb)                       |

**Learner tips:**

Read the explanations in each notebook, run the code, and try the exercises.
Reflect on the outcomes and think about what they mean in the context of game
theory.

## Material in Other Forms

While this tutorial was written in Jupyter Notebooks, you might prefer working
with Python scripts. The notebooks have been converted to PDFs and can be found
in the `notebooks` directory. These can serve as a guide if you wish to type
everything into scripts manually.

## Contributions

All contributions are welcome! This includes:

* Suggestions for new sections
* Bug reports
* Code contributions

## Events

This tutorial has been used in the following event:

* [PyCon Namibia 2017](https://na.pycon.org/pycon-namibia-2017/)
* [EGAI 2024](https://egai.cc)

Have you used this tutorial at an event? Let us know by [contacting
me](https://nikoleta-v3.github.io/) or opening a [pull
request](https://github.com/Nikoleta-v3/Game-Theory-and-Python/pulls) to add
your event to this list.

## License

This project is licensed under the [MIT
License](https://github.com/Nikoleta-v3/Game-Theory-and-Python/blob/master/LICENSE.txt),
including all code in the notebooks listed above.
