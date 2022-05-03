from __future__ import annotations

import curses
import random
import time

LAMP = "o"
LEAVE = "*"

LEAVE_COLOR = 1
TRUNK_COLOR = LEAVE_COLOR + 1
LIGHT_COLOR = TRUNK_COLOR + 1

COLORS = [
    curses.COLOR_MAGENTA,
    curses.COLOR_RED,
    curses.COLOR_WHITE,
    curses.COLOR_BLUE,
    curses.COLOR_CYAN,
]


def animate(stdscr: curses._CursesWindow) -> int:
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(LEAVE_COLOR, curses.COLOR_GREEN, -1)
    curses.init_pair(TRUNK_COLOR, curses.COLOR_YELLOW, -1)

    for i in range(len(COLORS)):
        curses.init_pair(LIGHT_COLOR + i, COLORS[i], -1)

    curses.curs_set(0)

    stdscr.nodelay(True)

    while True:
        try:
            wch = stdscr.get_wch()
        except curses.error:
            pass
        else:
            if wch == curses.KEY_RESIZE:
                curses.update_lines_cols()
            else:
                return 0

        tree_height = int(curses.LINES * 0.8)
        trunk_height = int(curses.LINES * 0.2)
        trunk_thickness = (
            int(curses.LINES * 0.1) + (int(curses.LINES * 0.1) % 2 == 0 if 1 else 0) + 2
        )

        for i in range(1, 2 * tree_height, 2):
            spaces = int((curses.COLS - i) / 2) * " "

            stdscr.addstr(spaces)

            for _ in range(i):
                if random.random() > 0.2:
                    stdscr.addstr(LEAVE, curses.color_pair(1))
                else:
                    stdscr.addstr(
                        LAMP,
                        curses.color_pair(
                            random.randint(LIGHT_COLOR, len(COLORS) + LIGHT_COLOR - 1)
                        ),
                    )

            stdscr.addstr(spaces)

        for _ in range(trunk_height):
            spaces = int((curses.COLS - trunk_thickness) / 2) * " "

            stdscr.addstr(spaces)

            stdscr.addstr(trunk_thickness * "|", curses.color_pair(TRUNK_COLOR))

            stdscr.addstr(spaces)

        stdscr.refresh()
        time.sleep(0.5)
        stdscr.erase()


def main() -> int:
    return curses.wrapper(animate)


if __name__ == "__main__":
    raise SystemExit(main())
