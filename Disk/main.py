from tkinter import *
import turtle as t
from Algorithm import *
import time
class Disk:
    def __init__(self):
        self.Al = Algorithm()
        self.track_request = [None] * self.Al.TRACK_REQUEST_COUNT
        for i in range(self.Al.TRACK_REQUEST_COUNT):
            self.track_request[i] = random.randint(0, self.Al.TRACK_MAX_COUNT)

        point =[]
        Window = Tk()
        Window.geometry('5000x5000')
        Window.title("python模拟磁盘调度算法")
        frame1 = Frame(Window,border=1,relief=SUNKEN)
        frame2 = Frame(Window,border=1,relief=SUNKEN)
        frame3 = Frame(Window,border=1,relief=SUNKEN)
        frame4 = Frame(Window,border=1,relief=SUNKEN)
        frame1.grid(row=1,column=1,)
        frame2.grid(row=1, column=2)
        frame3.grid(row=2, column=1)
        frame4.grid(row=2, column=2)
        self.canvas1 = Canvas(frame1, width=500,height=500,bg="yellow")
        self.canvas2 = Canvas(frame2, width=500,height=500,bg="yellow")
        self.canvas1.grid(row=1,column=1)
        self.canvas2.grid(row=1, column=1)
        self.oval_count = 0
        self.oval_x0 = 10
        self.oval_y0 = 10
        self.oval_x1 = 90
        self.oval_y1 = 90

        self.textLog = Text(frame3,height=17)
        self.textLog.grid(row=1,column=1)
        self.textLog.insert(END,'#每次生成的磁道序列是随机的，对于不同的序列算法的算法的性能是不一样的\n#通过多次比较观察结果，SSTF是算法中移动的磁道数最少的')
        self.textLog.insert(END,'\n#TRACK SEQUECE:\n'+str(self.track_request))

        self.var = StringVar()
        self.var.set('FCFS')
        r1 = Radiobutton(frame4, text='FCFS', variable=self.var, value='FCFS')
        r1.grid(row=1,column=1)
        r2 = Radiobutton(frame4, text='SSTF', variable=self.var, value='SSTF')
        r2.grid(row=1, column=2)
        r3 = Radiobutton(frame4, text='SCAN', variable=self.var, value='SCAN')
        r3.grid(row=1, column=3)
        r4 = Radiobutton(frame4, text='CSCAN', variable=self.var, value='CSCAN')
        r4.grid(row=1, column=4)
        r5 = Radiobutton(frame4, text='NstepSCAN', variable=self.var, value='NstepSCAN')
        r5.grid(row=1, column=5)
        r6 = Radiobutton(frame4, text='FSCAN', variable=self.var, value='FSCAN')
        r6.grid(row=1, column=6)


        self.btnAl_1 = Button(frame4, text="运行",command =lambda :self.displayStartLine(self.Al.caculate(self.track_request,self.var.get())))
        self.btnAl_1.grid(row=2,column=1)

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
        theScreen = t.TurtleScreen(self.canvas2)
        path = t.RawTurtle(theScreen)
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
        self.canvas2.create_line(-250, -230, 250, -230, fill="red")
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
        self.textLog.insert(END,'\n********'+str(self.var.get())+'************')
        self.textLog.insert(END,'\n访问的磁道序列为:\n'+str(point))
        sum_gap = sum([(abs(point[i] - point[i - 1])) for i in range(1, len(point))])
        self.textLog.insert(END,'\n移动的磁道数为：'+str(sum_gap))
        self.textLog.insert(END,'\n平均移动的磁道数为：'+str(sum_gap / self.Al.TRACK_REQUEST_COUNT))


    def displayDiskNum(self):
        self.canvas.create_text(10,15,text='20')

Disk()
