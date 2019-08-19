#!/usr/bin/env python3
import curses
import cursetup
import time
import random
from curses.textpad import Textbox, rectangle

stdscr = cursetup.setup()

def lal(stdscr):
    stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

    editwin = curses.newwin(5,30, 2,1)
    rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
    stdscr.refresh()

    box = Textbox(editwin)

    # Let the user edit until Ctrl-G is struck.
    box.edit()

    # Get resulting contents
    message = box.gather()

def centertext(text):
    stdscr.addstr(int(curses.LINES/2), int(curses.COLS/2), text)
    stdscr.refresh()

def animatetext(atext):
    btext=''
    for i in range(len(atext)):
        btext+=atext[i]
        stdscr.addstr(int(curses.LINES/2), int(curses.COLS/2), btext, curses.color_pair(1))
        stdscr.refresh()
        time.sleep(.05)

def displaykey():
    key = stdscr.getkey()
    centertext(key + str(random.randrange(0,100)))

randomtimer=5.0
def randomtext(text):
    stdscr.addstr( 
            random.randrange(0,(curses.LINES - 2)),
            random.randrange(0,(curses.COLS - 2)), 
            text)
    stdscr.refresh()
    time.sleep(0.15)

win = curses.newwin(1, curses.COLS, curses.LINES - 1, 0)
win.echochar('F')
stdscr.hline(curses.LINES - 2, 0, curses.ACS_HLINE, curses.COLS)
while True:
    key = stdscr.getkey()
    if key in (curses.KEY_ENTER, '\n'):
        win.echochar('G')
        break
    win.echochar(str(key))
win.echochar('2')
time.sleep(2)

time.sleep(5)
cursetup.quit(stdscr)
