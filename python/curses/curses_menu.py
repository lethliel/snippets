#!/usr/bin/env python

import curses

x = 0
while x != ord('4'):
    screen = curses.initscr()

    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, "Comments")
    screen.addstr(4, 4, "1 - Comment 1")
    screen.addstr(5, 4, "2 - Comment 2")
    screen.addstr(6, 4, "3 - Comment 3")
    screen.addstr(7, 4, "4 - Exit")
    screen.refresh()

    x = screen.getch()

curses.endwin()
