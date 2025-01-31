import socket
import ssl 

server = '192.168.1.100' 
port   = 12700 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("CA/ca-cert.pem")
    
client_ssl = context.wrap_socket(client_socket, server_hostname=server)
client_ssl.connect((server, port))
print("[+] Connecté au serveur.")

    
while True:
        #Get message
    msg=client_ssl.recv(1024).decode()
    print(f"Server : {msg}")

    #Send message
    msg=str(input("Client : ")).encode()
    client_ssl.send(msg)