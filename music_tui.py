import curses

def load_songs(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f]

def main(stdscr):
    curses.curs_set(0)  # Hide the cursor
    stdscr.nodelay(1)   # Make getch() non-blocking
    stdscr.timeout(100) # Refresh every 100ms

    songs = load_songs('songs.txt')
    current_index = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        for idx, song in enumerate(songs):
            x = width // 2 - len(song) // 2
            y = height // 2 - len(songs) // 2 + idx
            if idx == current_index:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, x, song)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, song)

        key = stdscr.getch()

        if key == ord('q'):
            break
        elif key in [ord('j'), curses.KEY_DOWN]:
            current_index = (current_index + 1) % len(songs)
        elif key in [ord('k'), curses.KEY_UP]:
            current_index = (current_index - 1) % len(songs)

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
