#!/usr/bin/env python3

def draw_grid():
    """
    Draws a 2x2 grid
    Horizontal rows are shown with the pattern +----+----+
    Vertical columsn are shown with (4 * |) - 4 vertical bars

    Args:
        void: no arguments taken

    Returns
        void: prints a grid
    """
    plusses = ['+' for _ in range(3)]
    spaces = [' ' for _ in range(5)]
    dashes = '-'.join(spaces)
    row = dashes.join(plusses)

    column_row = (9 * ' ').join(['|' for _ in range(3)])

    print(row)
    print(column_row)
    print(column_row)
    print(column_row)
    print(column_row)
    print(row)
    print(column_row)
    print(column_row)
    print(column_row)
    print(column_row)
    print(row)

def main():
    draw_grid()

if __name__ == '__main__':
    main()

