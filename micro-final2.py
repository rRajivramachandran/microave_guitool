from Tkinter import *

import tkMessageBox
import tkSimpleDialog
import cmath
import math
import turtle
import copy
import numpy as np
A=[]
c=0
At=[]
Bt=[]
voltcur=[]
x=-500
y=250

root=Tk()
canvas = Canvas(master = root, width = 1300, height = 800)
canvas.grid(row=13,column=0)
turtle1_screen = turtle.TurtleScreen(canvas)
turtle1_screen.bgcolor("black")
turtle1 = turtle.RawTurtle(turtle1_screen)
turtle1.hideturtle()
def complexmul(A,B,C,D):
    return [A*C-B*D,B*C+A*D]
def complexmatmul2(a,b):
    c=[[[]],[[]]]
    for i in range(2):
        s=[0,0]
        for k in range(2):
            s[0]+=complexmul(a[i][k][0],a[i][k][1],b[k][0][0],b[k][0][1])[0]
            s[1]+=complexmul(a[i][k][0],a[i][k][1],b[k][0][0],b[k][0][1])[1]
        c[i][0]=s
    return c
def complexmatmul(a,b):
    c=[[[],[]],[[],[]]]
    for i in range(2):
        for j in range(2):
            sum1=[0,0]
            for k in range (2):
                sum1[0]+=complexmul(a[i][k][0],a[i][k][1],b[k][j][0],b[k][j][1])[0]
                sum1[1]+=complexmul(a[i][k][0],a[i][k][1],b[k][j][0],b[k][j][1])[1]
                c[i][j]=sum1
    return c


def drawval((x,y),voltage,current,colour):
   v="V="+str(voltage)
   i="I="+str(current)
   turtle1.pencolor(colour) 
   turtle1.penup()
   turtle1.goto(x-10,y+50)  
   turtle1.pendown()
   turtle1.begin_fill()
   turtle1.write(v, font=("Arial", 8, "normal"))
   turtle1.pencolor(colour) 
   turtle1.penup()
   turtle1.goto(x-10,y+25)  
   turtle1.pendown()
   turtle1.begin_fill()
   turtle1.write(i, font=("Arial", 8, "normal"))
   turtle1.penup()

def printvals(calculations,colour):
   tempx=-500
   for i in range(0,len(calculations)/2):
        drawval((tempx,y),calculations[2*i],calculations[2*i+1],colour)
        tempx=tempx+150


def inverseMat(ABCD):
    ABCDinv=[[[1,1],[1,1]],[[1,1],[1,1]]]
    A=ABCD[0][0][0]+1j*ABCD[0][0][1]
    B=ABCD[0][1][0]+1j*ABCD[0][1][1]
    C=ABCD[1][0][0]+1j*ABCD[1][0][1]
    D=ABCD[1][1][0]+1j*ABCD[1][1][1]

    det=A*D-B*C

    Ainv=D/det
    Binv=-B/det
    Cinv=-C/det
    Dinv=A/det

    ABCDinv[0][0][0]=np.real(Ainv)
    ABCDinv[0][1][0]=np.real(Binv)
    ABCDinv[1][0][0]=np.real(Cinv)
    ABCDinv[1][1][0]=np.real(Dinv)

    ABCDinv[0][0][1]=np.imag(Ainv)
    ABCDinv[0][1][1]=np.imag(Binv)
    ABCDinv[1][0][1]=np.imag(Cinv)
    ABCDinv[1][1][1]=np.imag(Dinv)
    return ABCDinv

def drawPolyLine(start, end, lineColour="white", fillColour="white"):
    
    turtle1.pencolor(lineColour)
    #turtle1.fillcolor(fillColour)

    turtle1.penup()

    turtle1.goto(start)  

    turtle1.pendown()
    turtle1.begin_fill()

    turtle1.goto(end)
    turtle1.goto(start) 

    turtle1.end_fill()
    turtle1.penup()


def drawlambda(centre, lineColour="red", fillColour="white"):
   
    turtle1.pencolor(lineColour)
    #turtle1.fillcolor(fillColour)

    x,y=centre;
    turtle1.penup()
    turtle1.goto(x-50,y-60)  
    turtle1.pendown()
    turtle1.begin_fill()
    turtle1.goto(x+50,y-60)
    turtle1.penup()
    turtle1.goto(x-50,y)  
    turtle1.pendown()
    turtle1.begin_fill()
    turtle1.goto(x+50,y)  

    turtle1.penup()
    turtle1.goto(x-20,y-10)  
    turtle1.pendown()
    turtle1.begin_fill()
    turtle1.goto(x,y-30)
    turtle1.penup()
    turtle1.goto(x-10,y-20)  
    turtle1.pendown()
    turtle1.goto(x-20,y-30) 

    turtle1.penup()
    turtle1.goto(x+20,y-10)
    turtle1.pendown()
    turtle1.goto(x,y-40) 
    turtle1.end_fill()
    turtle1.penup()

    A=[]
    A.append((x-50,y))
    A.append((x-50,y-60))
    A.append((x+50,y))
    A.append((x+50,y-60))
    return A

def draw4(centre, lineColour="red", fillColour="white"):
   
    turtle1.pencolor(lineColour)
    #turtle1.fillcolor(fillColour)
    x,y=centre;
    turtle1.penup()
    turtle1.goto(x+20,y-40)  
    turtle1.pendown()
    turtle1.begin_fill()
    turtle1.write("4", font=("Arial", 16, "normal"))
    turtle1.end_fill()
    turtle1.penup()

def draw8(centre, lineColour="red", fillColour="white"):
   
    turtle1.pencolor(lineColour)
    #turtle1.fillcolor(fillColour)
    x,y=centre;
    turtle1.penup()
    turtle1.goto(x+20,y-40)  
    turtle1.pendown()
    turtle1.begin_fill()
    turtle1.write("8", font=("Arial", 16, "normal"))
    turtle1.end_fill()
    turtle1.penup()

def drawsquare(centre, lineColour="red", fillColour="white"):
   
    turtle1.pencolor(lineColour)
    #turtle1.fillcolor(fillColour)

    turtle1.penup()

    x,y=centre;
    turtle1.goto(x-20,y-20)  
    turtle1.pendown()
    turtle1.begin_fill()

    turtle1.goto(x-20,y+20)
    turtle1.goto(x+20,y+20)
    turtle1.goto(x+20,y-20)
    turtle1.goto(x-20,y-20)  

    turtle1.end_fill()
    turtle1.penup()

