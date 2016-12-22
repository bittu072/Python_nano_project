__author__ = 'BITTU'
#trial "SIMPLE WEB BROWSER" code, may work, but if you are not connected to the internet or have problem in writing URL-it may not work
####this will provide web page header information and html instances of the web page
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("www.coursera.org", 80))

#to send
mysock.send('GET https://www.coursera.org/learn/python-network-data/lecture/TdznM/understanding-html HTTP/1.0\n\n')

while True:

	data = mysock.recv(512) #to recieve data
	if (len(data)<1):
		break
	print data
#to close created socket
mysock.close()
