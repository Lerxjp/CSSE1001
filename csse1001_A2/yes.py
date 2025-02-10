class Card(object):
    
    def __init__(self, ):
        self._card = card
        self._players = players
    def play(self, player: Player, game: a2_support.CodersGame):
        pass
    def action(self, player: Player, game:a2_support.CodersGame, slot: int):
        pass
    def __str__(self):
        return  f":{self.__class__.__name__}()"
    def __repr__(self):
        return str(self)




    
class NumberCard(Card):
    def __init__(self, number):
        self._number = number
        
    def get_number(self):
        return self._number

    def __str__(self):
        return super(NumberCard, self).__str__()
