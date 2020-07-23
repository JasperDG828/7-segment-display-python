#7-segment display in python(SSPY)V1.0 By Jasper De Gussemé
#Check The GitHub-page for more info:
#https://github.com/JasperDG828/7-segment-display-python
#
#index:
#DrawSegments: Ln 10
#drawChar: Ln 50
#drawString: Ln 130
#----------------------------------------------------------------------------------------#
#drawSegments:
def drawSegments(a, b, c, d, e, f, g, size, thickness):
    turtle.width(thickness)
    turtle.pu()
    if d==True:
        turtle.pd()
    turtle.setheading(180)
    turtle.fd(10 * size)
    turtle.pu()
    turtle.setheading(90)
    if e==True:
        turtle.pd()
    turtle.fd(10 * size)
    turtle.pu()
    if f==True:
        turtle.pd()
    turtle.fd(10 * size)
    turtle.pu()
    turtle.setheading(0)
    if a==True:
        turtle.pd()
    turtle.fd(10 * size)
    turtle.pu()
    turtle.setheading(270)
    if b==True:
        turtle.pd()
    turtle.fd(10 * size)
    turtle.pu()
    turtle.setheading(180)
    if g==True:
        turtle.pd()
    turtle.fd(10 * size)
    turtle.pu()
    turtle.bk(10 * size)
    turtle.setheading(270)
    if c==True:
        turtle.pd()
    turtle.fd(10 * size)
    turtle.pu()
#----------------------------------------------------------------------------------------#
#drawChar:
    def drawChar(char, size, thickness):
    char = char.upper()
    if char==' ':
        drawSegments(False, False, False, False, False, False, False, size, thickness)
    elif char=='A':
        drawSegments(True, True, True, False, True, True, True, size, thickness)
    elif char=='B':
        drawSegments(False, False, True, True, True, True, True, size, thickness)
    elif char=='C':
        drawSegments(True, False, False, True, True, True, False, size, thickness)
    elif char=='D':
        drawSegments(False, True, True, True, True, False, True, size, thickness)
    elif char=='E':
        drawSegments(True, False, False, True, True, True, True, size, thickness)
    elif char=='F':
        drawSegments(True, False, False, False, True, True, True, size, thickness)
    elif char=='G':
        drawSegments(True, False, True, True, True, True, False, size, thickness)
    elif char=='H':
        drawSegments(False, False, True, False, True, True, True, size, thickness)
    elif char=='I':
        drawSegments(False, False, False, False, True, True, False, size, thickness)
    elif char=='J':
        drawSegments(False, True, True, True, True, False, False, size, thickness)
    elif char=='K':
        drawSegments(True, False, True, False, True, True, True, size, thickness)
    elif char=='L':
        drawSegments(False, False, False, True, True, True, False, size, thickness)
    elif char=='M':
        drawSegments(True, False, True, False, True, False, False, size, thickness)
    elif char=='N':
        drawSegments(True, True, True, False, True, True, False, size, thickness)
    elif char=='O':
        drawSegments(True, True, True, True, True, True, False, size, thickness)
    elif char=='P':
        drawSegments(True, True, False, False, True, True, True, size, thickness)
    elif char=='Q':
        drawSegments(True, True, True, False, False, True, True, size, thickness)
    elif char=='R':
        drawSegments(True, False, False, False, True, True, False, size, thickness)
    elif char=='S':
        drawSegments(True, False, True, True, False, True, True, size, thickness)
    elif char=='T':
        drawSegments(False, False, False, True, True, True, True, size, thickness)
    elif char=='U':
        drawSegments(False, True, True, True, True, True, False, size, thickness)
    elif char=='V':
        drawSegments(False, True, True, True, False, True, False, size, thickness)
    elif char=='W':
        drawSegments(False, True, False, True, False, True, False, size, thickness)
    elif char=='X':
        drawSegments(False, True, True, False, True, True, True, size, thickness)
    elif char=='Y':
        drawSegments(False, True, True, True, False, True, True, size, thickness)
    elif char=='Z':
        drawSegments(True, True, False, True, False, False, True, size, thickness)
    elif char=='0':
        drawSegments(True, True, True, True, True, True, False, size, thickness)
    elif char=='1':
        drawSegments(False, True, True, False, False, False, False, size, thickness)
    elif char=='2':
        drawSegments(True, True, False, True, True, False, True, size, thickness)
    elif char=='3':
        drawSegments(True, True, True, True, False, False, True, size, thickness)
    elif char=='4':
        drawSegments(False, True, True, False, False, True, True, size, thickness)
    elif char=='5':
        drawSegments(True, False, True, True, False, True, True, size, thickness)
    elif char=='6':
        drawSegments(True, False, True, True, True, True, True, size, thickness)
    elif char=='7':
        drawSegments(True, True, True, False, False, False, False, size, thickness)
    elif char=='8':
        drawSegments(True, True, True, True, True, True, True, size, thickness)
    elif char=='9':
        drawSegments(True, True, True, True, False, True, True, size, thickness)
    else:
        print('ERROR: Not able to print ' + str(char))
#----------------------------------------------------------------------------------------#
#drawString:
def drawString(string, size, thickness, spacing):
    i = 0
    while i < len(str(string)):
        turtle.pu()
        turtle.home()
        turtle.setheading(0)
        turtle.fd(300)
        turtle.setheading(180)
        turtle.fd((10*i)+((spacing*size)*i))
        pos = len(str(string)) - (i+1)
        drawChar(str(string[pos]), size, thickness)
        i = i+1
#----------------------------------------------------------------------------------------#
