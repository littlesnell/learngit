#!/usr/bin/python
#coding = utf-8
import socket, select, string, sys

def prompt() :
    sys.stdout.write('<You> ')
    sys.stdout.flush()

#main function
if __name__ == "__main__":

    if(len(sys.argv) < 3) :
        print 'Usage : python chat_client.py localhost 8192'
        sys.exit()

    host = sys.argv[1]
    port = int(sys.argv[2])

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.settimeout(2)

    # connect to remote host
    try :
        client_socket.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()

    print 'Connected to remote host. Start sending messages'
    prompt()

    while 1:
        rlist = [sys.stdin,client_socket]

        # Get the list sockets which are readable
        read_list, write_list, error_list = select.select(rlist , [], [])

        for sock in read_list:
            #incoming message from remote server
            if sock == client_socket:
                data = sock.recv(2048)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    prompt()

            #user entered a message
            else :
                msg = sys.stdin.readline()
                client_socket.send(msg)
                prompt()
