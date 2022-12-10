from ultil import * 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

root = Tk()
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

style = ttk.Style(tabControl)


tabControl.add(tab1, text='Thước đo VaR')
tabControl.add(tab2, text='Thước đo Volatility')
tabControl.add(tab3, text='Biểu đồ biến động')
tabControl.pack(expand=1, fill='both')

root.title("Hệ thống định lượng rủi ro thị trường chứng khoán Việt Nam")
root.configure(bg='#FFB6C1')
root.geometry("1000x650")

labelTitle=Label(tab1,text="Hệ thống định lượng rủi ro thị trường chứng khoán Việt Nam",font = ("Quicksand", 17),foreground="black")
labelTitle.pack(side = "top")

labelTickerStockA = Label(tab1,text="Mã Index A",font=("Quicksand",12))
labelTickerStockA.place(x = 40 , y = 100)
comboboxStockA = ttk.Combobox(tab1,width=20)
comboboxStockA.place(x = 170 , y =100)

labelTickerStockB = Label(tab1,text="Mã Index B",font=("Quicksand",12))
labelTickerStockB.place(x = 40 , y = 140)
comboboxStockB=ttk.Combobox(tab1,width=20)
comboboxStockB.place(x = 170 , y =140)

labelTickerStockC=Label(tab1,text="Mã Index C",font=("Quicksand",12))
labelTickerStockC.place(x = 40 , y = 180)
comboboxStockC=ttk.Combobox(tab1,width=20)

labelTickerStockD = Label(tab1,text="Mã Index D",font=("Quicksand",12))
labelTickerStockD.place(x = 40 , y = 220)
comboboxStockD = ttk.Combobox(tab1,width=20)
comboboxStockD.place(x = 170 , y =220)

# trong so

labelWeightA = Label(tab1,text="Trọng số đầu tư A",font=("Quicksand",12))
labelWeightA.place(x = 350 , y = 100)
inputWeightA = Entry(tab1,width=20,borderwidth=2)
inputWeightA.place(x = 520 , y = 100)

labelWeightB=Label(tab1,text= "Trọng số đầu tư B",font=("Quicksand",12))
labelWeightB.place(x = 350 , y = 140)
inputWeightB = Entry(tab1,width=20,borderwidth=2)
inputWeightB.place(x = 520 , y =140)

labelWeightC=Label(tab1,text="Trọng số đầu tư C",font=("Quicksand",12))
labelWeightC.place(x = 350 , y = 180)
inputWeightC = Entry(tab1,width=20,borderwidth=2)
inputWeightC.place(x = 520 , y =180)
comboboxStockC.place(x = 170 , y =180)

labelWeightD = Label(tab1,text="Trọng số đầu tư D",font=("Quicksand",12))
labelWeightD.place(x = 350 , y = 220)
inputWeightD=Entry(tab1,width=20,borderwidth=2)
inputWeightD.place(x = 520 , y = 220)

labelDateStart=Label(tab1,text="Ngày bắt đầu",font=("Quicksand",12))
labelDateStart.place(x = 680 , y = 100)
dateEntryStart= DateEntry(tab1,width=20, date_pattern='y/mm/dd')
dateEntryStart.place(x = 800 , y = 100)

labelVaRTotal = Label(tab1, text="VaR95",font=("Quicksand",12))
labelVaRTotal.place(x=40, y=330)

labelVaRTotal = Label(tab1, text="VaR99",font=("Quicksand",12))
labelVaRTotal.place(x=40, y=360)

labelListMeasure = Label(tab1, text="Bảng giá trị",font=("Quicksand",12))
labelListMeasure.place(x=40,y=400)

comboboxStockSearch = ttk.Combobox(tab1,width=20)
comboboxStockSearch.place(x = 680 , y =270)

tree = ttk.Treeview(tab1, columns=("","Var95", "Var99"),show="headings",height=5)
tree.place(x=40,y=430)

selected = StringVar()

def selectedFunc(): 
    data = pd.DataFrame()
    if (selected.get() == 'HNX'):
        data = pd.read_csv('data/HNX.csv')
    if (selected.get() == 'HSX'):
        data = pd.read_csv('data/HSX.csv')
    
    listStock = data['Ticker'].tolist()

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

radioExchangeHSX = ttk.Radiobutton(tab1, text="Sàn HSX", width=30,variable= selected ,value='HSX', command=selectedFunc)
radioExchangeHSX.place(x=100, y= 50)

radioExchangeHNX = ttk.Radiobutton(tab1, text="Sàn HNX", width=30, variable= selected, value='HNX', command=selectedFunc)
radioExchangeHNX.place(x=200, y= 50)


##################################################################### tab2

labelTitleTab2=Label(tab2,text="Hệ thống định lượng rủi ro thị trường chứng khoán Việt Nam",font = ("Quicksand", 17),foreground="black")
labelTitleTab2.pack(side = "top")

def selectedFunc2(): 
    data2 = pd.DataFrame()
    if (selected2.get() == 'HNX'):
        data2 = pd.read_csv('data/HNX.csv')
    if (selected2.get() == 'HSX'):
        data2 = pd.read_csv('data/HSX.csv')
    
    listStock2 = data2['Ticker'].tolist()
    comboboxStockSearchTab2['values'] = listStock2
    comboboxStockSearchTab2.current(0)

selected2 = StringVar()

