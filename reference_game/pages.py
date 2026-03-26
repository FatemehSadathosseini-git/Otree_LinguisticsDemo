from otree.api import *
from .models import C, Group, Player

class Speaker(Page):
    form_model = 'player'
    form_fields = ['word']

    def is_displayed(self):
        return self.player.id_in_group == 1

class Listener(Page):
    form_model = 'player'
    form_fields = ['guess']

    def is_displayed(self):
        return self.player.id_in_group == 2

class Results(Page):
    pass

page_sequence = [Speaker, Listener, Results]
