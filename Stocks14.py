from tkinter import *
import tkinter
import urllib.request
import re
from PIL import ImageTk
import PIL.Image
import PIL
import sys
import tkinter as tk
from tkinter import *
import urllib.request
import webbrowser
from functools import partial
from tkinter import Tk, StringVar , ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
#import fix_yahoo_finance as yf
#yf.pdr_override()
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
from PIL import Image, ImageTk
import tkinter as tk
#from tkinter.ttk import *
import tkinter.font as tkFont
import datetime as dt
import pandas as pd
import numpy as np
from pandas_datareader import data as pdr
from urllib.request import urlopen
import simplejson as json




##path = rb"C:\Users\DellGold\PycharmProjects\PROJECTS\stock_market_514592.jpg"
master = Tk()
master.geometry("500x350")

##img = ImageTk.PhotoImage(Image.open(path))
##il = Label(master, image=img, width=500)
##il.place(x=0, y=0)
l2 = Label(master, text="WELCOME TO LIVE STOCK MARKET", font=("WELCOME TO LIVE STOCK MARKET", 20))
l2.place(x=5, y=0)


def Manage():
    PropsP1 = Toplevel(width=350, height=200)

    symbolist = ['avenue-supermarts-ltd/17875','tata-consultancy-services-ltd/4126', 'hcl-infosystems-ltd/3988','Infosys-ltd/4076',
                 'hdfc-bank-ltd/6082', 'state-bank-of-india/6012', 'wipro-ltd/770',
                 'oil-and-natural-gas-corporation-ltd/2791', 'kotak-mahindra-bank-ltd/7256', 'yes-bank-ltd/6169','larsen-and-toubro-infotech-ltd/17505','bajaj-finance-ltd/7302','bharat-petroleum-corporation-ltd/2824','icici-bank-ltd/6084','siemens-ltd/4289','bharat-heavy-electricals-ltd/5033','itc-ltd/3916','maruti-suzuki-india-ltd/48']

    def func(value):
        symbolist = value
        ##print('1.infosys\n2.tcs\n3.hcl\n4hdfc\n5.sbi\n6.wipro\n7.ongc\n8.kotak mahindra\n9.yes bank')
        ##i = int(input('enter ur choice'))
        i = 0

        htmlfile = urllib.request.urlopen('http://www.religareonline.com/company-fundamentals/' + symbolist)
        htmltext = htmlfile.read().decode('utf-8')
        regex = '<span id="CompanyHeader_div_ltp" class="s50 cGy3 ftPtSans lh40">(.+?)</span>'
        pattern = re.compile(regex)
        price = re.findall(pattern, htmltext)
        return (price)

    MedCRLabel = Label(PropsP1, text="Select the company name", font=("Select the company name", 20))
    MedCRLabel.place(x=15, y=6)

    variable = StringVar(PropsP1)
    variable.set("select")  # default value

    w = OptionMenu(PropsP1, variable, *symbolist)
    w.place(x=10, y=50)



    val =variable.get()

##B1=Button(PropsP1,text="PRINT VALUE")
##B1.place(x=50,y=100)
    menu = w.nametowidget(w.menuname)
    menu.configure(font=('BOLD', 15))


    def ok():
        n2 = Toplevel(width=300, height=200)
        val = variable.get()
        l1 = Label(n2, text="STOCK PRICE IS:", font=("STOCK PRICE IS:", 20))
        l1.place(x=5, y=50)
        l = Label(n2, text=func(val), font=(func(val), 20))
        l.place(x=5, y=100)


    button = Button(PropsP1, text="GO", command=ok)
    button.place(x=50, y=100)


