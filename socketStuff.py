import socket


def tcp_echo():
    s = socket.socket()
    s.bind(('0.0.0.0', 12345))
    s.listen()

    while True:
        conn, address = s.accept()
        print('Connection accepted from {}'.format(address))
        conn.sendall(conn.recv(4096))
        conn.close()


def tcp_echo():
    s = socket.socket()
    s.connect(('127.0.0.1', 12345))
    s.sendall(b'hello world today is great')

    capture = s.recv(4096)
    print(capture)


def udp_echo():
    s = socket.socket(type= socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 12345))

    while True:
        data, address = s.recvfrom(4096)
        print(data, 'Received from {}'.format(address))
        s.sendto(data, address)


def udp_echo():
    s = socket.socket(type= socket.SOCK_DGRAM)
    s.sendto(b'Hello World from UDP', ('127.0.0.1', 12345))

    capture, address = s.recvfrom(4096)
    print(capture)