def drawz(centre, lineColour="red", fillColour="white"):
    
    drawsquare(centre)
    turtle1.pencolor(lineColour)
    #turtle1.fillcolor(fillColour)

    turtle1.penup()

    x,y=centre
    turtle1.goto(x-10,y+10)  

    turtle1.pendown()
    turtle1.begin_fill()

    turtle1.goto(x+10,y+10)
    turtle1.goto(x-10,y-10)
    turtle1.goto(x+10,y-10)  

    turtle1.end_fill()
    turtle1.penup()

def drawCoupler(turtle2,centre, lineColour="red", fillColour="white"):
    
    turtle2.pencolor(lineColour)
    #turtle1.fillcolor(fillColour)
    turtle2.penup()

    x,y=centre
    turtle2.goto(x-40,y-40)  
    turtle2.pendown()
    turtle2.begin_fill()

    turtle2.goto(x-40,y+40)
    turtle2.goto(x+40,y+40)
    turtle2.goto(x+40,y-40)
    turtle2.goto(x-40,y-40)

    turtle2.pencolor("white")
    turtle2.penup() 
    turtle2.goto(x-40,y-30)
    turtle2.pendown()
    turtle2.goto(x-70,y-30)
    turtle2.penup()  
    turtle2.goto(x+40,y-30)
    turtle2.pendown()
    turtle2.goto(x+70,y-30)
    turtle2.penup() 
    turtle2.goto(x-40,y+30)
    turtle2.pendown()
    turtle2.goto(x-70,y+30)
    turtle2.penup()  
    turtle2.goto(x+40,y+30)
    turtle2.pendown()
    turtle2.goto(x+70,y+30)
    turtle2.penup()
    turtle2.pencolor("white")
    turtle2.penup() 
    turtle2.goto(x-40,y-20)
    turtle2.pendown()
    turtle2.goto(x-70,y-20)
    turtle2.penup()  
    turtle2.goto(x+40,y-20)
    turtle2.pendown()
    turtle2.goto(x+70,y-20)
    turtle2.penup() 
    turtle2.goto(x-40,y+20)
    turtle2.pendown()
    turtle2.goto(x-70,y+20)
    turtle2.penup()  
    turtle2.goto(x+40,y+20)
    turtle2.pendown()
    turtle2.goto(x+70,y+20)
    turtle2.penup()
    turtle2.end_fill()

def drawABCD(centre, lineColour="red", fillColour="white"):
    
    turtle1.pencolor(lineColour)
    #turtle1.fillcolor(fillColour)
    turtle1.penup()

    x,y=centre
    turtle1.goto(x-40,y-40)  
    turtle1.pendown()
    turtle1.begin_fill()

    turtle1.goto(x-40,y+40)
    turtle1.goto(x+40,y+40)
    turtle1.goto(x+40,y-40)
    turtle1.goto(x-40,y-40)

    turtle1.penup()

    turtle1.goto(x-30,y-10)  

    turtle1.pendown()
    turtle1.begin_fill()

    turtle1.write("ABCD", font=("Arial", 16, "normal"))
    turtle1.pencolor("white")
    turtle1.penup() 
    turtle1.goto(x-40,y-30)
    turtle1.pendown()
    turtle1.goto(x-50,y-30)
    turtle1.penup()  
    turtle1.goto(x+40,y-30)
    turtle1.pendown()
    turtle1.goto(x+50,y-30)
    turtle1.penup() 
    turtle1.goto(x-40,y+30)
    turtle1.pendown()
    turtle1.goto(x-50,y+30)
    turtle1.penup()  
    turtle1.goto(x+40,y+30)
    turtle1.pendown()
    turtle1.goto(x+50,y+30)
    turtle1.penup()
    turtle1.end_fill()
    return calABCD((x,y))

def calABCD((x,y)):
   A=[]
   A.append((x-50,y+30))
   A.append((x-50,y-30))
   A.append((x+50,y+30))
   A.append((x+50,y-30))

   return A

def drawk(centre, lineColour="red", fillColour="white"):
  
    drawsquare(centre)
    turtle1.pencolor(lineColour)
    #turtle1.fillcolor(fillColour)

    turtle1.penup()

    x,y=centre
    turtle1.goto(x-5,y+10)  
    turtle1.pendown()
    turtle1.begin_fill()

    turtle1.goto(x-5,y-10)
    turtle1.penup()
    turtle1.goto(x-5,y)
    turtle1.pendown()
    turtle1.goto(x+10,y-10)
    turtle1.penup()
    turtle1.goto(x-5,y)
    turtle1.pendown()
    turtle1.goto(x+10,y+10) 

    turtle1.end_fill()
    turtle1.penup()

def drawj(centre, lineColour="red", fillColour="white"):
    
    drawsquare(centre)
    turtle1.pencolor(lineColour)
    #turtle1.fillcolor(fillColour)

    turtle1.penup()

    x,y=centre
    turtle1.goto(x-10,y+10)  
    turtle1.pendown()
    turtle1.begin_fill()

    turtle1.goto(x+10,y+10)
    turtle1.penup()
    turtle1.goto(x,y+10)
    turtle1.pendown()
    turtle1.goto(x,y-10)
    turtle1.goto(x-5,y-5) 

    turtle1.end_fill()
    turtle1.penup()
    #drawhoriz(centre)

def drawhoriz((x,y), lineColour="black", fillColour="white"):

    drawPolyLine((x-30,y),(x-20,y))
    drawPolyLine((x+30,y),(x+20,y))
    return calhoriz((x,y))

def drawlines((x,y), lineColour="black", fillColour="white"):

    drawPolyLine((x-30,y+10),(x-20,y+10))
    drawPolyLine((x-30,y-10),(x-20,y-10))
    drawPolyLine((x+30,y+10),(x+20,y+10))
    drawPolyLine((x+30,y-10),(x+20,y-10))
    return callines((x,y))

def calhoriz((x,y)):
   A=[]
   A.append((x-30,y))
   A.append((x+30,y))
   A.append((0,0))

   return A

def callines((x,y)):
   A=[]
   A.append((x-30,y+10))
   A.append((x-30,y-10))
   A.append((x+30,y+10))
   A.append((x+30,y-10))

   return A


def drawverti((x,y), lineColour="black", fillColour="white"):

    drawPolyLine((x,y-30),(x,y-20))
    drawPolyLine((x,y+30),(x,y+20))
    return calverti((x,y))

def calverti((x,y)):
   A=[]
   A.append((x,y+30))
   A.append((x,y-30))
   return A

def drawy(centre, lineColour="red", fillColour="white"):
    
    drawsquare(centre)
    turtle1.pencolor(lineColour)
    #turtle1.fillcolor(fillColour)

    turtle1.penup()

    x,y=centre
    turtle1.goto(x-10,y+10) 
    turtle1.pendown()
    turtle1.begin_fill()

    turtle1.goto(x,y)
    turtle1.goto(x+10,y+10)
    turtle1.penup()
    turtle1.goto(x,y)
    turtle1.pendown()
    turtle1.goto(x,y-10)  

    turtle1.end_fill()
    turtle1.penup()

