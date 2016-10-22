import sys
import shodan

SHODAN_API_KEY = 'SHODAN_API_KEY'

QUERY = 'raspbian port:"22","2222"'

def init_shodan():
    with open(SHODAN_API_KEY, 'r') as f:
        key = f.read().strip().replace('\n', '')
    return shodan.Shodan(key)

# todo: Find workaround for large queries.
# Shodan doesn't like it when max_results > 1000, gives:
# shodan.exception.APIError: Unable to parse JSON response
def search_shodan(max_results=100):
    api = init_shodan()
    results = api.search(QUERY, limit=max_results)
    for r in results['matches']:
        sys.stdout.write(r['ip_str'] + ':' + str(r['port']) + '\n')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        search_shodan(int(sys.argv[1]))
    else:
        search_shodan()