radioExchangeHSXTab2 = ttk.Radiobutton(tab2, text="Sàn HSX", width=30,variable= selected2 ,value='HSX', command=selectedFunc2)
radioExchangeHSXTab2.place(x=100, y= 50)

radioExchangeHNXTab2 = ttk.Radiobutton(tab2, text="Sàn HNX", width=30, variable= selected2, value='HNX', command=selectedFunc2)
radioExchangeHNXTab2.place(x=200, y= 50)

comboboxStockSearchTab2 = ttk.Combobox(tab2,width=20)
comboboxStockSearchTab2.place(x = 680 , y =270)

tree2 = ttk.Treeview(tab2, columns=("","Volatility Moth", "Volatility Year"),show="headings",height=5)
tree2.place(x=40,y=430)


################ tab3
labelTitleTab3=Label(tab3,text="Hệ thống định lượng rủi ro thị trường chứng khoán Việt Nam",font = ("Quicksand", 17),foreground="black")
labelTitleTab3.pack(side = "top")


def selectedFunc3(): 
    data3 = pd.DataFrame()
    if (selected3.get() == 'HNX'):
        data3 = pd.read_csv('data/HNX.csv')
    if (selected3.get() == 'HSX'):
        data3 = pd.read_csv('data/HSX.csv')
    
    listStock3 = data3['Ticker'].tolist()
    comboboxStockSearchTab3['values'] = listStock3
    comboboxStockSearchTab3.current(0)

selected3 = StringVar()

radioExchangeHSXTab3 = ttk.Radiobutton(tab3, text="Sàn HSX", width=30,variable= selected3 ,value='HSX', command=selectedFunc3)
radioExchangeHSXTab3.place(x=100, y= 50)

radioExchangeHNXTab3 = ttk.Radiobutton(tab3, text="Sàn HNX", width=30, variable= selected3, value='HNX', command=selectedFunc3)
radioExchangeHNXTab3.place(x=200, y= 50)

comboboxStockSearchTab3 = ttk.Combobox(tab3,width=20)
comboboxStockSearchTab3.place(x = 680 , y =270)





######################################## Function

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
        labelVaRTotal95 = Label(tab1, text=VaRList(dateTimeStart, stocks, listWeight),font=("Quicksand",12),bg='#FFB6C1')
        labelVaRTotal95.place(x=100, y=330)

        labelVaRTotal99 = Label(tab1, text=VaRList(dateTimeStart, stocks, listWeight),font=("Quicksand",12),bg='#FFB6C1')
        labelVaRTotal99.place(x=100, y=360)

        for item in tree.get_children():
            tree.delete(item)

        for stock in stocks:
            stock = str(stock)
            values = []
            values.append(stock)
            values.append(VaR(dateTimeStart, 0.05, stock))
            values.append(VaR(dateTimeStart, 0.01, stock))
            tree.column("#2", anchor=CENTER)
            tree.heading("#2",text="VaR95")
            tree.column("#3", anchor=CENTER)
            tree.heading("#3",text="VaR99")
            tree.insert('', END, values= values)

def searchVaR():
    stockTickerVaR = comboboxStockSearch.get()
    dateTimeStart = dateEntryStart.get().replace("/","-")

    status= True
    
    if not stockTickerVaR:
        messagebox.showerror('Error','Vui lòng điền đầy đủ thông tin')
        status = False
        return
    
    currentTime = dt.datetime.now().strftime("%Y-%m-%d")

    if (currentTime <= dateTimeStart):
        messagebox.showerror('Error','Vui lòng điền đầy đủ thông tin ngày bắt đầu')
        status = False
        return
    
    if (status):
        for item in tree.get_children():
            tree.delete(item)

        values = []
        values.append(stockTickerVaR)
        values.append(VaR(dateTimeStart, 0.05, stockTickerVaR))
        values.append(VaR(dateTimeStart, 0.01, stockTickerVaR))
        tree.column("#2", anchor=CENTER)
        tree.heading("#2",text="VaR95")
        tree.column("#3", anchor=CENTER)
        tree.heading("#3",text="VaR99")
        tree.insert('', END, values= values)
    
def searchVolatility():
    stockTickerVola = comboboxStockSearchTab2.get()

    status= True
    
    if not stockTickerVola:
        messagebox.showerror('Error','Vui lòng điền đầy đủ thông tin')
        status = False
        return
    
    if (status):
        values = []
        values.append(stockTickerVola)
        values.append(Volatility(stockTickerVola))
        values.append(Volatility(stockTickerVola))
        tree2.column("#2", anchor=CENTER)
        tree2.heading("#2",text="Volatility Moth")
        tree2.column("#3", anchor=CENTER)
        tree2.heading("#3",text="Volatility Year")
        tree2.insert('', END, values= values)

#btn tab1
btnResult = Button(tab1,text='Định lượng',foreground="blue", padx=5,command=quantitative).place(x=40, y=270)
btnSearch = Button(tab1,text='Tìm kiếm',foreground="blue",padx=5,command=searchVaR).place(x = 680 , y =300)

#btn search tab2
btnSearchVola = Button(tab2,text='Tìm kiếm',foreground="blue",padx=5,command=searchVolatility).place(x = 840 , y = 270)

#btn search tab3
btnSearcha = Button(tab3,text='Tìm kiếm',foreground="blue",padx=5,command=searchVolatility).place(x = 840 , y = 270)
mainloop()