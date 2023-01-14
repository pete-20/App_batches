import os
import tkinter as tk
from tkinter import font as font1
import subprocess
from subprocess import Popen, PIPE
from tkinter.ttk import *


top = tk.Tk()
top.title('Madzix')
top.geometry("390x342")
top.resizable(0, 0)
myFont = font1.Font(size=15, family='Helvetica',weight="bold")


import colorama
from colorama import init, Fore, Back, Style 
from datetime import date, datetime
from calendar import monthrange

#############################################################################################
#############################################################################################
#############################################################################################



def openNewWindow():
    def show_entry_fields():
        print("End date: %s\nStarting date: %s" % (date_components_1.get(), date_components_2.get()))

    ################################################################################################################
        dt = datetime.now()
        today = date.today()
        print('\n')
        print("Today's date:",today,',',dt.strftime('%A'))
        print('\n')
        date_components_3 = date_components_1.get().split('-')
        date_components_4 = date_components_2.get().split('-')
  
        
        year1, month1, day1 = [int(item) for item in date_components_3]

        d1 = date(year1, month1, day1)

        year2, month2, day2 = [int(item) for item in date_components_4]

        d2 = date(year2, month2, day2)

        delta=d1-d2

        newWindow2 = tk.Toplevel(newWindow)
        x = 'There are ' + str(delta.days) + ' days between ' + d1.strftime("%B") + ' ' + str(day1) + ', ' + str(year1) + ' (' + str(d1.strftime('%A')) + ')'
        y = '\n'+'and ' + d2.strftime("%B") + ' ' + str(day2) + ', ' + str(year2) + ' (' + str(d2.strftime('%A') + ').')
        my_text= Label(newWindow2, text= x +y, font=('Helvetica bold', 10))
        my_text.pack()
    ################################################################################################################


    newWindow = tk.Toplevel(top)

    logo = tk.PhotoImage(file="calendar.png")

    dupa = tk.Label(newWindow, image=logo)
    dupa.grid(row=3,column=0)
    dupa.image = logo

    tk.Label(newWindow, 
         text="End date",font=('Helvetica bold', 10)).grid(row=0,column=0)

    tk.Label(newWindow, 
         text="Starting date",font=('Helvetica bold', 10)).grid(row=1,column =0)

    tk.Label(newWindow, 
         text="Date format [YYYY-MM-DD]",font=('Helvetica bold', 7)).grid(row=3,column=1,sticky=tk.SE)

    date_components_1 = tk.Entry(newWindow)

    date_components_2 = tk.Entry(newWindow)


    date_components_1.grid(row=0, column=1)
    date_components_2.grid(row=1, column=1)

    tk.Button(newWindow, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.NE, 
                                                       padx=2)
#############################################################################################
#############################################################################################
#############################################################################################



def Bluetooth():
   os.system('cmd /c "%windir%\explorer.exe ms-settings:bluetooth"')

def WiFi():
   os.system('cmd /c "%windir%\explorer.exe ms-settings:network-wifi"')

def Unconnect():
   #proc = Popen([r"C:\!Python\Windows_batches\App_batches\App_batches\unconnect.bat"], shell=True,
   #          stdin=None, stdout=None, stderr=None, close_fds=True)
   os.system("net use * /delete /y")
def Ethernet():
   os.system('cmd /c "%windir%\explorer.exe ms-settings:network-ethernet"')

def Explorer():
    os.system('cmd /c "%windir%\explorer.exe"')

def Calculator():
    subprocess.call([r"calc.exe"])

