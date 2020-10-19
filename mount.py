import turtle
import math
import random
from random import randint

def draw_background():
    #create screen object
    screen = turtle.Screen()

    #dimentions for the screen
    screen.setup(1200,700)

    #background color
    screen.bgcolor('#b3d9ff')

    #create new turtle
    turtle.hideturtle()
    turtle.speed(10000)
    turtle.pensize(2)
    turtle.color('black')

    #parameters for mountain
    MAX_SLOPE = 45
    MIN_SLOPE = -40
    MIN_HEIGHT = 0

    def dist_squared(P1,P2):
        return (P1[0]-P2[0])**2 + (P1[1]-P2[1])**2

    #funtion for drawing mountain
    #if you dont need it delete it
    def mountain(P1,P2):
        if dist_squared(P1,P2) < 9:
            turtle.goto(P2)
            return
        x1,y1 = P1
        x2,y2 = P2
        x3 = random.uniform(x1,x2)
        y3_max = min((x3-x1)*math.tan(math.radians(MAX_SLOPE)) + y1, (x2-x3)*math.tan(-math.radians(MIN_SLOPE)) + y2)
        y3_min = max((x3-x1)*math.tan(math.radians(MIN_SLOPE)) + y1, (x2-x3)*math.tan(-math.radians(MAX_SLOPE)) + y2)
        y3_min = max(y3_min, MIN_HEIGHT)
        y3 = random.uniform(y3_min,y3_max)
        P3 = (x3, y3)
        mountain(P1,P3)
        mountain(P3,P2)
        return
    #function for drawing stars
    #if you dont need delete it
    def drawstar():
        turns=5
        turtle.begin_fill()
        while turns>0:
            turtle.forward(25)
            turtle.left(145)
            turns=turns-1
        turtle.end_fill()

    #if you dont need the mountain delete this too
    turtle.up()
    turtle.goto(-600,MIN_HEIGHT)
    turtle.down()
    mountain((-600,MIN_HEIGHT),(600,MIN_HEIGHT))

    #if you dont need the stars delete this too
    num_stars=0
    while num_stars<20:
        xt=randint(-600,600)
        yt=randint(150,390)
        drawstar()
        turtle.penup()
        turtle.goto(xt,yt)
        turtle.pendown()
        num_stars=num_stars+1


    #screen.exitonclick()


    def clouds(screen):  
        # function for movement of an object  
        def moving_object(obj):
            #obj= turtle.Turtle()
            #turtle.bgcolor('lightblue')
            obj.fillcolor('white')  

            #begin filling the object
            obj.begin_fill() 
            obj.speed(1000000)
            obj.left(90)
            
            #use 6 arcs of circle to create a cloud
            #following show those six
            for x in range (1,9):
              obj.left(10)
              obj.forward(2+0.3*x)
            obj.left(280)

            for y in range (1,18):
              obj.left(10)
              t=y
              if y>=10:
                t=19-y
              obj.forward(2+0.1*t)

            obj.left(280)
            for z in range (1,9):
              obj.left(10)
              obj.forward(4.7-0.3*z)

            obj.left(100)
            obj.left(270)
            for x in range (1,9):
              obj.left(10)
              obj.forward(2+0.3*x)
            obj.left(280)

            for y in range (1,18):
              obj.left(10)
              t=y
              if y>=10:
                t=19-y
              obj.forward(2+0.1*t)

            obj.left(280)
            for z in range (1,9):
              obj.left(10)
              obj.forward(4.7-0.3*z)

            obj.left(100)
            obj.left(180)
            obj.end_fill()
          

        # screen updaion  
        screen.tracer(0)            

        # create a turtle object object 
        move = turtle.Turtle()  
        move1=turtle.Turtle()
        move2= turtle.Turtle()  
        move3=turtle.Turtle()
        move4 = turtle.Turtle()  

        # set a turtle object color 
        move.color('white') 
        move1.color('white') 
        move2.color('white') 
        move3.color('white') 
        move4.color('white') 

        # set turtle object speed 
        #move.speed(0)  

        # set turtle object width 
        move.width(2) 
        move1.width(2)       

        # hide turtle object 
        move.hideturtle()           

        # turtle object in air 
        move.penup() 
        move1.penup()

        #generate random number for use for parameters of the clouds 
        c=randint(100,340)
        c1=randint(100,340)
        c2=randint(100,340)
        c3=randint(100,340)
        c4=randint(100,340)              

        # set initial position for 5 cloud with random possition
        move.goto(-600, c) 
        move1.goto(-800, c1)
        move2.goto(-1000, c2)
        move3.goto(200, c3)
        move4.goto(-300, c4)  

        #set moving speed for the clouds using random number
        m=((c/800.0)+.2)
        m1=((c1/800.0)+.2)
        m2=((c2/800)+.2)
        m3=((c3/800)+.2)
        m4=((c4/800)+.2)
        # move turtle object to surface 
        move.pendown()              
        move1.pendown()
        move2.pendown()
        move3.pendown()
        move4.pendown()
        #initialize a parameter to loop the clouds
        b=0
        b1=0
        b2=0
        b3=0
        b4=0

        # infinite loop
        while True : 
              
            # clear turtle work 
            move.clear()
            move1.clear() 
            move2.clear()
            move3.clear()
            move4.clear()

              
            # call function to draw ball 
            moving_object(move)
            moving_object(move1)
            moving_object(move2)
            moving_object(move3)
            moving_object(move4)

            # update screen 
            screen.update()     
              
            # forward motion by turtle object 
            move.forward(m)
            move1.forward(m1)
            move2.forward(m2)
            move3.forward(m3)
            move4.forward(m4) 

            #increment the finfing criteria
            b=b+1
            b1=b1+1
            b2=b2+1
            b3=b3+1
            b4=b4+1

            #fimdimg wether coloud gone out if gone out again bring back randomly
            if b*m>=1500:
                c=randint(0,375)
                b=0
                m=((c/800)+.2)
                move.goto(-620,c)
            if b1*m1>=1600:
                c1=randint(0,375)
                b1=0
                m1=((c1/800)+.2)
                move1.goto(-600-c1,c1)
            if b2*m2>=1600:
                c2=randint(0,375)
                b2=0
                m2=((c2/800)+.2)
                move2.goto(-600-c2,c2)
            if b3*m3>=1600:
                c3=randint(0,375)
                b3=0
                m3=((c3/800)+.2)
                move3.goto(-600-c3,c3)
            if b4*m4>=1600:
                c4=randint(0,375)
                b4=0
                m4=((c4/800)+.2)
                move4.goto(-600-c4,c4)

    clouds(screen)