def CurrencyConverter():
    ids = {"US Dollar": 'USD', "Euros": 'EUR', "Indian Rupees": 'INR', "Qatar Doha": 'QAR', "Zimbabwe Harare": 'ZWD',
           "Arab Emirates Dirham": 'AED', "Pound Sterling": 'GBP', "Japanese Yen": 'JPY', "Yuan Renminbi": 'CNY'}

    def convert(amt, frm, to):
        html = urllib.request.urlopen(
            "http://www.exchangerate-api.com/%s/%s/%f?k=99e83ad14b479bcc366858ed" % (frm, to, amt))
        return html.read().decode('utf-8')

    def callback():
        try:
            amt = float(in_field.get())

        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    root = Toplevel()
    root.title("Currency Converter")

    # initiate frame
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.pack(fill=BOTH, expand=1)
    titleLabel = Label(mainframe, text="Currency Converter", font=("Arial", 12, "bold"), justify=CENTER).grid(column=1,
                                                                                                              row=1)
    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    # Add input field
    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    # Add drop-down for input unit
    in_select = OptionMenu(mainframe, in_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha", "Zimbwabe Harare",
                           "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3,
                                                                                                           row=1,
                                                                                                           sticky=W)

    # Add output field and drop-down
    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "US Dollar", "Euros", "Indian Rupees", "Qatar Doha", "Zimbwabe Harare",
                           "Arab Emirates Dirham", "Pound Sterling", "Japanese Yen", "Yuan Renminbi").grid(column=3,
                                                                                                           row=3,
                                                                                                           sticky=W)

    calc_button = ttk.Button(mainframe, text="Calculate", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()



LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
lightColor = "#00A3E0"
darkColor = "#183A54"
style.use("dark_background")
f = plt.figure()
# g = plt.figure()
a = f.add_subplot(111)
exchange = "BTC"
ChangeCurrency = "BTC in USD"


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def changeExchange(toWha):
    global exchange

    exchange = toWha


def changeCurrency(toWhat):
    global ChangeCurrency

    ChangeCurrency = toWhat

def animate(i):
    if exchange == "BTC":
        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)
        '''data = pdr.get_data_yahoo('INFY', start="2018-03-06", end="2018-03-14")
        print(data)
        plt.legend()
        data[['High', 'Close']].plot()
        plt.show()'''
        dataLink = 'https://wex.nz/api/3/trades/btc_usd?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["btc_usd"]
        data = pd.DataFrame(data)

        data["datestamp"] = np.array((data["timestamp"]).astype("datetime64[s]"))
        dateStamps = data["datestamp"].tolist()

        # buys = data[(data['type'] == "bid")]
        # buys["datestamp"] = np.array((buys["timestamp"]).astype("datetime64[s]"))
        # buyDates = (buys["datestamp"]).tolist()

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        sellDates = (sells["datestamp"]).tolist()

        volume = data["amount"]

        a.clear()

        a.plot_date(sellDates, sells["price"], lightColor, label="price")
        # plt.xlabel('Time(Date)')
        # plt.ylabel('Volume and Price')
        a.set_ylabel("Price")
        a2.set_ylabel("Volume")
        a2.set_xlabel("Date(Time)")
        a2.fill_between(dateStamps, 0, volume, facecolor=darkColor)

        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
        a2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                 ncol=2, borderaxespad=0)

        title = "BitCoin Prices\nOpen :$8200 (-8.06%)\n Last Price:$ " + str(data["price"][0])
        # title1 = "Volume: " + str(data["amount"][1999])
        a.set_title(title)
        # a.set_title(title1)

    if exchange == "LTC":
        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)

        dataLink = 'https://wex.nz/api/3/trades/ltc_usd?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["ltc_usd"]
        data = pd.DataFrame(data)

        data["datestamp"] = np.array(data['timestamp'].apply(int)).astype("datetime64[s]")
        dateStamps = data["datestamp"].tolist()
        # allDates = data["datestamp"].tolist()

        buys = data[(data['type'] == "bid")]
        # buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
        buyDates = (buys["datestamp"]).tolist()

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        sellDates = (sells["datestamp"]).tolist()

        volume = data["amount"].apply(float).tolist()

        a.clear()

        a.plot_date(dateStamps, data["price"], darkColor, label="price")
        a.set_ylabel("Price")
        a2.set_ylabel("Volume")
        a2.set_xlabel("Date(Time)")

        a2.fill_between(dateStamps, 0, volume, facecolor=darkColor)

        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
        a2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                 ncol=2, borderaxespad=0)

        title = "LTC USD Prices\nLast Price:$ " + str(data["price"][0])
        a.set_title(title)

    if exchange == "ETH":
        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)

        dataLink = 'https://wex.nz/api/3/trades/eth_usd?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["eth_usd"]
        data = pd.DataFrame(data)

        data["datestamp"] = np.array(data['timestamp'].apply(int)).astype("datetime64[s]")
        dateStamps = data["datestamp"].tolist()
        # allDates = data["datestamp"].tolist()

        buys = data[(data['type'] == "bid")]
        # buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
        buyDates = (buys["datestamp"]).tolist()

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        sellDates = (sells["datestamp"]).tolist()

        volume = data["amount"].apply(float).tolist()

        a.clear()

        a.plot_date(dateStamps, data["price"], lightColor, label="price")
        a.set_ylabel("Price")
        a2.set_ylabel("Volume")
        a2.set_xlabel("Date(Time)")

        a2.fill_between(dateStamps, 0, volume, facecolor=darkColor)

        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
        a2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                 ncol=2, borderaxespad=0)

        title = "ETH USD Prices\nLast Price:$ " + str(data["price"][0])
        a.set_title(title)

    if exchange == "BCH":
        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)

        dataLink = 'https://wex.nz/api/3/trades/bch_usd?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["bch_usd"]
        data = pd.DataFrame(data)

        data["datestamp"] = np.array(data['timestamp'].apply(int)).astype("datetime64[s]")
        dateStamps = data["datestamp"].tolist()
        # allDates = data["datestamp"].tolist()

        buys = data[(data['type'] == "bid")]
        # buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
        buyDates = (buys["datestamp"]).tolist()

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        sellDates = (sells["datestamp"]).tolist()

        volume = data["amount"].apply(float).tolist()

        a.clear()

        a.plot_date(dateStamps, data["price"], lightColor, label="price")
        a.set_ylabel("Price")
        a2.set_ylabel("Volume")
        a2.set_xlabel("Date(Time)")

        a2.fill_between(dateStamps, 0, volume, facecolor=darkColor)

        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
        a2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                 ncol=2, borderaxespad=0)

        title = "BCH USD Prices\nLast Price:$ " + str(data["price"][0])
        a.set_title(title)

    if exchange == "DASH":
        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)

        dataLink = 'https://wex.nz/api/3/trades/dsh_usd?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["dsh_usd"]
        data = pd.DataFrame(data)

        data["datestamp"] = np.array(data['timestamp'].apply(int)).astype("datetime64[s]")
        dateStamps = data["datestamp"].tolist()
        # allDates = data["datestamp"].tolist()

        buys = data[(data['type'] == "bid")]
        # buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
        buyDates = (buys["datestamp"]).tolist()

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        sellDates = (sells["datestamp"]).tolist()

        volume = data["amount"].apply(float).tolist()

        a.clear()

        a.plot_date(dateStamps, data["price"], lightColor, label="price")
        a.set_ylabel("Price")
        a2.set_ylabel("Volume")
        a2.set_xlabel("Date(Time)")

        a2.fill_between(dateStamps, 0, volume, facecolor=darkColor)

        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
        a2.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                 ncol=2, borderaxespad=0)

        title = "DSH USD Prices\nLast Price:$ " + str(data["price"][0])
        a.set_title(title)

    if exchange == "ZEC":
        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)

        dataLink = 'https://wex.nz/api/3/trades/zec_usd?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["zec_usd"]
        data = pd.DataFrame(data)

        data["datestamp"] = np.array(data['timestamp'].apply(int)).astype("datetime64[s]")
        dateStamps = data["datestamp"].tolist()
        # allDates = data["datestamp"].tolist()

        buys = data[(data['type'] == "bid")]
        # buys["datestamp"] = np.array(buys["timestamp"]).astype("datetime64[s]")
        buyDates = (buys["datestamp"]).tolist()

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        sellDates = (sells["datestamp"]).tolist()

        volume = data["amount"].apply(float).tolist()

        a.clear()

        a.plot_date(dateStamps, data["price"], lightColor, label="price")
        a.set_ylabel("Price")
        a2.set_ylabel("Volume")
        a2.set_xlabel("Date(Time)")

        a2.fill_between(dateStamps, 0, volume, facecolor=darkColor)

        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M"))

        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3,
                 ncol=2, borderaxespad=0)

        title = "ZEC USD Prices\nLast Price:$ " + str(data["price"][0])
        a.set_title(title)