def drawt(centre, lineColour="red", fillColour="white"):
   x,y=centre
   drawz((x-45,y))
   drawPolyLine((x-25,y),(x,y))
   drawPolyLine((x-65,y),(x-75,y))
   drawz((x+45,y))
   drawPolyLine((x+25,y),(x,y))
   drawPolyLine((x+65,y),(x+75,y))
   drawz((x,y-60))
   drawPolyLine((x,y-40),(x,y))
   drawPolyLine((x-20,y-60),(x-75,y-60))
   drawPolyLine((x+20,y-60),(x+75,y-60))
   return calt(centre)

def calt((x,y)):
   A=[]
   A.append((x-75,y))
   A.append((x-75,y-60))
   A.append((x+75,y))
   A.append((x+75,y-60))
   return A

def drawpi(centre, lineColour="red", fillColour="white"):
   x,y=centre
   drawsquare((x-45,y))
   drawz((x-45,y))
   drawPolyLine((x-45,y-45),(x-45,y-20))
   drawPolyLine((x-45,y+45),(x-45,y+20))
   drawsquare((x+45,y))
   drawz((x+45,y))
   drawPolyLine((x+45,y-45),(x+45,y-20))
   drawPolyLine((x+45,y+45),(x+45,y+20))
   drawsquare((x,y+45))
   drawz((x,y+45))
   drawPolyLine((x-20,y+45),(x-75,y+45))
   drawPolyLine((x+20,y+45),(x+75,y+45))
   drawPolyLine((x-75,y-45),(x+75,y-45))
   return calpi(centre)

def calpi((x,y)):
   A=[]
   A.append((x-75,y+45))
   A.append((x-75,y-45))
   A.append((x+75,y+45))
   A.append((x+75,y-45))
   return A
 
class MyDialogvoltages:
     
   
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Enter value of input voltage").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)
        Label(top, text="Enter the value of input current").pack()

        self.f = Entry(top)
        self.f.pack(padx=5)
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global voltcur
        printvals(voltcur,"black")
        voltcur=[]
        sourcevolt=complex(self.e.get())
        sourcecur=complex(self.f.get())
        prev=[[[sourcevolt.real,sourcevolt.imag]],[[sourcecur.real,sourcecur.imag]]]
        for i in ab:
            next=complexmatmul2(inverseMat(i),prev)
            prev=next
            voltcur.append(complex(round(prev[0][0][0],4),round(prev[0][0][1],4)))
            voltcur.append(complex(round(prev[1][0][0],4),round(prev[1][0][1],4)))
        self.top.destroy()
        printvals(voltcur,"green")
        



class MyDialoglamdaby8:
     
   
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Enter value of zo(a+jb format)").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)
        
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global x,y,At,Bt
        z=complex(self.e.get())
        a=math.cos(math.pi/4)
        b=1j*z*math.sin(math.pi/4)
        c=1j*math.sin(math.pi/4)/z
        d=math.cos(math.pi/4)
        self.top.destroy()
        Bt=drawlambda((x,y))
        draw8((x,y))
        print Bt
        x=x+150
        atl=len(At)
        print atl
        if atl!=0:
         if atl==3:
           drawPolyLine(At[atl-2],Bt[0])
           if At[atl-1]!=(0,0):
            drawPolyLine(At[atl-1],Bt[1])
         else: 
           drawPolyLine(At[atl-2],Bt[0])
           drawPolyLine(At[atl-1],Bt[1])
        At=Bt
        print At
        ab.append([[[a.real,a.imag],[b.real,b.imag]],[[c.real,c.imag],[d.real,d.imag]]])
        #print "value is", self.e.get(),self.f.get(),self.g.get()
class MyDialogT:
    
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Z1(a+jb format)").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)
        Label(top, text="Z2").pack()

        self.f = Entry(top)
        self.f.pack(padx=5)
        Label(top, text="Z3").pack()

        self.g = Entry(top)
        self.g.pack(padx=5)
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global x,y,At,Bt
        z1=complex(self.e.get())
        z2=complex(self.f.get())
        z3=complex(self.g.get())
        a=1+z1/z2
        b=z1+z2+(z1*z2)/z3
        c=1/z3
        d=1+z2/z3
        self.top.destroy() 
        Bt=drawt((x,y))
        print Bt
        x=x+150
        atl=len(At)
        print atl
        if atl!=0:
         if atl==3:
           drawPolyLine(At[atl-2],Bt[0])
           if At[atl-1]!=(0,0):
            drawPolyLine(At[atl-1],Bt[1])
         else: 
           drawPolyLine(At[atl-2],Bt[0])
           drawPolyLine(At[atl-1],Bt[1])
        At=Bt
        print At
        ab.append([[[a.real,a.imag],[b.real,b.imag]],[[c.real,c.imag],[d.real,d.imag]]])
   
class MyDialogLineAdmittance:
     
   
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        Label(top, text="Enter Z in (a+jb) format").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global At,Bt,x,y
        a=[[[1,0],[0,0]],[[complex(self.e.get()).real,complex(self.e.get()).imag],[1,0]]] 
        ab.append(a)
        #print "value is", self.e.get(),self.f.get()
        self.top.destroy()
        drawy((x,y-30))
        Bt=drawverti((x,y-30))
        x=x+150
        atl=len(At)
        print atl
        if atl!=0:
         if atl==3:
           drawPolyLine(At[atl-2],Bt[0])
           if At[atl-1]!=(0,0):
            drawPolyLine(At[atl-1],Bt[1])
         else: 
           drawPolyLine(At[atl-2],Bt[0])
           drawPolyLine(At[atl-1],Bt[1])
        At=Bt
        print At
class MyDialogLineImpedance:
     
    def __init__(self, parent):
        top = self.top = Toplevel(parent)
        Label(top, text="Enter Z in (a+jb) format").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global x,y,At,Bt
        a=[[[1,0],[complex(self.e.get()).real,complex(self.e.get()).imag]],[[0,0],[1,0]]] 
        ab.append(a)
        #print "value is", self.e.get(),self.f.get()
        self.top.destroy()
        drawz((x,y))
        Bt=drawhoriz((x,y))
        x=x+150
        atl=len(At)
        print atl
        if atl!=0:
         if atl==3:
           drawPolyLine(At[atl-2],Bt[0])
         else: 
           drawPolyLine(At[atl-2],Bt[0])
        if atl!=0:
         Bt[2]=At[atl-1]
        At[:]=[]
        At.append(Bt[0])
        At.append(Bt[1])
        if atl==0:
         At.append((0,0))
        else:
         At.append(Bt[2])
        print At
