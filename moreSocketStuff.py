import socket


def qotd(host, port):
    s = socket.socket()

    msg = bytearray()

    s.connect((host, port))
    buf = s.recv(4096)

    while buf:
        print(msg)
        msg.extend(buf)
        buf = s.recv(4096)

    print(msg)


if __name__ == '__main__':
    qotd('djxmmx.net', 17)