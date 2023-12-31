import os
import requests
from bs4 import BeautifulSoup
import time
import sheetconnection

def get_problem_count(profile_link):
     response=requests.get(profile_link)
     soup=BeautifulSoup(response.content,'html.parser')
     v=soup.find_all('div')
    
     easy,medium,hard,total,rating=0,0,0,0,0
     contest_attended,contest_ranking=0,0

     if 'Contest' and 'Rating' and "Attended" in v[0].text :
        contest_attended=v[0].text.split("Attended")[-1].split("Solved")[0]
        contest_ranking=v[0].text.split("Rating")[-1].split("Global")[0]
            
     for i in v:
          if 'Easy' in i.text and 'Medium' in i.text and 'Hard' in i.text:
               easy=i.text.split('Easy')[-1].split('/')[0]
               medium=i.text.split('Medium')[-1].split('/')[0]
               hard=i.text.split('Hard')[-1].split('/')[0]
               total=int(easy)+int(medium)+int(hard)
               rating=i.text.split("Community")[0].split("Rank")[-1]
               for j in range(0,len(rating)):
                    if rating[j]==',':
                         continue
                    if ord(rating[j])-ord('0')>9:
                         rating=rating[:j]
                         break
                      
               if len(rating)==0:
                    rating=0
               break

          
     
     return rating,easy,medium,hard,total,contest_attended,contest_ranking


for ctr in  range(0,len(sheetconnection.allsheets)):

     links=sheetconnection.get_list(ctr)
          

     for i in range(0,len(links)):
          time.sleep(2)
          if links[i]=='':
               continue
          rating,easy,medium,hard,total,contest_attended,contest_ranking=get_problem_count(links[i])
          sheetconnection.put_data(sheetconnection.allsheets[ctr],i+2,rating,easy,medium,hard,total,contest_attended,contest_ranking)
