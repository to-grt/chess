

from cgitb import text
from msilib.schema import TextStyle
from turtle import position, width


class Button:


    def __init__(self, text, text_size, color_text, color_rect, position):

        self.text = text
        self.text_size = text_size
        self.color_text = color_text
        self.color_rect = color_rect
        self.position = position
        self.width = len(text) * 43
        self.height = text_size+30

