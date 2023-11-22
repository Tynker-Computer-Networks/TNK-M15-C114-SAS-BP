Display the Message Box
===================




In this activity, you will learn to confirm the payment.




<img src= "https://media.slid.es/uploads/1525749/images/10888607/pasted-from-clipboard.png" width = "480" height = "160">


Follow the given steps to add the feature of players taking chances to roll the die when they click the "Roll Dice" button:


1. Check the Player Type and Place the Button.
* Open the files `client.py`.
* Create variables and check the player type to display the button for the player.
~~~python
player_turn = None
player_type = None
...
...
def game():
    global player_type, player_turn
    ...
    if(player_type == 'player1' and player_turn):
        roll_button.place(x=(screen_width * 0.5) - font_size*2, y= screen_height * 0.7)
    else:
        roll_button.pack_forget()
~~~


2. Disable the Button.


* Send the player type to the server by checking the player type.
~~~python
def roll_dice():  
    if(player_type == 'player1'):
        SERVER.send(f'{value}player2_turn'.encode())
 
    if(player_type == 'player2'):
        SERVER.send(f'{value}player1_turn'.encode())
~~~
3. Send the Player Type to the Server.
* Disable the "Roll Dice" button after the button is clicked by destroying the button.
~~~python
def roll_dice():
    ...
    ...
    player_turn = False
    roll_button.destroy()


~~~
4. Send the Message to all the Players.
* Open the files `server.py`.
* Send the message to all the clients by sending the message received from the player.
~~~python
def handle_client(player_socket,player_name):
    global CLIENTS
    player_type =CLIENTS[player_name]["player_type"]
    if(player_type== 'player1'):
        CLIENTS[player_name]['turn'] = True
    else:
        CLIENTS[player_name]['turn'] = False
    player_socket.send(str(
            {'player_type' : CLIENTS[player_name]["player_type"] ,
             'turn': CLIENTS[player_name]['turn'] }).encode())
~~~
5. Store the message from the server.
* Open the files `client.py`.
* Store the message from the server by checking the player type in the message received from the server.
~~~python
def received_msg():
   ...
   ...
   elif('player_type' in message):
         recv_msg = eval(message)
         player_type = recv_msg['player_type']
         player_turn = recv_msg['turn']


~~~
6. Create and Place the “Roll Dice” Button.
* Create and place the roll button by setting the player turn to True if the player turn matches.
~~~python
def received_msg():
        ...
        ...
        if(('player1_turn' in message and player_type == 'player1') or
           ('player2_turn' in message and player_type == 'player2')
            ):
            player_turn = True
            roll_button = Button(game_window,text="Roll Dice", fg='black', font=("Chalkboard SE", int(font_size * 0.5)), bg="grey",command=roll_dice, width=10, height=1)
            roll_button.place(x=(screen_width * 0.5) - font_size*2, y= screen_height * 0.7)


~~~
* Save and run the code to check the output.