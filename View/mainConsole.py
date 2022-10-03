import tkinter as tk                    
from tkinter import ttk

class mainConsole():
    def viewMain():
        root = tk.Tk()
        root.title("Dashboard")
        root.geometry("800x600")

        def openRegSettingWindow():
            from View.regSetting import regSetting
            regSetting.viewRegSetting()

        tabControl = ttk.Notebook(root)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab1, text ='Facebook')
        tabControl.add(tab2, text ='Tiktok')
        tabControl.pack(expand = 1, fill ="both")

        regSetting=ttk.Button(tab1, text="Reg",command=openRegSettingWindow)
        regSetting.grid(column=0,row=1,padx=15, pady=15)
        ttk.Label(tab2,text ="Lets dive into the\world of computers").grid(column = 0,row = 0,padx = 30,pady = 30)

        root.mainloop()