def DaysCounter():
    #proc1 = Popen([r"C:\!Python\Windows_batches\App_batches\App_batches\days_counter.exe"], shell=True,
    #         stdin=None, stdout=None, stderr=None, close_fds=True)
    #subprocess.call([r"C:\!Python\Windows_batches\App_batches\App_batches\days_counter.exe"], shell=True)
    
    openNewWindow()
    """
    os.system("mode con cols=69 lines=37")

    init(convert=True)

#########################################################
    print(Style.BRIGHT + Fore.BLUE + Back.BLACK + '''                                                                                                                
                                                                                              ''')

    dt = datetime.now()
    today = date.today()

    print(Style.BRIGHT + Fore.WHITE + "Today's date:",today,',',dt.strftime('%A'))
    print('\n')

    def days_in_month(year=2019, month=2):
        return monthrange(year, month)[1]

    y=days_in_month(2022, 10)

    obecny = int(today.strftime("%d"))

    date_components_1 = input('Enter an end date formatted as YYYY-MM-DD: ').split('-')
    print('\n')

    year1, month1, day1 = [int(item) for item in date_components_1]

    d1 = date(year1, month1, day1)

    date_components_2 = input('Enter a starting date formatted as YYYY-MM-DD: ').split('-')
    print('\n')

    year2, month2, day2 = [int(item) for item in date_components_2]

    d2 = date(year2, month2, day2)

    delta=d1-d2

    print('There are ' + str(delta.days) + ' days between ' + d1.strftime("%B") + ' ' + str(day1) + ', ' + str(year1) + ' (' + str(d1.strftime('%A')) + ')' )

    print('and ' + d2.strftime("%B") + ' ' + str(day2) + ', ' + str(year2) + ' (' + str(d2.strftime('%A') + ').'))


    input("\nPress enter to exit...")

    """
def Excel2023():
    proc2 = Popen([r"C:\!MF\OneDrive\2023.xlsx"], shell=True,
                  stdin=None, stdout=None, stderr=None, close_fds=True)

def ExcelFIN():
    proc3 = Popen([r"C:\!MF\OneDrive\FIN.xlsx"], shell=True,
                  stdin=None, stdout=None, stderr=None, close_fds=True)

def Snipping():
    subprocess.call([r'C:\\Windows\System32\SnippingTool.exe', '/clip'])

  
Bsc =  tk.Button(top, text ="Bluetooth", command = Bluetooth, height= 4, width=10, bg='#0052cc', fg='#ffffff')
Wsc =  tk.Button(top, text ="Wi-Fi", command = WiFi,height= 4, width=10, bg='#0052cc', fg='#ffffff')
Usc =  tk.Button(top, text ="Unconnect", command = Unconnect,height= 4, width=10, bg='#0052cc', fg='#ffffff')
Esc =  tk.Button(top, text ="Ethernet", command = Ethernet,height= 4, width=10, bg='#0052cc', fg='#ffffff')
Exsc = tk.Button(top, text ="Explorer", command = Explorer,height= 4, width=10, bg='green', fg='#ffffff')
Csc =  tk.Button(top, text ="Calculator", command = Calculator,height= 4, width=10, bg='#0052cc', fg='#ffffff')
Dcsc = tk.Button(top, text ="Days counter",wraplength=80, command = DaysCounter,height= 4, width=10, bg='#0052cc', fg='#ffffff')
Ssc =  tk.Button(top, text ="Screenshot", command = Snipping,height= 4, width=10, bg='#0052cc', fg='#ffffff')
Excel2023sc = tk.Button(top, text ="2023", command = Excel2023,height= 1, width=10, bg='#0052cc', fg='#ffffff')
ExcelFINsc= tk.Button(top, text ="FIN", command = ExcelFIN,height= 2, width=10, bg='#0052cc', fg='#ffffff')


Bsc['font'] = myFont
Wsc['font'] = myFont
Usc['font'] = myFont
Esc['font'] = myFont
Exsc['font'] = myFont
Csc['font'] = myFont
Dcsc['font'] = myFont
Ssc['font'] = myFont
Excel2023sc['font'] = myFont
ExcelFINsc['font'] = myFont


Bsc.grid(row=2,column=0,sticky="NSEW")
Bsc.place()
Wsc.grid(row=1,column=0,sticky="NSEW")
Wsc.place()
Usc.grid(row=3,column=0,sticky="NSEW")
Usc.place()
Esc.grid(row=1,column=1,sticky="NSEW")
Esc.place()
Exsc.grid(row=2,column=1,sticky="NSEW")
Exsc.place()
Csc.grid(row=3,column=1,sticky="NSEW")
Csc.place()
Dcsc.grid(row=1,column=2,sticky="NSEW")
Dcsc.place()
Ssc.grid(row=2,column=2,sticky="NSEW")
Ssc.place()
Excel2023sc.grid(row=3,column=2,ipady= 2,sticky='n')
Excel2023sc.place()
ExcelFINsc.grid(row=3,column=2,ipady= 1,sticky='s')
ExcelFINsc.place()


top.mainloop()

