import socket
import sys
import traceback


def client(msg, log_buffer=sys.stderr):

    msg_block_size = 16
    server_host = "127.0.0.1"
    server_port = 8000
    server_address = (server_host, server_port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    client_socket.connect((server_host, server_port))
    received_message = ""
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        client_socket.sendall(msg.encode('utf-8'))
        print('waiting server reply')
        while True:
            msg_chunk = client_socket.recv(msg_block_size)
            received_message += msg_chunk.decode()
            #print(received_message)
            #print(str(len(received_message)))
            if (len(received_message) >= len(msg)):
                #print("done msg rcvd")
                break

        print("Server says: {}".format(received_message))
        
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        print('closing socket', file=log_buffer)
        client_socket.close()

    return(received_message)
    
    
def client_WhatToDo(msg, log_buffer=sys.stderr):
    server_address = ('localhost', 10000)
    # TODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    sock = None
    print('connecting to {0} port {1}'.format(*server_address), file=log_buffer)
    # TODO: connect your socket to the server here.

    # you can use this variable to accumulate the entire message received back
    # from the server
    received_message = ''

    # this try/finally block exists purely to allow us to close the socket
    # when we are finished with it
    try:
        print('sending "{0}"'.format(msg), file=log_buffer)
        # TODO: send your message to the server here.

        # TODO: the server should be sending you back your message as a series
        #       of 16-byte chunks. Accumulate the chunks you get to build the
        #       entire reply from the server. Make sure that you have received
        #       the entire message and then you can break the loop.
        #
        #       Log each chunk you receive.  Use the print statement below to
        #       do it. This will help in debugging problems
        chunk = ''
        print('received "{0}"'.format(chunk.decode('utf8')), file=log_buffer)
    except Exception as e:
        traceback.print_exc()
        sys.exit(1)
    finally:
        # TODO: after you break out of the loop receiving echoed chunks from
        #       the server you will want to close your client socket.
        print('closing socket', file=log_buffer)

        # TODO: when all is said and done, you should return the entire reply
        # you received from the server as the return value of this function.


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage = '\nusage: python echo_client.py "this is my message"\n'
        print(usage, file=sys.stderr)
        sys.exit(1)

    msg = sys.argv[1]
    client(msg)
