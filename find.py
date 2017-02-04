#!/usr/bin/env python

import sys
import time
import shodan

banners = {
    'ssh_rpi': 'raspbian port:"22","2222"'
}

def init_shodan():
    with open('SHODAN_API_KEY', 'r') as f:
        key = f.read().strip().replace('\n', '')
    return shodan.Shodan(key)

def search_shodan(max_results=100):
    sys.stderr.write('Searching...\n')
    api = init_shodan()

    total = 0
    offset = 0
    count = 500
    
    while offset < max_results:
        try:
            results = api.search(banners['ssh_rpi'], offset=offset, limit=count, minify=True)
        except shodan.APIError as e:
            sys.stderr.write(str(e) + '\n')
            if 'Request limit reached' in str(e):
                time.sleep(5)
            continue
        
        for r in results['matches']:
            sys.stdout.write(r['ip_str'] + ':' + str(r['port']) + '\n')
            total += 1
            if total == max_results:
                return
        offset += len(results['matches'])

if __name__ == '__main__':
    if len(sys.argv) > 1:
        search_shodan(int(sys.argv[1]))
    else:
        search_shodan()
