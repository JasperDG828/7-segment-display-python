# 7 segment display module for python
use this module/these functions to make 7-segment characters

### how to install:
#### OPTION1: using as a module:
First, you'll need to make a decision for your own program: will you use **'t.'** or **'turtle.'** for the turtle-commands.
If you use 't.', download Version 1.0(SSPY1.0.py), if you use 'turtle.', download version 1.1(SSPY1.1.py).

Then, put it in the same directory as your project.

Rename the module to a short name you can use in your code.

Now, import the module in your project with:
```python
import TheNameYouGaveTheModule
```
#### OPTION2: copying the functions
First, you'll need to make a decision for your own program: will you use **'t.'** or **'turtle.'** for the turtle-commands.
If you use 't.', download Version 1.0(SSPY1.0.py), if you use 'turtle.', download version 1.1(SSPY1.1.py).

Then open it and just copy the functions to your own project. Make sure you copied all of them.

### how to use:
first, you can choose the colors and more of the turtle with turtle commands:
```python
t.color('colorOfTheText')
t.bgcolor('backgroundColor')
t.hideturtle()
t.speed(speedYouWant)
```
Then, you can use the different functions to print 7-segment-characters:
#### drawSegments
with this function, you can completely customize the segments with parameters:
 * segments a-g, either True or False
 * size, size of the character
 * thickness, how thick the lines must be

for example:
```python
SSPY.drawSegments(True, False, True, False, True, False, True, 5, 5)
```
becomes:

![Picture 1](https://github-files-jdg.jasperdg.repl.co/SSPY/manualPic1.jpg)

#### drawChar
with this function, you can print preprogrammed characters with parameters:
 * character, a character from A-Z or 0-9
 * size
 * thickness

for example:
```python
SSPY.drawChar('A', 5, 5)
```

becomes:

![Picture 2](https://github-files-jdg.jasperdg.repl.co/SSPY/manualPic2.jpg)

#### drawString
with this function, you can print strings:
 * string
 * size
 * thickness
 * spacing
 
for example:

```python
SSPY.drawString('I LIKE PYTHON', 3, 3, 10)
```

becomes:


![Picture 3](https://github-files-jdg.jasperdg.repl.co/SSPY/manualPic3.jpg)

> SSPY by Jasper De Gussemé

> Questions: contact.jdgbe@yahoo.com
