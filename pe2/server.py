#!/usr/bin/env python3
import socket
import multiprocessing
import random

PAYLOAD = b'aW1wb3J0IHdlYmJyb3dzZXIKd2ViYnJvd3Nlci5vcGVuKCdodHRwczovL3d3dy55b3V0dWJlLmNv\nbS93YXRjaD92PW9IZzVTSllSSEEwJyxuZXc9MSk=\n'


def connection_handler(connection):
    cp = multiprocessing.current_process()
    print('Spawned {} with PID {}'.format(cp.name, cp.pid))

    # connection.sendall(PAYLOAD)
    right = random.randint(1, 10)
    left = 0
    while left < len(PAYLOAD):
        print('PAYLOAD[{}:{}]'.format(left, right))
        left += connection.send(PAYLOAD[left:right])
        right = left + random.randint(1, 10)

    # Server initiates the close resulting in TIME_WAIT.
    # Client can then detect end-of-data by receiving 0 bytes.
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()
    print('Terminating {} with PID {}'.format(cp.name, cp.pid))


def server(bindto='', port=12345):
    s = socket.socket()
    s.bind((bindto, port))
    s.listen()
    while True:
        connection, address = s.accept()
        print('connection accepted from', address)

        # Hand the connection off to another process to handle it.
        multiprocessing.Process(target=connection_handler, args=(connection,)).start()


if __name__ == '__main__':
    server()