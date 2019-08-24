#!/usr/bin/env python3
import curses
import cursetup
def rendermenu(window, items):
    menustring =""
    for i in items:
        menustring += i[0] + " | " + i[1] + "\n"
    cursetup.vcentertext(menustring, window)
    keys = [i[0] for i in items]
    key = ""
    while not key in keys:
        key = window.getkey()
    window.clear()
    window.refresh()
    return key