class Stocks(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        exchangeChoice = tk.Menu(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        exchangeChoice1 = tk.Menu(container)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command=lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        exchangeChoice = tk.Menu(menubar, tearoff=2)
        exchangeChoice.add_cascade(label="BTC", command=lambda: changeExchange("BTC"))

        exchangeChoice.add_command(label="LTC", command=lambda: changeExchange("LTC"))
        exchangeChoice.add_command(label="ETH", command=lambda: changeExchange("ETH"))

        exchangeChoice.add_command(label="BCH", command=lambda: changeExchange("BCH"))
        exchangeChoice.add_command(label="DASH", command=lambda: changeExchange("DASH"))
        exchangeChoice.add_command(label="ZEC", command=lambda: changeExchange("ZEC"))

        menubar.add_cascade(label="Exchange", menu=exchangeChoice)

        '''CurrencyCon = tk.Menu(menubar, tearoff=2)
        CurrencyCon.add_command(label="BTC in USD", command=lambda: changeCurrency("BTC in USD"))

        CurrencyCon.add_command(label="BTC in EURO", command=lambda: changeCurrency("BTC in EURO"))
        CurrencyCon.add_command(label="BTC in RUSSIAN", command=lambda: changeCurrency("BTC in RUSSIAN"))

        CurrencyCon.add_command(label="LTC in EURO", command=lambda: changeCurrency("LTC in EURO"))

        menubar.add_cascade(label="Change Currency", menu=CurrencyCon)'''

        tk.Tk.config(self, menu=menubar)

        self.frames = {}
        for F in (StartPage, PageOne, PageOne1, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="CryptoCurrency", font="Times 20 bold")
        label.grid()
        label1 = tk.Label(self, text="")
        label1.grid()

        rad1 = Radiobutton(self, text='Bitcoin (BTC)', value=1, command=lambda: controller.show_frame("PageOne"))

        rad2 = Radiobutton(self, text='LTC', value=2, command=lambda: controller.show_frame("PageThree"))

        rad3 = Radiobutton(self, text='ETH', value=3, command=lambda: controller.show_frame("PageTwo"))

        rad4 = Radiobutton(self, text='BCH', value=4, command=lambda: controller.show_frame("PageFive"))

        rad5 = Radiobutton(self, text='DASH', value=5, command=lambda: controller.show_frame("PageSix"))

        rad6 = Radiobutton(self, text='ZEC', value=6, command=lambda: controller.show_frame("PageSeven"))

        rad1.grid()

        rad2.grid()

        rad3.grid()

        rad4.grid()
        rad5.grid()
        rad6.grid()

        label2 = tk.Label(self, text="")
        label2.grid()

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.grid()
        button2.grid()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # logo = tk.PhotoImage(file="857.jpg")
        # w1 = tk.Label(self, image=logo).pack(side="right")

        label = tk.Label(self, text="BitCoin (BTC)", font="Times 20 bold", fg="red")
        label.grid()
        label01 = tk.Label(self, text="      ")
        label01.grid()
        label1 = tk.Label(self, text='''              Bitcoin is a cryptocurrency and worldwide payment system.
It is the first decentralized digital currency,    
                        as the system works without a central bank or single administrator.''', font="Times 15 italic")
        label1.grid()
        label04 = tk.Label(self, text="      ")
        label04.grid()
        label34 = tk.Label(self, text="      ")
        label34.grid()
        # Current price
        dataLink = 'https://wex.nz/api/3/trades/btc_usd?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["btc_usd"]
        data = pd.DataFrame(data)

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        # sellDates = (sells["datestamp"]).tolist()
        label011 = Label(self, text="Current Price In USD :$" + str(data["price"][0]), font="Times 15").place(x=180,y=130)
        #label011.grid()


        '''dataLink = 'https://wex.nz/api/3/trades/btc_eur?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["btc_eur"]
        data = pd.DataFrame(data)

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        # sellDates = (sells["datestamp"]).tolist()
        label012 = tk.Label(self, text="Last Price In EURO :$" + str(data["price"][0]), font="Times 15")
        label012.grid()

        dataLink = 'https://wex.nz/api/3/trades/btc_rur?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["btc_rur"]
        data = pd.DataFrame(data)

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        # sellDates = (sells["datestamp"]).tolist()
        label013 = tk.Label(self, text="Last Price In RUSSIAN :$" + str(data["price"][0]), font="Times 15")
        label013.grid()
        label014 = tk.Label(self, text="Last Price In RUPEE :$" + str((data["price"][0]) * 1.13), font="Times 15")
        label014.grid()'''

        label112 = tk.Label(self, text="      ")
        label112.grid()
        label14 = tk.Label(self, text="      ")
        label14.grid()
        widget0 = Button(self, text="In Euro", bg="white", fg="red", font=("Arial", 14, "bold"),
                         relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                         activebackground="green", activeforeground="blue",
                         command=lambda: controller.show_frame("PageOne1")).place(x=150, y=155)

        widget02 = Button(self, text="More Currencies", bg="white", fg="red", font=("Arial", 14, "bold"),
                          relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                          activebackground="green", activeforeground="blue",
                          command=CurrencyConverter).place(x=300, y=155)

        label06 = tk.Label(self, text="      ")
        label06.grid()
        label09 = tk.Label(self, text="      ")
        label09.grid()
        label000 = tk.Label(self, text="      ")
        label000.grid()
        label02 = tk.Label(self, text="OHLC (Open High Low Close) values of last 5 days....     ", font="Times 15")
        label02.grid()
        label03 = tk.Label(self, text="    ")
        label03.grid()

        label2 = tk.Label(self, text="      Date              Open          High                 Low             Close",
                          font="Times 12")
        label2.grid()
        label3 = tk.Label(self, text="20-05-2018          8000          7500                8500            8200",
                          font="Times 12")
        label3.grid()
        label4 = tk.Label(self, text="19-05-2018          8100          7900                9000            8100",
                          font="Times 12")
        label4.grid()
        label5 = tk.Label(self, text="18-05-2018          8200          7100                8900            8700",
                          font="Times 12")
        label5.grid()
        label6 = tk.Label(self, text="17-05-2018          8300          7600                7200            7900",
                          font="Times 12")
        label6.grid()

        label05 = tk.Label(self, text="      ")
        label05.grid()

        widget1 = Button(self, text="Live Graph", bg="white", fg="red", font=("Arial", 14, "bold"),
                         relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                         activebackground="green", activeforeground="blue", command=lambda: controller.show_frame("PageFour")).place(x=270,y=580)
        #button = tk.Button(self, text="Graph",
                           #command=lambda: controller.show_frame("PageFour"))
        #button.grid()


class PageOne1(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # logo = tk.PhotoImage(file="857.jpg")
        # w1 = tk.Label(self, image=logo).pack(side="right")

        label = tk.Label(self, text="BitCoin (BTC)", font="Times 20 bold", fg="red")
        label.grid()
        label01 = tk.Label(self, text="      ")
        label01.grid()
        label1 = tk.Label(self, text='''              Bitcoin is a cryptocurrency and worldwide payment system.
It is the first decentralized digital currency,    
                        as the system works without a central bank or single administrator.''', font="Times 15 italic")
        label1.grid()
        label04 = tk.Label(self, text="      ")
        label04.grid()
        # Current price
        dataLink = 'https://wex.nz/api/3/trades/btc_eur?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["btc_eur"]
        data = pd.DataFrame(data)

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        # sellDates = (sells["datestamp"]).tolist()
        label011 = Label(self, text="Current Price In Euro :" + str(data["price"][0]), font="Times 15").place(x=180,y=130)
        # label011.grid()

        '''dataLink = 'https://wex.nz/api/3/trades/btc_eur?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["btc_eur"]
        data = pd.DataFrame(data)

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        # sellDates = (sells["datestamp"]).tolist()
        label012 = tk.Label(self, text="Last Price In EURO :$" + str(data["price"][0]), font="Times 15")
        label012.grid()

        dataLink = 'https://wex.nz/api/3/trades/btc_rur?limit=1000'
        data = urlopen(dataLink)
        data = data.read().decode("utf-8")
        data = json.loads(data)

        data = data["btc_rur"]
        data = pd.DataFrame(data)

        sells = data[(data['type'] == "ask")]
        # sells["datestamp"] = np.array(sells["timestamp"]).astype("datetime64[s]")
        # sellDates = (sells["datestamp"]).tolist()
        label013 = tk.Label(self, text="Last Price In RUSSIAN :$" + str(data["price"][0]), font="Times 15")
        label013.grid()
        label014 = tk.Label(self, text="Last Price In RUPEE :$" + str((data["price"][0]) * 1.13), font="Times 15")
        label014.grid()'''

        label112 = tk.Label(self, text="      ")
        label112.grid()
        label14 = tk.Label(self, text="      ")
        label14.grid()
        widget0 = Button(self, text="In USD", bg="white", fg="red", font=("Arial", 14, "bold"),
                         relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                         activebackground="green", activeforeground="blue",
                         command=lambda: controller.show_frame("PageOne")).place(x=150, y=155)

        widget02 = Button(self, text="More Currencies", bg="white", fg="red", font=("Arial", 14, "bold"),
                          relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                          activebackground="green", activeforeground="blue",
                          command=CurrencyConverter).place(x=300, y=155)

        label06 = tk.Label(self, text="      ")
        label06.grid()
        label09 = tk.Label(self, text="      ")
        label09.grid()
        label000 = tk.Label(self, text="      ")
        label000.grid()
        label02 = tk.Label(self, text="OHLC (Open High Low Close) values of last 5 days....     ", font="Times 15")
        label02.grid()
        label03 = tk.Label(self, text="    ")
        label03.grid()

        label2 = tk.Label(self, text="      Date              Open          High                 Low             Close",
                          font="Times 12")
        label2.grid()
        label3 = tk.Label(self, text="20-05-2018          8000          7500                8500            8200",
                          font="Times 12")
        label3.grid()
        label4 = tk.Label(self, text="19-05-2018          8100          7900                9000            8100",
                          font="Times 12")
        label4.grid()
        label5 = tk.Label(self, text="18-05-2018          8200          7100                8900            8700",
                          font="Times 12")
        label5.grid()
        label6 = tk.Label(self, text="17-05-2018          8300          7600                7200            7900",
                          font="Times 12")
        label6.grid()

        label05 = tk.Label(self, text="      ")
        label05.grid()

        widget1 = Button(self, text="Live Graph", bg="white", fg="red", font=("Arial", 14, "bold"),
                         relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                         activebackground="green", activeforeground="blue",
                         command=lambda: controller.show_frame("PageFour")).place(x=270, y=580)
        # button = tk.Button(self, text="Graph",
        # command=lambda: controller.show_frame("PageFour"))
        # button.grid()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # logo = tk.PhotoImage(file="857.jpg")
        # w1 = tk.Label(self, image=logo).pack(side="right")

        label = tk.Label(self, text=" (LTC)", font="Times 20 bold", fg="red")
        label.grid()
        label01 = tk.Label(self, text="      ")
        label01.grid()
        label1 = tk.Label(self, text='''              Bitcoin is a cryptocurrency and worldwide payment system.
It is the first decentralized digital currency,    
                        as the system works without a central bank or single administrator.''', font="Times 15 italic")
        label1.grid()
        label04 = tk.Label(self, text="      ")
        label04.grid()
        label02 = tk.Label(self, text="OHLC (Open High Low Close) values of last 5 days....     ", font="Times 15")
        label02.grid()
        label03 = tk.Label(self, text="    ")
        label03.grid()

        label2 = tk.Label(self, text="      Date              Open          High                 Low             Close",
                          font="Times 12")
        label2.grid()
        label3 = tk.Label(self, text="20-05-2018          8000          7500                8500            8200",
                          font="Times 12")
        label3.grid()
        label4 = tk.Label(self, text="19-05-2018          8100          7900                9000            8100",
                          font="Times 12")
        label4.grid()
        label5 = tk.Label(self, text="18-05-2018          8200          7100                8900            8700",
                          font="Times 12")
        label5.grid()
        label6 = tk.Label(self, text="17-05-2018          8300          7600                7200            7900",
                          font="Times 12")
        label6.grid()

        label05 = tk.Label(self, text="      ")
        label05.grid()

        widget1 = Button(self, text="Live Graph", bg="white", fg="red", font=("Arial", 14, "bold"),
                         relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                         activebackground="green", activeforeground="blue",
                         command=lambda: controller.show_frame("PageFour")).place(x=270, y=580)
        '''button = tk.Button(self, text="Graph",
                           command=lambda: controller.show_frame("PageFour"))
        button.grid()'''


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # logo = tk.PhotoImage(file="857.jpg")
        # w1 = tk.Label(self, image=logo).pack(side="right")

        label = tk.Label(self, text=" (ETH)", font="Times 20 bold", fg="red")
        label.grid()
        label01 = tk.Label(self, text="      ")
        label01.grid()
        label1 = tk.Label(self, text='''              Bitcoin is a cryptocurrency and worldwide payment system.
It is the first decentralized digital currency,    
                        as the system works without a central bank or single administrator.''', font="Times 15 italic")
        label1.grid()
        label04 = tk.Label(self, text="      ")
        label04.grid()
        label02 = tk.Label(self, text="OHLC (Open High Low Close) values of last 5 days....     ", font="Times 15")
        label02.grid()
        label03 = tk.Label(self, text="    ")
        label03.grid()

        label2 = tk.Label(self, text="      Date              Open          High                 Low             Close",
                          font="Times 12")
        label2.grid()
        label3 = tk.Label(self, text="20-05-2018          8000          7500                8500            8200",
                          font="Times 12")
        label3.grid()
        label4 = tk.Label(self, text="19-05-2018          8100          7900                9000            8100",
                          font="Times 12")
        label4.grid()
        label5 = tk.Label(self, text="18-05-2018          8200          7100                8900            8700",
                          font="Times 12")
        label5.grid()
        label6 = tk.Label(self, text="17-05-2018          8300          7600                7200            7900",
                          font="Times 12")
        label6.grid()

        label05 = tk.Label(self, text="      ")
        label05.grid()

        widget1 = Button(self, text="Live Graph", bg="white", fg="red", font=("Arial", 14, "bold"),
                         relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                         activebackground="green", activeforeground="blue",
                         command=lambda: controller.show_frame("PageFour")).place(x=270, y=580)



class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text=" Live Graph")

        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()
        '''menubar = tk.Menu(self)
        fileMenu = tk.Menu(self)
        recentMenu = tk.Menu(self)

        menubar.add_cascade(label="File")
        fileMenu.add_cascade(label="Open Recent")
        for name in ("file1.txt", "file2.txt", "file3.txt"):
            recentMenu.add_command(label=name)
        tk.Tk.config(self, menubar=menubar)'''
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side="top", fill="x", pady=20)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side="top", fill="x", pady=20)


