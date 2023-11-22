Modify the Board Design
=================




In this activity, you will learn to Create an L-shaped board by adding a few more boxes.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10902559/pasted-from-clipboard.png" width = "480" height = "150">


Follow the given steps to complete this activity:
	
1. Set the Vertical Position of the Box.


* Open the file `client.py`.


* Initialize the `ypos` in the left and right board functions.
~~~python
def left_board():
	yPos = box_width
def right_board():
yPos = box_width
~~~
2. Create 15 boxes on each side.
* Create 5 boxes vertically then 10 boxes horizontally
~~~python
def left_board():
	. . .
    for box in range(0,15):
	. . .
box_label.place(x=xPos, y=yPos)
left_boxes.append(box_label)
if box<5:
         yPos +=box_width*2
      else:
         xPos += box_width*2


def right_board():
	. . .
    for box in range(0,15):
	. . .
	box_label.place(x=xPos, y=yPos)        
      right_boxes.append(box_label)
      if box<5:
          yPos +=box_width*2 
      else:
          xPos -= box_width*2
~~~
* Save and run the code to check the output.