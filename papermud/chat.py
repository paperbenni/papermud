#!/usr/bin/env python3

import curses
def open(stdscr):
    chatstring = ''
    win = curses.newwin(1, curses.COLS, curses.LINES - 1, 0)
    stdscr.hline(curses.LINES - 2, 0, curses.ACS_HLINE, curses.COLS)
    while True:
        key = str(stdscr.getkey())
        if key in (curses.KEY_ENTER, '\n'):
            return chatstring
            break
        chatstring += key
        win.echochar(str(key))
