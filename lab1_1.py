def draw(offset = 1, lenght = 1, color = 21):
    line = (' ') * lenght
    print(f'{""*offset}\x1b[48;5;{color}m{line}\x1b[0m', end = "")


COLORS = [21,231,9]


def flag():
    height = 3
    lenght = 2
    offset = 1

    for color in COLORS:
        for line in range(offset):
            draw(offset,lenght,color)


if __name__ == '__main__':
    flag()
