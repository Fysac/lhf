import os
import sys
import paramiko
from threading import Thread

PARAMIKO_LOGGING = False
USER = 'pi'
PASS = 'raspberry'
TIMEOUT = 10

class SSHThread(Thread):
    def __init__(self, host, port, username, password, timeout=10):
        super(SSHThread, self).__init__()
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.timeout = timeout

    def login(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(self.host, port=int(self.port), username=self.username, password=self.password, allow_agent=False, look_for_keys=False, timeout=self.timeout)
        except Exception as e:
            sys.stderr.write(self.host + ':' + self.port + ': ' + str(e) + '\n')
            sys.stderr.flush()
        else:
            sys.stdout.write(self.host + ':' + self.port + '\n')
            sys.stdout.flush()
        finally:
            ssh.close()

    def run(self):
        self.login()

def scan():
    for line in sys.stdin.readlines():
        pi = line.split(':')
        (host, port) = (pi[0], pi[1].replace('\n', ''))
        t = SSHThread(host, port, USER, PASS, TIMEOUT)
        t.start()

if __name__ == '__main__':
    if PARAMIKO_LOGGING:
        LOG_DIR = './log/'
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
        paramiko.util.log_to_file(LOG_DIR + 'paramiko.log')

    scan()
