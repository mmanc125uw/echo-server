import socket
import sys
import traceback


def server(log_buffer=sys.stderr):

    msg_block_size = 16
    server_host = "127.0.0.1"
    server_port = 8000
    server_address = (server_host, server_port)
    print("making a server on {0}:{1}".format(*server_address), file=log_buffer)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server_socket.bind(server_address)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)
            server_socket.listen(1)
            connection, client_address = server_socket.accept()
            print('connection accepted - {0}:{1}'.format(*client_address), file=log_buffer)
    
            print('waiting too recv msg')
            totmsg = ""
            while True:
                received_message = connection.recv(msg_block_size)
                #print('rcvd len is ' + str(len(received_message)))
                #print("rcvd msg block: {}".format(received_message.decode()))

                totmsg += format(received_message.decode())

                if (len(received_message) < msg_block_size):
                    #print('done breaking out of inner loop')
                    print("Client says: {}".format(totmsg))
                    connection.sendall(totmsg.encode('utf8'))
                    
                    break
                
            connection.shutdown(socket.SHUT_RDWR)
            connection.close()
            
                
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        print(
            'echo complete, client connection closed', file=log_buffer
        )
        server_socket.close()


def server_WhatToDo(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = None
    # TODO: You may find that if you repeatedly run the server script it fails,
    #       claiming that the port is already used.  You can set an option on
    #       your socket that will fix this problem. We DID NOT talk about this
    #       in class. Find the correct option by reading the very end of the
    #       socket library documentation:
    #       http://docs.python.org/3/library/socket.html#example

    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    # TODO: bind your new sock 'sock' to the address above and begin to listen
    #       for incoming connections

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)

            # TODO: make a new socket when a client connects, call it 'conn',
            #       at the same time you should be able to get the address of
            #       the client so we can report it below.  Replace the
            #       following line with your code. It is only here to prevent
            #       syntax errors
            conn, addr = ('foo', ('bar', 'baz'))
            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    # TODO: receive 16 bytes of data from the client. Store
                    #       the data you receive as 'data'.  Replace the
                    #       following line with your code.  It's only here as
                    #       a placeholder to prevent an error in string
                    #       formatting
                    data = b''
                    print('received "{0}"'.format(data.decode('utf8')))
                    
                    # TODO: Send the data you received back to the client, log
                    # the fact using the print statement here.  It will help in
                    # debugging problems.
                    print('sent "{0}"'.format(data.decode('utf8')))
                    
                    # TODO: Check here to see whether you have received the end
                    # of the message. If you have, then break from the `while True`
                    # loop.
                    # 
                    # Figuring out whether or not you have received the end of the
                    # message is a trick we learned in the lesson: if you don't
                    # remember then ask your classmates or instructor for a clue.
                    # :)
            except Exception as e:
                traceback.print_exc()
                sys.exit(1)
            finally:
                # TODO: When the inner loop exits, this 'finally' clause will
                #       be hit. Use that opportunity to close the socket you
                #       created above when a client connected.
                print(
                    'echo complete, client connection closed', file=log_buffer
                )

    except KeyboardInterrupt:
        # TODO: Use the python KeyboardInterrupt exception as a signal to
        #       close the server socket and exit from the server function.
        #       Replace the call to `pass` below, which is only there to
        #       prevent syntax problems
        pass
        print('quitting echo server', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)
