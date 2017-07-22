#!/usr/bin/env python

import os
import sys
import paramiko
import Queue
from threading import Thread

username = 'pi'
password = 'raspberry'
connect_timeout = 5

def ssh_login(q):
    while not q.empty():
        (host, port) = q.get()

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(host, port=int(port), username=username, password=password,
            allow_agent=False, look_for_keys=False, timeout=connect_timeout)
        except Exception as e:
            sys.stderr.write(host + ':' + port + ': ' + str(e) + '\n')
            sys.stderr.flush()
        else:
            sys.stdout.write(host + ':' + port + '\n')
            sys.stdout.flush()
        finally:
            ssh.close()

        q.task_done()

def scan(num_threads=50):
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
    if len(sys.argv) > 1:
        scan(int(sys.argv[1]))
    else:
        scan()
