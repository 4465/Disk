from tkinter import *
import turtle as t
from Algorithm import *
import time
class Disk:
    def __init__(self):
        self.Al = Algorithm()
        point =[]
        Window = Tk()
        Window.geometry('5000x5000')
        Window.title("python模拟磁盘调度算法")
        self.canvas = Canvas(Window, width=500,height=500,bg="yellow")
        self.canvas.pack()
        self.oval_count = 0
        self.oval_x0 = 10
        self.oval_y0 = 10
        self.oval_x1 = 90
        self.oval_y1 = 90

        frame = Frame(Window)
        frame.pack()
        btnOval = Button(frame,text="Oval",command=self.displayOval)
        btnLine = Button(frame,text="Line",command=self.displayStartLine)
        btnText = Button(frame,text="Text",command=self.displayDiskNum)
        btnOval.grid(row=1, column=1)
        btnLine.grid(row=1, column=2)
        btnText.grid(row=1, column=3)

        btnAl_1 = Button(frame, text="FCFS",command =lambda :self.displayStartLine(self.Al.FCFS())).grid(row=2,column=1)
        btnAl_2 = Button(frame, text="SSTF", command=lambda :self.displayStartLine(self.Al.SSTF())).grid(row=2,column=2)
        btnAl_3 = Button(frame, text="SCAN", command=lambda :self.displayStartLine(self.Al.SCAN())).grid(row=2,column=3)
        btnAl_4 = Button(frame, text="CSCAN", command=lambda :self.displayStartLine(self.Al.CSCAN())).grid(row=2,column=4)
        btnAl_5 = Button(frame, text="NstepSCAN", command=lambda :self.displayStartLine(self.Al.NStepSCAN())).grid(row=2,column=5)

        Window.mainloop()

    def displayOval(self):
        color = ['white','blue','red','green']
        self.oval_x0 += self.oval_count * 10
        self.oval_y0 += self.oval_count * 10
        self.oval_x1 -= self.oval_count * 10
        self.oval_y1 -= self.oval_count * 10
        #self.canvas.create_rectangle(self.oval_x0,self.oval_y0,self.oval_x1,self.oval_y1)
        self.canvas.create_oval(self.oval_x0,self.oval_y0,self.oval_x1,self.oval_y1,fill=color[self.oval_count])
        self.oval_count += 1

    def displayStartLine(self,point):
        #point = [20,45, 51, 66, 73, 84, 93, 26, 20, 3]
        point = list(point)
        theScreen = t.TurtleScreen(self.canvas)
        path = t.RawTurtle(self.canvas)
        path.clear()
        #隐藏画笔
        path.hideturtle()
        #抬起画笔
        path.penup()
        for i in range(len(point)):
            path.goto(point[i]*5-250,230)
            path.write(str(point[i]))
        path.goto(point[0]*5-250,230)
        path.pendown()
        self.canvas.create_line(-250, -230, 250, -230, fill="red")
        x = 10
        path.pendown()
        for i in range(len(point)):
            # self.canvas.create_line(point[i],x+(i+1)*10,point[i+1],x+(i+2)*10,fill="red")
            path.goto(point[i]*5-250,230-20*i)
            path.penup()
            path.write(point[i],font=("Arial",8))
            path.pendown()
            # path.penup()
            # path.goto(point[i] * 5 - 250, 230 - 20 * i)
            # path.pendown()

        print("TRACK SEQUECE:    ")
        print(self.Al.track_request)
        print('访问的磁道序列为: ', end='')
        print(point)
        sum_gap = sum([(abs(point[i] - point[i - 1])) for i in range(1, len(point))])
        print('移动的磁道数为：%d' % sum_gap)
        print('平均移动的磁道数为：%.2f' % (sum_gap / self.Al.TRACK_REQUEST_COUNT))
        print("")

    def displayDiskNum(self):
        self.canvas.create_text(10,15,text='20')

Disk()
