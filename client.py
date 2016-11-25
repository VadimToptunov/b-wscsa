#author = "Vadim Toptunov"
import os
import random
import string
from socket import *

bword = []
trigger = "shut up!"
letter = "b"
#directory = "/tmp/"
directory = "C:/Users/vatoptun/"
name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for x in range(10))
filename = directory + name + ".txt"
#print filename

print "Write some words to add into a file (To stop writing, just write 'shup up!'.):"
word = raw_input()
wordlist = []
wordlist.append(word)

#Here the words are inserted into wordlist.
while word != trigger:
    word = raw_input()
    wordlist.append(word)
#print "WRDLST: "
#print wordlist


#Check if an inserted word contains a letter 'b' and add the word into the bword list

for w in wordlist:
    if letter in w:
        bword.append(w + "\n")
    elif letter.upper() in w:
        bword.append(w + "\n")
#print "BWord: "
#print bword

#Then open a file, write down the words with the letter 'b' and close it.
with open(filename, "w") as bfile:
    bfile.writelines(bword)
bfile.close()

#server

HOST = 'localhost'    #server name goes in here
PORT = 3820
socket = socket(AF_INET, SOCK_STREAM)
socket.connect((HOST, PORT))
with open(filename, 'rb') as file_to_send:
    for data in file_to_send:
        socket.sendall(data)
socket.close()

print "The %s will now be removed" % filename
os.remove(filename)
print "The %s is removed" % filename
