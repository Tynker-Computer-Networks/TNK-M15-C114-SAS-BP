import socket
from  threading import Thread

SERVER = None
PORT = None
IP_ADDRESS = None
CLIENTS = {}
player_names = []

# Define handle_client function that accepts player_socket and player_name

    # Access CLIENTS as global
    

    # Create an infinite while loop
    
        # Start a try block
        
            # receive message from player_socket
            
            # Check if message
            
                # Run a for loop for cName in CLIENTS
                
                    # Get player_socket from CLIENTS[cName] in cSocket
                    
                    # Send message on the cSocket
                    
        # Except
        
            # Add pass
            


def accept_connections():
    global CLIENTS
    global SERVER

    while True:
        player_socket, addr = SERVER.accept()
        player_name = player_socket.recv(1024).decode().strip()
            
        if(len(CLIENTS.keys()) == 0):
            CLIENTS[player_name] = {'player_type' : 'player1'}
        else:
            CLIENTS[player_name] = {'player_type' : 'player2'}

        CLIENTS[player_name]["player_socket"] = player_socket
        CLIENTS[player_name]["address"] = addr
        CLIENTS[player_name]["player_name"] = player_name
        CLIENTS[player_name]["turn"] = False

        print(f"Connection established with {player_name} : {addr}")
        print(CLIENTS)

        # Create thread that calls handle_client function
        
        # Start the thread
        

def setup():
    print("\n")
    print("\t\t\t\t\t\t*** LUDO LADDER ***")

    global SERVER
    global PORT
    global IP_ADDRESS

    IP_ADDRESS = '127.0.0.1'
    PORT = 5000
    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...")
    print("\n")

    accept_connections()

setup()
