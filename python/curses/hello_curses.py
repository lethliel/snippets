#!/usr/bin/env python

import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

stdscr.bkgd(curses.color_pair(1))
stdscr.refresh()

win = curses.newwin(10, 40, 20, 20)
win.bkgd(curses.color_pair(2))
win.box()
win.addstr(2, 2, "Hallo, Welt!")
win.refresh()

c = stdscr.getch()

curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
