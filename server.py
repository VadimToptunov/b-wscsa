# server
#author = "Vadim Toptunov"
import os
import random
from socket import *
import string
trigger = 'shut up!'
#directory = "/tmp/"
directory = "C:/Users/"
name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for x in range(10))
filename = directory + name + ".txt"

HOST = 'localhost'
PORT = 3820
socket = socket(AF_INET, SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen(1)
while (1):
    conn, addr = socket.accept()
    print 'New client connected...'
    with open(filename, 'wb') as file_to_write:
        while True:
            data = conn.recv(1024)
            #print data
            if not data:
                break
            file_to_write.write(data)
            file_to_write.close()
    print "The data is saved in %s." % filename
    print "The words are:"
    f = open(filename, 'r')
    print f.read()
    f.close()
    conn.close()
    print "Do you want to switch off the server? (yes/no)"
    answer = raw_input()
    if answer == "yes":
        break

    elif answer == "no":
        pass
    else:
        print "Answer, please! Yes or no?"
        if answer == "yes":
            break
        else:
            pass
socket.close()
print "The %s will now be removed from server" % filename
os.remove(filename)
print "The %s is removed from server" % filename
