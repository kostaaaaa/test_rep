import socket

sock = socket.socket()
sock.bind(('localhost', 8888))
sock.listen(1)
conn, addr = sock.accept()

print(f'Connected {addr}')

while True:
    data = conn.recv(2048)
    if data:
        str_data = data.decode()
        print(f'Client: {str_data}')
        answer = str_data.upper()
        conn.send(str.encode(answer))
