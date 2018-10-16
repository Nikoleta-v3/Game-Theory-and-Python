"""This is a script which calls the human strategy and creates a match against
any selected player from the Axelrod library.

Usage:
    human.py [-h] [-n NAME] [-t TURNS]

 Options:
      -h --help         Show This
      -n NAME           The name of the human strategy [default: me]
      -t TURNS          The number of turns [default: 5]
"""
import random

import axelrod as axl
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__)

    # get values
    name = arguments['-n']
    turns = int(arguments['-t'])

    # create players and match
    opponent = random.choice(axl.strategies)
    me = axl.Human(name=name)
    players = [opponent(), me]

    # play the match and return winner and final score
    match = axl.Match(players, turns=turns)
    match.play()
    print('You have competed against {}, the final score of the match is: '
          '{} and the winner was {}'.format(opponent.name, match.final_score(),
                                            match.winner()))
