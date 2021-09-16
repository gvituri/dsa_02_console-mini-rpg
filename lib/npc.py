class Npc:

    def __init__(self, name, symbol, position_x, position_y):
       self.name = name
       self.symbol = symbol
       self.coordinate = [int(position_y), int(position_x)]