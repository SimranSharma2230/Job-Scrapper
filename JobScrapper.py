import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PrivateJobs import PrivateJobs
from GovtJobs import GovtJobs




def scrapp():
    
    top=tk.Toplevel()
    top["bg"] = "white"
    p = PrivateJobs(top)
    p.mainloop()
def scrapg():
    
    top=tk.Toplevel()
    top["bg"] = "white"
    g = GovtJobs(top)
    g.mainloop()

def aboutus():
    tk.messagebox.showinfo("About Us","Prepared By: Simran and Himanshi")

def quit():
    top.destroy()

    
top = tk.Tk()
top.title("Job Scrapper")
top["bg"] = "white"

img1 = tk.PhotoImage(file='image\Logo.gif')
img = tk.PhotoImage(file='image\Benefits.gif')

lblLogo = tk.Label(top, image=img1, bg='white')
lblLogo.grid(row=0, column=0,columnspan=4,sticky=tk.E+tk.W)

lbl = tk.Label(top, text='                             ......a python scrapper', bg='orange', fg='blue', borderwidth = 0,font=3)
lbl.grid(row=1, column=0, columnspan=4 ,sticky=tk.E+tk.W)

btnPrivate = tk.Button(top, text='Private Jobs', command = scrapp, fg= 'dark blue', width=10, borderwidth = 1,font=10, activebackground='grey', activeforeground='white')
btnPrivate.grid(row=2, column=0,sticky=tk.E+tk.W)

btnGovt = tk.Button(top, text='Govt Jobs', command = scrapg, fg= 'dark blue', width=10, borderwidth = 1,font=10, activebackground='grey', activeforeground='white')
btnGovt.grid(row=2, column=1,sticky=tk.E+tk.W)

btnAboutUs = tk.Button(top, text='About Us', command = aboutus, fg= 'dark blue', width=10, borderwidth = 1,font=10, activebackground='grey', activeforeground='white')
btnAboutUs.grid(row=2, column=2,sticky=tk.E+tk.W)

btnQuit = tk.Button(top, text='Quit', command = quit, fg= 'dark blue', width=10, borderwidth = 1,font=10, activebackground='grey', activeforeground='white')
btnQuit.grid(row=2, column=3,sticky=tk.E+tk.W)


lblimg = tk.Label(top, image=img, bg='white')
lblimg.grid(row=3, column=0,columnspan=4)



lblFooter1 = tk.Label(top, text='About Web Scrapping...... concept used in Job Scrapper', bg='orange', fg='blue',width=50, borderwidth = 0,font=3)
lblFooter1.grid(row=4, column=0, columnspan=4 ,sticky=tk.E+tk.W)

msg = "Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites.Web scrapping is the process of automatically mining  data or collecting information from the World wide Web.  \n\nIt is the field of active developments sharing a common goal with the semantic web vision, an ambitious initiative that still requires breakthroughs in text processing, semantic understanding, artificial intelligence and human-computer interactions."

lblFooter = tk.Label(top, text=msg, bg='green', fg='white',width=50, borderwidth = 7,font=3,padx="0",wraplength=450 )
lblFooter.grid(row=5, column=0, columnspan=4 ,sticky=tk.E+tk.W)

top.mainloop()
