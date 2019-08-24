#!/usr/bin/env python3
import curses
import cursetup
import time
import random
from curses.textpad import Textbox, rectangle
import papermud.chat as chat
import papermud.chatbox

import papermud

def centerheader(text, window):
    textl = text.split('\n')
    height, width = window.getmaxyx()
    textcounter = 0
    for i in textl:
        window.addstr(int(height/2 - int(len(textl)/2) + textcounter),
                      int(width/2 - (len(i)/2)), i)
        textcounter += 1
    window.refresh()

stdscr = cursetup.setup()

stdheight, stdwidth = stdscr.getmaxyx()

winleft = curses.newwin(stdheight - 2, int(stdwidth/3) - 3, 1,1)
winright = curses.newwin(stdheight - 2, int(2 * (float(stdwidth)/3)) - 3, 1, int(stdwidth/3) + 1)
stdscr.vline(1, int(stdwidth/3) -1 , curses.ACS_VLINE, stdheight - 2)
stdscr.refresh()
items = (("g", "go away"), ("f", "to pay respect"), ("q", "to quit"))
key = papermud.rendermenu(winleft, items)

tb = papermud.chatbox.Chatbox(winleft)
winleft.refresh()
tb.edit()

time.sleep(5)
cursetup.quit(stdscr)
