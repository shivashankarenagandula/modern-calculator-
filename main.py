import customtkinter
from tkinter import END
from tkinter import messagebox

#functional part
def clear():
    entryField.delete(0,END)
def answer():
    expression=entryField.get()
    try:
        result= eval(expression)
        entryField.delete(0,END)
        entryField.insert(0,result)
    except SyntaxError:
        messagebox.showerror('error','invalid expression')
    except ZeroDivisionError:
        messagebox.showerror('error', 'number does not divisible by zero')
def click(number):
    entryField.insert(END,number)
#GUI
root = customtkinter.CTk()
root.geometry("300*320")
root.config(background='black')
root.title("modern calculator")
entryField=customtkinter.CTkEntry(root,font=('arial',20,'bold'),text_color='black',border_color='white',width = 280, height = 50 , bg_color='black')
entryField.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

b7=customtkinter.CTkButton(root,text='7',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2' ,command= lambda : click('7'))
b7.grid(row=1,column=0,padx=10, pady=10)
b8=customtkinter.CTkButton(root,text='8',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command= lambda : click('8'))
b8.grid(row=1,column=1)
b9=customtkinter.CTkButton(root,text='9',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command= lambda : click('9'))
b9.grid(row=1,column=2)
bp=customtkinter.CTkButton(root,text='+',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3',command= lambda : click('+'))
bp.grid(row=1,column=3)
b4=customtkinter.CTkButton(root,text='4',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command= lambda : click('4'))
b4.grid(row=2,column=0,padx=10, pady=10)
b5=customtkinter.CTkButton(root,text='5',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command= lambda : click('5'))
b5.grid(row=2,column=1)
b6=customtkinter.CTkButton(root,text='6',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command= lambda : click('6'))
b6.grid(row=2,column=2)
bm=customtkinter.CTkButton(root,text='-',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3',command= lambda : click('-'))
bm.grid(row=2,column=3)
b1=customtkinter.CTkButton(root,text='1',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command= lambda : click('1'))
b1.grid(row=3,column=0,padx=10, pady=10)
b2=customtkinter.CTkButton(root,text='2',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command= lambda : click('2'))
b2.grid(row=3,column=1)
b3=customtkinter.CTkButton(root,text='3',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command= lambda : click('3'))
b3.grid(row=3 ,column=2)
bmu=customtkinter.CTkButton(root,text='*',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3',command= lambda : click('*'))
bmu.grid(row=3 ,column=3)
b0=customtkinter.CTkButton(root,text='0',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command= lambda : click('0'))
b0.grid(row=4 ,column=0)
b_period=customtkinter.CTkButton(root,text='.',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',command= lambda : click('.'))
b_period.grid(row=4 ,column=1)
bC=customtkinter.CTkButton(root,text='C',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2' ,command=clear)
bC.grid(row=4 ,column=2)
bd=customtkinter.CTkButton(root,text='/',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3',command= lambda : click('/'))
bd.grid(row=4,column=3,padx=10,pady=10)
beq=customtkinter.CTkButton(root,text='=',font=('arial',20,'bold'),width=60,bg_color='black',cursor='hand2',fg_color='orange',hover_color='orange3', command=answer)
beq.grid(row=5,column=0,padx=10,pady=10,columnspan=4)
root.mainloop()