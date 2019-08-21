from tkinter import *
from bs4 import BeautifulSoup
from ShowResult import ShowResult
import tkinter as tk
from tkinter import messagebox
import requests
import csv


class times_job:

    def __init__(self,url):
        self.url=url
        

#print(soup.prettify())
    def retrive_jobs(self):
        rows=[]
        rows.append(["Job Title","Organization","Posted","Description","Location"])
        
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        all_jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
        i=0
        print("length of all_jobs : "+ str(len(all_jobs)))
        for job in all_jobs:
            row=[]
            i=i+1
            job_title = ""
            
            job_loc = ""
            job_org =  ""
            job_posted = ""
            job_desc = ""
            
            if(i==5):break
            
            t = job.find('header',class_='clearfix')
            if t is not None:
                job_title = t.find('a').getText().strip()
                

                t = job.find('ul',class_='list-job-dtl clearfix')            
                if t is not None:
                    job_desc = t.find('li').getText().strip()
                    job_desc = job_desc.replace('\n', ' ')
                    job_desc = job_desc.replace('\t', ' ')
                    job_desc = job_desc.replace('\r', ' ')
                    job_desc = job_desc.replace('"', ' ')
                    job_desc = job_desc.strip()
                    loc = job_desc.find("Job Description:")
                    if(loc!=-1):
                        job_desc = job_desc[loc+len("Job Description:"):]
                
                t = job.find('ul',class_='top-jd-dtl clearfix')            
                if t is not None:
                    job_loc = t.find('span').getText().strip()
                    
                    
                t = job.find('h3',class_='joblist-comp-name')
                if t is not None:
                    job_org = t.getText().strip()
                    
                t = job.find('span',class_='sim-posted')
                if t is not None:
                    job_posted = t.find('span').getText().strip()
                    
                row.append(job_title)
                row.append(job_org)
                row.append(job_posted)
                row.append(job_desc)
                row.append(job_loc)
                
                rows.append(row)
                
                print("********************************  " , i," ********************************")
                print("\n",job_title)
                print("**********************************************************************")        
                print("\n\t Location: ",job_loc)
                print("\n\t Posted: ",job_posted)
                print("\n\t Org: ",job_org)
                print("\n\t Description: ",job_desc)
        if (len(rows)-1)>0:
            #store in csv file
            csv.register_dialect('myDialect', delimiter = ',')

            with open('scrapResult.csv', 'w') as f:
                writer = csv.writer(f, dialect='myDialect')
                writer.writerows(rows)

            f.close()
            root=Tk()
            s = ShowResult(root,"scrapResult.csv",self.url)
            s.mainloop()
        else:
            tk.messagebox.showinfo("Job Scrapper","No matching jobs found")
    
if __name__ == '__main__':
   a=times_job("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Software+Developer&txtLocation=Cochin%2F+Kochi%2F+Ernakulam")
   a.retrive_jobs()
