import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 9999))  # Écoute sur toutes les interfaces
    server_socket.listen(5)
    print("Serveur en attente de connexions...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connexion établie avec {address}")
        client_socket.send(b"Bienvenue sur le serveur. Envoyez une commande : ")

        while True:
            command = input("Commande à envoyer : ")
            client_socket.send(command.encode())

            if command.lower() == "exit":
                print("Fermeture de la connexion.")
                client_socket.close()
                break

            response = client_socket.recv(1024).decode()
            print(f"Réponse du client : {response}")

start_server()
