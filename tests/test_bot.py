#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from macro.bot import bot

bot.dl = 0.5

def test_press_and_tap():
    bot.press_and_tap("ctrl", "c")
    bot.press_and_tap("alt", "tab", 5, interval=0.5)
    
test_press_and_tap()

def test_get_screen_size():
    print(bot.get_screen_size())
    print(bot.get_position())
    
test_get_screen_size()