#for drawing rectangle
def draw_rectangle(length,width):
    #t = turtle.Turtle()
    #t.hideturtle()
    
    t.fillcolor('black')
    t.begin_fill() 
    for _ in range(4):
       
      # drawing length

      if _% 2 == 0:
        t.forward(length) # Forward turtle by l units
        t.left(90) # Turn turtle by 90 degree
     
      # drawing width
      else:
        t.forward(width) # Forward turtle by w units
        t.left(90) # Turn turtle by 90 degree
    t.end_fill()

#create new turtle for drawing buildings 
t = turtle.Turtle()
t.color("#b3d9ff")
t.hideturtle()

#go to the cordinate 0,-350 (the midle of the bottom of the screen)
t.goto(-0,-350)
#going to the -250 of the bottom line to draw the first rectangle
t.goto(-250,-350)
#drawo 230 hight and 20 widgt rectange 
#the corner cordinates of the base of rectangle (-220,-350),(-250,-350)
#upper cordinates  (-220,-120),(-250,-120)
draw_rectangle(30,230)

#draw next rectangle with 40x470 dimention
#cordinates of the base (-220,-350),(-180,-350)
#upper cordinates  (-220,120),(-180,120)
t.goto(-220,-350)
draw_rectangle(40,470)

#Drawing rectangle with dimention 60x400
#cordinates of the base (-120,-350),(-180,-350)
#upper cordinates  (-180,50),(-120,50)
t.goto(-180,-350)
draw_rectangle(60,400)

#Drawing rectangle with dimention 60x190
#cordinates of the base (-120,-350),(-60,-350)
#upper cordinates  (-120,-160),(-60,-160)
t.goto(-120,-350)
draw_rectangle(60,190)
#draw the conical shaape at the top of rectangle
t.goto(-120,-160)
t.begin_fill() 
t.goto(-90,-130)
t.goto(-60,-160)
t.end_fill()

#Drawing rectangle with dimention 60x320
#cordinates of the base (-60,-350),(0,-350)
#upper cordinates  (-60,-30),(0,-30)
t.goto(-60,-350)
draw_rectangle(60,320)

#draw the conical shape at the top
t.goto(-60,-30)
t.begin_fill() 
t.goto(-30,0)
t.goto(0,-30)
t.end_fill()

#Drawing rectangle with dimention 70x370
#cordinates of the base (20,-350),(90,-350)
#upper cordinates  (20,20),(90,20)
t.goto(20,-350)
draw_rectangle(70,370)

#the bas of the building is (120,-350),(170,-350)
#the uppper cordinates are (130,-50),(160,-50)
t.goto(120,-350)
t.begin_fill() 
t.goto(130,-50)
t.goto(160,-50)
t.goto(170,-350)
t.end_fill()

#dra the pattern of the building
t.goto(120,-350)
t.color("white")
t.goto(168,-290)
t.goto(124,-230)
t.goto(164,-170)
t.goto(128,-110)
t.goto(160,-50)
t.color("#b3d9ff")
t.goto(170,-350)
t.color("white")
t.goto(122,-290)
t.goto(166,-230)
t.goto(126,-170)
t.goto(162,-110)
t.goto(130,-50)
t.color("#b3d9ff")
t.goto(135,0)
t.color("black")
t.goto(135,-50)
t.goto(155,-50)
t.goto(155,0)

t.color("")

draw_background()