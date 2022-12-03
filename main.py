from ultil import * 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

root = Tk()
root.title("Hệ thống định lượng rủi ro thị trường chứng khoán Việt Nam")
root.configure(bg='#FFB6C1')
root.geometry("1000x650")

labelTitle=Label(root,text="Hệ thống định lượng rủi ro thị trường chứng khoán Việt Nam",font = ("Quicksand", 17),foreground="black",bg='#FFB6C1')
labelTitle.pack(side = "top")

labelTickerStockA = Label(root,text="Mã Index A",font=("Quicksand",12),bg='#FFB6C1')
labelTickerStockA.place(x = 40 , y = 70)
comboboxStockA = ttk.Combobox(root,width=20)
comboboxStockA['values'] = getListTicker().tolist()
comboboxStockA.current(0)
comboboxStockA.place(x = 170 , y =70)

labelTickerStockB = Label(root,text="Mã Index B",font=("Quicksand",12),bg='#FFB6C1')
labelTickerStockB.place(x = 40 , y = 110)
comboboxStockB=ttk.Combobox(root,width=20)
comboboxStockB['values'] = getListTicker().tolist()
comboboxStockB.current(1)
comboboxStockB.place(x = 170 , y =110)

labelTickerStockC=Label(root,text="Mã Index C",font=("Quicksand",12),bg='#FFB6C1')
labelTickerStockC.place(x = 40 , y = 150)
comboboxStockC=ttk.Combobox(root,width=20)
comboboxStockC['values'] = getListTicker().tolist()
comboboxStockC.current(2)
comboboxStockC.place(x = 170 , y =150)

labelTickerStockD = Label(root,text="Mã Index D",font=("Quicksand",12),bg='#FFB6C1')
labelTickerStockD.place(x = 40 , y = 190)
comboboxStockD = ttk.Combobox(root,width=20)
comboboxStockD['values'] = getListTicker().tolist()
comboboxStockD.current(3)
comboboxStockD.place(x = 170 , y =190)

# trong so

labelWeightA = Label(root,text="Trọng số đầu tư A",font=("Quicksand",12),bg='#FFB6C1')
labelWeightA.place(x = 350 , y = 70)
inputWeightA = Entry(root,width=20,borderwidth=2)
inputWeightA.place(x = 520 , y =70)

labelWeightB=Label(root,text= "Trọng số đầu tư B",font=("Quicksand",12),bg='#FFB6C1')
labelWeightB.place(x = 350 , y = 110)
inputWeightB = Entry(root,width=20,borderwidth=2)
inputWeightB.place(x = 520 , y =110)

labelWeightC=Label(root,text="Trọng số đầu tư C",font=("Quicksand",12),bg='#FFB6C1')
labelWeightC.place(x = 350 , y = 150)
inputWeightC = Entry(root,width=20,borderwidth=2)
inputWeightC.place(x = 520 , y =150)

labelWeightD = Label(root,text="Trọng số đầu tư D",font=("Quicksand",12),bg='#FFB6C1')
labelWeightD.place(x = 350 , y = 190)
inputWeightD=Entry(root,width=20,borderwidth=2)
inputWeightD.place(x = 520 , y =190)

label13=Label(root,text="Ngày bắt đầu",font=("Quicksand",12),bg='#FFB6C1')
label13.place(x = 680 , y = 70)
d3= DateEntry(root,width=20)
d3.place(x = 800 , y = 70)


btnResult = Button(root,text='Định lượng',foreground="blue",command=a).place(x=40, y=250)
mainloop()