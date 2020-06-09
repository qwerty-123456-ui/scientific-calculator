from tkinter import *
import math
import parser
import tkinter.messagebox

root=Tk()
root.title('Scientific Calculator')
root.configure(background="powder blue")
root.resizable(width=False,height=False)
root.geometry("480x560+0+0")

calc=Frame(root)
calc.grid()

txtDisplay=Entry(calc,font=('arial',20,'bold'),bg='powder blue',bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

numberpad="789456123"
i=0
btn=[]
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc,width=6,height=2,font=('arial',20,'bold'),bd=4,text=numberpad[i]))
        btn[i].grid(row=j,column=k,pady=1)
        i+=1
# ******************************************************##****************************************************************************




# *****************************************************MENU AND FUNCTION*****************************************************************

def iExit():
    iExit=tkinter.messagebox.askyesno('Scientific Calculator','Confirm you want to exit')
    if iExit>0:
        root.destroy()
        return
        
def Standard():
    root.resizable(width=False,height=False)
    root.geometry("480x568+0+0")

def Scientific():
    root.resizable(width=False,height=False)
    root.geometry("944x568+0+0")

menubar=Menu(calc)

filemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="Standard",command=Standard)
filemenu.add_command(label="Scientific",command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=iExit)

editmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_separator()
editmenu.add_command(label="Paste")


helpmenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpmenu)
helpmenu.add_command(label="View Help")

root.configure(menu=menubar)
root.mainloop()