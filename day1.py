from enum import Enum


class State:
    """Stateクラスは、迷路問題における現在の状態を示すクラスである。これは、のちに集約のために使われる。"""
    def __init__(self, row=-1, column=-1):
        self.row = row
        self.column = column

    def __repr__(self):
        """__repr__はprintの際に参照されるマジックメソッドである。"""
        return "<State: [{}, {}]>".format(self.row, self.column)

    def clone(self):
        return State(self.row, self.column)

    def __hash__(self):
        return hash((self.row, self.column))

    def __eq__(self, other):
        return self.row == other.row and self.column == other.colmn


class Action(Enum):
    UP = 1
    Down = -1
    LEFT = 2
    RIGHT = -2
