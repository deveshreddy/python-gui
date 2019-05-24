import tkinter

mainwindow = tkinter.Tk()
mainwindow.title("Building windows - Advanced GUI")
mainwindow.geometry('640x480-8+200')
mainwindow['padx']=8

label = tkinter.Label(mainwindow,text = "nice way of looking at the world")
label.grid(row=0,column = 0, columnspan=3)

mainwindow.columnconfigure(0,weight =1)
mainwindow.columnconfigure(1,weight =1)
mainwindow.columnconfigure(2,weight =3)
mainwindow.columnconfigure(3,weight =3)
mainwindow.columnconfigure(4,weight =3)

mainwindow.rowconfigure(0,weight =1)
mainwindow.rowconfigure(1,weight= 10)
mainwindow.rowconfigure(2,weight =1)
mainwindow.rowconfigure(3,weight =3)
mainwindow.rowconfigure(4,weight =3)

#making the list box
fileList = tkinter.Listbox(mainwindow)
fileList.grid(row=1,column=0,sticky='nsew',rowspan=2)
fileList.config(border=2, relief = 'ridge')

import os
for zone in os.listdir('C:/Windows/System32'):
    fileList.insert(tkinter.END,zone)

listscroll = tkinter.Scrollbar(mainwindow, orient=tkinter.VERTICAL, command = fileList.yview)
listscroll.grid(row=1,column =1,sticky='nsw', rowspan=2)
fileList['yscrollcommand']=listscroll.set

#frame for radio buttons
optionFrame = tkinter.LabelFrame(mainwindow, text ="radio-zaone")
optionFrame.grid(row=1,column =2,sticky ='ne')

rbValue = tkinter.IntVar()
#set default value
rbValue.set(2)
#buttons begin here
radio1 = tkinter.Radiobutton(optionFrame, text = 'files', value = 1, variable = rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text = 'filez', value = 2, variable = rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text = 'filex', value = 3, variable = rbValue)

radio1.grid(row=0,column=0,sticky='w')
radio2.grid(row=1,column=0,sticky='w')

radio3.grid(row=2,column=0,sticky='w')

#for displaying the result
resultLabel = tkinter.Label(mainwindow, text = ' w r i t e')
resultLabel.grid(row=2,column=2,sticky='nw')
result = tkinter.Entry(mainwindow)
result.grid(row=2,column=2,sticky='sw')

#frame for time spinners
timeframe = tkinter.LabelFrame(mainwindow, text ='time time time')
timeframe.grid(row=3,column=0)
#time spinners
hourspinner = tkinter.Spinbox(timeframe,width=2,values=tuple(range(0,24)))
minutespinner = tkinter.Spinbox(timeframe,width=2,from_ = 0, to = 59)
secondspinner = tkinter.Spinbox(timeframe,width=2,from_ = 0, to = 59)

hourspinner.grid(row=0,column=0)
tkinter.Label(timeframe, text=':').grid(row=0,column=1)
minutespinner.grid(row=0,column=2)
tkinter.Label(timeframe,text=':').grid(row=0,column=3)
secondspinner.grid(row=0,column=4)
timeframe['padx']=36

#Frame for the date spinners
dateframe = tkinter.Frame(mainwindow)
dateframe.grid(row=4,column=0,sticky='new')

#Date Labels
daylabel = tkinter.Label(dateframe, text ='day')
monthlabel = tkinter.Label(dateframe, text = 'month')
yearlabel = tkinter.Label(dateframe, text='year')

daylabel.grid(row=0,column=0,sticky='new')
monthlabel.grid(row=0,column=1,sticky='new')
yearlabel.grid(row=0, column=2,sticky='new')

#date spinners
dayspin = tkinter.Spinbox(dateframe, width=5, from_=1, to = 31).grid(row=1,column=0)
monthspin = tkinter.Spinbox(dateframe, width = 5, values = ("jan", "feb", "mar","apr","may","jun","jul","aug","sep","oct","nov","dec")).grid(row=1,column=1)
yearspin = tkinter.Spinbox(dateframe, from_ = 2000, to = 2019).grid(row=1,column=2)


# adding final phase buttons

okbutton = tkinter.Button(mainwindow,text='OKAY')
cancelbutton = tkinter.Button(mainwindow, text ="cancel", command = mainwindow.destroy)
okbutton.grid(row =4 , column =3, sticky ='e')
cancelbutton.grid(row=4,column=4,sticky = 'w')



mainwindow.mainloop()
print(rbValue.get())