class MyDialogABCD:

    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="A (enter in a+jb format)").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)
        Label(top, text="B ").pack()
        self.g = Entry(top)
        self.g.pack(padx=5)
        Label(top, text="C").pack()
        self.i = Entry(top)
        self.i.pack(padx=5)
        Label(top, text="D").pack()
        self.k = Entry(top)
        self.k.pack(padx=5)
      
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global At,Bt,x,y
        a=complex(self.e.get())
        b=complex(self.g.get())
        c=complex(self.i.get())
        d=complex(self.k.get())
        self.top.destroy()
        Bt=drawABCD((x,y-30))
        print Bt
        x=x+150
        atl=len(At)
        print atl
        if atl!=0:
         if atl==3:
           drawPolyLine(At[atl-2],Bt[0])
           if At[atl-1]!=(0,0):
            drawPolyLine(At[atl-1],Bt[1])
         else: 
           drawPolyLine(At[atl-2],Bt[0])
           drawPolyLine(At[atl-1],Bt[1])
        At=Bt
        print At
        ab.append([[[a.real,a.imag],[b.real,b.imag]],[[c.real,c.imag],[d.real,d.imag]]])
        #print "value is", self.e.get(),self.f.get(),self.g.get(),self.h.get(),self.i.get(),self.j.get(),self.k.get(),self.l.get()

class MyDialogPi:

    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="ZA in the (a+jb) format").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)
        Label(top, text="ZB").pack()

        self.f = Entry(top)
        self.f.pack(padx=5)
        Label(top, text="ZC").pack()

        self.g = Entry(top)
        self.g.pack(padx=5)
       
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global At,Bt,x,y
        z1=complex(self.e.get())
        z2=complex(self.f.get())
        z3=complex(self.g.get())
        a=1+z3/z2
        b=z3
        c=(1/z1)+(1/z2)+(z3/z1*z2)
        d=1+z3/z1
        ab.append([[[a.real,a.imag],[b.real,b.imag]],[[c.real,c.imag],[d.real,d.imag]]])
        self.top.destroy() 
        Bt=drawpi((x,y-45))
        print Bt
        x=x+150
        atl=len(At)
        print atl
        if atl!=0:
         if atl==3:
           drawPolyLine(At[atl-2],Bt[0])
           if At[atl-1]!=(0,0):
            drawPolyLine(At[atl-1],Bt[1])
         else: 
           drawPolyLine(At[atl-2],Bt[0])
           drawPolyLine(At[atl-1],Bt[1])
        At=Bt
        print At
def SParameters(ABCD,Z01,Z02): #Z01: Source Impedance  Z02: Load Impedance
    S=[[[],[]],[[],[]]]

    A=ABCD[0][0][0]+1j*ABCD[0][0][1]
    B=ABCD[0][1][0]+1j*ABCD[0][1][1]
    C=ABCD[1][0][0]+1j*ABCD[1][0][1]
    D=ABCD[1][1][0]+1j*ABCD[1][1][1]
    Z1=Z01[0]+1j*Z01[1]
    Z2=Z02[0]+1j*Z02[1]

    denom=A*Z2+B+C*Z1*Z2+D*Z1

    S11=(A*Z2+B-C*np.conj(Z1)*Z2-D*np.conj(Z1))/denom
    S12=(2*(A*D-B*C)*math.sqrt(Z01[0]*Z02[0]))/denom
    S21=(2*math.sqrt(Z01[0]*Z02[0]))/denom
    S22=(-A*np.conj(Z2)+B-C*Z1*np.conj(Z2)+D*Z1)/denom

    S[0][0].append(round(np.real(S11),4))
    S[0][1].append(round(np.real(S12),4))
    S[1][0].append(round(np.real(S21),4))
    S[1][1].append(round(np.real(S22),4))
    
    S[0][0].append(round(np.imag(S11),4))
    S[0][1].append(round(np.imag(S12),4))
    S[1][0].append(round(np.imag(S21),4))
    S[1][1].append(round(np.imag(S22),4))
    

    return S

def returnloss(S):
    RS11=-20*math.log10(math.sqrt(S[0][0][0]**2+S[0][0][1]**2))
    RS22=-20*math.log10(math.sqrt(S[1][1][0]**2+S[1][1][1]**2))
    RS11=round(RS11,4)
    RS22=round(RS22,4)
    return [RS11,RS22]

def insertionloss(S):
    IS12=-20*math.log10(math.sqrt(S[0][1][0]**2+S[0][1][1]**2))
    IS21=-20*math.log10(math.sqrt(S[1][0][0]**2+S[1][0][1]**2))
    IS12=round(IS12,4)
    IS21=round(IS21,4)
    return [IS12,IS21]
              
