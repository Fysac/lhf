import sys
import shodan

SHODAN_API_KEY = 'SHODAN_API_KEY'

# Identifying SSH banners for Raspbian
BANNERS = [
    'SSH-2.0-OpenSSH_6.7p1 Raspbian-5+deb8u1',
    'SSH-2.0-OpenSSH_6.7p1 Raspbian-5+deb8u2',
    'SSH-2.0-OpenSSH_6.7p1 Raspbian-5+deb8u3'
]

def init_shodan():
    with open(SHODAN_API_KEY, 'r') as f:
        key = f.read().strip().replace('\n', '')
    return shodan.Shodan(key)

def search_shodan(max_results=100):
    api = init_shodan()

    for banner in BANNERS:
        results = api.search(banner, limit=(max_results / len(BANNERS)))
        for r in results['matches']:
            sys.stdout.write(r['ip_str'] + ':' + str(r['port']) + '\n')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        search_shodan(int(sys.argv[1]))
    else:
        search_shodan()
