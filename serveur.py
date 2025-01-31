import socket
import ssl

def ip():
    hostname=socket.gethostname()
    ip_address=socket.gethostbyname(hostname)
    print("Server local IP :",ip_address)
    return str(ip_address)

host = ip()
port = 12700 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((host, port))
server_socket.listen(5)
print("Serveur up Listening on 12700")    

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain("CERT/cert-server.pem", "CERT/cert-key.pem") 
    
server_ssl = context.wrap_socket(server_socket, server_side=True)
    
client_ssl, ip = server_ssl.accept()
print("L'ip",ip,"c'est connecté")

while True:
    try:
        #Send message
        msg=str(input("Server : ")).encode()
        client_ssl.send(msg)    

            #Get message
        msg=client_ssl.recv(1024).decode()
        print(f"Client : {msg}")
    except:
            break
print("-- END --")  
client_ssl.close()
server_ssl.close()
server_socket.close()