class MyDialogsl:

    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Source Impedance (enter in a+jb format)").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)
        Label(top, text="Load impedance ").pack()
        self.g = Entry(top)
        self.g.pack(padx=5)

      
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        zs=complex(self.e.get())
        zl=complex(self.g.get())
        c=[[[0,0],[0,0]],[[0,0],[0,0]]]
        if len(ab)==1:
            c=ab[0]
        elif len(ab)==2:
            c=complexmatmul(ab[0],ab[1])
        elif len(ab)!=0:
            c=complexmatmul(ab[0],ab[1])
            for i in range(2,len(ab)):
                c=complexmatmul(c,ab[i])
                
        res=Toplevel(root,background='black')
        res.geometry('1300x1300')
        abcd=Label(res,padx=10,background='black',foreground='#FF59FF',text='\t\t\tresultant ABCD:',font=("Times", 18, "bold"))
        zs=[zs.real,zs.imag]
        zl=[zl.real,zl.imag]
        s=SParameters(c,zs,zl)
        for i in range(2):
         for j in range(2):
            for k in range(2):
               c[i][j][k]=round(c[i][j][k],4)
        as1=str(complex(c[0][0][0]+1j*c[0][0][1]))
        bs=str(complex(c[0][1][0]+1j*c[0][1][1]))
        cs=str(complex(c[1][0][0]+1j*c[1][0][1]))
        ds=str(complex(c[1][1][0]+1j*c[1][1][1]))
        a1=Label(res,padx=10,background='black',text=as1,foreground='red',font=("Times", 15, "bold"))
        a2=Label(res,background='black',text=bs,foreground='red',font=("Times", 15, "bold"))
        a3=Label(res,background='black',text=cs,foreground='red',font=("Times", 15, "bold"))
        a4=Label(res,background='black',text=ds,foreground='red',font=("Times", 15, "bold"))
        
        abcd.grid(row=0,column=0)
        a1.grid(row=1,column=0)
        a2.grid(row=1,column=1)
        a3.grid(row=2,column=0)
        a4.grid(row=2,column=1)
        res.title('results')
        
        s11=str(complex(s[0][0][0]+1j*s[0][0][1]))
        s12=str(complex(s[0][1][0]+1j*s[0][1][1]))
        s21=str(complex(s[1][0][0]+1j*s[1][0][1]))
        s22=str(complex(s[1][1][0]+1j*s[1][1][1]))
        sh=Label(res,padx=20,background='black',foreground='#FF59FF',text=' \t\tS parameters:',font=("Times", 18, "bold"))
        Label(res,background='black',text=s11,foreground='red',font=("Times", 15, "bold")).grid(row=1,column=2)
        Label(res,background='black',text=s12,foreground='red',font=("Times", 15, "bold")).grid(row=1,column=3)
        Label(res,background='black',text=s21,foreground='red',font=("Times", 15, "bold")).grid(row=2,column=2)
        Label(res,background='black',text=s22,foreground='red',font=("Times", 15, "bold")).grid(row=2,column=3)
        i12=insertionloss(s)
        i11=returnloss(s)
        print i11,i12
        Label(res,padx=10,background='black',foreground='#FF59FF',text='\t\tInsertion loss',font=("Times", 18, "bold")).grid(row=5,column=0)
        Label(res,background='black',text='i12 = '+str(i12[0])+'dB',foreground='red',font=("Times", 15, "bold")).grid(row=6,column=0)
        Label(res,background='black',text='i21 = '+str(i12[1])+'dB',foreground='red',font=("Times", 15, "bold")).grid(row=6,column=1)
        Label(res,padx=10,background='black',foreground='#FF59FF',text='\t\tReturn loss',font=("Times", 18, "bold")).grid(row=5,column=2)
        Label(res,background='black',text='r11 = '+str(i11[0])+'dB',foreground='red',font=("Times", 15, "bold")).grid(row=6,column=2)
        Label(res,background='black',text='r22 = '+str(i11[1])+'dB',foreground='red',font=("Times", 15, "bold")).grid(row=6,column=3)
        

        sh.grid(row=0,column=2)

        #res.mainloop()
        #tkMessageBox.geometry('400x400')
        
        #print "value is", self.e.get(),self.f.get(),self.g.get(),self.h.get(),self.i.get(),self.j.get(),self.k.get(),self.l.get()

        self.top.destroy()
class MyDialoglamdaby4:

    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Enter value of zo(a+jb format)").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)
        
        
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global x,y,At,Bt
        z=complex(self.e.get())
        a=0
        b=1j*z
        c=1j/z
        d=0
        self.top.destroy()
        Bt=drawlambda((x,y))
        draw4((x,y))
        print Bt
        x=x+150
        atl=len(At)
        print atl
        if atl!=0:
         if atl==3:
           drawPolyLine(At[atl-2],Bt[0])
           if At[atl-1]!=(0,0):
            drawPolyLine(At[atl-1],Bt[1])
         else: 
           drawPolyLine(At[atl-2],Bt[0])
           drawPolyLine(At[atl-1],Bt[1])
        At=Bt
        print At
        ab.append([[[a.real,a.imag],[b.real,b.imag]],[[c.real,c.imag],[d.real,d.imag]]])
        #print "value is", self.e.get(),self.f.get(),self.g.get()
def jInv(J,phase):
        ABCD=[[[0,0],[0,0]],[[0,0],[0,0]]]
        ABCD[0][0][0]=0
        ABCD[0][1][0]=np.real(math.sin(math.radians(phase))/J)
        ABCD[1][0][0]=np.real(math.sin(math.radians(phase))*J)
        ABCD[1][1][0]=0
        ABCD[0][0][1]=0
        ABCD[0][1][1]=np.imag(math.sin(math.radians(phase))/J)
        ABCD[1][0][1]=np.imag(math.sin(math.radians(phase))*J)
        ABCD[1][1][1]=0
        return ABCD

def kInv(K,phase):
        ABCD=[[[0,0],[0,0]],[[0,0],[0,0]]]
        ABCD[0][0][0]=0
        ABCD[0][1][0]=np.real(math.sin(math.radians(phase))*K)
        ABCD[1][0][0]=np.real(math.sin(math.radians(phase))/K)
        ABCD[1][1][0]=0
        ABCD[0][0][1]=0
        ABCD[0][1][1]=np.imag(math.sin(math.radians(phase))*K)
        ABCD[1][0][1]=np.imag(math.sin(math.radians(phase))/K)
        ABCD[1][1][1]=0
        return ABCD



class MyDialogJinverter:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Enter value of J").pack()
        self.e = Entry(top)
        self.e.pack(padx=5)
        Label(top, text="Enter value of phase(+90 or -90)").pack()
        self.f = Entry(top)
        self.f.pack(padx=5)
        
        
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global ab
        global x,y,At,Bt
        Jval=complex(self.e.get())
        phase=int(self.f.get())
        #print Jval,phase
        q=jInv(Jval,phase)
        ab.append(q)
        #print ab
        self.top.destroy()
        drawj((x,y-20))
        Bt=drawlines((x,y-20))
        x=x+150
        atl=len(At)
        print atl
        if atl!=0:
         if atl==3:
           drawPolyLine(At[atl-2],Bt[0])
           if At[atl-1]!=(0,0):
            drawPolyLine(At[atl-1],Bt[1])
         else: 
           drawPolyLine(At[atl-2],Bt[0])
           drawPolyLine(At[atl-1],Bt[1])
        At=Bt
        print At

class MyDialogKinverter:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Enter value of K").pack()
        self.e = Entry(top)
        self.e.pack(padx=5)
        Label(top, text="Enter value of phase(+90 or -90)").pack()
        self.f = Entry(top)
        self.f.pack(padx=5)
        
        
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
        global ab
        global x,y,At,Bt
        Kval=complex(self.e.get())
        phase=int(self.f.get())
        #print Jval,phase
        q=kInv(Kval,phase)
        ab.append(q)
        #print ab
        self.top.destroy()
        self.top.destroy()
        drawk((x,y-20))
        Bt=drawlines((x,y-20))
        x=x+150
        atl=len(At)
        print atl
        if atl!=0:
         if atl==3:
           drawPolyLine(At[atl-2],Bt[0])
           if At[atl-1]!=(0,0):
            drawPolyLine(At[atl-1],Bt[1])
         else: 
           drawPolyLine(At[atl-2],Bt[0])
           drawPolyLine(At[atl-1],Bt[1])
        At=Bt
        print At
