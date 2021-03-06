# -*- coding: utf8 -*- 

class State(object):
    def __init__(self, name):
        self.name = name
        self.ended = False
        self.game = None

    def set_game(self, game):
        self.game = game

    def update(self, dt):
        pass

    def draw(self, rgb):
        pass

    def onAxisChanged(self, player, xAxis, yAxis, previousXAxis, previousYAxis):
        pass

    def onClampedAxisChanged(self, player, x, y):
        pass

    def onButtonChanged(self, player, aButton, bButton, previousAButton, previousBButton):
        pass

    def onEnter(self, oldState):
        self.ended = False

    def onLeave(self, newState):
        self.ended = True