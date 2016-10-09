# lhf

Low-Hanging Fruit: A toolset for finding unsecured Raspberry Pis

lhf uses Shodan to search for Internet-connected Raspberry Pis, then attempts to SSH into them with the default admin credentials (`pi`:`raspberry`).

On a default install of Raspbian, `pi` has full sudo access – if you can log in, you already have root.

lhf should only be used for educational purposes with consent, etc. etc.

### Dependencies
* `find.py`
 * `pip install shodan`
* `brute.py`
 * `pip install paramiko`

### Examples
Find 100 Raspberry Pis on Shodan (ports 22 and 2222):

`python find.py 600`

Find 100 Pis, attempt logins, and write unsecured Pis to file:

`python find.py 100 | python brute.py > owned_pies.txt`
