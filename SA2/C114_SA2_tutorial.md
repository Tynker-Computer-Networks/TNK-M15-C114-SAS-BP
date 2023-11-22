Roll the Die
===========================


In this activity, you will learn to add the functionality to roll the die when the "Roll Dice" button is clicked.


<img src= "https://media.slid.es/uploads/1525749/images/10883886/SA2.gif" width = "480" height = "180">


Follow the given steps to complete this activity:


1. Send the Die Number to the Server.
* Open the file `client.py`.
~~~sh
    SERVER.send(f'{value}player1_turn'.encode())
~~~


2. Send the die number to all the players. 
* Open the file `server.py`.
* Place the order by uncommenting the `placeOrder` function definition.
~~~sh
def handle_client(player_socket,player_name):
    global CLIENTS
    while True:
        try:
            message = player_socket.recv(2048)
            if(message):
                for cName in CLIENTS:
                    cSocket = CLIENTS[cName]["player_socket"]
                    cSocket.send(message)
        except:
            pass
~~~
3. Receive the die number from the server.
* Open the file `client.py`.
~~~sh
def received_msg():
    global SERVER, canvas2, dice
    while True:
        message = SERVER.recv(2048).decode()


~~~


4. Display the face of the die.
~~~sh
if('\u2680' in message):
            canvas2.itemconfigure(dice, text='\u2680')
        elif('\u2681' in message):
            canvas2.itemconfigure(dice, text='\u2681')
        elif('\u2682' in message):
            canvas2.itemconfigure(dice, text='\u2682')
        elif('\u2683' in message):
            canvas2.itemconfigure(dice, text='\u2683')
        elif('\u2684' in message):
            canvas2.itemconfigure(dice, text='\u2684')
        elif('\u2685' in message):
            canvas2.itemconfigure(dice, text='\u2685')
~~~
5. Create a thread that targets `received_msg` function.
* Open the file `client.py`.
~~~sh
def setup():
...
...
...
    thread = Thread(target=received_msg)
    thread.start()
~~~
6. Create a thread that calls `handle_client` function.
* Open the file `server.py`.
~~~sh
def accept_connections():
        thread = Thread(target = handle_client, args=(player_socket,player_name))
        thread.start()


~~~




* Save and run the code to check the output.