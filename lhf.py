import sys
import search

def print_usage():
    print('usage: ' + sys.argv[0] + ' <search> [max results]')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print_usage()
    else:
        if sys.argv[1] == 'search':
            if len(sys.argv) >= 3:
                search.search_shodan(int(sys.argv[2]))
            else:
                search.search_shodan()
        else:
            print_usage()
