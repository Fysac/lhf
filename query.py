#!/usr/bin/env python

import shodan

with open('SHODAN_API_KEY', 'r') as f:
    SHODAN_API_KEY = f.read().replace('\n', '')

# Maximum number of hosts to retrieve from Shodan
MAX_SHODAN_RESULTS = 1000

# Identifying SSH banners for Raspbian
SSH_BANNERS = ['SSH-2.0-OpenSSH_6.7p1 Raspbian-5+deb8u1', 'SSH-2.0-OpenSSH_6.7p1 Raspbian-5+deb8u2']

api = shodan.Shodan(SHODAN_API_KEY)

for banner in SSH_BANNERS:
    for page in range(1, 1 + (MAX_SHODAN_RESULTS / (len(SSH_BANNERS) * 100))):
        results = api.search(banner, page)
        with open('pies.txt', 'a') as f:
            for r in results['matches']:
                f.write(r['ip_str'] + ':' + str(r['port']) + '\n')
