# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:20:50 2020

@author: MAGUI02
"""


class Player:
    def __init__(self, name: str):
        self.name_player = name
        self.points = 0

    def get_name(self) -> str:
        return self.name_player

    def get_points(self) -> int:
        return self.points

    def add_point(self) -> None:
        self.points += 1
