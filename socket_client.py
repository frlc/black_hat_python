import socket

target_host = "0.0.0.0"
target_port = 9999

#objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#conexao com cliente
client.connect((target_host, target_port))

#envia dados
client.send("teste ABCD")

#recebe dados
response = client.recv(4096)

print response