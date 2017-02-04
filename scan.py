import os
import sys
import paramiko
import Queue
from threading import Thread

def ssh_login(q):
    USER = 'pi'
    PASS = 'raspberry'

    while not q.empty():
        (host, port) = q.get()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(host, port=int(port), username=USER, password=PASS,
            allow_agent=False, look_for_keys=False, timeout=10)
        except Exception as e:
            sys.stderr.write(host + ':' + port + ': ' + str(e) + '\n')
            sys.stderr.flush()
        else:
            sys.stdout.write(host + ':' + port + '\n')
            sys.stdout.flush()
        finally:
            ssh.close()
        q.task_done()

def scan(num_threads=10):
    q = Queue.Queue()

    for line in sys.stdin.readlines():
        pi = line.split(':')
        (host, port) = (pi[0], pi[1].replace('\n', ''))
        q.put((host, port))

    for i in range(num_threads):
        t = Thread(target=ssh_login, args=(q,))
        t.daemon = True
        t.start()

    q.join()

if __name__ == '__main__':
    LOGGING = False

    if LOGGING:
        LOG_DIR = './log/'
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)
        paramiko.util.log_to_file(LOG_DIR + 'paramiko.log')

    if len(sys.argv) > 1:
        scan(int(sys.argv[1]))
    else:
        scan()
