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
        self.rectangle = []
        # 声明一个是否按下开始的变量
        self.isloop = False
        self.newloop = False
        Window = Tk()
        Window.geometry('1100x1100')
        Window.title("python模拟磁盘调度算法")
        frame = Frame(Window)
        frame.grid(row=0,column=0)
        frame1 = Frame(frame,bg="white",bd=2,relief=GROOVE,width=500)
        frame2 = Frame(frame)
        frame3 = Frame(frame)
        frame4 = Frame(frame)
        frame1.grid(row=1, column=1,padx=10)
        frame2.grid(row=1, column=2)
        frame3.grid(row=2, column=1)
        frame4.grid(row=2, column=2)
        self.canvas1 = Canvas(frame1, width=510,height=510)
        self.canvas2 = Canvas(frame2, width=500,height=500,bg="white")
        self.canvas1.grid(row=1,column=1)
        self.canvas2.grid(row=1, column=1)

        self.textLog = Text(frame3,height=17)
        self.textLog.grid(row=0,column=1,padx=5)
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
        self.btnAl_2 = Button(frame4,text="运行",command=lambda :self.RectangleShow(self.Al.caculate(self.track_request,self.var.get())))
        self.btnAl_2.grid(row=2,column=2)
        self.displayRectangle()
        Window.mainloop()

    def displayStartLine(self,point):
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
        self.textLog.insert(END,'\n********'+str(self.var.get())+'************')
        self.textLog.insert(END,'\n访问的磁道序列为:\n'+str(point))
        sum_gap = sum([(abs(point[i] - point[i - 1])) for i in range(1, len(point))])
        self.textLog.insert(END,'\n移动的磁道数为：'+str(sum_gap))
        self.textLog.insert(END,'\n平均移动的磁道数为：'+str(sum_gap / self.Al.TRACK_REQUEST_COUNT))
        self.RectangleShow(point)

    def displayRectangle(self):
        x0 = 0
        y0 = 0
        x1 = 50
        y1 = 50
        count = 1
        for i in range(10):
            y0 = i * 50
            y1 = i * 50 + 50
            for j in range(10):
                x0 = j * 50
                x1 = j * 50 +50
                if count in self.track_request:
                    self.rectangle.append(self.canvas1.create_rectangle(x0,y0,x1,y1,fill="red"))
                elif count == 11:
                    print(x0,y0,x1,y1)
                    self.rectangle.append(self.canvas1.create_rectangle(x0,y0,x1,y1,fill="pink"))
                else:
                    self.rectangle.append(self.canvas1.create_rectangle(x0, y0, x1, y1))
                self.canvas1.create_text((x0 + x1) / 2, (y0 + y1) / 2, text=str(count))
                count += 1

    def RectangleShow(self,point):
        self.displayRectangle()
        count = point[0]                #11
        print("count:",count)
        cnt = 1
        x0 = (count % 10 - 1) * 50
        x1 = count % 10 * 50
        y0 = (count // 10) * 50
        y1 = count // 10 * 50 + 50
        # print(x0,y0,x1,y1)
        cv = self.canvas1.create_rectangle(x0, y0, x1, y1, fill="green")
        while True:
            if self.newloop == True:
                self.newloop = False
                return
                # 延时操作
            time.sleep(0.1)
            if count % 10 != 0:
                x0 = x0 + 50
                x1 = x1 + 50
                self.canvas1.coords(cv,x0,y0,x1,y1)   #右移
                print("右移一个",count)
                self.canvas1.update_idletasks()
                self.canvas1.update()
            else:
                if count == 100:
                    count = 0
                    x0 = 0
                    x1 = 50
                    y0 = 0
                    y1 = 50
                    self.canvas1.coords(cv,0,0,50,50)      #移动到0位置
                    print("移动到0位置")
                    self.canvas1.update_idletasks()
                    self.canvas1.update()
                else:                                      #移动到下一行行首
                    x0 = 0
                    y0 = y0 + 50
                    x1 = 50
                    y1 = y1+ 50
                    self.canvas1.coords(cv,x0,y0,x1,y1)
                    print("移动到下一行行首")
                    self.canvas1.update_idletasks()
                    self.canvas1.update()
            count += 1
            if count == point[cnt]:
                cv = self.canvas1.create_rectangle(x0, y0, x1, y1,fill="green")
                cnt += 1
                print("抓取",cnt)
                self.canvas1.update_idletasks()
                self.canvas1.update()
            if cnt == 11:
                print(count)
                return


Disk()