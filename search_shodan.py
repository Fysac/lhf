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

def search_shodan(max_results=500):
    api = init_shodan()

    for banner in BANNERS:
        for page in range(1, 1 + (max_results / (len(BANNERS) * 100))):
            results = api.search(banner, page)
            for r in results['matches']:
                sys.stdout.write(r['ip_str'] + ':' + str(r['port']) + '\n')
                sys.stdout.flush()

if __name__ == '__main__':
    search_shodan(int(sys.argv[1]))
