 #!/usr/bin/env python3


import sys
sys.path.append("/usr/lib/python3/dist-packages")
import requests
from bs4 import BeautifulSoup
import csv

date=input('can u enter the date please follow thi format MM/DD/YYYY:')
page = requests.get(f'https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}')


def main(page):
    src = page.content
    soup=BeautifulSoup(src,'lxml')
    championships=soup.find_all('div',{'class':'matchCard'})
    number_champions=len(championships)
    match_details =[]

    def get_match_details(championships):
       titel =championships.find('div',{'class':'title'}).find('h2').text.strip() 
       all_match = championships.find_all('li')
       number_match =len(all_match)
       
       for i in range(number_match):
           teamA = all_match[i].find('div',{'class':'teamA'}).text.strip()
           teamB = all_match[i].find('div',{'class':'teamB'}).text.strip()
           time = all_match[i].find('span',{'class':'time'}).text.strip()
           result=all_match[i].find('div',{'class':'MResult'}).find_all('span',{'class':'score'})
           score = f"{result[0].text.strip()} - {result[1].text.strip()}"

           match_details.append({'نوع البطولة':titel,'الفريق الاول':teamA,'الفريق الثاني':teamB,' الوقت':time,'النتيجة':score})


    for i in range(number_champions):

        get_match_details(championships[i])

    keys= match_details[0].keys()
    print(keys)
    
    with open('/home/kheira/Documents/scraping/yallakoura2.csv','w') as  output_file:
        dict_writer=csv.DictWriter(output_file,keys)
        dict_writer.writeheader()
        for match in match_details:
          dict_writer.writerow(match)
        print('yallakoura2.csv')


main(page)