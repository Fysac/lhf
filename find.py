import sys
import shodan

SHODAN_API_KEY = 'SHODAN_API_KEY'

QUERY = 'raspbian port:"22","2222"'

def init_shodan():
    with open(SHODAN_API_KEY, 'r') as f:
        key = f.read().strip().replace('\n', '')
    return shodan.Shodan(key)

def search_shodan(max_results=100):
    api = init_shodan()
    i = 0
    for result in api.search_cursor(QUERY, minify=True):
        sys.stdout.write(result['ip_str'] + ':' + str(result['port']) + '\n')
        i += 1
        if i == max_results:
            return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        search_shodan(int(sys.argv[1]))
    else:
        search_shodan()
