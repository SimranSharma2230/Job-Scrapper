from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from govt_indeed_code import Indeed


class GovtJobs(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        
    def init_window(self):
        
        self.master.title("Job Scrapper [Government Jobs]")

        img=PhotoImage(file="image\Logo.gif")
        lblLogo = Label(self.master, image=img, bg='white')
        lblLogo.image=img
        lblLogo.grid(row=0, column=0,columnspan=4,sticky=E+W)

        lbl = Label(self.master, text='                             ......a python scrapper', bg='orange', fg='blue', borderwidth = 0,font=3)
        lbl.grid(row=1, column=0, columnspan=4 ,sticky=E+W)
        
        l1=Label(self.master,text="Title",bg="white",padx='2',pady='4', font = 5)
        l1.grid(row=2,column=0,columnspan=2)

        self.d1=ttk.Combobox(self.master,state="readonly",values=["Railway","Bank","Teacher","Police"], font = 5)
        self.d1.current(0)
        self.d1.grid(row=2,column=2,columnspan=2)
        
        
        b2=Button(self.master,text="Find Jobs",command=self.find_job,padx=2,pady=5, fg= 'dark blue', width=10, borderwidth = 1,font=5, activebackground='grey', activeforeground='white')
        b2.grid(row=5,column=3)
        self.master.grid_rowconfigure(5,weight=5)

        lblFooter1 = Label(self.master, text='Why JobScrapper for government jobs ....', bg='orange', fg='blue',width=50, borderwidth = 0,font=3)
        lblFooter1.grid(row=6, column=0, columnspan=4 ,sticky=E+W)

        msg = "Opportunities in Central Government Jobs, State Government Jobs, Public Sector Companies, Public Sector Banks, Indian Railway, Army, Navy, Air Force and Government organizing Institutions, Organizations and Universities. Everyday 24X7, Job scrapper updating Free Govt Jobs Alert of Centraland State Govt Vacancies and Public Sector Jobs for all type of Job Seekers. \n\n Job Scrapper every day updating the Latest Govt Jobs, Govt Recruitment Vacancies in this application. 8th Pass, 10th Pass, 12th Pass, ITI, Diploma, MA, M.Com, MSW, MBA, MCA, ME, M.Tech etc.) and all other educational qualified Indian Citizens find your Qualification/ Eligibility wise Latest Govt Jobs 2019-20 and Upcoming Government Jobs 2019 Notifications listed in this applicatoin."

        lblFooter = Label(self.master, text=msg, bg='green', fg='white',width=50, borderwidth = 7,font=3,padx="0",wraplength=450 )
        lblFooter.grid(row=7, column=0, columnspan=4 ,sticky=E+W)
        


    def find_job(self):
        title = self.d1.current()

        tA0 = 'https://www.indeed.co.in/jobs?q=railway&l='
        tB0 = 'https://www.indeed.co.in/jobs?q=Government+Bank&l='
        tC0 = 'https://www.indeed.co.in/jobs?q=government+teacher&l='
        tD0 = 'https://www.indeed.co.in/jobs?q=government+police&l='
        
        govtindeedjobs=[tA0,tB0,tC0,tD0]

        url = govtindeedjobs[title]
        
        a=Indeed(url)
        a.retrive_jobs()
    


