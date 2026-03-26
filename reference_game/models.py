from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'reference_game'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    OBJECTS = ["big circle", "small circle", "big square", "small square"]
    WORDS = ["circle", "square", "big", "small"]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    target = models.StringField()

class Player(BasePlayer):
    word = models.StringField(choices=C.WORDS)
    guess = models.StringField()

def creating_session(subsession):
    for group in subsession.get_groups():
        group.target = random.choice(C.OBJECTS)