class PageFive(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # logo = tk.PhotoImage(file="857.jpg")
        # w1 = tk.Label(self, image=logo).pack(side="right")

        label = tk.Label(self, text=" (BCH)", font="Times 20 bold", fg="red")
        label.grid()
        label01 = tk.Label(self, text="      ")
        label01.grid()
        label1 = tk.Label(self, text='''              Bitcoin is a cryptocurrency and worldwide payment system.
It is the first decentralized digital currency,    
                        as the system works without a central bank or single administrator.''', font="Times 15 italic")
        label1.grid()
        label04 = tk.Label(self, text="      ")
        label04.grid()
        label02 = tk.Label(self, text="OHLC (Open High Low Close) values of last 5 days....     ", font="Times 15")
        label02.grid()
        label03 = tk.Label(self, text="    ")
        label03.grid()

        label2 = tk.Label(self, text="      Date              Open          High                 Low             Close",
                          font="Times 12")
        label2.grid()
        label3 = tk.Label(self, text="20-05-2018          8000          7500                8500            8200",
                          font="Times 12")
        label3.grid()
        label4 = tk.Label(self, text="19-05-2018          8100          7900                9000            8100",
                          font="Times 12")
        label4.grid()
        label5 = tk.Label(self, text="18-05-2018          8200          7100                8900            8700",
                          font="Times 12")
        label5.grid()
        label6 = tk.Label(self, text="17-05-2018          8300          7600                7200            7900",
                          font="Times 12")
        label6.grid()

        label05 = tk.Label(self, text="      ")
        label05.grid()

        widget1 = Button(self, text="Live Graph", bg="white", fg="red", font=("Arial", 14, "bold"),
                         relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                         activebackground="green", activeforeground="blue",
                         command=lambda: controller.show_frame("PageFour")).place(x=270, y=580)


class PageSix(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # logo = tk.PhotoImage(file="857.jpg")
        # w1 = tk.Label(self, image=logo).pack(side="right")

        label = tk.Label(self, text=" (DASH)", font="Times 20 bold", fg="red")
        label.grid()
        label01 = tk.Label(self, text="      ")
        label01.grid()
        label1 = tk.Label(self, text='''              Bitcoin is a cryptocurrency and worldwide payment system.
It is the first decentralized digital currency,    
                        as the system works without a central bank or single administrator.''', font="Times 15 italic")
        label1.grid()
        label04 = tk.Label(self, text="      ")
        label04.grid()
        label02 = tk.Label(self, text="OHLC (Open High Low Close) values of last 5 days....     ", font="Times 15")
        label02.grid()
        label03 = tk.Label(self, text="    ")
        label03.grid()

        label2 = tk.Label(self, text="      Date              Open          High                 Low             Close",
                          font="Times 12")
        label2.grid()
        label3 = tk.Label(self, text="20-05-2018          8000          7500                8500            8200",
                          font="Times 12")
        label3.grid()
        label4 = tk.Label(self, text="19-05-2018          8100          7900                9000            8100",
                          font="Times 12")
        label4.grid()
        label5 = tk.Label(self, text="18-05-2018          8200          7100                8900            8700",
                          font="Times 12")
        label5.grid()
        label6 = tk.Label(self, text="17-05-2018          8300          7600                7200            7900",
                          font="Times 12")
        label6.grid()

        label05 = tk.Label(self, text="      ")
        label05.grid()

        widget1 = Button(self, text="Live Graph", bg="white", fg="red", font=("Arial", 14, "bold"),
                         relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                         activebackground="green", activeforeground="blue",
                         command=lambda: controller.show_frame("PageFour")).place(x=270, y=580)


class PageSeven(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # logo = tk.PhotoImage(file="857.jpg")
        # w1 = tk.Label(self, image=logo).pack(side="right")

        label = tk.Label(self, text=" (ZEC)", font="Times 20 bold", fg="red")
        label.grid()
        label01 = tk.Label(self, text="      ")
        label01.grid()
        label1 = tk.Label(self, text='''              Bitcoin is a cryptocurrency and worldwide payment system.
It is the first decentralized digital currency,    
                        as the system works without a central bank or single administrator.''', font="Times 15 italic")
        label1.grid()
        label04 = tk.Label(self, text="      ")
        label04.grid()
        label02 = tk.Label(self, text="OHLC (Open High Low Close) values of last 5 days....     ", font="Times 15")
        label02.grid()
        label03 = tk.Label(self, text="    ")
        label03.grid()

        label2 = tk.Label(self, text="      Date              Open          High                 Low             Close",
                          font="Times 12")
        label2.grid()
        label3 = tk.Label(self, text="20-05-2018          8000          7500                8500            8200",
                          font="Times 12")
        label3.grid()
        label4 = tk.Label(self, text="19-05-2018          8100          7900                9000            8100",
                          font="Times 12")
        label4.grid()
        label5 = tk.Label(self, text="18-05-2018          8200          7100                8900            8700",
                          font="Times 12")
        label5.grid()
        label6 = tk.Label(self, text="17-05-2018          8300          7600                7200            7900",
                          font="Times 12")
        label6.grid()

        label05 = tk.Label(self, text="      ")
        label05.grid()

        widget1 = Button(self, text="Live Graph", bg="white", fg="red", font=("Arial", 14, "bold"),
                         relief=RAISED, bd=5, justify=CENTER, highlightbackground="red", overrelief=GROOVE,
                         activebackground="green", activeforeground="blue",
                         command=lambda: controller.show_frame("PageFour")).place(x=270, y=580)

def CryptoConverter():
            app = Stocks()
            ani = animation.FuncAnimation(f, animate, interval=5000)
            app.geometry('1280x720')
            app.mainloop()
'''def CryptoConverter():
    app = Stocks()
    ani = animation.FuncAnimation(f, animate, interval=5000)
    app.geometry('1280x720')'''

widget1 = Button(master, text="Currency converter", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=CurrencyConverter).place(x=50,y=125)
widget2 = Button(master, text="Crypto Currency", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=CryptoConverter).place(x=50,y=75)
widget3 = Button(master, text="Stocks", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=Manage).place(x=50,y=175)
widget4 = Button(master, text="QUIT", bg="white" , fg="red",font = ("Arial", 14, "bold"), relief = RAISED, bd=5, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "green", activeforeground="blue", command=master.quit).place(x=50,y=225)

'''b1 = Button(master, text='CURRENCY', command=CurrencyConverter, font=("Quit", 20))
b1.place(x=50, y=125)
b2 = Button(master, text='STOCKS', font=("START", 20), command=Manage)
b2.place(x=50, y=75)

b3 = Button(master, text='CRYPTOCURRENCY', font=("START", 20), command=CryptoConverter)
b3.place(x=50, y=175)

b3 = Button(master, text='QUIT', font=("START", 20), command=master.quit)
b3.place(x=50, y=225)'''



mainloop()
