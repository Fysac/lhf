import paramiko
import os
import sys

USER = 'pi'
PASS = 'raspberry'
PARAMIKO_LOGGING = False
TIMEOUT = 5

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

if PARAMIKO_LOGGING:
    LOG_DIR = './log/'
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    paramiko.util.log_to_file(LOG_DIR + 'paramiko.log')

def attempt_login():
    for line in sys.stdin.readlines():
        pi = line.split(':')
        (host, port) = (pi[0], pi[1].replace('\n', ''))

        try:
            ssh.connect(host, port=int(port), username=USER, password=PASS, timeout=TIMEOUT)
            sys.stdout.write(host + ':' + port + '\n')
            sys.stdout.flush()
            ssh.close()
        except Exception as e:
            sys.stderr.write(host + ':' + port + ': ' + str(e) + '\n')
            sys.stderr.flush()
            continue

if __name__ == '__main__':
    attempt_login()
