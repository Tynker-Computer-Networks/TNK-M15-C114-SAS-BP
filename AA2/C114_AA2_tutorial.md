Use Two Dice
==============




In this activity, you will learn to add another die to play the game.




<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10902566/pasted-from-clipboard.png" width = "480" height = "150">


Follow the given steps to complete this activity:
1. Create another die label on the canvas.
* Open the file `client.py`.
~~~python
def game():
. . .
dice2 = canvas2.create_text(screen_width * 0.5, screen_height * 0.7, text = "\u2680", font=("Chalkboard SE",font_size * 2), fill="white")
~~~
2. Send the Randomly Chosen Value of both the dice to the Server.
~~~python
def roll_dice():
	value2 = random.choice(dice_choices)
	if(player_type == 'player1'):
        SERVER.send(f'{value}player2_turn dice1'.encode())
        SERVER.send(f'{value2}player2_turn dice2'.encode())


    if(player_type == 'player2'):
        SERVER.send(f'{value}player1_turn dice1'.encode())
        SERVER.send(f'{value2}player1_turn dice2'.encode())
~~~
3. Display the Die.
* Display the values of both the dice on the canvas by checking the message from the server.
~~~python
def received_msg():
	. . . 
	while True:
	. . . 
	if('dice1' in message): 
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
        else:
            if('\u2680' in message):
                canvas2.itemconfigure(dice2, text='\u2680')
            elif('\u2681' in message):
                canvas2.itemconfigure(dice2, text='\u2681')
            elif('\u2682' in message):
                canvas2.itemconfigure(dice2, text='\u2682')  
            elif('\u2683' in message):
                canvas2.itemconfigure(dice2, text='\u2683')
            elif('\u2684' in message):
                canvas2.itemconfigure(dice2, text='\u2684')
            elif('\u2685' in message):
                canvas2.itemconfigure(dice2, text='\u2685')


~~~
* Save and run the code to check the output.