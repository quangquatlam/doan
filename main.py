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

root.title("Hệ thống định lượng rủi ro thị trường chứng khoán Việt Nam")
root.configure(bg='#FFB6C1')
root.geometry("1024x720")


tabControl.add(tab1, text='Biểu đồ biến động')
tabControl.add(tab2, text='Thước đo VaR')
tabControl.add(tab3, text='Thước đo Volatility')
tabControl.pack(expand=1, fill='both')

#tab1

labelTitle1=Label(tab1,text="Biểu đồ biến động thị trường chứng khoán Việt Nam",font = ("Quicksand", 17),foreground="black")
labelTitle1.pack(side = "top", pady=(20,0))

labelSelectExchangesTab1 = Label(tab1,text="Vui lòng chọn sàn giao dịch",font=("Quicksand",12))
labelSelectExchangesTab1.place(x = 100 , y = 100)


selected1 = StringVar()


def selectedFuncTab1(): 
    data = pd.DataFrame()
    if (selected1.get() == 'HNX'):
        data = pd.read_csv('data/HNX.csv')
    if (selected1.get() == 'HSX'):
        data = pd.read_csv('data/HSX.csv')

    listStock = data['Ticker'].tolist()

    cbStockTab1['values'] = listStock
    cbStockTab1.current(0)

rbHSXTab1 = ttk.Radiobutton(tab1, text="Sàn HSX", width=20,variable= selected1 ,value='HSX', command=selectedFuncTab1)
rbHSXTab1.place(x=400, y= 100)

rbHNXTab1 = ttk.Radiobutton(tab1, text="Sàn HNX", width=20, variable= selected1, value='HNX', command=selectedFuncTab1)
rbHNXTab1.place(x=600, y= 100)

labelSelectStockTab1 = Label(tab1,text="Mã Index",font=("Quicksand",12))
labelSelectStockTab1.place(x = 100 , y = 150)

cbStockTab1 = ttk.Combobox(tab1,width=20)
cbStockTab1.place(x = 300 , y = 150)

labelDateStartTab1=Label(tab1,text="Từ ngày",font=("Quicksand",12))
labelDateStartTab1.place(x = 100 , y = 200)
dateEntryStartTab1= DateEntry(tab1,width=20, date_pattern='y/mm/dd')
dateEntryStartTab1.place(x = 300 , y = 200)

labelDateEndTab1=Label(tab1,text="Đến ngày",font=("Quicksand",12))
labelDateEndTab1.place(x = 100 , y = 250)
dateEntryEndTab1= DateEntry(tab1,width=20, date_pattern='y/mm/dd')
dateEntryEndTab1.place(x = 300 , y = 250)

def viewChart():
    status = True
    stockMarket = cbStockTab1.get()

    if not stockMarket:
        messagebox.showerror('Error','Vui lòng điền thông tin mã index')
        status = False
        return
    
    dateTimeStartTab1 = dateEntryStartTab1.get().replace("/","-")
    dateTimeEndTab1 = dateEntryEndTab1.get().replace("/","-")
    
    if (dateTimeStartTab1 >= dateTimeEndTab1):
        messagebox.showerror('Error','Ngày bắt đầu và kết thúc không hợp lệ')
        status = False
        return
    
    currentTime = dt.datetime.now().strftime("%Y-%m-%d")

    if (currentTime <= dateTimeEndTab1):
        messagebox.showerror('Error','Ngày kết thúc không hợp lệ')
        status = False
        return
    
    if status:
        Draw(stockMarket,dateTimeStartTab1,dateTimeEndTab1)

#btn tab1
btnViewChart = Button(tab1,text='Xem biểu đồ',foreground="blue",padx=5,command=viewChart).place(x = 100 , y = 320)

#########################tab2

labelTitle2=Label(tab2,text="Hệ thống định lượng rủi ro thị trường chứng khoán Việt Nam",font = ("Quicksand", 17),foreground="black")
labelTitle2.pack(side = "top")

labelTickerStockA = Label(tab2,text="Mã Index A",font=("Quicksand",12))
labelTickerStockA.place(x = 40 , y = 100)
comboboxStockA = ttk.Combobox(tab2,width=20)
comboboxStockA.place(x = 170 , y =100)

labelTickerStockB = Label(tab2,text="Mã Index B",font=("Quicksand",12))
labelTickerStockB.place(x = 40 , y = 140)
comboboxStockB=ttk.Combobox(tab2,width=20)
comboboxStockB.place(x = 170 , y =140)

labelTickerStockC=Label(tab2,text="Mã Index C",font=("Quicksand",12))
labelTickerStockC.place(x = 40 , y = 180)
comboboxStockC=ttk.Combobox(tab2,width=20)

labelTickerStockD = Label(tab2,text="Mã Index D",font=("Quicksand",12))
labelTickerStockD.place(x = 40 , y = 220)
comboboxStockD = ttk.Combobox(tab2,width=20)
comboboxStockD.place(x = 170 , y =220)

