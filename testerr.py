import curses
import papermud

stdscr = curses.initscr()
curses.cbreak()
curses.noecho()
stdscr.keypad(True)

curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)


lal = papermud.rendermenu(0, 2, stdscr, ["this", "is", "a", "test", "lol", "going", "good", "so", "far"])

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()

print("lal", lal)