import socket , sys

print sys.argv[1]
for i in range(1,65535):
	try:
		s = socket.socket()
		stat =s.connect((sys.argv[1],i))
		out = ''
		if i == 22 :
			s.send('hamid ooooo \n')
			out = s.recv(20)
		if stat == None:
			print ('[*] ' + sys.argv[1] + ':' + str(i) + ' OPEN' + out)
		s.close() 
	except :
		pass