# trong so

labelWeightA = Label(tab2,text="Trọng số đầu tư A",font=("Quicksand",12))
labelWeightA.place(x = 350 , y = 100)
inputWeightA = Entry(tab2,width=20,borderwidth=2)
inputWeightA.place(x = 520 , y = 100)

labelWeightB=Label(tab2,text= "Trọng số đầu tư B",font=("Quicksand",12))
labelWeightB.place(x = 350 , y = 140)
inputWeightB = Entry(tab2,width=20,borderwidth=2)
inputWeightB.place(x = 520 , y =140)

labelWeightC=Label(tab2,text="Trọng số đầu tư C",font=("Quicksand",12))
labelWeightC.place(x = 350 , y = 180)
inputWeightC = Entry(tab2,width=20,borderwidth=2)
inputWeightC.place(x = 520 , y =180)
comboboxStockC.place(x = 170 , y =180)

labelWeightD = Label(tab2,text="Trọng số đầu tư D",font=("Quicksand",12))
labelWeightD.place(x = 350 , y = 220)
inputWeightD=Entry(tab2,width=20,borderwidth=2)
inputWeightD.place(x = 520 , y = 220)

labelDateStart=Label(tab2,text="Ngày bắt đầu",font=("Quicksand",12))
labelDateStart.place(x = 680 , y = 100)
dateEntryStart= DateEntry(tab2,width=20, date_pattern='y/mm/dd')
dateEntryStart.place(x = 800 , y = 100)

labelVaRTotal = Label(tab2, text="VaR95",font=("Quicksand",12))
labelVaRTotal.place(x=40, y=330)

labelVaRTotal = Label(tab2, text="VaR99",font=("Quicksand",12))
labelVaRTotal.place(x=40, y=360)

labelListMeasure = Label(tab2, text="Bảng giá trị",font=("Quicksand",12))
labelListMeasure.place(x=40,y=400)

comboboxStockSearch = ttk.Combobox(tab2,width=20)
comboboxStockSearch.place(x = 680 , y =270)

def displayChart(e):
    rowSelected = tree.focus()
    values = tree.item(rowSelected, 'values')
    drawCharVar(values[5],values[0])

tree = ttk.Treeview(tab2, columns=("","VaR95", "VaR99","CVaR95", "CVaR99", "Date"),show="headings",height=5)
tree.place(x=40,y=430)
tree.bind('<Double-1>', displayChart)

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

labelSelectMarket = Label(tab2, text="Chọn sàn giao dịch",font=("Quicksand",12))
labelSelectMarket.place(x=50,y=50)

radioExchangeHSX = ttk.Radiobutton(tab2, text="Sàn HSX", width=30,variable= selected ,value='HSX', command=selectedFunc)
radioExchangeHSX.place(x=400, y= 50)

radioExchangeHNX = ttk.Radiobutton(tab2, text="Sàn HNX", width=30, variable= selected, value='HNX', command=selectedFunc)
radioExchangeHNX.place(x=600, y= 50)

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
        labelVaRTotal95 = Label(tab2, text=VaRList(dateTimeStart, stocks, listWeight, 0.05),font=("Quicksand",12))
        labelVaRTotal95.place(x=100, y=330)

        labelVaRTotal99 = Label(tab2, text=VaRList(dateTimeStart, stocks, listWeight, 0.01),font=("Quicksand",12))
        labelVaRTotal99.place(x=100, y=360)

        for item in tree.get_children():
            tree.delete(item)

        for stock in stocks:
            stock = str(stock)
            values = []
            values.append(stock)
            values.append(VaRHistorical(dateTimeStart, 0.05, stock))
            values.append(VaRHistorical(dateTimeStart, 0.01, stock))
            values.append(CVaRHistorical(dateTimeStart, 0.05, stock))
            values.append(CVaRHistorical(dateTimeStart, 0.01, stock))
            values.append(dateTimeStart)
            tree.column("#2", anchor=CENTER)
            tree.heading("#2",text="VaR95")
            tree.column("#3", anchor=CENTER)
            tree.heading("#3",text="VaR99")
            tree.column("#4", anchor=CENTER)
            tree.heading("#4",text="CVaR95")
            tree.column("#5", anchor=CENTER)
            tree.heading("#5",text="CVaR99")
            tree.column("#6", anchor=CENTER, width=0, minwidth=0)
            tree.heading("#6")
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
        values.append(VaRHistorical(dateTimeStart, 0.05, stockTickerVaR))
        values.append(VaRHistorical(dateTimeStart, 0.01, stockTickerVaR))
        values.append(CVaRHistorical(dateTimeStart, 0.05, stockTickerVaR))
        values.append(CVaRHistorical(dateTimeStart, 0.01, stockTickerVaR))
        values.append(dateTimeStart)
        tree.column("#2", anchor=CENTER)
        tree.heading("#2",text="VaR95")
        tree.column("#3", anchor=CENTER)
        tree.heading("#3",text="VaR99")
        tree.column("#4", anchor=CENTER)
        tree.heading("#4",text="CVaR95")
        tree.column("#5", anchor=CENTER)
        tree.heading("#5",text="CVaR99")
        tree.column("#6", anchor=CENTER, width=0, minwidth=0)
        tree.heading("#6")
        tree.insert('', END, values= values)