class MyDialoghybridCouplercalculator:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Enter value of Ya").pack()
        self.e = Entry(top)
        self.e.pack(padx=5)
        
        Label(top, text="Enter value of Yb").pack()
        self.f = Entry(top)
        self.f.pack(padx=5)
        
        
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
       res=Toplevel(root,background='black')
       res.geometry('1300x1300')
       abcd=Label(res,padx=10,background='black',foreground='#FF59FF',text='\t\t\t ABCD odd mode:',font=("Times", 18, "bold"))
       abcd.grid(row=0,columnspan=2)
       Ya=complex(self.e.get())
       Yb=complex(self.f.get())
       a,b,c,d,e,f,g=SParametersCalchybrid(Ya,Yb)
       a11=complex(round(a[0][0][0],4),round(a[0][0][1],4))
       a12=complex(round(a[0][1][0],4),round(a[0][1][1],4))
       a21=complex(round(a[1][0][0],4),round(a[1][0][1],4))
       a22=complex(round(a[1][1][0],4),round(a[1][1][1],4))
       Label(res,background='black',text=a11,foreground='red',font=("Times", 15, "bold")).grid(row=1,column=1)
       Label(res,background='black',text=a12,foreground='red',font=("Times", 15, "bold")).grid(row=1,column=2)
       Label(res,background='black',text=a21,foreground='red',font=("Times", 15, "bold")).grid(row=2,column=1)
       Label(res,background='black',text=a22,foreground='red',font=("Times", 15, "bold")).grid(row=2,column=2)
       Label(res,padx=10,background='black',foreground='#FF59FF',text='\t\t\t ABCD even mode:',font=("Times", 18, "bold")).grid(row=3,columnspan=2)
       b11=complex(round(b[0][0][0],4),round(b[0][0][1],4))
       b12=complex(round(b[0][1][0],4),round(b[0][1][1],4))
       b21=complex(round(b[1][0][0],4),round(b[1][0][1],4))
       b22=complex(round(b[1][1][0],4),round(b[1][1][1],4))
       Label(res,background='black',text=b11,foreground='red',font=("Times", 15, "bold")).grid(row=4,column=1)
       Label(res,background='black',text=b12,foreground='red',font=("Times", 15, "bold")).grid(row=4,column=2)
       Label(res,background='black',text=b21,foreground='red',font=("Times", 15, "bold")).grid(row=5,column=1)
       Label(res,background='black',text=b22,foreground='red',font=("Times", 15, "bold")).grid(row=5,column=2)
       Label(res,padx=10,background='black',foreground='#FF59FF',text='\t\t\t Resultant S parameters: S11,S12,S13,S14',font=("Times", 18, "bold")).grid(row=6,columnspan=2)
       c11=complex(round(c[0][0][0],4),round(c[0][0][1],4))
       c12=complex(round(c[0][1][0],4),round(c[0][1][1],4))
       c21=complex(round(c[1][0][0],4),round(c[1][0][1],4))
       c22=complex(round(c[1][1][0],4),round(c[1][1][1],4))
       Label(res,background='black',text=c11,foreground='red',font=("Times", 15, "bold")).grid(row=7,column=1)
       Label(res,background='black',text=c12,foreground='red',font=("Times", 15, "bold")).grid(row=7,column=2)
       Label(res,background='black',text=c21,foreground='red',font=("Times", 15, "bold")).grid(row=8,column=1)
       Label(res,background='black',text=c22,foreground='red',font=("Times", 15, "bold")).grid(row=8,column=2)
       dr=round(np.real(d),4)
       db=round(np.imag(d),4)
       d=complex(dr,db)
       er=round(np.real(e),4)
       eb=round(np.imag(e),4)
       e=complex(er,eb)
       fr=round(np.real(f),4)
       fb=round(np.imag(f),4)
       f=complex(fr,fb)
       gr=round(np.real(g),4)
       gb=round(np.imag(g),4)
       g=complex(gr,gb)
       Label(res,pady=30,padx=10,background='black',foreground='#FF59FF',text=' S11e:',font=("Times", 18, "bold")).grid(row=9,column=1)       
       Label(res,background='black',text=d,foreground='red',font=("Times", 15, "bold")).grid(row=10,column=1)
       Label(res,pady=30,padx=10,background='black',foreground='#FF59FF',text=' S11o:',font=("Times", 18, "bold")).grid(row=9,column=2)
       Label(res,background='black',text=e,foreground='red',font=("Times", 15, "bold")).grid(row=10,column=2)
       Label(res,pady=30,padx=10,background='black',foreground='#FF59FF',text=' S12e:',font=("Times", 18, "bold")).grid(row=11,column=1)       
       Label(res,background='black',text=f,foreground='red',font=("Times", 15, "bold")).grid(row=12,column=1)
       Label(res,pady=30,padx=10,background='black',foreground='#FF59FF',text=' S12o:',font=("Times", 18, "bold")).grid(row=11,column=2)
       Label(res,background='black',text=g,foreground='red',font=("Times", 15, "bold")).grid(row=12,column=2)
       canvas1=Canvas(master = res, width = 1300, height = 500)
       canvas1.grid(row=13,columnspan=3)
       turtle2_screen = turtle.TurtleScreen(canvas1)
       turtle2_screen.bgcolor("black")
       turtle2 = turtle.RawTurtle(turtle2_screen)
       turtle2.hideturtle()
       drawCoupler(turtle2,(-200,150))

