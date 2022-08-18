import socket

sock = socket.socket()
sock.connect(('localhost', 8888))
while True:
    message = input('Your message: ')
    byte_message = str.encode(message)
    sock.send(byte_message)

    data = sock.recv(2048)
    print(f'Server: {data.decode()}')
