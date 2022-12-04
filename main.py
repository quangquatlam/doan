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

labelTickerStockA = Label(root,text="Mã Index A",font=("Quicksand",12), bg='#FFB6C1')
labelTickerStockA.place(x = 40 , y = 100)
comboboxStockA = ttk.Combobox(root,width=20)
comboboxStockA.place(x = 170 , y =100)

labelTickerStockB = Label(root,text="Mã Index B",font=("Quicksand",12),bg='#FFB6C1')
labelTickerStockB.place(x = 40 , y = 140)
comboboxStockB=ttk.Combobox(root,width=20)
comboboxStockB.place(x = 170 , y =140)

labelTickerStockC=Label(root,text="Mã Index C",font=("Quicksand",12),bg='#FFB6C1')
labelTickerStockC.place(x = 40 , y = 180)
comboboxStockC=ttk.Combobox(root,width=20)

labelTickerStockD = Label(root,text="Mã Index D",font=("Quicksand",12),bg='#FFB6C1')
labelTickerStockD.place(x = 40 , y = 220)
comboboxStockD = ttk.Combobox(root,width=20)
comboboxStockD.place(x = 170 , y =220)

# trong so

labelWeightA = Label(root,text="Trọng số đầu tư A",font=("Quicksand",12),bg='#FFB6C1')
labelWeightA.place(x = 350 , y = 100)
inputWeightA = Entry(root,width=20,borderwidth=2)
inputWeightA.place(x = 520 , y = 100)

labelWeightB=Label(root,text= "Trọng số đầu tư B",font=("Quicksand",12),bg='#FFB6C1')
labelWeightB.place(x = 350 , y = 140)
inputWeightB = Entry(root,width=20,borderwidth=2)
inputWeightB.place(x = 520 , y =140)

labelWeightC=Label(root,text="Trọng số đầu tư C",font=("Quicksand",12),bg='#FFB6C1')
labelWeightC.place(x = 350 , y = 180)
inputWeightC = Entry(root,width=20,borderwidth=2)
inputWeightC.place(x = 520 , y =180)
comboboxStockC.place(x = 170 , y =180)

labelWeightD = Label(root,text="Trọng số đầu tư D",font=("Quicksand",12),bg='#FFB6C1')
labelWeightD.place(x = 350 , y = 220)
inputWeightD=Entry(root,width=20,borderwidth=2)
inputWeightD.place(x = 520 , y = 220)

labelDateStart=Label(root,text="Ngày bắt đầu",font=("Quicksand",12),bg='#FFB6C1')
labelDateStart.place(x = 680 , y = 100)
dateEntryStart= DateEntry(root,width=20, date_pattern='y/mm/dd')
dateEntryStart.place(x = 800 , y = 100)

labelVaRTotal = Label(root, text="VaR",font=("Quicksand",12),bg='#FFB6C1')
labelVaRTotal.place(x=40, y=330)

labelListMeasure = Label(root, text="Bảng giá trị",font=("Quicksand",12),bg='#FFB6C1')
labelListMeasure.place(x=40,y=360)

comboboxStockSearch = ttk.Combobox(root,width=20)
comboboxStockSearch.place(x = 680 , y =270)

tree = ttk.Treeview(root, columns=("","Var95", "Var99", "Volatility"),show="headings",height=5)
tree.place(x=40,y=400)
tree.column("#2", anchor=CENTER)
tree.heading("#2",text="VaR95")
tree.column("#3", anchor=CENTER)
tree.heading("#3",text="VaR99")
tree.column("#4", anchor=CENTER)
tree.heading("#4",text="Volatility")

selected = StringVar()

def selectedFunc(): 
    data = pd.DataFrame()
    if (selected.get() == 'HNX'):
        data = pd.read_csv('data/HNX.csv')
    if (selected.get() == 'HSX'):
        data = pd.read_csv('data/HSX.csv')
    
    listStock = data.iloc[:,0].tolist()

    comboboxStockA['values'] = listStock
    comboboxStockA.current(0)

    comboboxStockB['values'] = listStock
    comboboxStockB.current(1)

    comboboxStockC['values'] = listStock
    comboboxStockC.current(2)

    comboboxStockD['values'] = listStock
    comboboxStockD.current(3)

    comboboxStockSearch['values'] = listStock
    comboboxStockSearch.current(0)

radioExchangeHSX = ttk.Radiobutton(root, text="Sàn HSX", width=30,variable= selected ,value='HSX', command=selectedFunc)
radioExchangeHSX.place(x=100, y= 50)

radioExchangeHNX = ttk.Radiobutton(root, text="Sàn HNX", width=30, variable= selected, value='HNX', command=selectedFunc)
radioExchangeHNX.place(x=200, y= 50)


def quantitative():
    stockTickerA = comboboxStockA.get()
    stockTickerB = comboboxStockB.get()
    stockTickerC = comboboxStockC.get()
    stockTickerD = comboboxStockD.get()

    stockTickerAWeight = inputWeightA.get()
    stockTickerBWeight = inputWeightB.get()
    stockTickerCWeight = inputWeightC.get()
    stockTickerDWeight = inputWeightD.get()

    dateTimeStart = dateEntryStart.get().replace("/","-")

    listWeight = []

    status = True

    if not stockTickerAWeight and not stockTickerBWeight and not stockTickerCWeight and not stockTickerDWeight:
        messagebox.showerror('Error','Vui lòng điền đầy đủ thông tin')
        status = False
        return

    else: 
        listWeight = [float(stockTickerAWeight), float(stockTickerBWeight), float(stockTickerCWeight), float(stockTickerDWeight)]
        if (sum(listWeight) !=1 ):
            messagebox.showerror('Error','Tổng các trọng số phải bằng 1')
            listWeight = []
            status = False
            return
    stocks = [stockTickerA, stockTickerB, stockTickerC, stockTickerD]

    currentTime = dt.datetime.now().strftime("%Y-%m-%d")

    if (currentTime <= dateTimeStart):
        messagebox.showerror('Error','Vui lòng điền đầy đủ thông tin ngày bắt đầu')
        status = False
        return

    if status:
        labelVaRTotal = Label(root, text=VaRList(dateTimeStart, stocks, listWeight),font=("Quicksand",12),bg='#FFB6C1')
        labelVaRTotal.place(x=100, y=330)
    

    


btnResult = Button(root,text='Định lượng',foreground="blue", padx=5,command=quantitative).place(x=40, y=270)
btnSearch = Button(root,text='Tìm kiếm',foreground="blue",padx=5,command=quantitative).place(x = 840 , y = 270)
mainloop()