class MyDialogCouplercalculator:
    def __init__(self, parent):

        top = self.top = Toplevel(parent)

        Label(top, text="Enter value of Ya").pack()
        self.e = Entry(top)
        self.e.pack(padx=5)
        
        Label(top, text="Enter value of Yb").pack()
        self.f = Entry(top)
        self.f.pack(padx=5)
        
        
        
        b = Button(top, text="OK", command=self.ok)
        b.pack(pady=5)

    def ok(self):
       res=Toplevel(root,background='black')
       res.geometry('1300x1300')
       abcd=Label(res,padx=10,background='black',foreground='#FF59FF',text='\t\t\t ABCD odd mode:',font=("Times", 18, "bold"))
       abcd.grid(row=0,columnspan=2)
       Ya=complex(self.e.get())
       Yb=complex(self.f.get())
       a,b,c,d,e,f,g=SParametersCalc(Ya,Yb)
       a11=complex(round(a[0][0][0],4),round(a[0][0][1],4))
       a12=complex(round(a[0][1][0],4),round(a[0][1][1],4))
       a21=complex(round(a[1][0][0],4),round(a[1][0][1],4))
       a22=complex(round(a[1][1][0],4),round(a[1][1][1],4))
       Label(res,background='black',text=a11,foreground='red',font=("Times", 15, "bold")).grid(row=1,column=1)
       Label(res,background='black',text=a12,foreground='red',font=("Times", 15, "bold")).grid(row=1,column=2)
       Label(res,background='black',text=a21,foreground='red',font=("Times", 15, "bold")).grid(row=2,column=1)
       Label(res,background='black',text=a22,foreground='red',font=("Times", 15, "bold")).grid(row=2,column=2)
       Label(res,padx=10,background='black',foreground='#FF59FF',text='\t\t\t ABCD even mode:',font=("Times", 18, "bold")).grid(row=3,columnspan=2)
       b11=complex(round(b[0][0][0],4),round(b[0][0][1],4))
       b12=complex(round(b[0][1][0],4),round(b[0][1][1],4))
       b21=complex(round(b[1][0][0],4),round(b[1][0][1],4))
       b22=complex(round(b[1][1][0],4),round(b[1][1][1],4))
       Label(res,background='black',text=b11,foreground='red',font=("Times", 15, "bold")).grid(row=4,column=1)
       Label(res,background='black',text=b12,foreground='red',font=("Times", 15, "bold")).grid(row=4,column=2)
       Label(res,background='black',text=b21,foreground='red',font=("Times", 15, "bold")).grid(row=5,column=1)
       Label(res,background='black',text=b22,foreground='red',font=("Times", 15, "bold")).grid(row=5,column=2)
       Label(res,padx=10,background='black',foreground='#FF59FF',text='\t\t\t Resultant S parameters: S11,S12,S13,S14',font=("Times", 18, "bold")).grid(row=6,columnspan=2)
       c11=complex(round(c[0][0][0],4),round(c[0][0][1],4))
       c12=complex(round(c[0][1][0],4),round(c[0][1][1],4))
       c21=complex(round(c[1][0][0],4),round(c[1][0][1],4))
       c22=complex(round(c[1][1][0],4),round(c[1][1][1],4))
       Label(res,background='black',text=c11,foreground='red',font=("Times", 15, "bold")).grid(row=7,column=1)
       Label(res,background='black',text=c12,foreground='red',font=("Times", 15, "bold")).grid(row=7,column=2)
       Label(res,background='black',text=c21,foreground='red',font=("Times", 15, "bold")).grid(row=8,column=1)
       Label(res,background='black',text=c22,foreground='red',font=("Times", 15, "bold")).grid(row=8,column=2)
       dr=round(np.real(d),4)
       db=round(np.imag(d),4)
       d=complex(dr,db)
       er=round(np.real(e),4)
       eb=round(np.imag(e),4)
       e=complex(er,eb)
       fr=round(np.real(f),4)
       fb=round(np.imag(f),4)
       f=complex(fr,fb)
       gr=round(np.real(g),4)
       gb=round(np.imag(g),4)
       g=complex(gr,gb)
       Label(res,pady=30,padx=10,background='black',foreground='#FF59FF',text=' S11e:',font=("Times", 18, "bold")).grid(row=9,column=1)       
       Label(res,background='black',text=d,foreground='red',font=("Times", 15, "bold")).grid(row=10,column=1)
       Label(res,pady=30,padx=10,background='black',foreground='#FF59FF',text=' S11o:',font=("Times", 18, "bold")).grid(row=9,column=2)
       Label(res,background='black',text=e,foreground='red',font=("Times", 15, "bold")).grid(row=10,column=2)
       Label(res,pady=30,padx=10,background='black',foreground='#FF59FF',text=' S12e:',font=("Times", 18, "bold")).grid(row=11,column=1)       
       Label(res,background='black',text=f,foreground='red',font=("Times", 15, "bold")).grid(row=12,column=1)
       Label(res,pady=30,padx=10,background='black',foreground='#FF59FF',text=' S12o:',font=("Times", 18, "bold")).grid(row=11,column=2)
       Label(res,background='black',text=g,foreground='red',font=("Times", 15, "bold")).grid(row=12,column=2)
       canvas1=Canvas(master = res, width = 1300, height = 500)
       canvas1.grid(row=13,columnspan=3)
       turtle2_screen = turtle.TurtleScreen(canvas1)
       turtle2_screen.bgcolor("black")
       turtle2 = turtle.RawTurtle(turtle2_screen)
       turtle2.hideturtle()
       drawCoupler(turtle2,(-200,150))
       

def EvenOddCoupler(ABCD):
    Y0=1.0/50;
    Acomp=ABCD[0][0][0]+ABCD[0][0][1]*1j
    Bcomp=ABCD[0][1][0]+ABCD[0][1][1]*1j
    Ccomp=ABCD[1][0][0]+ABCD[1][0][1]*1j
    Dcomp=ABCD[1][1][0]+ABCD[1][1][1]*1j
    
    S11eo=(Acomp+Bcomp*Y0-Ccomp/Y0-Dcomp)/(Acomp+Bcomp*Y0+Ccomp/Y0+Dcomp)
    print S11eo
    sr=round(np.real(S11eo),4)
    sd=round(np.imag(S11eo),4)
    S11eo=complex(sr,sd)
    S12eo=2.0/(Acomp+Bcomp*Y0+Ccomp/Y0+Dcomp)
    
    sr=round(np.real(S12eo),4)
    sd=round(np.imag(S12eo),4)
    S12eo=complex(sr,sd)
    print 'S12e0',S12eo,(Acomp+Bcomp*Y0+Ccomp/Y0+Dcomp)
    return (S11eo,S12eo)

    
def SParametersCalc(Ya,Yb):
    Y0=1.0/50;
    Yb=((Ya**2)-(Y0**2))**0.5
    ABCDEven=[[[0.0,0.0],[0.0,0.0]],[[0.0,0.0],[0.0,0.0]]]
    print 'h',Yb
    ABCDOdd=[[[0.0,0.0],[0.0,0.0]],[[0.0,0.0],[0.0,0.0]]]
    
    ABCDEven[0][0][0]=np.real(-1.0*(Yb)/Ya)
    ABCDEven[0][1][0]=np.real(1.0j/Ya)
    ABCDEven[1][0][0]=np.real(1j*(Ya-(Yb*Yb)/Ya))
    #print 'hi',Ya,Yb,np.real(1j*(Ya-(Yb*Yb)/float(Ya))),np.imag(1j*(Ya-(Yb*Yb)/float(Ya)))
    ABCDEven[1][1][0]=np.real(-1.0*(Yb)/Ya)
    
    ABCDEven[0][0][1]=np.imag(-1.0*(Yb)/Ya)
    ABCDEven[0][1][1]=np.imag(1.0j/Ya)
    ABCDEven[1][0][1]=np.imag(1j*(Ya-(Yb*Yb)/Ya))
    ABCDEven[1][1][1]=np.imag(-1.0*(Yb)/Ya)
    
    ABCDOdd[0][0][0]=np.real(1.0*(Yb)/Ya)
    ABCDOdd[0][1][0]=np.real(1.0j/Ya)
    ABCDOdd[1][0][0]=np.real(1j*(Ya-(Yb*Yb)/Ya))
    ABCDOdd[1][1][0]=np.real(1.0*(Yb)/Ya)
    
    ABCDOdd[0][0][1]=np.imag(1.0*(Yb)/Ya)
    ABCDOdd[0][1][1]=np.imag(1.0j/Ya)
    ABCDOdd[1][0][1]=np.imag(1j*(Ya-(Yb*Yb)/Ya))
    ABCDOdd[1][1][1]=np.imag(1.0*(Yb)/Ya)
   
    (S11e,S12e)=EvenOddCoupler(ABCDEven)
    (S11o,S12o)=EvenOddCoupler(ABCDOdd)
    #print 's11e,s12e,',S11e,S12e,S11o,S12o

    S11=(S11e+S11o)/2.0
    S12=(S12e+S12o)/2.0
    S13=(S12e-S12o)/2.0
    S14=(S11e-S11o)/2.0
    #print S11,S11e,S11o,S14
    S=[[[0,0],[0,0]],[[0,0],[0,0]]]
    
    S[0][0][0]=round(np.real(S11),4)
    S[0][1][0]=round(np.real(S12),4)
    S[1][0][0]=round(np.real(S13),4)
    S[1][1][0]=round(np.real(S14),4)
    
    S[0][0][1]=round(np.imag(S11),4)
    S[0][1][1]=round(np.imag(S12),4)
    S[1][0][1]=round(np.imag(S13),4)
    S[1][1][1]=round(np.imag(S14),4)
    #print S
    return ABCDOdd,ABCDEven,S,S11e,S11o,S12e,S12o

