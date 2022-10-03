import io
import os
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import _thread
import threading
import sys
from EmulatorClick.LdClick import EmulatorClick


class regSetting():
    mailPathVar = ""
    proxyPathVar = ""
    thNumVar = int

    def viewRegSetting():
        root = tk.Tk()
        root.title("Reg Setting")
        root.geometry("650x500")
        root.lift()

        def insertPath(any,a=str):
            any.insert(0,a)
            pass
        def selectFile():
            global fileName
            filetypes=(('text files','*.txt'),('All files','*.*'))
            fileName = filedialog.askopenfilename(
                title='Open a file',
                initialdir='/',
                filetypes=filetypes
            )
            return fileName
        def stopService():
            
            sys.exit()
        def startAppiumPort():
            global thNumVar

            if int(thNum.get()) > 0:
                thNumVar = int(thNum.get())
                for i in range(thNumVar):
                    p = 4723+i
                    os.system('appium -p '+str(p))
                # threading.Thread._delete()
            else: 
                messagebox.showerror("Error","Hay nhap du thong tin")
        def startReg():
            global mailPathVar
            global proxyPathVar
            def ld(a):
                EmulatorClick.regFb(a, mailPathVar, proxyPathVar)
                _thread.join()
                pass
            if mailPath.get() != '' and proxyPath.get() != '' and int(thNum.get()) > 0:
                # root.withdraw()
                mailPathVar = mailPath.get()
                proxyPathVar = proxyPath.get()
                # startAppiumPort()
                try:
                    for i in range(int(thNum.get())):
                        f=io.open(mailPath.get(),'r',encoding='utf-8')
                        mailList = f.readlines()
                        f.close()
                        if mailList[i] != '':
                            _thread.start_new_thread(ld, (i, ))
                except:
                    print('Error: khong the bat dau thread')
                while 1:
                    pass
                
            else: 
                messagebox.showerror("Error","Hay nhap du thong tin")


        mail=Label(root,text="Hotmail Path: ")
        mail.grid(column=0, row=0,padx=15,pady=15)
        mailPath=Entry(root, width=45)
        mailPath.grid(column=1, row=0,padx=15,pady=15)
        fileBrowser=ttk.Button(root, text="Select File", command= lambda:[insertPath(mailPath, selectFile())])
        fileBrowser.grid(column=2, row=0,padx=15,pady=15)
        start = ttk.Button(root, text="Start", command=threading.Thread(target=startReg).start)
        start.grid(column=3, row=0 ,padx=15, pady=15)

        proxy=Label(root, text="Proxy Path: ")
        proxy.grid(column=0, row=1, padx=15, pady=15)
        proxyPath=Entry(root, width=45)
        proxyPath.grid(column=1, row=1,padx=15,pady=15)
        fileBrowser=ttk.Button(root, text="Select File", command= lambda:[insertPath(proxyPath, selectFile())])
        fileBrowser.grid(column=2, row=1,padx=15,pady=15)
        stop = ttk.Button(root, text='Stop', command=threading.Thread(target=stopService).start)
        stop.grid(column=3, row=1,padx=15,pady=15)

        th=Label(root, text="Thread: ")
        th.grid(column=0, row=2, padx=15, pady=15)
        thNum=Spinbox(root, from_=0, to=50, font=5)
        thNum.grid(column=1, row=2,padx=15,pady=15)
        prepara = ttk.Button(root, text='Prepare', command=threading.Thread(target=startAppiumPort).start)
        prepara.grid(column=2, row=2,padx=15,pady=15)


        root.mainloop()
regSetting.viewRegSetting()