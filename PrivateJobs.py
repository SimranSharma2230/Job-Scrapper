from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from timesjob_code import times_job
from indeed_code import Indeed
from simplyHired_code import SimplyHired


class PrivateJobs(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        
    def init_window(self):
        
        self.master.title("Job Scrapper [Private Jobs]")

        img=PhotoImage(file="image\Logo.gif")
        lblLogo = Label(self.master, image=img, bg='white')
        lblLogo.image=img
        lblLogo.grid(row=0, column=0,columnspan=4,sticky=E+W)

        lbl = Label(self.master, text='                             ......a python scrapper', bg='orange', fg='blue', borderwidth = 0,font=3)
        lbl.grid(row=1, column=0, columnspan=4 ,sticky=E+W)
        
        l1=Label(self.master,text="Title",bg="white",padx='2',pady='4', font = 5)
        l1.grid(row=2,column=0,columnspan=2)

        self.d1=ttk.Combobox(self.master,state="readonly",values=["Software Developer","Software Tester","Designer","Data Analyst"], font = 5)
        self.d1.current(0)
        self.d1.grid(row=2,column=2,columnspan=2)
                
        l2=Label(self.master,text="Location",bg="white",padx='2',pady='4', font = 5)
        l2.grid(row=3,column=0,columnspan=2)

        self.d2=ttk.Combobox(self.master,state="readonly",values=["Noida","Pune","Bengluru","Gurgaon","Hyderabad","Kochi"], font = 5)
        self.d2.current(0)
        self.d2.grid(row=3,column=2,columnspan=2)
        
        l3=Label(self.master,text="From",bg="white",padx='2',pady='4', font = 5)
        l3.grid(row=4,column=0,columnspan=2)

        self.d3=ttk.Combobox(self.master,state="readonly",values=["indeed.com","timesjobs.com","simplyhired.com"], font = 5)
        self.d3.current(0)
        self.d3.grid(row=4,column=2,columnspan=2)
        
        
        b2=Button(self.master,text="Find Jobs",command=self.find_job,padx=2,pady=5, fg= 'dark blue', width=10, borderwidth = 1,font=5, activebackground='grey', activeforeground='white')
        b2.grid(row=5,column=3)
        self.master.grid_rowconfigure(5,weight=5)

        lblFooter1 = Label(self.master, text='Why JobScrapper for private jobs ....', bg='orange', fg='blue',width=50, borderwidth = 0,font=3)
        lblFooter1.grid(row=6, column=0, columnspan=4 ,sticky=E+W)

        msg = "There are thousands of job sites on the web, but the best job boards and job search engine sites have search tools that are quick and easy to use and allow you to search based on the type of job you're looking for, your location, and other criteria. \n\n There are also sites that focus on certain types of positions or match you with employers. These sites are worth incorporating into your job search, because not all employers list on every website, even though it may seem that way. Don't limit yourself to just one job website, because each job site only lists jobs from particular websites or companies.\n\nJob Scrapper provides you job search engines like Indeed.com and SimplyHired.com that pull listings from many different sources.So go ahead and find your a job where you fits in...."

        lblFooter = Label(self.master, text=msg, bg='green', fg='white',width=50, borderwidth = 7,font=3,padx="0",wraplength=450 )
        lblFooter.grid(row=7, column=0, columnspan=4 ,sticky=E+W)
        


    def find_job(self):
        title = self.d1.current()
        loc = self.d2.current()
        site = self.d3.current()


        iA0='https://www.indeed.co.in/jobs?q=software+developer&l=Noida%2C+Uttar+Pradesh'
        iB0='https://www.indeed.co.in/jobs?q=software+developer&l=Pune%2C+Maharashtra'
        iC0='https://www.indeed.co.in/jobs?q=software+developer&l=Bengaluru%2C+Karnataka'
        iD0='https://www.indeed.co.in/jobs?q=software+developer&l=Gurgaon%2C+Haryana'
        iE0='https://www.indeed.co.in/jobs?q=software+developer&l=Hyderabad%2C+Telangana#'
        iF0='https://www.indeed.co.in/jobs?q=software+developer&l=kochi'
        
        iA1='https://www.indeed.co.in/jobs?q=Tester&l=Noida%2C+Uttar+Pradesh'
        iB1='https://www.indeed.co.in/jobs?q=Tester&l=Pune%2C+Maharashtra'
        iC1='https://www.indeed.co.in/jobs?q=software+developer&l=Bengaluru%2C+Karnataka'
        iD1='https://www.indeed.co.in/jobs?q=software+developer&l=Gurgaon%2C+Haryana'
        iE1='https://www.indeed.co.in/jobs?q=Tester&l=Hyderabad%2C+Telangana'
        iF1='https://www.indeed.co.in/jobs?q=software+developer&l=kochi'

        iA2='https://www.indeed.co.in/jobs?q=designer&l=Noida%2C+Uttar+Pradesh'
        iB2='https://www.indeed.co.in/jobs?q=designer&l=Pune%2C+Maharashtra'
        iC2='https://www.indeed.co.in/jobs?q=designer&l=Bengalore%2C+Karnataka'
        iD2='https://www.indeed.co.in/jobs?q=designer&l=Gurgaon%2C+Haryana'
        iE2='https://www.indeed.co.in/jobs?q=designer&l=Hyderabad%2C+Telangana'
        iF2='https://www.indeed.co.in/jobs?q=designer&l=kochi'

        iA3='https://www.indeed.co.in/jobs?q=data+analyst&l=Noida%2C+Uttar+Pradesh'
        iB3='https://www.indeed.co.in/jobs?q=data+analyst&l=Pune%2C+Maharashtra'
        iC3='https://www.indeed.co.in/jobs?q=data+analyst&l=Bengaluru%2C+Karnataka'
        iD3='https://www.indeed.co.in/jobs?q=data+analyst&l=gurgaon'
        iE3='https://www.indeed.co.in/jobs?q=data+analyst&l=Hyderabad%2C+Telangana'
        iF3='https://www.indeed.co.in/jobs?q=data+analyst&l=kochi'



        tA0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Noida%2F+Greater+Noida'
        tB0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Pune'
        tC0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Bengaluru%2F+Bangalore'
        tD0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Gurgaon'
        tE0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Hyderabad%2F+Secunderabad'
        tF0='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Cochin%2F+Kochi%2F+Ernakulam'
    
        tA1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Noida%2F+Greater+Noida'
        tB1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Pune'
        tC1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Bengaluru%2F+Bangalore'
        tD1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Gurgaon'
        tE1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Hyderabad%2F+Secunderabad'
        tF1='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Tester&txtLocation=Cochin%2F+Kochi%2F+Ernakulam'

        tA2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Noida%2F+Greater+Noida'
        tB2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Pune'
        tC2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Bengaluru%2F+Bangalore'
        tD2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Gurgaon'
        tE2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Hyderabad%2F+Secunderabad'
        tF2='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Designer&txtLocation=Hyderabad%2F+Secunderabad'

        tA3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Noida%2F+Greater+Noida'
        tB3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Pune'
        tC3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Bengaluru%2F+Bangalore'
        tD3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Gurgaon'
        tE3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Hyderabad%2F+Secunderabad'
        tF3='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Data+Analyst&txtLocation=Cochin%2F+Kochi%2F+Ernakulam'




        sA0='https://www.simplyhired.co.in/search?q=Software+Developer&l=Noida%2C+Uttar+Pradesh&job=W_kPuWvs5Q0aqHoMCpDDn1N7sFB9oOAllOjxRhI7Y2ygMJ6SK8_uVA'
        sB0='https://www.simplyhired.co.in/search?q=software+developer&l=Pune%2C+Maharashtra&job=0uyrInBqiqjwYR_vGhR-IVWxmdalvh25FrOjR925Qgst1J3rFxR19Q'
        sC0='https://www.simplyhired.co.in/search?q=software+developer&l=Bengaluru%2C+Karnataka&job=hjMYN6C-eVTA3lSP99o-qJFwPsKmzUKcY0TmOQsYxdH8mJ-SpxJFYw'
        sD0='https://www.simplyhired.co.in/search?q=software+developer&l=Gurgaon%2C+Haryana&job=Nmy6dT7BLhrvhjWT86llz2mCpGkkdJc0dXvZJQIgDmebIkpMQF_qEQ'
        sE0='https://www.simplyhired.co.in/search?q=software+developer&l=Hyderabad%2C+Telangana&job=iT4_u4V4BqoxfuUwpUwa-ITiRRVLDwRW0Z8TWkIdtoTwcATWeFwT-g'
        sF0='https://www.simplyhired.co.in/search?q=software+developer&l=Cochin%2C+Kerala&job=T4g855nKwNHbMAO7BOuBMXJIiyYq5PaOBVgb0-aEh3hN_A-eBFQcdg'
    
        sA1='https://www.simplyhired.co.in/search?q=tester&l=Noida%2C+Uttar+Pradesh&job=FGBxD_rKDO_G5jTEoQWYtdTQEPGlhxDSGmn2LdjMGHVClN4pLOba9A'
        sB1='https://www.simplyhired.co.in/search?q=tester&l=Pune%2C+Maharashtra&job=Eaqp9vaLbcK5wL8u-qNbEkYymrl8wlrNc1oTCi20kaamLBix6z7A7w'
        sC1='https://www.simplyhired.co.in/search?q=tester&l=Bengaluru%2C+Karnataka&job=WSkmk9ISMGKw3BmQHoqBU-7uKKpsCANkBpme3wk305x4ok99OzwAIQ'
        sD1='https://www.simplyhired.co.in/search?q=tester&l=Gurgaon%2C+Haryana&job=Xlfr4Z678N6VOjrCotO_NyyhCptiHpJFcmEPQ0N3OM8AnEe3ZpS_MQ'
        sE1='https://www.simplyhired.co.in/search?q=tester&l=Hyderabad%2C+Telangana&job=-HikS5AH5nCArpKQud20K9TWpuS_yT9H9SCdDF6ksvKe_r7MO-vSvA'
        sF1='https://www.simplyhired.co.in/search?q=tester&l=Kochi%2C+Kerala&job=HcuuR38muoGToZ-WGuWpcG3sDtnQrnhvOOuY1_wM9kwtWgNo6-ht5w'

        sA2='https://www.simplyhired.co.in/search?q=designer&l=Noida%2C+Uttar+Pradesh&job=-bwv1Xe4xDaKjS6iEdjuxgj4SomTExknzxJebKkQMKpRA1dh6F6tag'
        sB2='https://www.simplyhired.co.in/search?q=designer&l=Pune%2C+Maharashtra&job=HfGsu9Uq2Qr9nyZU4IJHr-oEJNMPP05-7reE3bCorlJXduJDRbCehA'
        sC2='https://www.simplyhired.co.in/search?q=designer&l=Bengaluru%2C+Karnataka&job=uyPggHfG8ZJQSB3RwGDJggU6EdU3HD3oeiXvefXoMFbvgdttxHUQQw'
        sD2='https://www.simplyhired.co.in/search?q=designer&l=Gurgaon%2C+Haryana&job=WpWdDYpEo8qXIFokPct6U_R51whbo1iC7xOj6UQ7yTNjZEHFXQHBog'
        sE2='https://www.simplyhired.co.in/search?q=designer&l=Hyderabad%2C+Telangana&job=vDudgQXE0QE6GCImqtgv5Uqa8DVhdgh6a6My-DAjvc4RtSWdIwqWcA'
        sF2='https://www.simplyhired.co.in/search?q=tester&l=Kochi%2C+Kerala&job=HcuuR38muoGToZ-WGuWpcG3sDtnQrnhvOOuY1_wM9kwtWgNo6-ht5wS'

        sA3='https://www.simplyhired.co.in/search?q=data+analyst&l=Noida%2C+Uttar+Pradesh&job=RdpN5lR6n2XJOyANGKVRHfZrXKt9tpT6HOa5X9bD0qhITRi3VxS4Hg'
        sB3='https://www.simplyhired.co.in/search?q=data+analyst&l=Pune%2C+Maharashtra&job=1Bk-xxq5gLF1Ecd1hNqDjnqwqUd1t3PtNhrKdyHXZ7TXjcgiaBJOdw'
        sC3='https://www.simplyhired.co.in/search?q=Data+Analyst&l=Bengaluru%2C+Karnataka&job=h7dwjSPHxxranQTdNQD1BkiNn4mi1qW28VPOMn3pv6CC-vyvCIArnQ'
        sD3='https://www.simplyhired.co.in/search?q=Data+Analyst&l=Gurgaon%2C+Haryana&job=G6pWUDm5DvQvIR5mC0rXplOOCW99C5J61bd4Mp9wZrZnOBnirx4ENQ'
        sE3='https://www.simplyhired.co.in/search?q=data+analyst&l=Hyderabad%2C+Telangana&job=zps1BTGikh2-Q9b6mI0M-r9L7Tc2VUMhr0wI6CAaw0XXFsm4ElcdPw'
        sF3='https://www.simplyhired.co.in/search?q=Data+Analyst&l=Kochi%2C+Kerala&job=9RswRvLZ0iq0PmXTXOMeJzE3OMRIyer-ycgmS0nNt9GD7y2ygtfo5Q'


        indeed=[[iA0,iB0,iC0,iD0,iE0,iF0],
            [iA1,iB1,iC1,iD1,iE1,iF1],
            [iA2,iB2,iC2,iD2,iE2,iF2],
            [iA3,iB3,iC3,iD3,iE3,iF3]]
        
        timesjob=[[tA0,tB0,tC0,tD0,tE0,tF0],
              [tA1,tB1,tC1,tD1,tE1,tF1],
              [tA2,tB2,tC2,tD2,tE2,tF2],
              [tA3,tB3,tC3,tD3,tE3,tF3]]

        simplyhired=[[sA0,sB0,sC0,sD0,sE0,sF0],
              [sA1,sB1,sC1,sD1,sE1,sF1],
              [sA2,sB2,sC2,sD2,sE2,sF2],
              [sA3,sB3,sC3,sD3,sE3,sF3]]
    
        if site==0:
            l=indeed[title]
            url=l[loc]
        
            a=Indeed(url)
            a.retrive_jobs()
        elif site==1:
            l=timesjob[title]
            url=l[loc]
        
            a=times_job(url)
            a.retrive_jobs()

        elif site==2:
            l=simplyhired[title]
            url=l[loc]
        
            a=SimplyHired(url)
            a.retrive_jobs()
    