def SParametersCalchybrid(Ya,Yb):
    Y0=1.0/50
    #Ya=Ya/Y0
    #Yb=Yb/Y0
    Yb=(1-((Ya/Y0)**2))**0.5*Y0
    print Yb,'kk',Ya
    #Yb=((Ya**2)-(Y0**2))**0.5
    ABCDEven=[[[0.0,0.0],[0.0,0.0]],[[0.0,0.0],[0.0,0.0]]]
    ABCDOdd=[[[0.0,0.0],[0.0,0.0]],[[0.0,0.0],[0.0,0.0]]]
    
    ABCDEven[0][0][0]=np.real(-1.0*(Ya)/Yb)
    ABCDEven[0][1][0]=np.real(1.0j/Yb)
    ABCDEven[1][0][0]=np.real(1j*(((Ya*Ya)+(Yb*Yb))/Yb))
    #print 'hi',Ya,Yb,np.real(1j*(Ya-(Yb*Yb)/float(Ya))),np.imag(1j*(Ya-(Yb*Yb)/float(Ya)))
    ABCDEven[1][1][0]=np.real(1.0*(Ya)/Yb)
    
    ABCDEven[0][0][1]=np.imag(-1.0*(Ya)/Yb)
    ABCDEven[0][1][1]=np.imag(1.0j/Yb)
    ABCDEven[1][0][1]=np.imag(1j*(((Ya*Ya)+(Yb*Yb))/Yb))
    ABCDEven[1][1][1]=np.imag(1.0*(Ya)/Yb)
    
    ABCDOdd[0][0][0]=np.real(1.0*(Ya)/Yb)
    ABCDOdd[0][1][0]=np.real(1.0j/Yb)
    ABCDOdd[1][0][0]=np.real(1j*(((Ya*Ya)+(Yb*Yb))/Yb))
    ABCDOdd[1][1][0]=np.real(-1.0*(Ya)/Yb)
    
    ABCDOdd[0][0][1]=np.imag(1.0*(Ya)/Yb)
    ABCDOdd[0][1][1]=np.imag(1.0j/Yb)
    ABCDOdd[1][0][1]=np.imag(1j*(((Ya*Ya)+(Yb*Yb))/Yb))
    ABCDOdd[1][1][1]=np.imag(-1.0*(Ya)/Yb)
   
    (S11e,S12e)=EvenOddCoupler(ABCDEven)
    (S11o,S12o)=EvenOddCoupler(ABCDOdd)
    #print 's11e,s12e,',S11e,S12e,S11o,S12o

    S11=(S11e+S11o)/2.0
    S12=(S12e+S12o)/2.0
    S13=(S12e-S12o)/2.0
    S14=(S11e-S11o)/2.0
    #print S11,S11e,S11o,S14
    S=[[[0,0],[0,0]],[[0,0],[0,0]]]
    
    S[0][0][0]=round(np.real(S11),4)
    S[0][1][0]=round(np.real(S12),4)
    S[1][0][0]=round(np.real(S13),4)
    S[1][1][0]=round(np.real(S14),4)
    
    S[0][0][1]=round(np.imag(S11),4)
    S[0][1][1]=round(np.imag(S12),4)
    S[1][0][1]=round(np.imag(S13),4)
    S[1][1][1]=round(np.imag(S14),4)
    #print S
    return ABCDOdd,ABCDEven,S,S11e,S11o,S12e,S12o


#from Tkinter import simpledialog
ab=[]
def click(i):
    res=[[[],[]],[[],[]]]
    if i =='Impedance':
        d = MyDialogLineImpedance(root)
    elif i =='Admittance':
        d = MyDialogLineAdmittance(root)
    elif i=='T-network':
        d = MyDialogT(root)
    elif i=='pi-network':
        d = MyDialogPi(root)
    elif i=='ABCD N/W':
        d=MyDialogABCD(root)
    elif i=='lambda/4 line':
        d = MyDialoglamdaby4(root)
    elif i=='lambda/8 line':
        d = MyDialoglamdaby8(root)
    elif i=='J Inverter':
        d = MyDialogJinverter(root)
    elif i=='K Inverter':
        d = MyDialogKinverter(root)
    elif i=='calculate parameters':
        d=MyDialogsl(root)
    elif i=='Analyse currents and voltages':
        d=MyDialogvoltages(root)
    elif i=='Directional Coupler calculator':
        d=MyDialogCouplercalculator(root)
    elif i=='Hybrid ring calculator':
        d=MyDialoghybridCouplercalculator(root)
        
        
def main():
    lis_buttons=['Impedance','Admittance','lambda/4 line','lambda/8 line','T-network','pi-network','ABCD N/W','J Inverter','K Inverter','calculate parameters','Analyse currents and voltages','Directional Coupler calculator','Hybrid ring calculator']
    func_lis=[]
    
    root.title('ABCD generator')
    k=0
    for i in lis_buttons:
        print i
        button = Button(root,text=i,width=26,command= lambda x=i: click(x),font=("Times", 11, "bold"),fg='red',bg='black',highlightcolor='white',borderwidth=0.5)
        button.grid(row=k,column=0)
        k=k+1
    
    root.geometry('1300x1300')
    root.configure(background='black')
    root.mainloop()
    
        
                 

        
if __name__ == '__main__':
       main()    