def viewChartVar():
    stockTickerA = comboboxStockA.get()
    stockTickerB = comboboxStockB.get()
    stockTickerC = comboboxStockC.get()
    stockTickerD = comboboxStockD.get()

    stocks = [stockTickerA, stockTickerB, stockTickerC, stockTickerD]

    dateTimeStart = dateEntryStart.get().replace("/","-")
    status = True

    currentTime = dt.datetime.now().strftime("%Y-%m-%d")

    if (currentTime <= dateTimeStart):
        messagebox.showerror('Error','Vui lòng điền đầy đủ thông tin ngày bắt đầu')
        status = False
        return
    
    if (status):
        viewChartVarDraw(stocks,dateTimeStart)


btnResultTab2 = Button(tab2,text='Định lượng',foreground="blue", padx=5,command=quantitative).place(x=40, y=270)
btnSearch = Button(tab2,text='Tìm kiếm',foreground="blue",padx=5,command=searchVaR).place(x = 680 , y =300)
btnViewChart = Button(tab2,text='Biểu đồ biến động',foreground="blue",padx=5,command=viewChartVar).place(x = 140 , y =270)

##################################################################### tab3

labelTitleTab3 =Label(tab3,text="Hệ thống định lượng rủi ro thị trường chứng khoán Việt Nam",font = ("Quicksand", 17),foreground="black")
labelTitleTab3.pack(side = "top")

def selectedFunc2(): 
    data2 = pd.DataFrame()
    if (selected3.get() == 'HNX'):
        data2 = pd.read_csv('data/HNX.csv')
    if (selected3.get() == 'HSX'):
        data2 = pd.read_csv('data/HSX.csv')
    
    listStock2 = data2['Ticker'].tolist()
    comboboxStockSearchTab3['values'] = listStock2
    comboboxStockSearchTab3.current(0)


tree2 = ttk.Treeview(tab3, columns=("","Volatility Moth", "Volatility Year"),show="headings",height=5)
tree2.place(x=40,y=430)


################ tab3
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

labelStockMarket = Label(tab3, text="Mã Index",font=("Quicksand",12))
labelStockMarket.place(x=100, y=150)

comboboxStockSearchTab3 = ttk.Combobox(tab3,width=20)
comboboxStockSearchTab3.place(x = 250 , y =150)

labelDateStartTab3=Label(tab3,text="Từ ngày",font=("Quicksand",12))
labelDateStartTab3.place(x = 100 , y = 200)
dateEntryStartTab3= DateEntry(tab3,width=20, date_pattern='y/mm/dd')
dateEntryStartTab3.place(x = 250 , y = 200)

labelDateEndTab3=Label(tab3,text="Đến ngày",font=("Quicksand",12))
labelDateEndTab3.place(x = 100 , y = 250)
dateEntryEndTab3= DateEntry(tab3,width=20, date_pattern='y/mm/dd')
dateEntryEndTab3.place(x = 250 , y = 250)

######################################## Function

def searchVolatility():
    stockTickerVola = comboboxStockSearchTab3.get()
    dateTimeStartTab3 = dateEntryStartTab3.get().replace("/","-")
    dateTimeEndTab3 = dateEntryEndTab3.get().replace("/","-")

    status= True
    
    if not stockTickerVola:
        messagebox.showerror('Error','Vui lòng điền đầy đủ thông tin')
        status = False
        return
    
    if (dateTimeStartTab3 >= dateTimeEndTab3):
        messagebox.showerror('Error','Ngày bắt đầu và kết thúc không hợp lệ')
        status = False
        return
    
    currentTime = dt.datetime.now().strftime("%Y-%m-%d")

    if (currentTime <= dateTimeEndTab3):
        messagebox.showerror('Error','Ngày kết thúc không hợp lệ')
        status = False
        return
    
    if (status):
        values = []
        values.append(stockTickerVola)
        values.append(Volatility(stockTickerVola,dateTimeStartTab3,dateTimeEndTab3,20 ))
        values.append(Volatility(stockTickerVola,dateTimeStartTab3,dateTimeEndTab3,252 ))
        tree2.column("#2", anchor=CENTER)
        tree2.heading("#2",text="Volatility Moth")
        tree2.column("#3", anchor=CENTER)
        tree2.heading("#3",text="Volatility Year")
        tree2.insert('', END, values= values)

#bn tab3
btnSearchVola = Button(tab3,text='Tìm kiếm',foreground="blue",padx=5,command=searchVolatility).place(x = 100 , y = 300)

mainloop()