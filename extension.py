
"""
Author: Kray Nguyen @ University of Washington 

Date: 5/20/2020

Description: This program extends from the original code written by 'Zhiya Zuo' to collect "Subject terms" and "Participants"
values

Pre: SeleniumScraper.py, utils.py, main.py, UNTCScraper.py
"""
import requests
from bs4 import BeautifulSoup
import mechanize
from re import search

"""
This function returns all the subject terms for each url input

Pre: url 
Post: subject terms 
"""
def find_Sterms(url, list):
    #Get HTML text 
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    #direct to the HTML address of subject terms 
    try:
        table1 = soup.find('table',id = 'dgSubject')
        subject_term_final = "" 
        for row in table1.findAll('tr'):  
            subj_term = row.find('td',class_='prn-no-bdr').text.strip()
            subject_term_final += (subj_term + "\n" )
    except: 
        print('')
    return subject_term_final

"""
This function returns values in participant(s) and participant columns 

Pre: url
Post: Participants
"""
def find_Par(url, list):
    # Get HTML text from url
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    participant_final = ""

    # Direct to HTML address of participant(s) column
    try:
        table2 = soup.find('table',cellspacing='2', id = 'dgParticipants')
        
        for row in table2.findAll('tr'):
            participants = row.find('span').text.strip()
            participant_final += (participants + "\n")
    except:
        print('')
    
    # Direct to HTML address of participant column
    try:
        table3 = soup.find('table', class_= "table table-striped table-bordered table-hover table-condensed", id='dgActions')
        
        # Create a list to store participant values with "ratification" action ONLY
        list = []
        internal_list = []
        for act in table3.findAll('tr'):
            for act2 in act.findAll('td'):
                action = act2.text
                internal_list.append(action)

        for element in range(len(internal_list)):
            if(internal_list[element] == 'Ratification'):
                participant = str(internal_list[element-1])
                print(participant)
                list.append(participant)
            
            

        # sorting and deduplicating the values in the list 
        
        list = sorted(set(list))
        for l in range(len(list)):
            print(list[l])
            participant_final += (list[l] + "\n")
    except:
        print('')
    
    return participant_final



print('-------------------------------RESTART-----------------------------')
print('-------------------------------------------------------------------')