import requests
import browserhistory as bh
from requests.packages.urllib3.connectionpool import HTTPConnectionPool
from tkinter import *

win = Tk()

TopFrame = Frame(win, width=1000)
# Title Picture
TitlePic = PhotoImage(file="Title.png")
TitleLabel = Label(TopFrame, image=TitlePic)

# Credit Picture
CreditPic = PhotoImage(file="Credit.png")
CreditLabel = Label(TopFrame, image=CreditPic)

ValueList = []

# User pics which browser they use
BrowserFrame = Frame(win, width=1000, height=100)
BrowserList = ["chrome", "firefox", "safari"]
BrowserChoice = 0

var = IntVar()
BrowserPicker1 = Radiobutton(BrowserFrame, text="Chrome", relief=RAISED, variable=var, value=0,
                             command=lambda: print(var.get()))
BrowserPicker2 = Radiobutton(BrowserFrame, text="Firefox", relief=RAISED, variable=var, value=1,
                             command=lambda: print(var.get()))
BrowserPicker3 = Radiobutton(BrowserFrame, text="Safari", relief=RAISED, variable=var, value=2,
                             command=lambda: print(var.get()))
StartScanButton = Button(BrowserFrame, text="START", command=lambda: BrowserCheck(var, BrowserList))

# Where the URLs will be
UrlText = Text(win, width=200)
S = Scrollbar(win)


# Gets the IP Address
def _make_request(self, conn, method, url, **kwargs):
    response = self._old_make_request(conn, method, url, **kwargs)
    sock = getattr(conn, 'sock', False)
    if sock:
        setattr(response, 'peer', sock.getpeername())
    else:
        setattr(response, 'peer', None)
    return response


HTTPConnectionPool._old_make_request = HTTPConnectionPool._make_request
HTTPConnectionPool._make_request = _make_request


# Links each URL with Its IP
def BrowserCheck(var, BrowserList):
    history = bh.get_browserhistory()
    history = history.get(BrowserList[var.get()])
    for i in range(len(history)):
        UrlIP = (history[i][0])
        r = requests.get(UrlIP)
        IPaddress = r.raw._original_response.peer
        IPaddress = str(IPaddress).replace("(", "").replace(")", "").replace("'", "")
        result = (UrlIP + " ---- " + IPaddress)
        UrlText.insert(INSERT, "\n"+result)
        print(result)


TopFrame.pack()
# Loads title image
TitleLabel.pack(side=LEFT)

# Loads credits image
CreditLabel.pack(side=RIGHT)

# Loads all widgets in the Browser frame
BrowserFrame.pack(side=TOP)
BrowserPicker1.pack(side=LEFT)
BrowserPicker2.pack(side=LEFT)
BrowserPicker3.pack(side=LEFT)
StartScanButton.pack(side=LEFT)

# Loads the URL frame
UrlText.pack(side=BOTTOM)
S.pack(side=RIGHT, fill=Y)
win.mainloop()
