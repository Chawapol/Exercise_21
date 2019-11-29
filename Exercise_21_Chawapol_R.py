from tkinter import *
import math

def leftClickButton(event):
    print(float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    labelResult.configure(text=float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2))
    x = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    if x > 30:
        print("อ้วนมาก")
        sizeResult.configure(text = "อ้วนมาก")
    elif x > 25:
        print("อ้วน")
        sizeResult.configure(text = "อ้วน")
    elif x > 23:
        print("น้ำหนักเกิน")
        sizeResult.configure(text = "น้ำหนักเกิน")
    elif x > 18.6:
        print("น้ำหนักปกติ")
        sizeResult.configure(text = "น้ำหนักปกติ")
    elif x < 18.5:
        print("ผอมเกินไป")
        sizeResult.configure(text = "ผอมเกินไป")


MainWindow = Tk()
labelHeight = Label(MainWindow,text ="ส่วนสูง (cm.)",font = ("AngsanaUPC",18))
labelHeight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow,font = ("AngsanaUPC",14))
textBoxHeight.grid(row=0,column=1)
labelWeight = Label(MainWindow,text ="น้ำหนัก (Kg.)",font = ("AngsanaUPC",18))
labelWeight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow,font = ("AngsanaUPC",14))
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวณ",font = ("AngsanaUPC",12))
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=2)
labelResult = Label(MainWindow,text ="ผลลัพธ์",font = ("AngsanaUPC",12))
labelResult.grid(row=2,column=1)
sizeResult = Label(MainWindow,text ="อยู่ในเกณท์",font = ("AngsanaUPC",12))
sizeResult.grid(row=2,column=2)

MainWindow.mainloop()