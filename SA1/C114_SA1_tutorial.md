Create the Ludo Board
============================


In this activity, you will learn to create the boxes on the board.


<img src= "https://media.slid.es/uploads/1525749/images/10883885/SA1.gif" width = "480" height = "320">


Follow the given steps to complete this activity:


1. Set the box width and position.


* Open the `client.py` file.


* Set the box width and position of the yellow box.
~~~sh
box_width = int(screen_width/50)
xPos = int(screen_width - box_width*2.5)
~~~
2. Create the box.
* Create ten boxes by creating the labels in a loop.
~~~sh
for box in range(0,10):
        if(box == 0):
            box_label = Label(game_window, font=("Helvetica",box_width), width=2, height=1, borderwidth=0, bg="yellow")
        else:
            box_label = Label(game_window, font=("Helvetica",box_width), width=2, height=1, borderwidth=0, bg="white")
~~~
3. Place the box.
* Place the box on the ludo board window.
~~~sh
        box_label.place(x=xPos, y=screen_height/3)
~~~


4. Store the box.
* Store the boxes by appending the label to a list of right boxes.
~~~sh
        right_boxes.append(box_label)
~~~
5. Set the position of the next box.
* Set the position of the next box by multiplying the box width with a number.
~~~sh
        xPos -= box_width*2
~~~


6. Display the finishing box.
* Create and display the finishing box on the board.
~~~sh
finishing_box = Label(game_window, text="Home", font=("Chalkboard SE", box_width), width=10, height=4, borderwidth=0, bg="green", fg="white")
finishing_box.place(x=screen_width/2 - box_width*4, y=screen_height/3 - box_width*2)
~~~
* Save and run the code to check the output.