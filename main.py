import getopt
import sys

from gameHost import Host


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'dc:p:')
    except getopt.GetoptError:
        sys.exit(2)
    if opts:
        for opt, arg in opts:
            if opt in ['-d']:
                duplicate = True
            elif opt in ['-c']:
                column = int(arg)
            elif opt in ['-p']:
                pool = int(arg)
            else:
                duplicate = False
                column = 4
                pool = 6
        my_host = Host(duplicate=duplicate, column=column, pool=pool)
    else:
        my_host = Host()
    while not my_host.guess_input():
        continue


if __name__ == '__main__':
    main()
