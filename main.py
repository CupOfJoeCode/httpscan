import requests
import thread
import pygame as pg
import tkinter as tk
import easygui as gui

curnt = 0

def lbar():
    global curnt
    pg.init()
    icn = pg.Surface((32,32),pg.SRCALPHA)
    icn.fill((0,0,0,0))
    pg.display.set_icon(icn)
    d = pg.display.set_mode((400,32))
    while True:
        d.fill((0,0,0))
        pg.draw.rect(d,(0,255,0),(0,0,int(curnt/float(255)*400),32))
        pg.display.set_caption('Loading Bar ' + str(curnt) + '/255')
        pg.display.update()


thread.start_new_thread(lbar,())




def scanHttp():
    global ipEntry,portEntry,timEntry,ipList,curnt
    ipList.delete(0,tk.END)
    for i in range(0,256):
        try:
            r = requests.get("http://" + ipEntry.get() + '.' + str(i) + ':' + portEntry.get(),verify=False,timeout=float(timEntry.get()))
            code = r.status_code
            ipList.insert(tk.END,str(code) + ' - ' + str(ipEntry.get() + '.' + str(i) + ':' + portEntry.get()))
        except requests.ConnectionError:
            pass
        except Exception as e:
            gui.msgbox(str(e),'Error')
            return
        curnt = i

root = tk.Tk()
root.title("Http Server Scanner")
tk.Label(root,text="First 3 IP Address Numbers (eg. 192.168.0)").pack()
ipEntry = tk.Entry(root)
ipEntry.pack()

tk.Label(root,text="Port").pack()
portEntry = tk.Entry(root)
portEntry.insert(tk.END,'80')
portEntry.pack()

tk.Label(root,text="Timeout (sec)").pack()
timEntry = tk.Entry(root)
timEntry.insert(tk.END,'0.5')
timEntry.pack()


tk.Button(root,text='Scan',command=scanHttp).pack()

ipList = tk.Listbox(root)
ipList.pack()


root.mainloop()