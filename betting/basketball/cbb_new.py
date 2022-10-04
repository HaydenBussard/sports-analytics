from os import pipe
from typing import Match, Text
from urllib import request
import bs4
import pandas as pd
import numpy as np
import json
from json import scanner
from pandas.core.indexing import convert_from_missing_indexer_tuple, convert_missing_indexer
import requests
import re
from datetime import date, timedelta
import urllib  
import urllib.parse
import urllib.request
import gettext
from gettext import gettext
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import statistics
import numpy as np
from scipy import stats
from scipy.stats import poisson
import matplotlib.pyplot as plt
import math
import random
import sqlite3
from operator import itemgetter
import schedule
import pyderman as dr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

start_time = time.perf_counter()

url_draftkings_cbb = 'https://sportsbook.draftkings.com/leagues/basketball/88670771'
df_draftkings_cbb = pd.read_html(url_draftkings_cbb)
draftKingsData = df_draftkings_cbb[0].values.tolist()
dk_length = len(df_draftkings_cbb)
i = 0
draftkings_cbb = []
while True:
    if i < dk_length:
        x = df_draftkings_cbb[i].values.tolist()
        draftkings_cbb = draftkings_cbb + x
        i += 1
        continue
    else:
        break

# fix sublist index 0 with gametimes and team names
i = 0
a = 0 
while True:
    if i < len(draftkings_cbb):
        name_scraped = str(draftkings_cbb[i][0])
        if name_scraped[5:7] == 'AM':
            m = name_scraped.index('AM')
            m += 2
            team = name_scraped[m:]
            draftkings_cbb[i][0] = team
            i += 1
            continue
        elif name_scraped[4:6] == 'AM':
            m = name_scraped.index('AM')
            m += 2
            team = name_scraped[m:]
            draftkings_cbb[i][0] = team
            i += 1
            continue
        elif name_scraped[5:7] == 'PM':
            m = name_scraped.index('PM')
            m += 2
            team = name_scraped[m:]
            draftkings_cbb[i][0] = team
            i += 1
            continue
        elif name_scraped[4:6] == 'PM':
            m = name_scraped.index('PM')
            m += 2
            team = name_scraped[m:]
            draftkings_cbb[i][0] = team
            i += 1
            continue
        elif name_scraped[4:6] == 'OT':
            m = name_scraped.index('OT')
            m += 2
            team = name_scraped[m:]
            draftkings_cbb[i][0] = team
            i += 1
            continue
        elif name_scraped[0:15] == 'RegularTimeEnd':
            m = name_scraped.index('PM')
            team = name_scraped[14:]
            draftkings_cbb[i][0] = team
            i += 1
            continue
        elif 'Half' in name_scraped[7:13]:
            m = name_scraped.index('Half')
            name_scraped = str(name_scraped[m + 4:])
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        elif 'Half' in name_scraped[3:8]:
            m = name_scraped.index('Half')
            name_scraped = str(name_scraped[m + 4:])
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        # elif name_scraped[2] == ':':
        #     game_time = 'LIVE'
        #     name_scraped = str(name_scraped[16:])
        #     draftkings_cbb[i][0] = name_scraped
        #     draftkings_cbb[i].append(game_time)
        #     i += 1
        #     continue
        # elif name_scraped[8:15] == 'Quarter':
        #     print(name_scraped)
        #     game_time = 'LIVE'
        #     name_scraped = name_scraped[15:]
        #     draftkings_cbb[i][0] = name_scraped
        #     draftkings_cbb[i].append(game_time)
        #     i += 1
        #     continue
        # elif name_scraped[9:16] == 'Quarter':
        #     print(name_scraped)
        #     game_time = 'LIVE'
        #     name_scraped = name_scraped[16:]
        #     draftkings_cbb[i][0] = name_scraped
        #     draftkings_cbb[i].append(game_time)
        #     i += 1
        #     continue
        elif 'Overtime' in name_scraped:
            m = name_scraped.index('Overtime')
            team = name_scraped[m + 8:]
            draftkings_cbb[i][0] = team
            i += 1
            continue
        else:
            i += 1
            continue
    else: 
        break

i = 0
while True:
    if i < len(draftkings_cbb):
        name_scraped = draftkings_cbb[i][0]
        # print(name_scraped)
        if name_scraped[-1] == '0':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            # i += 1
            continue
        elif name_scraped[-1] == '1':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            # i += 1
            continue
        elif name_scraped[-1] == '2':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            # i += 1
            continue
        elif name_scraped[-1] == '3':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            # i += 1
            continue
        elif name_scraped[-1] == '4':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            # i += 1
            continue
        elif name_scraped[-1] == '5':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            # i += 1
            continue
        elif name_scraped[-1] == '6':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            # i += 1
            continue
        elif name_scraped[-1] == '7':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            # i += 1
            continue
        elif name_scraped[-1] == '8':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            # i += 1
            continue
        elif name_scraped[-1] == '9':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            # i += 1
            continue
        else:
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
    else: 
        break

i = 0
while True:
    if i < len(draftkings_cbb):
        name_scraped = str(draftkings_cbb[i][0])
        if name_scraped[-1] == '0':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        elif name_scraped[-1] == '1':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        elif name_scraped[-1] == '2':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        elif name_scraped[-1] == '3':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        elif name_scraped[-1] == '4':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        elif name_scraped[-1] == '5':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        elif name_scraped[-1] == '6':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        elif name_scraped[-1] == '7':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        elif name_scraped[-1] == '8':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        elif name_scraped[-1] == '9':
            name_scraped = name_scraped[0:-1]
            draftkings_cbb[i][0] = name_scraped
            i += 1
            continue
        else:
            i += 1
            continue
    else: 
        break

i = 0
while True:
    if i < len(draftkings_cbb):
        spr = str(draftkings_cbb[i][1])
        ml = str(draftkings_cbb[i][2])
        if spr == 'nan' or ml == 'nan':
            del draftkings_cbb[i]
            continue
        else:
            i += 1
            continue
    else:
        break
    

for elem in draftkings_cbb:
    # print(elem)
    spr = str(elem[1])
    print(spr)
    # if spr == 'nan':
    #     del elem
    #     continue
    # if str(elem[2]) == 'nan':
    #     del elem
    #     continue
    # print(spr)
    s = 1
    while True:
        # print(spr[s])
        if spr[s] != '-' and spr[s] != '+':
            s += 1
            continue
        else:
            break
    spread = spr[:s]
    if '.' in spread:
        spread = float(spread)
    else:
        spread = int(spread)
    spread_o = spr[s:]
    spread_o = int(spread_o)
    ou = str(elem[2])
    ou = ou.split()
    print(ou)
    ou = str(ou[1])
    if '+' in ou:
        ind = ou.index('+')
    else:
        ind = ou.index('-')
    total = ou[:ind]
    if '.' in total:
        total = float(total)
    else:
        total = int(total)
    total_o = ou[ind:]
    total_o = int(total_o)
    ml = elem[-1]
    del elem[1:]
    elem.append(spread)
    elem.append(spread_o)
    elem.append(ml)
    elem.append(total)
    elem.append(total_o)
    continue

# print('\n')
print('DraftKings:')
for elem in draftkings_cbb:
    print(elem)

#### END OF SCRAPING ODDS FROM DRAFTKINGS ####

dk_scraped_time = time.perf_counter()
print('\n')
print(f'Scraped and organized DraftKings data in {dk_scraped_time - start_time:0.4f} seconds')
print('\n')

#### BEGIN SCRAPING ODDS FROM FANDUEL ####

browser0 = webdriver.Chrome()
browser0.get('https://pa.sportsbook.fanduel.com/navigation/ncaab')
fdElems = browser0.find_elements(By.TAG_NAME, 'SPAN')

fd_cbb = []
for elem in fdElems:
    txt = elem.text
    fd_cbb.append(txt)

page_title_index = fd_cbb.index("NCAA Men's Games")# NCAA Men's Games, Featured Men's Games
page_title_index += 5
del fd_cbb[0:page_title_index]

i = 0
while True:
    if i < len(fd_cbb):
        if fd_cbb[i] == 'More wagers':
            del fd_cbb[i]
            continue
        if fd_cbb[i] == '':
            del fd_cbb[i]
            continue
        if 'HALF' in fd_cbb[i]:# -11 and -13
            a_score = i - 13
            h_score = i - 11
            del fd_cbb[h_score]
            del fd_cbb[a_score]
            i -= 1
            continue
        if fd_cbb[i] == 'NCAA Basketball Mens Matches':
            del fd_cbb[i]
            continue
        if fd_cbb[i] == 'NCAA Basketball':
            del fd_cbb[i]
            continue
        if fd_cbb[i] == 'SPREAD':
            del fd_cbb[i]
            continue
        if fd_cbb[i] == 'MONEY':
            del fd_cbb[i]
            continue
        if fd_cbb[i] == 'TOTAL':
            del fd_cbb[i]
            continue
        if 'FanDuel Sportsbook offers college basketball odds' in fd_cbb[i]:
            del fd_cbb[i:]
            break
        else:
            i += 1
            continue
    else:
        break

for elem in fd_cbb:
    print(elem)

game_times = []
fanduel_cbb = []
i = 0
while True:
    if len(fd_cbb) > 12:
        t = 0
        while True:
            if t < len(fd_cbb):
                if 'HALF' in fd_cbb[t]:
                    break
                else:
                    t += 1
                    continue
        if t != 12:
            if t > 12:
                fix = int(t - 12)
                del fd_cbb[:fix + 1]
                continue
            else:
                fix = int(12 - t)
                del fd_cbb[:fix + 1]
                continue
        if 'PM' in str(fd_cbb[2]) and 'ET' in str(fd_cbb[2]):
            del fd_cbb[:3]
            continue
        h = i + 1
        a_spr = i + 2     #away team spread
        a_spr_o = i + 3   #away team spread odds
        a_ml = i + 4      #away team moneyline
        over = i + 5      #over
        over_o = i + 6    #over odds
        h_spr = i + 7     #home team spread
        h_spr_o = i + 8   #home team spread odds
        h_ml = i + 9      #home team moneyline
        under = i + 10    #under
        under_o = i + 11  #under odds
        gt = i + 12       #game time
        end = i + 13
        gt_lst0 = [fd_cbb[i], fd_cbb[gt]]
        gt_lst1 = [fd_cbb[h], fd_cbb[gt]]
        away = [fd_cbb[i], fd_cbb[a_spr], fd_cbb[a_spr_o], fd_cbb[a_ml], fd_cbb[over], fd_cbb[over_o]]
        home = [fd_cbb[h], fd_cbb[h_spr], fd_cbb[h_spr_o], fd_cbb[h_ml], fd_cbb[under], fd_cbb[under_o]]
        fanduel_cbb.append(away)
        fanduel_cbb.append(home)
        game_times.append(gt_lst0)
        game_times.append(gt_lst1)
        print(fd_cbb[:end])
        del fd_cbb[:end]
        continue
    else:
        break

for elem in fanduel_cbb:
    print(elem)
    elem[1] = float(elem[1])
    elem[2] = int(elem[2])
    elem[3] = int(elem[3])
    total = elem[4]
    total = total[2:]
    if '.' in total:
        elem[4] = float(total)
    else:
        elem[4] = int(total)
    elem[5] = int(elem[5])

print('\n')
print('Fanduel:')
for elem in fanduel_cbb:
    print(elem)

# for elem in game_times:
#     print(elem)

# # browser.quit()

#### END OF SCRAPING ODDS FROM DRAFTKINGS ####

fd_scraped_time = time.perf_counter()
print('\n')
print(f'Scraped and organized Fanduel data in {fd_scraped_time - start_time:0.4f} seconds')
print('\n')

#### BEGIN SCRAPING ODDS FROM BARSTOOL ####

browser1 = webdriver.Chrome()
browser1.get('https://www.barstoolsportsbook.com/sports/basketball/ncaab')
time.sleep(25)
bsElems = browser1.find_elements(By.TAG_NAME, 'LABEL')

bs_cbb = []
for elem in bsElems:
    txt = elem.text
    # print(txt)
    bs_cbb.append(txt)

bs_splits = []
i = 0
for elem in bs_cbb:
    lst = elem.split()
    lng = len(lst)
    end = lng - 1
    a = 0
    while True:
        if a < lng:
            bs_splits.append(lst[a])
            a += 1
            continue
        else:
            break

barstool_cbb = []
i = 0
while True:
    if len(bs_splits) > 12:
        under_index = bs_splits.index('U')
        end = under_index + 3
        match = bs_splits[:end]
        # print(match)
        while True:
            if len(match) > 14:
                a_ml = match[5]
                if a_ml[0] != '+' and a_ml[0] != '-':
                    n1 = match[4]
                    n2 = a_ml
                    name = str(n1 + ' ' + n2)
                    match[4] = name
                    del match[5]
                    continue
                h_ml = match[7]
                if h_ml[0] != '+' and h_ml[0] != '-':
                    n1 = match[6]
                    n2 = h_ml
                    name = str(n1 + ' ' + n2)
                    match[6] = name
                    del match[7]
                    continue
            else:
                break
        if len(match) == 10:
            del bs_splits[:end]
            continue
        a_spr = i        # away team spread
        a_spr_o = i + 1  # away team spread odds
        h_spr = i + 2    # home team spread
        h_spr_o = i + 3  # home team spread odds
        a = i + 4        # away team name
        a_ml = i + 5     # away team moneyline
        h = i + 6        # home team name
        h_ml = i + 7     # home team moneyline
        ou = i + 9       # over / under
        over_o = i + 10  # over odds
        under_o = i + 13 # under odds
        away = [match[a], match[a_spr], match[a_spr_o], match[a_ml], match[ou], match[over_o]]
        home = [match[h], match[h_spr], match[h_spr_o], match[h_ml], match[ou], match[under_o]]
        j = 1
        k = 1
        while True:
            if j < len(away):
                if '.' in away[j]:
                    away[j] = float(away[j])
                    j += 1
                    continue
                else:
                    away[j] = int(away[j])
                    j += 1
                    continue
            else:
                break
        while True:
            if k < len(home):
                if '.' in home[k]:
                    home[k] = float(home[k])
                    k += 1
                    continue
                else:
                    home[k] = int(home[k])
                    k += 1
                    continue
            else:
                break
        barstool_cbb.append(away)
        barstool_cbb.append(home)
        del bs_splits[:end]
        continue
    else:
        break

print('\n')
print('Barstool:')
for elem in barstool_cbb:
    print(elem)

#### END OF SCRAPING ODDS FROM DRAFTKINGS ####

bs_scraped_time = time.perf_counter()
print('\n')
print(f'Scraped and organized Barstool data in {bs_scraped_time - start_time:0.4f} seconds')
print('\n')

#### GETTING STATS FROM TEAMRANKINGS ####

# teamrankings.com stats
url_tr_pfa = 'https://www.teamrankings.com/ncaa-basketball/stat/points-per-game'
url_tr_paa = 'https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game'
df_yahoo_total_against = pd.read_html(url_tr_pfa)
df_yahoo_total_for = pd.read_html(url_tr_paa)
tr_for_table = df_yahoo_total_against[0].values.tolist()
tr_against_table = df_yahoo_total_for[0].values.tolist()

i = 0
while True:
    if i < len(tr_for_table):
        del tr_for_table[i][0]
        del tr_for_table[i][2:4]
        del tr_for_table[i][-1]
        i+=1
        continue
    else:
        break
# tr_for_table: [i][0] = teamname , [i][1] = total pfa, [i][2] = home pfa, [i][3] = away pfa

i = 0
while True:
    if i < len(tr_against_table):
        del tr_against_table[i][0]
        del tr_against_table[i][2:4]
        del tr_against_table[i][-1]
        i+=1
        continue
    else:
        break
# tr_against_table: [i][0] = teamname , [i][1] = total paa, [i][2] = home paa, [i][3] = away paa

tr_for_table.sort(key=lambda x: x[0])
tr_against_table.sort(key=lambda x: x[0])

# tr_data: [i][0] = teamname , [i][1] = total pfa, [i][2] = home pfa, 
# [i][3] = away pfa , [i][4] = total paa, [i][5] = home paa, [i][6] = away paa

tr_data = tr_for_table
i = 0
while True:
    if i < len(tr_data):
        tr_data[i].append(tr_against_table[i][1])
        tr_data[i].append(tr_against_table[i][2])
        tr_data[i].append(tr_against_table[i][3])
        i+=1
        continue
    else:
        break


tr_data.sort(key=lambda x: x[0])
# for elem in tr_data:
#     print(elem)
tr_scraped_time = time.perf_counter()
print('\n')
print(f'Scraped and organized TeamRankings stats in {tr_scraped_time - start_time:0.4f} seconds')
print('\n')
#### END OF GETTING STATS FROM TEAMRANKINGS ####

#### BEGIN MATCHING TEAM NAMES ####

def rename(lst):
    for elem in lst:
        team_name = str(elem[0])
        if team_name == 'AR Lit Rock' or team_name == 'UALR' or team_name == 'Little RockUALR': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Little Rock'
            continue
        elif team_name == 'Hampton' or team_name == 'HAMP' or team_name == 'HamptonHAMP': # added tr / dk / fd / bs / nf / espn
            elem[0] = 'Hampton'
            continue 
        elif team_name == 'Abl Christian' or team_name == 'ACU' or team_name == 'Abilene ChristianACU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Abilene Christian'
            continue
        elif team_name == 'Wm & Mary' or team_name == 'W&amp;M' or team_name == 'William & MaryW&M': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'William & Mary'
            continue
        elif team_name == 'Air Force' or team_name == 'AFA' or team_name == 'Air ForceAFA': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Air Force'
            continue
        elif team_name == 'Akron' or team_name == 'AKR' or team_name == 'AkronAKR': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Akron'
            continue
        elif team_name == 'Alab A&M' or team_name == 'AAMU' or team_name == 'Alabama A&MAAMU': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Alabama A&M'
            continue
        elif team_name == 'Alabama St' or team_name == 'ALST' or team_name == 'Alabama StateALST': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Alabama State'
            continue
        elif team_name == 'Prairie View' or team_name == 'Prairie View A&M' or team_name == 'PV' or team_name == 'Prairie View A&MPV': # added tr / dk / fd / bs / nf / espn  
            elem[0] = 'Prairie View'
            continue 
        elif team_name == 'Albany' or team_name == 'ALBY' or team_name == 'AlbanyALB': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Albany NY'
            continue
        elif team_name == 'Alcorn State' or team_name == 'Alcorn' or team_name == 'ALCN' or team_name == 'Alcorn StateALCN': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Alcorn'
            continue
        elif team_name == 'American' or team_name == 'AMER' or team_name == 'American UniversityAMER': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'American'
            continue
        elif team_name == 'App State' or team_name == 'APP' or team_name == 'Appalachian StateAPP': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Appalachian State'
            continue
        elif team_name == 'N Arizona' or team_name == 'NAU' or team_name == 'Northern ArizonaNAU': # added tr / dk / fd / nf / espn | need bs 
            elem[0] = 'Northern Arizona'
            continue
        elif team_name == 'NC-Wilmgton' or team_name == 'UNC Wilmington' or team_name == 'UNC WilmingtonUNCW': # added tr / dk / fd / bs / nf / espn
            elem[0] = 'UNCW'
            continue
        elif team_name == 'Arizona St' or team_name == 'ASU' or team_name == 'Arizona StateASU': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Arizona State'
            continue
        elif team_name == 'Arizona' or team_name == 'ARIZ' or team_name == 'ArizonaARIZ': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Arizona'
            continue
        elif team_name == 'Ark Pine Bl' or team_name == 'Arkansas Pine Bluff' or team_name == 'ARPB' or team_name == 'Arkansas-Pine BluffUAPB': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Arkansas-Pine Bluff'
            continue
        elif team_name == 'Arkansas St' or team_name == 'ARST' or team_name == 'Arkansas StateARST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Arkansas State'
            continue
        elif team_name == 'Army' or team_name == 'ARMY' or team_name == 'ArmyARMY': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Army West Point'
            continue
        elif team_name == 'Auburn' or team_name == 'AUB' or team_name == 'AuburnAUB': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Auburn'
            continue
        elif team_name == 'Austin Peay' or team_name == 'PEAY' or team_name == 'Austin PeayAPSU': # added tr / dk / fd / nf / espn | need bs 
            elem[0] = 'Austin Peay'
            continue
        elif team_name == 'BYU' or team_name == 'BYUBYU': # added tr / dk / nf | need fd / bs / espn  #
            elem[0] = 'BYU'
            continue
        elif team_name == 'Ball State' or team_name == 'BALL' or team_name == 'Ball StateBALL': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Ball State'
            continue
        elif team_name == 'Baylor' or team_name == 'BAY' or team_name == 'BaylorBAY': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Baylor'
            continue
        elif team_name == 'Bellarmine' or team_name == 'BELL' or team_name == 'BellarmineBELL': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Bellarmine'
            continue
        elif team_name == 'Belmont' or team_name == 'BEL' or team_name == 'BelmontBEL': # added tr / dk / fd / nf / espn | need bs
            elem[0] = 'Belmont'
            continue
        elif team_name == 'Beth-Cook' or team_name == 'Bethune Cookman' or team_name == 'COOK' or team_name == 'Bethune-CookmanBCU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Bethune-Cookman'
            continue
        elif team_name == 'Binghamton' or team_name == 'BING' or team_name == 'BinghamtonBING': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Binghamton'
            continue
        elif team_name == 'Boise State' or team_name == 'BSU' or team_name == 'Boise StateBSU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Boise State'
            continue
        elif team_name == 'Boston Col' or team_name == 'BC' or team_name == 'Boston CollegeBC': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Boston College'
            continue
        elif team_name == 'Boston U' or team_name == 'BU' or team_name == 'Boston UniversityBU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Boston University'
            continue
        elif team_name == 'Bowling Grn' or team_name == 'BGSU' or team_name == 'Bowling GreenBGSU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Bowling Green'
            continue
        elif team_name == 'Bradley' or team_name == 'BRAD' or team_name == 'BradleyBRAD': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Bradley'
            continue 
        elif team_name == 'Brown' or team_name == 'BRWN' or team_name == 'BrownBRWN': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Brown'
            continue
        elif team_name == 'Bryant' or team_name == 'BRY' or team_name == 'BryantBRY': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Bryant'
            continue
        elif team_name == 'Bucknell' or team_name == 'BUCK' or team_name == 'BucknellBUCK': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Bucknell'
            continue
        elif team_name == 'Buffalo' or team_name == 'BUFF' or team_name == 'BuffaloBUFF': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Buffalo'
            continue
        elif team_name == 'Butler' or team_name == 'BUT' or team_name == 'ButlerBUT': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Butler'
            continue
        elif team_name == 'CS Bakersfld' or team_name == 'CSB' or team_name == 'CSU BakersfieldCSUB': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'CSU Bakersfield'
            continue
        elif team_name == 'CS Fullerton' or team_name == 'CSF' or team_name == 'CSU FullertonCSUF': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Cal State Fullerton'
            continue
        elif team_name == 'Cal Baptist' or team_name == 'CBU' or team_name == 'California BaptistCBU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'California Baptist'
            continue
        elif team_name == 'Cal Poly' or team_name == 'CP' or team_name == 'Cal PolyCP': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Cal Poly'
            continue
        elif team_name == 'Cal St Nrdge' or team_name == 'CSN' or team_name == 'CSU NorthridgeCSUN': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'CSUN'
            continue
        elif team_name == 'California' or team_name == 'CAL' or team_name == 'CaliforniaCAL': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'California'
            continue
        elif team_name == 'Campbell' or team_name == 'CAMP' or team_name == 'CampbellCAMP': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Campbell'
            continue
        elif team_name == 'Canisius' or team_name == 'CAN' or team_name == 'CanisiusCAN': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Canisius'
            continue
        elif team_name == 'Central Ark' or team_name == 'CARK' or team_name == 'Central ArkansasCARK': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Central Arkansas'
            continue
        elif team_name == 'Arkansas' or team_name == 'ARK' or team_name == 'ArkansasARK': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Arkansas'
            continue
        elif team_name == 'Central Conn' or team_name == 'CCSU' or team_name == 'Central ConnecticutCCSU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Central Connecticut State'
            continue
        elif team_name == 'Central FL' or team_name == 'UCFUCF': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'UCF'
            continue
        elif team_name == 'Central Mich' or team_name == 'CMU' or team_name == 'Central MichiganCMU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Central Michigan'
            continue
        elif team_name == 'Charl South' or team_name == 'CHSO' or team_name == 'Charleston SouthernCHSO': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Charleston Southern'
            continue
        elif team_name == 'Charlotte' or team_name == 'CHAR' or team_name == 'CharlotteCLT': # name same from tr / dk / fd / bs / nf / ESPN  
            elem[0] = 'Charlotte'
            continue
        elif team_name == 'Chattanooga' or team_name == 'CHAT' or team_name == 'ChattanoogaUTC': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Chattanooga'
            continue
        elif team_name == 'Chicago St' or team_name == 'CHS' or team_name == 'Chicago StateCHIC': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Chicago State'
            continue 
        elif team_name == 'Cincinnati' or team_name == 'CIN' or team_name == 'CincinnatiCIN': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Cincinnati'
            continue
        elif team_name == 'Citadel' or team_name == 'CIT' or team_name == 'The CitadelCIT': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Citadel'
            continue
        elif team_name == 'Clemson' or team_name == 'CLEM'or team_name == 'ClemsonCLEM': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Clemson'
            continue
        elif team_name == 'Cleveland St' or team_name == 'CLEV' or team_name == 'Cleveland StateCLEV': # added tr / dk / espn / nf | need fd / bs 
            elem[0] = 'Cleveland State'
            continue
        elif team_name == 'N Carolina' or team_name == 'UNC' or team_name == 'North CarolinaUNC': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'North Carolina'
            continue
        elif team_name == 'Coastal Car' or team_name == 'CCAR' or team_name == 'Coastal CarolinaCCU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Coastal Carolina'
            continue
        elif team_name == 'Col Charlestn' or team_name == 'COFC' or team_name == 'CharlestonCOFC': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Charleston'
            continue
        elif team_name == 'Colgate' or team_name == 'COLG' or team_name == 'ColgateCOLG': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Colgate'
            continue
        elif team_name == 'Colorado St' or team_name == 'CSU' or team_name == 'Colorado StateCSU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Colorado State'
            continue
        elif team_name == 'N Colorado' or team_name == 'UNCO' or team_name == 'Northern ColoradoUNCO': # added tr / dk / fd / nf | need bs / espn 
            elem[0] = 'Northern Colorado'
            continue
        elif team_name == 'Colorado' or team_name == 'COLO'or team_name == 'ColoradoCOLO': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Colorado'
            continue
        elif team_name == 'Columbia' or team_name == 'CLMB' or team_name == 'ColumbiaCLMB': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Columbia'
            continue
        elif team_name == 'Connecticut' or team_name == 'CONN' or team_name == 'UConnCONN': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'UConn'
            continue
        elif team_name == 'Coppin State' or team_name == 'COPP' or team_name == 'Coppin StateCOPP': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Coppin State'
            continue
        elif team_name == 'Cornell' or team_name == 'COR' or team_name == 'CornellCOR': # added tr / dk / nf / espn | need fd / bs #
            elem[0] = 'Cornell'
            continue 
        elif team_name == 'Creighton' or team_name == 'CREI' or team_name == 'CreightonCREI': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Creighton'
            continue
        elif team_name == 'Dartmouth' or team_name == 'DART' or team_name == 'DartmouthDART': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Dartmouth'
            continue
        elif team_name == 'Davidson' or team_name == 'DAV' or team_name == 'DavidsonDAV': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Davidson'
            continue 
        elif team_name == 'Dayton' or team_name == 'DAY' or team_name == 'DaytonDAY': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Dayton'
            continue
        elif team_name == 'DePaul' or team_name == 'DEP' or team_name == 'DePaulDEP': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'DePaul'
            continue
        elif team_name == 'Delaware St' or team_name == 'DSU' or team_name == 'Delaware StateDSU': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Delaware State'
            continue
        elif team_name == 'Delaware' or team_name == 'DEL' or team_name == 'DelawareDEL': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Delaware'
            continue
        elif team_name == 'Denver' or team_name == 'DEN' or team_name == 'DenverDEN': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Denver'
            continue
        elif team_name == 'Detroit' or team_name == 'DET' or team_name == 'Detroit MercyDET': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Detroit Mercy'
            continue
        elif team_name == 'Dixie State' or team_name == 'DXST' or team_name == 'Dixie StateDXST': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Dixie State'
            continue
        elif team_name == 'Stetson' or team_name == 'STET' or team_name == 'StetsonSTET': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Stetson'
            continue
        elif team_name == 'Drake' or team_name == 'DRKE' or team_name == 'DrakeDRKE': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Drake'
            continue
        elif team_name == 'Drexel' or team_name == 'DREX' or team_name == 'DrexelDREX': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Drexel'
            continue
        elif team_name == 'Duke' or team_name == 'DUKE' or team_name == 'DukeDUKE': # added tr / dk / fd / bs / nf / espn  
            elem[0] = 'Duke'
            continue
        elif team_name == 'Duquesne' or team_name == 'DUQ' or team_name == 'DuquesneDUQ': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Duquesne'
            continue
        elif team_name == 'E Carolina' or team_name == 'ECU' or team_name == 'East CarolinaECU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'East Carolina'
            continue
        elif team_name == 'W Illinois' or team_name == 'WIU' or team_name == 'Western IllinoisWIU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Western Illinois'
            continue
        elif team_name == 'E Illinois' or team_name == 'Eastern Illinois' or team_name == 'EIU' or team_name == 'Eastern IllinoisEIU': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Eastern Illinois'
            continue
        elif team_name == 'E Kentucky' or team_name == 'EKY' or team_name == 'Eastern KentuckyEKU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Eastern Kentucky'
            continue
        elif team_name == 'E Michigan' or team_name == 'EMU' or team_name == 'Eastern MichiganEMU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Eastern Michigan'
            continue
        elif team_name == 'E Tenn St' or team_name == 'East Tennessee State' or team_name == 'East Tennessee StateETSU': # added tr / dk / fd / bs / espn | need / nf 
            elem[0] = 'ETSU'
            continue
        elif team_name == 'E Washingtn' or team_name == 'EWU' or team_name == 'Eastern WashingtonEWU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Eastern Washington'
            continue
        elif team_name == 'Elon' or team_name == 'ELON' or team_name == 'ElonELON': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Elon'
            continue
        elif team_name == 'Evansville' or team_name == 'EVAN' or team_name == 'EvansvilleEVAN': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Evansville'
            continue
        elif team_name == 'F Dickinson' or team_name == 'FDU' or team_name == 'Fairleigh DickinsonFDU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Fairleigh Dickinson'
            continue
        elif team_name == 'Fairfield' or team_name == 'FAIR' or team_name == 'FairfieldFAIR': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Fairfield'
            continue
        elif team_name == 'Fla Atlantic' or team_name == 'FAU' or team_name == 'Florida AtlanticFAU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Florida Atlantic'
            continue
        elif team_name == 'Fla Gulf Cst' or team_name == 'FGCU' or team_name == 'Florida Gulf CoastFGCU': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'FGCU'
            continue
        elif team_name == 'Florida A&M' or team_name == 'FAMU' or team_name == 'Florida A&MFAMU': # added tr / dk / fd / bs / nf / espn
            elem[0] = 'Florida A&M'
            continue
        elif team_name == 'Florida Intl' or team_name == 'Florida International' or team_name == 'Florida InternationalFIU': # added tr / fd / bs / dk / nf / espn
            elem[0] = 'FIU'
            continue
        elif team_name == 'Florida St' or team_name == 'FSU' or team_name == 'Florida StateFSU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Florida State'
            continue
        elif team_name == 'N Florida' or team_name == 'UNF' or team_name == 'North FloridaUNF': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'North Florida'
            continue
        elif team_name == 'S Florida' or team_name == 'USF' or team_name == 'South FloridaUSF': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'South Florida'
            continue 
        elif team_name == 'Florida' or team_name == 'FLA' or team_name == 'FloridaFLA': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Florida'
            continue
        elif team_name == 'Fordham' or team_name == 'FOR' or team_name == 'FordhamFOR': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Fordham'
            continue
        elif team_name == 'Fresno St' or team_name == 'FRES' or team_name == 'Fresno StateFRES': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Fresno State'
            continue
        elif team_name == 'Furman' or team_name == 'FUR' or team_name == 'FurmanFUR': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Furman'
            continue 
        elif team_name == 'GA Southern' or team_name == 'GASO' or team_name == 'Georgia SouthernGASO': # added tr / dk / nf / espn | need fd / bs #
            elem[0] = 'Georgia Southern'
            continue 
        elif team_name == 'GA Tech' or team_name == 'GT' or team_name == 'Georgia TechGT': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Georgia Tech'
            continue
        elif team_name == 'Gard-Webb' or team_name == 'WEBB' or team_name == 'Gardner-WebbGWEB': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Gardner-Webb'
            continue
        elif team_name == 'Geo Mason' or team_name == 'GMU' or team_name == 'George MasonGMU': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'George Mason'
            continue 
        elif team_name == 'Geo Wshgtn' or team_name == 'GW' or team_name == 'George WashingtonGW': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'George Washington'
            continue 
        elif team_name == 'Georgetown' or team_name == 'GTWN' or team_name == 'GeorgetownGTWN': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Georgetown'
            continue 
        elif team_name == 'Georgia' or team_name == 'UGA' or team_name == 'GeorgiaUGA': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Georgia'
            continue 
        elif team_name == 'Georgia St' or team_name == 'GAST' or team_name == 'Georgia StateGAST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Georgia State'
            continue 
        elif team_name == 'Gonzaga' or team_name == 'GONZ' or team_name == 'GonzagaGONZ': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Gonzaga'
            continue 
        elif team_name == 'Grambling St' or team_name == 'Grambling State' or team_name == 'GRAM' or team_name == 'GramblingGRAM': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Grambling'
            continue 
        elif team_name == 'Grd Canyon' or team_name == 'GCU' or team_name == 'Grand CanyonGCU': # added tr / dk / nf/ espn | need fd / bs 
            elem[0] = 'Grand Canyon'
            continue 
        elif team_name == 'Hartford' or team_name == 'HART' or team_name == 'HartfordHART': # added tr / dk / fd / bs / nf / espn
            elem[0] = 'Hartford'
            continue 
        elif team_name == 'Harvard' or team_name == 'HARV' or team_name == 'HarvardHARV': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Harvard'
            continue 
        elif team_name == 'Hawaii' or team_name == 'HAW' or team_name == "Hawai'iHAW": # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Hawaii'
            continue 
        elif team_name == 'High Point' or team_name == 'HP' or team_name == 'High PointHP': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'High Point'
            continue 
        elif team_name == 'Hofstra' or team_name == 'HOF' or team_name == 'HofstraHOF': # added tr / dk / fd / bs / nf / espn
            elem[0] = 'Hofstra'
            continue 
        elif team_name == 'Holy Cross' or team_name == 'HC' or team_name == 'Holy CrossHC': # added tr / dk / fd / bs / espn / nf 
            elem[0] = 'Holy Cross'
            continue 
        elif team_name == 'Houston Bap' or team_name == 'HBU' or team_name == 'Houston BaptistHBU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Houston Baptist'
            continue 
        elif team_name == 'Houston' or team_name == 'HOU' or team_name == 'HoustonHOU': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Houston'
            continue 
        elif team_name == 'Howard' or team_name == 'HOW' or team_name == 'HowardHOW': # added tr / dk / fd / bs / nf / espn
            elem[0] = 'Howard'
            continue 
        elif team_name == 'IL-Chicago' or team_name == 'UICUIC': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'UIC'
            continue 
        elif team_name == 'IPFW' or team_name == 'Purdue Fort WaynePFW': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Purdue Fort Wayne'
            continue 
        elif team_name == 'IUPUI' or team_name == 'IUPU' or team_name == 'IUPUIIUPU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'IUPUI'
            continue 
        elif team_name == 'Idaho State' or team_name == 'IDST' or team_name == 'Idaho StateIDST': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Idaho State'
            continue 
        elif team_name == 'Idaho' or team_name == 'IDHO' or team_name == 'IdahoIDHO': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Idaho'
            continue 
        elif team_name == 'S Illinois' or team_name == 'SIU' or team_name == 'Southern IllinoisSIU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Southern Illinois'
            continue 
        elif team_name == 'Illinois St' or team_name == 'ILST' or team_name == 'Illinois StateILST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Illinois State'
            continue 
        elif team_name == 'Incar Word' or team_name == 'IW' or team_name == 'Incarnate WordUIW': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'UIW'
            continue 
        elif team_name == 'Indiana St' or team_name == 'INST' or team_name == 'Indiana StateINST': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Indiana State'
            continue 
        elif team_name == 'Indiana' or team_name == 'IND' or team_name == 'IndianaIU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Indiana'
            continue 
        elif team_name == 'Iona' or team_name == 'IONA' or team_name == 'IonaIONA': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Iona'
            continue 
        elif team_name == 'N Iowa' or team_name == 'Northern IowaUNI': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'UNI'
            continue
        elif team_name == 'Iowa State' or team_name == 'ISU' or team_name == 'Iowa StateISU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Iowa State'
            continue
        elif team_name == 'Iowa' or team_name == 'IOWA' or team_name == 'IowaIOWA': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Iowa'
            continue 
        elif team_name == 'Jackson St' or team_name == 'JKST' or team_name == 'Jackson StateJKST': # added tr / dk / fd / bs / espn | need  nf 
            elem[0] = 'Jackson State'
            continue
        elif team_name == 'Jacksonville' or team_name == 'JAC' or team_name == 'JacksonvilleJAX': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Jacksonville'
            continue
        elif team_name == 'James Mad' or team_name == 'JMU' or team_name == 'James MadisonJMU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'James Madison'
            continue
        elif team_name == 'Jksnville St' or team_name == 'JVST' or team_name == 'Jacksonville StateJVST': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Jacksonville State'
            continue
        elif team_name == 'Kansas St' or team_name == 'KSU' or team_name == 'Kansas StateKSU': # added tr / dk / espn / nf | need fd / bs 
            elem[0] = 'Kansas State'
            continue
        elif team_name == 'Kansas' or team_name == 'KU' or team_name == 'KansasKU': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Kansas'
            continue
        elif team_name == 'Kennesaw St' or team_name == 'KENN' or team_name == 'Kennesaw StateKENN': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Kennesaw State'
            continue
        elif team_name == 'Kent State' or team_name == 'KENT' or team_name == 'Kent StateKENT': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Kent State'
            continue
        elif team_name == 'LA Lafayette' or team_name == 'ULL' or team_name == 'LouisianaULL': # added tr / dk / nf | need fd / bs / espn 
            elem[0] = 'Louisiana-Lafayette'
            continue
        elif team_name == 'LA Monroe' or team_name == 'UL MonroeULM': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'ULM'
            continue
        elif team_name == 'LA Tech' or team_name == 'LT' or team_name == 'Louisiana TechLT': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Louisiana Tech'
            continue
        elif team_name == 'LIU' or team_name == 'Long Island UniversityLIU': # added tr / dk / nf | need fd / bs / espn 
            elem[0] = 'LIU'
            continue
        elif team_name == 'LSU' or team_name == 'LSULSU': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'LSU'
            continue
        elif team_name == 'La Salle' or team_name == 'LAS' or team_name == 'La SalleLAS': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'La Salle'
            continue
        elif team_name == 'Lafayette' or team_name == 'LAF' or team_name == 'LafayetteLAF': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Lafayette'
            continue
        elif team_name == 'Lamar' or team_name == 'LAM' or team_name == 'LamarLAM': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Lamar'
            continue
        elif team_name == 'Lehigh' or team_name == 'LEH' or team_name == 'LehighLEH': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Lehigh'
            continue
        elif team_name == 'Lg Beach St' or team_name == 'LBSU' or team_name == 'Long Beach StateLBSU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Long Beach State'
            continue
        elif team_name == 'Liberty' or team_name == 'LIB' or team_name == 'LibertyLIB': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Liberty'
            continue
        elif team_name == 'Lipscomb' or team_name == 'LIP' or team_name == 'LipscombLIP': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Lipscomb'
            continue
        elif team_name == 'Longwood' or team_name == 'LONG' or team_name == 'LongwoodLONG': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Longwood'
            continue
        elif team_name == 'Louisville' or team_name == 'LOU' or team_name == 'LouisvilleLOU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Louisville'
            continue
        elif team_name == 'Loyola Mymt' or team_name == 'Loyola MarymountLMU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'LMU'
            continue
        elif team_name == 'Loyola-Chi' or team_name == 'L-IL' or team_name == 'Loyola ChicagoLUC': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Loyola Chicago'
            continue
        elif team_name == 'Loyola-MD' or team_name == 'L-MD' or team_name == 'Loyola (MD)L-MD': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Loyola Maryland'
            continue
        elif team_name == 'Maine' or team_name == 'ME' or team_name == 'MaineMAINE': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Maine'
            continue
        elif team_name == 'Manhattan' or team_name == 'MAN' or team_name == 'ManhattanMAN': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Manhattan'
            continue
        elif team_name == 'Marist' or team_name == 'MRST' or team_name == 'MaristMRST': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Marist'
            continue
        elif team_name == 'Marquette' or team_name == 'MARQ' or team_name == 'MarquetteMARQ': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Marquette'
            continue 
        elif team_name == 'Marshall' or team_name == 'MRSH' or team_name == 'MarshallMRSH': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Marshall'
            continue
        elif team_name == 'Maryland BC' or team_name == 'UMBCUMBC' or team_name == 'UMBC': # added tr / dk / espn / nf | need fd / bs 
            elem[0] = 'UMBC'
            continue
        elif team_name == 'Maryland ES' or team_name == 'Maryland-Eastern ShoreUMES': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'UMES'
            continue
        elif team_name == 'Maryland' or team_name == 'MD' or team_name == 'MarylandMD': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Maryland'
            continue
        elif team_name == 'Mass Lowell' or team_name == 'UMass Lowell' or team_name == 'UML' or team_name == 'UMass LowellUML': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'UMass Lowell'
            continue
        elif team_name == 'McNeese St' or team_name == 'MCNS' or team_name == 'McNeeseMCNS': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'McNeese'
            continue
        elif team_name == 'Memphis' or team_name == 'MEM' or team_name == 'MemphisMEM': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Memphis'
            continue
        elif team_name == 'Mercer' or team_name == 'MER' or team_name == 'MercerMER': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Mercer'
            continue
        elif team_name == 'Merrimack' or team_name == 'MRMK' or team_name == 'MerrimackMRMK': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Merrimack'
            continue
        elif team_name == 'Miami (FL)' or team_name == 'MIA' or team_name == 'MiamiMIA': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Miami FL'
            continue
        elif team_name == 'Miami (OH)' or team_name == 'M-OH' or team_name == 'Miami (OH)M-OH': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Miami OH' 
            continue
        elif team_name == 'W Michigan' or team_name == 'WMU' or team_name == 'Western MichiganWMU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Western Michigan'
            continue
        elif team_name == 'Michigan St' or team_name == 'MSU' or team_name == 'Michigan StateMSU': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Michigan State'
            continue
        elif team_name == 'Michigan' or team_name == 'MICH' or team_name == 'MichiganMICH': # added tr / dk / nf | need fd / bs / espn 
            elem[0] = 'Michigan'
            continue
        elif team_name == 'Middle Tenn' or team_name == 'MTU' or team_name == 'Middle TennesseeMTSU': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Middle Tennessee'
            continue
        elif team_name == 'Minnesota' or team_name == 'MINN' or team_name == 'MinnesotaMINN': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Minnesota'
            continue
        elif team_name == 'Miss State' or team_name == 'MSST' or team_name == 'Mississippi StateMSST': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Mississippi State'
            continue
        elif team_name == 'Miss Val St' or team_name == 'Miss Valley State' or team_name == 'Mississippi Valley State' or team_name == 'MVSU' or team_name == 'Mississippi Valley StateMVSU': # added tr / dk / fd / bs / nf / espn
            elem[0] = 'Mississippi Valley'
            continue
        elif team_name == 'S Mississippi' or team_name == 'USM' or team_name == 'Southern MissUSM': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Southern Mississippi'
            continue 
        elif team_name == 'Mississippi' or team_name == 'MISS' or team_name == 'Ole MissMISS': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Ole Miss'
            continue
        elif team_name == 'Missouri St' or team_name == 'MOSU' or team_name == 'Missouri StateMOST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Missouri State'
            continue
        elif team_name == 'Monmouth' or team_name == 'MONM' or team_name == 'MonmouthMONM': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Monmouth'
            continue 
        elif team_name == 'Montana St' or team_name == 'MTST' or team_name == 'Montana StateMTST': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Montana State'
            continue
        elif team_name == 'Montana' or team_name == 'MONT' or team_name == 'MontanaMONT': # added tr / dk / fd / nf / espn | need bs 
            elem[0] = 'Montana'
            continue
        elif team_name == 'Morehead St' or team_name == 'MORE' or team_name == 'Morehead StateMORE': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Morehead State'
            continue
        elif team_name == 'Morgan St' or team_name == 'MORG' or team_name == 'Morgan StateMORG': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Morgan State'
            continue
        elif team_name == 'Mt St Marys' or team_name == 'MSM' or team_name == "Mount St. Mary'sMSM": # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Mount Saint Marys'
            continue
        elif team_name == 'Murray St' or team_name == 'MURR' or team_name == 'Murray StateMUR': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Murray State'
            continue
        elif team_name == 'N Alabama' or team_name == 'UNA' or team_name == 'North AlabamaUNA': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'North Alabama'
            continue
        elif team_name == 'N Dakota St' or team_name == 'NDSU' or team_name == 'North Dakota StateNDSU': # added tr / dk / fd / bs / nf / espn  
            elem[0] = 'North Dakota State'
            continue
        elif team_name == 'N Hampshire' or team_name == 'UNH' or team_name == 'New HampshireUNH': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'New Hampshire'
            continue 
        elif team_name == 'N Illinois' or team_name == 'NIU' or team_name == 'Northern IllinoisNIU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Northern Illinois'
            continue
        elif team_name == 'Illinois' or team_name == 'ILL' or team_name == 'IllinoisILL': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Illinois'
            continue 
        elif team_name == 'N Kentucky' or team_name == 'NKU' or team_name == 'Northern KentuckyNKU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Northern Kentucky'
            continue 
        elif team_name == 'N Mex State' or team_name == 'NMSU' or team_name == 'New Mexico StateNMSU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'New Mexico State'
            continue
        elif team_name == 'NC A&T' or team_name == 'NCAT' or team_name == 'North Carolina A&TNCAT': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'North Carolina A&T'
            continue
        elif team_name == 'NC Central' or team_name == 'NCCU' or team_name == 'North Carolina CentralNCCU': # added tr / dk / bs / nf / espn | need fd 
            elem[0] = 'North Carolina Central'
            continue
        elif team_name == 'NC State' or team_name == 'NCST' or team_name == 'NC StateNCST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'North Carolina State'
            continue
        elif team_name == 'NC-Asheville' or team_name == 'UNCA' or team_name == 'UNC AshevilleUNCA': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'UNC Asheville'
            continue
        elif team_name == 'NC-Grnsboro' or team_name == 'UNCG' or team_name == 'UNC GreensboroUNCG': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'UNC Greensboro'
            continue
        elif team_name == 'NC-Wilmgton' or team_name == '': # added tr / dk | need fd / bs / espn / nf #
            elem[0] = 'UNC Wilmington'
            continue
        elif team_name == 'NJIT' or team_name == 'NJITNJIT': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'NJIT'
            continue
        elif team_name == 'NW State' or team_name == 'NWST' or team_name == 'Northwestern StateNWST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Northwestern State'
            continue
        elif team_name == 'Navy' or team_name == 'NAVY' or team_name == 'NavyNAVY': # added tr / dk / fd / bs / nf / espn
            elem[0] = 'Navy'
            continue
        elif team_name == 'Neb Omaha' or team_name == 'NEOM' or team_name == 'OmahaOMA': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Omaha'
            continue
        elif team_name == 'Nebraska' or team_name == 'NEB' or team_name == 'NebraskaNEB': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Nebraska'
            continue
        elif team_name == 'Nevada' or team_name == 'NEV' or team_name == 'NevadaNEV': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Nevada'
            continue
        elif team_name == 'New Mexico' or team_name == 'UNM' or team_name == 'New MexicoUNM': # added tr / dk / espn / nf | need fd / bs 
            elem[0] = 'New Mexico'
            continue
        elif team_name == 'New Orleans' or team_name == 'NEW' or team_name == 'New OrleansUNO': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'New Orleans'
            continue
        elif team_name == 'Niagara' or team_name == 'NIAG' or team_name == 'NiagaraNIAG': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Niagara'
            continue
        elif team_name == 'Nicholls St' or team_name == 'NICH' or team_name == 'NichollsNICH': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Nicholls State'
            continue
        elif team_name == 'Norfolk St' or team_name == 'NORF' or team_name == 'Norfolk StateNORF': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Norfolk State'
            continue
        elif team_name == 'North Dakota' or team_name == 'UND' or team_name == 'North DakotaUND': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'North Dakota'
            continue
        elif team_name == 'North Texas' or team_name == 'UNT' or team_name == 'North TexasUNT': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'North Texas'
            continue
        elif team_name == 'Northeastrn' or team_name == 'NE' or team_name == 'NortheasternNE': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Northeastern'
            continue
        elif team_name == 'Northwestern' or team_name == 'NW' or team_name == 'NorthwesternNU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Northwestern'
            continue
        elif team_name == 'Notre Dame' or team_name == 'ND' or team_name == 'Notre DameND': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Notre Dame'
            continue
        elif team_name == 'Oakland' or team_name == 'OAK' or team_name == 'OaklandOAK': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Oakland'
            continue
        elif team_name == 'Ohio State' or team_name == 'OSU' or team_name == 'Ohio StateOSU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Ohio State'
            continue
        elif team_name == 'Ohio' or team_name == 'OHIO' or team_name == 'OhioOHIO': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Ohio'
            continue
        elif team_name == 'Oklahoma St' or team_name == 'OKST' or team_name == 'Oklahoma StateOKST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Oklahoma State'
            continue
        elif team_name == 'Oklahoma' or team_name == 'OKLA' or team_name == 'OklahomaOU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Oklahoma'
            continue
        elif team_name == 'Old Dominion' or team_name == 'ODU' or team_name == 'Old DominionODU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Old Dominion'
            continue
        elif team_name == 'Oral Roberts' or team_name == 'ORU' or team_name == 'Oral RobertsORU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Oral Roberts'
            continue 
        elif team_name == 'Oregon St' or team_name == 'ORST' or team_name == 'Oregon StateORST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Oregon State'
            continue
        elif team_name == 'Oregon' or team_name == 'ORE' or team_name == 'OregonORE': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Oregon'
            continue 
        elif team_name == 'Pacific' or team_name == 'PAC' or team_name == 'PacificPAC': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Pacific'
            continue
        elif team_name == 'Penn State' or team_name == 'PSU' or team_name == 'Penn StatePSU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Penn State'
            continue 
        elif team_name == 'Pepperdine' or team_name == 'PEPP' or team_name == 'PepperdinePEPP': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Pepperdine'
            continue 
        elif team_name == 'Pittsburgh' or team_name == 'PITT' or team_name == 'PittsburghPITT': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Pittsburgh'
            continue 
        elif team_name == 'Portland St' or team_name == 'PRST' or team_name == 'Portland StatePRST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Portland State'
            continue 
        elif team_name == 'Portland' or team_name == 'PORT' or team_name == 'PortlandPORT': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Portland'
            continue 
        elif team_name == 'Presbyterian' or team_name == 'PRE' or team_name == 'PresbyterianPRE': # added tr / dk / fd / bs / nf / espn
            elem[0] = 'Presbyterian'
            continue 
        elif team_name == 'Princeton' or team_name == 'PRIN' or team_name == 'PrincetonPRIN': # added tr / dk / nf / espn | need fd / bs #
            elem[0] = 'Princeton'
            continue 
        elif team_name == 'Providence' or team_name == 'PROV' or team_name == 'ProvidencePROV': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Providence'
            continue 
        elif team_name == 'Purdue' or team_name == 'PUR' or team_name == 'PurduePUR': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Purdue'
            continue 
        elif team_name == 'Quinnipiac' or team_name == 'QUIN' or team_name == 'QuinnipiacQUIN': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Quinnipiac'
            continue 
        elif team_name == 'Radford' or team_name == 'RAD' or team_name == 'RadfordRAD': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Radford'
            continue 
        elif team_name == 'Rhode Island' or team_name == 'URI' or team_name == 'Rhode IslandURI': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Rhode Island'
            continue 
        elif team_name == 'Rice' or team_name == 'RICE' or team_name == 'RiceRICE': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Rice'
            continue 
        elif team_name == 'Richmond' or team_name == 'RICH' or team_name == 'RichmondRICH': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Richmond'
            continue 
        elif team_name == 'Rider' or team_name == 'RID' or team_name == 'RiderRID': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Rider'
            continue 
        elif team_name == 'Rob Morris' or team_name == 'RMU' or team_name == 'Robert MorrisRMU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Robert Morris'
            continue 
        elif team_name == 'Rutgers' or team_name == 'RUTG' or team_name == 'RutgersRUTG': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Rutgers'
            continue 
        elif team_name == 'S Alabama' or team_name == 'USA' or team_name == 'South AlabamaUSA': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'South Alabama'
            continue 
        elif team_name == 'Alabama' or team_name == 'ALA' or team_name == 'AlabamaALA': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Alabama'
            continue
        elif team_name == 'S Car State' or team_name == 'SCST' or team_name == 'South Carolina StateSCST': # added tr / dk / bs / nf / espn | need fd 
            elem[0] = 'South Carolina State'
            continue 
        elif team_name == 'S Carolina' or team_name == 'SCAR' or team_name == 'South CarolinaSC': # added tr / dk / nf | need fd / bs / espn 
            elem[0] = 'South Carolina'
            continue 
        elif team_name == 'S Dakota St' or team_name == 'SDST' or team_name == 'South Dakota StateSDST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'South Dakota State'
            continue 
        elif team_name == 'S Methodist' or team_name == 'SMUSMU': # added tr / dk | need fd / bs / espn / nf 
            elem[0] = 'SMU'
            continue 
        elif team_name == 'S Utah' or team_name == 'SUU' or team_name == 'Southern UtahSUU': # added tr / dk / fd / nf / espn | need bs 
            elem[0] = 'Southern Utah'
            continue 
        elif team_name == 'SC Upstate' or team_name == 'SCUS' or team_name == 'South Carolina UpstateSCUP': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'USC Upstate'
            continue 
        elif team_name == 'SE Louisiana' or team_name == 'SELA' or team_name == 'SE LouisianaSELA': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Southeastern Louisiana'
            continue 
        elif team_name == 'SE Missouri' or team_name == 'SE Missouri State' or team_name == 'SEMO' or team_name == 'Southeast Missouri StateSEMO': # added tr / dk / fd / nf / espn | need bs
            elem[0] = 'Southeast Missouri State'
            continue 
        elif team_name == 'Missouri' or team_name == 'MIZZ' or team_name == 'MissouriMIZ': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Missouri'
            continue
        elif team_name == 'SIU Edward' or team_name == 'SIU Edwardsville' or team_name == 'SIU EdwardsvilleSIUE': # added tr / dk / fd / nf / espn | need bs 
            elem[0] = 'SIUE'
            continue
        elif team_name == 'Sac State' or team_name == 'CSUS' or team_name == 'Sacramento StateSAC': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Sacramento State'
            continue
        elif team_name == 'Sacred Hrt' or team_name == 'SHU' or team_name == 'Sacred HeartSHU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Sacred Heart'
            continue
        elif team_name == 'Saint Louis' or team_name == 'SLU' or team_name == 'Saint LouisSLU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Saint Louis'
            continue
        elif team_name == 'Sam Hous St' or team_name == 'SHSU' or team_name == 'Sam HoustonSHSU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Sam Houston'
            continue
        elif team_name == 'Samford' or team_name == 'SAM' or team_name == 'SamfordSAM': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Samford'
            continue
        elif team_name == 'San Diego St' or team_name == 'SDSU' or team_name == 'San Diego StateSDSU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'San Diego State'
            continue
        elif team_name == 'UC San Diego' or team_name == 'UCSD' or team_name == 'UC San DiegoUCSD': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'UC San Diego'
            continue
        elif team_name == 'San Diego' or team_name == 'USD' or team_name == 'San DiegoUSD': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'San Diego'
            continue
        elif team_name == 'San Fransco' or team_name == 'SF' or team_name == 'San FranciscoSF': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'San Francisco'
            continue
        elif team_name == 'San Jose St' or team_name == 'SJSU' or team_name == 'San José StateSJSU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'San Jose State'
            continue
        elif team_name == 'Santa Clara' or team_name == 'SCU' or team_name == 'Santa ClaraSCU': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Santa Clara'
            continue
        elif team_name == 'Seattle' or team_name == 'SEA' or team_name == 'Seattle USEA': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Seattle'
            continue
        elif team_name == 'Seton Hall' or team_name == 'HALL' or team_name == 'Seton HallHALL': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Seton Hall'
            continue
        elif team_name == 'Siena' or team_name == 'SIE' or team_name == 'SienaSIE': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Siena'
            continue
        elif team_name == 'South Dakota' or team_name == 'SDAK' or team_name == 'South DakotaSDAK': # added tr / dk / fd / bs / nf / espn
            elem[0] = 'South Dakota'
            continue
        elif team_name == 'Southern' or team_name == 'SOU' or team_name == 'SouthernSOU': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Southern University'
            continue
        elif team_name == 'St Bonavent' or team_name == 'SBON' or team_name == 'St. BonaventureSBU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Saint Bonaventure'
            continue
        elif team_name == 'St Fran (NY)' or team_name == 'SFNY' or team_name == 'St. Francis (BKN)SFBK': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Saint Francis Brooklyn'
            continue
        elif team_name == 'St Fran (PA)' or team_name == 'SFPA' or team_name == 'St. Francis (PA)SFPA': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Saint Francis PA'
            continue
        elif team_name == 'St Johns' or team_name == 'SJU' or team_name == "St. John'sSJU": # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Saint Johns'
            continue
        elif team_name == 'St Josephs' or team_name == 'JOES' or team_name == "Saint Joseph'sJOES": # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Saint Josephs'
            continue
        elif team_name == 'St Marys' or team_name == 'SMC' or team_name == "Saint Mary'sSMC": # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Saint Marys'
            continue
        elif team_name == 'St Peters' or team_name == 'SPC' or team_name == "Saint Peter'sSPU": # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Saint Peters'
            continue
        elif team_name == 'St. Thomas (MN)' or team_name == 'STMN' or team_name == 'St. Thomas - MinnesotaSTMN': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Saint Thomas MN'
            continue
        elif team_name == 'Stanford' or team_name == 'STAN' or team_name == 'StanfordSTAN': # added tr / dk / nf | need fd / bs / espn 
            elem[0] = 'Stanford'
            continue
        elif team_name == 'Ste F Austin' or team_name == 'Stephen F. AustinSFA': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'SFA'
            continue
        elif team_name == 'Stony Brook' or team_name == 'STON' or team_name == 'Stony BrookSTBK': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Stony Brook'
            continue
        elif team_name == 'Syracuse' or team_name == 'SYR' or team_name == 'SyracuseSYR': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Syracuse'
            continue
        elif team_name == 'TN Martin' or team_name == 'UTM' or team_name == 'UT MartinUTM': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'UT Martin'
            continue
        elif team_name == 'TN State' or team_name == 'TNST' or team_name == 'Tennessee StateTNST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Tennessee State'
            continue 
        elif team_name == 'TN Tech' or team_name == 'Tennessee Tech' or team_name == 'TNTC' or team_name == 'Tennessee TechTNTC': # added tr / dk / fd / bs / nf / espn
            elem[0] = 'Tennessee Tech'
            continue
        elif team_name == 'TX A&M-CC' or team_name == 'AMCC' or team_name == 'Texas A&M-CCAMCC': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'A&M-Corpus Christi'
            continue
        elif team_name == 'TX Christian' or team_name == 'TCUTCU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'TCU'
            continue
        elif team_name == 'TX El Paso' or team_name == 'UTEPUTEP': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'UTEP'
            continue
        elif team_name == 'TX Southern' or team_name == 'TXSO' or team_name == 'Texas SouthernTXSO': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Texas Southern'
            continue
        elif team_name == 'TX-Arlington' or team_name == 'UTA' or team_name == 'UT ArlingtonUTA': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'UT Arlington'
            continue
        elif team_name == 'TX-Pan Am' or team_name == 'TRGV' or team_name == 'UT Rio Grande ValleyRGV': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'UTRGV'
            continue
        elif team_name == 'TX-San Ant' or team_name == 'UTSAUTSA': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'UTSA'
            continue
        elif team_name == 'Tarleton State' or team_name == 'TAR' or team_name == 'TarletonTAR': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Tarleton State'
            continue
        elif team_name == 'Temple' or team_name == 'TEM' or team_name == 'TempleTEM': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Temple'
            continue
        elif team_name == 'Tennessee' or team_name == 'TENN' or team_name == 'TennesseeTENN': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Tennessee'
            continue
        elif team_name == 'Texas A&M' or team_name == 'TA&M' or team_name == 'Texas A&MTA&M': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Texas A&M'
            continue
        elif team_name == 'Texas State' or team_name == 'TXST' or team_name == 'Texas StateTXST': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Texas State'
            continue
        elif team_name == 'Texas Tech' or team_name == 'TTU' or team_name == 'Texas TechTTU': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Texas Tech'
            continue
        elif team_name == 'Texas' or team_name == 'TEX' or team_name == 'TexasTEX': # added tr / dk / fd / bs / nf / espn  
            elem[0] = 'Texas'
            continue
        elif team_name == 'Toledo' or team_name == 'TOL' or team_name == 'ToledoTOL': # added tr / dk / espn / nf | need fd / bs
            elem[0] = 'Toledo'
            continue
        elif team_name == 'Towson' or team_name == 'TOWS' or team_name == 'TowsonTOW': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Towson'
            continue
        elif team_name == 'Troy' or team_name == 'TROY' or team_name == 'TroyTROY': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Troy'
            continue
        elif team_name == 'Tulane' or team_name == 'TULN' or team_name == 'TulaneTULN': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Tulane'
            continue
        elif team_name == 'Tulsa' or team_name == 'TLSA' or team_name == 'TulsaTLSA': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Tulsa'
            continue
        elif team_name == 'U Mass' or team_name == 'MASS' or team_name == 'UMassMASS': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Massachusetts'
            continue 
        elif team_name == 'U Penn' or team_name == 'PENN' or team_name == 'PennsylvaniaPENN': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Pennsylvania'
            continue
        elif team_name == 'UAB'  or team_name == 'UABUAB': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'UAB'
            continue
        elif team_name == 'UC Davis' or team_name == 'UCD' or team_name == 'UC DavisUCD': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'UC Davis'
            continue
        elif team_name == 'UC Irvine' or team_name == 'UCI' or team_name == 'UC IrvineUCI': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'UC Irvine'
            continue
        elif team_name == 'UC Riverside' or team_name == 'UCRV' or team_name == 'UC RiversideUCR': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'UC Riverside'
            continue
        elif team_name == 'UCLA' or team_name == 'UCLAUCLA': # added tr / dk / nf / espn | need fd / bs  ### SHOULD CHECK UCLA ON ESPN
            elem[0] = 'UCLA'
            continue
        elif team_name == 'UCSB' or team_name == 'UC Santa BarbaraUCSB': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'UC Santa Barbara'
            continue
        elif team_name == 'UMKC' or team_name == 'Kansas CityKC': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Kansas City'
            continue
        elif team_name == 'UNLV' or team_name == 'UNLVUNLV': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'UNLV'
            continue
        elif team_name == 'USC' or team_name == 'USCUSC': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'USC'
            continue
        elif team_name == 'Utah State' or team_name == 'USU' or team_name == 'Utah StateUSU': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Utah State'
            continue 
        elif team_name == 'Utah Val St' or team_name == 'UVU' or team_name == 'Utah ValleyUVU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Utah Valley'
            continue
        elif team_name == 'Utah' or team_name == 'UTAH' or team_name == 'UtahUTAH': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Utah'
            continue
        elif team_name == 'VA Military' or team_name == 'VMIVMI': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'VMI'
            continue
        elif team_name == 'VA Tech' or team_name == 'Virginia Tech' or team_name == 'VT' or team_name == 'Virginia TechVT': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Virginia Tech'
            continue 
        elif team_name == 'VCU' or team_name == 'VCUVCU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'VCU'
            continue
        elif team_name == 'Valparaiso' or team_name == 'VALP' or team_name == 'ValparaisoVALP': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Valparaiso'
            continue
        elif team_name == 'Vanderbilt' or team_name == 'VAN' or team_name == 'VanderbiltVAN': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Vanderbilt'
            continue
        elif team_name == 'Vermont' or team_name == 'UVM' or team_name == 'VermontUVM': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Vermont'
            continue
        elif team_name == 'Villanova' or team_name == 'VILL' or team_name == 'VillanovaVILL': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Villanova'
            continue
        elif team_name == 'W Virginia' or team_name == 'WVU' or team_name == 'West VirginiaWVU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'West Virginia'
            continue
        elif team_name == 'Virginia' or team_name == 'UVA' or team_name == 'VirginiaUVA': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Virginia'
            continue
        elif team_name == 'W Carolina' or team_name == 'WCU' or team_name == 'Western CarolinaWCU': # added tr / dk / fd / bs / nf / espn 
            elem[0] = 'Western Carolina'
            continue
        elif team_name == 'W Kentucky' or team_name == 'WKU' or team_name == 'Western KentuckyWKU': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Western Kentucky'
            continue
        elif team_name == 'Kentucky' or team_name == 'UK' or team_name == 'KentuckyUK': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Kentucky'
            continue
        elif team_name == 'WI-Grn Bay' or team_name == 'GB' or team_name == 'Green BayGB': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Green Bay'
            continue
        elif team_name == 'WI-Milwkee' or team_name == 'MILW' or team_name == 'MilwaukeeMILW': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Milwaukee'
            continue
        elif team_name == 'Wagner' or team_name == 'WAG' or team_name == 'WagnerWAG': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Wagner'
            continue
        elif team_name == 'Wake Forest' or team_name == 'WAKE' or team_name == 'Wake ForestWAKE': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Wake Forest'
            continue
        elif team_name == 'Wash State' or team_name == 'WSU' or team_name == 'Washington StateWSU': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Washington State'
            continue
        elif team_name == 'Washington' or team_name == 'WASH' or team_name == 'WashingtonWASH': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Washington'
            continue
        elif team_name == 'Weber State' or team_name == 'WEB' or team_name == 'Weber StateWEB': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Weber State'
            continue
        elif team_name == 'Wichita St' or team_name == 'WICH' or team_name == 'Wichita StateWICH': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Wichita State'
            continue
        elif team_name == 'Winthrop' or team_name == 'WIN' or team_name == 'WinthropWIN': # added tr / dk / nf / espn | need fd / bs
            elem[0] = 'Winthrop'
            continue
        elif team_name == 'Wisconsin' or team_name == 'WIS' or team_name == 'WisconsinWISC': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Wisconsin'
            continue
        elif team_name == 'Wofford' or team_name == 'WOF' or team_name == 'WoffordWOF': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Wofford'
            continue
        elif team_name == 'Wright State' or team_name == 'WRST' or team_name == 'Wright StateWRST': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Wright State'
            continue
        elif team_name == 'Wyoming' or team_name == 'WYO' or team_name == 'WyomingWYO': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Wyoming'
            continue
        elif team_name == 'Xavier' or team_name == 'XAV' or team_name == 'XavierXAV': # added tr / dk / nf / espn | need fd / bs  
            elem[0] = 'Xavier'
            continue
        elif team_name == 'Yale' or team_name == 'YALE' or team_name == 'YaleYALE': # added tr / dk / nf / espn | need fd / bs 
            elem[0] = 'Yale'
            continue
        elif team_name == 'Youngs St' or team_name == 'YSU' or team_name == 'Youngstown StateYSU': # added tr / dk / espn / nf | need fd / bs 
            elem[0] = 'Youngstown State'
            continue
        else:
            elem[0] = team_name
            continue
    return lst

        
draftkings_cbb = rename(draftkings_cbb)
barstool_cbb = rename(barstool_cbb)
fanduel_cbb = rename(fanduel_cbb)
tr_data = rename(tr_data)

# for elem in draftkings_cbb:
#     print(elem)
# print('\n')
# for elem in barstool_cbb:
#     print(elem)
# print('\n') 
# for elem in fanduel_cbb:
#     print(elem)
# print('\n')
# print(tr_data)
# print('\n') 
# for elem in game_times:
#     print(elem)
# print('\n')

### COMBINING STATS AND ODDS, INDIVIDUALLY ###


dict_draftkings_cbb = {x[0]:x[1:] for x in draftkings_cbb}
dict_fanduel_cbb = {x[0]:x[1:] for x in fanduel_cbb}
dict_barstool_cbb = {x[0]:x[1:] for x in barstool_cbb}


dict_tr_data = {x[0]:x[1:] for x in tr_data}
tr_keys = (dict_tr_data.keys())

def concat(lst):
    global dict_tr_data
    global tr_keys 
    awayHome = ['A', 'H']
    i = 0
    m = 0
    lst_cbb = []
    while True: 
        if i < len(lst):
            b = i + 1
            if lst[i][0] not in tr_keys or lst[b][0] not in tr_keys:
                i += 2
                continue
            else:
                awayTeam = dict_tr_data[lst[i][0]]
                homeTeam = dict_tr_data[lst[b][0]]
                lst_cbb.append(lst[i] + awayTeam + [awayHome[0]])
                lst_cbb.append(lst[b] + homeTeam + [awayHome[1]])
                i += 2
                continue
        else:
            break
    return lst_cbb

draftkings_cbb = concat(draftkings_cbb)
barstool_cbb = concat(barstool_cbb)
fanduel_cbb = concat(fanduel_cbb)

concat_scraped_time = time.perf_counter()
print('\n')
print(f'Added team stats to each sportsbook list in {concat_scraped_time - start_time:0.4f} seconds')
print('\n')

# print("draftkings:")
# for elem in draftkings_cbb:
#     print(elem)
# print('\n')
# print('barstool')
# for elem in barstool_cbb:
#     print(elem)
# print('\n')
# print('fanudel')
# for elem in fanduel_cbb:
#     print(elem)

### DONE COMBINING STATS AND ODDS ###
 
### CURRENT LIST STRUCTURE ###   
# _cbb = spr, spr_o, ml, total, o/u_odds (a/h), t_pfa, h_pfa, a_pfa, t_paa, h_paa, a_paa

### GETTING LEAGUE AVERAGE STATS ###

for elem in tr_data:
    if elem[5] == '--':
        continue
    else:
        elem[5] = float(elem[5])

# get League Avg Points Against
i = 0
a = 0
h = 0
while True:
    if i < len(tr_data):
        if tr_data[i][5] != '--' and tr_data[i][6] != '--':
            a = a + tr_data[i][6] #tr_data[i][5] = Home Pts Against ..... tr_data[i][6] = Away Pts Against
            h = h + tr_data[i][5]
            i += 1
            continue
        else:
            a = a + tr_data[i][4] # backup total if data for home/away is not yet available
            h = h + tr_data[i][4]
            i += 1
            continue
    else:
        a = a / len(tr_data)
        leagueAvgAgainst_away = round(a, 2)
        h = h / len(tr_data)
        leagueAvgAgainst_home = round(h, 2)
        break

### NOW HAVE LEAGUE AVERAGE POINTS AGAINST FOR HOME AND AWAY TEAMS ###

### CALCULATING EXPECTED POINTS ###
# Expected Points
def exppts(lst):
    i = 0
    length = len(lst)
    while True: 
        if i < length:
            h = i + 1
            print(lst[i])
            print(lst[h])
            a = float(lst[i][8]) * float(lst[h][10]) / leagueAvgAgainst_home # [6] and [9] for totals, [8] and [10] for away team
            # a_spr = float(lst[i][8]) * float(lst[h][10]) / leagueAvgAgainst_home
            # a_spr = round(a_spr, 2)
            away = round(a, 2)
            a_spr = away + float(lst[i][1])
            a_spr = round(a_spr, 2)
            lst[i].append(away) #[i][13] straight points
            lst[i].append(a_spr) #[i][14] points + spread
            # home_spr = (float(lst[h][7]) + float(lst[h][1])) * float(lst[i][11]) / leagueAvgAgainst_away # [6] and [9] for totals, [7] and [11] for home team
            # home_spr = round(home_spr, 2)
            home = float(lst[h][7]) * float(lst[i][11]) / leagueAvgAgainst_away
            home = round(home, 2)
            home_spr = home + float(lst[i][1])
            home_spr = round(home_spr, 2)
            lst[h].append(home) #[i][13] straight points
            lst[h].append(home_spr) #[i][14] points + spread
            total = away + home
            lst[i].append(total) #[i][15] total
            lst[h].append(total) #[i][15] total
            i += 2
            continue
        else:
            break
    return lst

#[i][13] straight points [i][14] points + spread [i][15] total

fanduel_cbb = exppts(fanduel_cbb)
draftkings_cbb = exppts(draftkings_cbb)
barstool_cbb = exppts(barstool_cbb)


### CREATING LIST OF POSSIBLE POINTS ###
possiblePoints = []
p = 0
while True: 
    if p < 120:
        possiblePoints.append(int(p))
        p += 1
        continue
    else: 
        break

def poi(lst):
    # Poisson for range for each team, EXPECTED = 13, SPREAD = 14, EXP TOTAL = 15
    poissonAway = []
    poissonHome = []
    poissonAway_spr = []
    poissonHome_spr = []
    i = 0
    p = 0
    h = i + 1
    while True: 
        if p < len(possiblePoints) and i < len(lst):
            expectA = float(lst[i][13])
            expectH = float(lst[h][13])
            chancePerScoreAway = ((expectA**(possiblePoints[p])) * (math.exp(-expectA)) / math.factorial(possiblePoints[p]))
            poissonAway.append(chancePerScoreAway)
            chancePerScoreHome = ((expectH**(possiblePoints[p])) * (math.exp(-expectH)) / math.factorial(possiblePoints[p]))
            poissonHome.append(chancePerScoreHome)
            expectA_spr = float(lst[i][14])
            expectH_spr = float(lst[h][14])
            chancePerScoreAway = ((expectA_spr**(possiblePoints[p])) * (math.exp(-expectA_spr)) / math.factorial(possiblePoints[p]))
            poissonAway_spr.append(chancePerScoreAway)
            chancePerScoreHome = ((expectH_spr**(possiblePoints[p])) * (math.exp(-expectH_spr)) / math.factorial(possiblePoints[p]))
            poissonHome_spr.append(chancePerScoreHome)
            p += 1
            continue
        elif len(poissonAway) == len(possiblePoints):
            if h <= len(lst):
                lst[i].append(poissonAway) #[i][16]
                lst[h].append(poissonHome) #[i][16]
                lst[i].append(poissonAway_spr) #[i][17]
                lst[h].append(poissonHome_spr) #[i][17]
                p = 0
                i += 2
                h = i + 1
                poissonAway = []
                poissonHome = []
                poissonAway_spr = []
                poissonHome_spr = []
                continue
            else:
                break
        else:
            break
    return lst

fanduel_cbb = poi(fanduel_cbb)
draftkings_cbb = poi(draftkings_cbb)
barstool_cbb = poi(barstool_cbb)

### CALCULATING CHANCES ###

def win_chance(lst):
    h = 0
    a = 0
    h_s = 0
    a_s = 0
    x = 0
    y = x + 1
    while True: # poisson
        if y <= len(lst):
            for i in range (100000):
                q = np.asarray(possiblePoints)
                awayArray_poisson = np.asarray(lst[x][16])
                awayArray_spr_poisson = np.asarray(lst[x][17])
                homeArray_poisson = np.asarray(lst[y][16])
                homeArray_spr_poisson = np.asarray(lst[y][17])
                awayChance = random.choices(q, awayArray_poisson)
                awayChance_spr = random.choices(q, awayArray_spr_poisson)
                homeChance = random.choices(q, homeArray_poisson)
                homeChance_spr = random.choices(q, homeArray_spr_poisson)
                if homeChance > awayChance:
                    h += 1
                if awayChance > homeChance:
                    a += 1
                if homeChance_spr > awayChance_spr:
                    h_s += 1
                if awayChance_spr > homeChance_spr:
                    a_s += 1
            w = round(a + h, 2)
            w_s = round(a_s + h_s, 2)
            a = (a / w) * 100
            a = round(a, 2)
            a_s = (a_s / w_s) * 100
            a_s = round(a_s, 2)
            h = (h / w) * 100
            h = round(h, 2)
            h_s = (h_s / w) * 100
            h_s = round(h_s, 2)
            lst[x].append(a) #[i][18] ... [i][16] calculated chance
            lst[x].append(a_s) #[i][19] ... [i][17] calculated chance vs spread
            lst[y].append(h) #[i][18] ... [i][16]
            lst[y].append(h_s) #[i][19] ... [i][17]
            del lst[x][16:18]
            del lst[y][16:18]
            x += 2
            y = x + 1
            h = 0
            a = 0
            a_s = 0
            h_s = 0
            continue
        else:
            break
    return lst

#[i][13] straight points [i][14] points + spread [i][15] total [i][16] calculated chance [i][17] calculated chance vs spread

fanduel_cbb = win_chance(fanduel_cbb)
draftkings_cbb = win_chance(draftkings_cbb)
barstool_cbb = win_chance(barstool_cbb)

calc_chance_time = time.perf_counter()
print('\n')
print(f'Calculated chances in {calc_chance_time - start_time:0.4f} seconds')
print('\n')


### NUMBERFIRE CHANCES ###
today = date.today()
tomorrow = today + timedelta(1)
twodays = today + timedelta(2)
threedays = today + timedelta(3)
fourdays = today + timedelta(4)
fivedays = today + timedelta(5)
url_nf_cbb = "https://www.numberfire.com/ncaab/games/" 
nf_html = requests.get(url_nf_cbb) #url_today
nf_soup = bs4.BeautifulSoup(nf_html.content, features='html.parser') 
scrapeNumberfireNCAAB_teams = nf_soup.findAll('span', attrs={'class':'abbrev'})

nf_team = []
for elem in scrapeNumberfireNCAAB_teams:
    el = elem.text
    nf_team.append(el)

x = int(len(nf_team) / 2)
nf_team = np.array_split(nf_team, x)

nf_teams = []
for elem in nf_team:
    lst = list(elem)
    nf_teams.append(lst)
    
scrapeNumberfireNCAAB = nf_soup.findAll('div', attrs={'class':'win-probability-wrap'}) 

nf_chances = []
for elem in scrapeNumberfireNCAAB:
    ch = elem.text
    ch = ch.replace('\n', '')
    # print(ch)
    ch = ch.replace('win probability', '')
    # print(ch)
    l = ch.split('%')
    team = l[1]
    team = team.replace('                    ', '')
    team = team.replace('                                ', '')
    team = team.replace('            ', '')
    chance = l[0]
    chance = chance.replace('                                                                    ', '')
    chance = float(l[0])
    chance = round(chance, 1)
    nf_lst = []
    nf_lst.append(team)
    nf_lst.append(chance)
    nf_chances.append(nf_lst)
    
dict_nf_chances = {x[0]:x[1:] for x in nf_chances}
nf_keys = (dict_nf_chances.keys())

for elem in nf_teams:
    a = elem[0]
    h = elem[1]
    if a in nf_keys:
        away_chance = dict_nf_chances[a]
        away_chance = away_chance[0]
        home_chance = 100 - away_chance
        home_chance = round(home_chance, 1)
        elem.insert(1, away_chance)
        elem.append(home_chance)
    else:
        home_chance = dict_nf_chances[h]
        home_chance = home_chance[0]
        away_chance = 100 - home_chance
        away_chance = round(away_chance, 1)
        elem.insert(1, away_chance)
        elem.append(home_chance)

nf_chances = []       
for elem in nf_teams:
    away = elem[:2]
    home = elem[2:]
    nf_chances.append(away)
    nf_chances.append(home)
    
# for elem in nf_chances:
#     print(elem)

#[i][13] straight points [i][14] points + spread [i][15] total [i][16] calculated chance [i][17] calculated chance vs spread [18] numberfire chance

### GOT LIST OF NUMBERFIRE CHANCES ###

### CHANGING NAMES OF NUMBERFIRE CHANCES AND APPENDING TO LISTS FROM FD / DK / BS ###

nf_chances = rename(nf_chances)

# print('NUMBERFIRE CHANCES / NAMES CHANGED')
# for elem in nf_chances:
#     print(elem)
# print('\n')

### NUMBERFIRE NAMES CHANGED ###

### ADDING NF CHANCES TO LISTS ###

dict_nf_chances = {x[0]:x[1:] for x in nf_chances}
nf_keys = (dict_nf_chances.keys())

# print(dict_nf_chances)

def nf(lst):
    i = 0
    while True: 
        if i < len(lst):
            b = i + 1
            if lst[i][0] in nf_keys and lst[b][0] in nf_keys:
                awayTeamList = dict_nf_chances[lst[i][0]]
                if len(awayTeamList) == 0:
                    i += 2
                    continue
                # print(awayTeamList)
                # print('\n')
                awayTeamChance = awayTeamList[0]
                # print(awayTeamChance)
                # print('\n')
                homeTeamList = dict_nf_chances[lst[b][0]]
                if len(homeTeamList) == 0:
                    i += 2
                    continue
                # print(homeTeamList)
                # print('\n')
                homeTeamChance = homeTeamList[0]
                # print(homeTeamChance)
                # print('\n')
                lst[i].append(awayTeamChance) #[i][18] numberfire chance
                lst[b].append(homeTeamChance) #[i][18] numberfire chance
                i += 2
                continue
            else:
                i += 2
                continue
        else:
            break  
    # for elem in lst:
        # print(elem)
        # print(len(elem))
        # if len(elem) != 19:
        #     del elem
        # print('\n')
    return lst

fanduel_cbb = nf(fanduel_cbb)
draftkings_cbb = nf(draftkings_cbb)
barstool_cbb = nf(barstool_cbb)

### DONE DDING NF CHANCES TO LISTS ###

nf_chance_time = time.perf_counter()
print('\n')
print(f'Scraped Numberfire chances in {nf_chance_time - start_time:0.4f} seconds')
print('\n')

### GETTING ESPN CHANCES ###

today = date.today().strftime("%Y%m%d")
df_espn = pd.read_html('http://www.espn.com/mens-college-basketball/bpi/_/view/predictions/group/50/date/' + str(today))
espn_chances = df_espn[0].values.tolist()

# for elem in espn_chances:
#     print(elem)

i = 0
j = i + 1
while True:
    if i < len(espn_chances):
        if len(espn_chances[i]) > 3:
            if str(espn_chances[i][0]) == 'PAC12':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ESPN':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEESPN':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ESPNN':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ACCNX':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEACCNX':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'FOX': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ESPNU/ESPN+': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEFOX': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEPAC12':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'SECN+/ESPN+': 
                del espn_chances[i][0]
                continue 
            elif str(espn_chances[i][0]) == 'ESPNU/ESPN3': 
                del espn_chances[i][0]
                continue 
            elif str(espn_chances[i][0]) == 'ACCNX/ESPN+':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'Final':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'Final/OT':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEESPN2':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ESPN2/ESPNU': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ESPN2':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'nan':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'FS1':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ESPN+':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEFS1':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ACCN/ACCNX':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ACCN':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'TNT':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LHN': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEACCN':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVECBSSN':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'CBSSN':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'CBS':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVECBS':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'BTN':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEBTN':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEESPN+':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ESPN3':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'SECN/ESPN+':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'USA Net': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEESPNU':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'Canceled':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ESPNU': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'SECN+': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'FS2':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEFS2':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEESPN3':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'BIG12|ESPN+':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'SECN':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ABC':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVESECN':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'ESPN2/ESPN3':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVE':
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'Postponed': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVELHN': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEACCN/ESPN+': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVEBIG12|ESPN+': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'LIVESECN+/ESPN+': 
                del espn_chances[i][0]
                continue
            elif str(espn_chances[i][0]) == 'Forfeit': 
                del espn_chances[i]
                continue
            elif str(espn_chances[i][0]) == 'Canceled': 
                del espn_chances[i]
                continue
            elif type(espn_chances[i][1]) is float:
                del espn_chances[i][1]
                continue
            elif str(espn_chances[i][1][-1]) != '%':
                del espn_chances[i][1]
                continue
            elif str(espn_chances[i][1][-1]) == '%':
                del espn_chances[i][2:]
                i += 1
                continue
        else:
            i += 1
            j = i + 1
            continue
    else:
        break

i = 0
r = 1
while True:
    if i < len(espn_chances):
        if len(espn_chances[i]) == 3:
            del espn_chances[i][1:]
            i += 1
            continue
        else:
            i += 1
            continue
    else:
        break
    
i = 0
while True:
    if i < len(espn_chances):
        name = espn_chances[i][0]
        if name[-1] == '-':
            name = name[0:-1]
            espn_chances[i][0] = name
            continue
        elif name[-1] == '0':
            name = name[0:-1]
            espn_chances[i][0] = name
            continue
        elif name[-1] == '1':
            name = name[0:-1]
            espn_chances[i][0] = name
            continue
        elif name[-1] == '2':
            name = name[0:-1]
            espn_chances[i][0] = name
            continue
        elif name[-1] == '3':
            name = name[0:-1]
            espn_chances[i][0] = name
            continue
        elif name[-1] == '4':
            name = name[0:-1]
            espn_chances[i][0] = name
            continue
        elif name[-1] == '5':
            name = name[0:-1]
            espn_chances[i][0] = name
            continue
        elif name[-1] == '6':
            name = name[0:-1]
            espn_chances[i][0] = name
            continue
        elif name[-1] == '7':
            name = name[0:-1]
            espn_chances[i][0] = name
            continue
        elif name[-1] == '8':
            name = name[0:-1]
            espn_chances[i][0] = name
            continue
        elif name[-1] == '9':
            name = name[0:-1]
            espn_chances[i][0] = name
            continue
        else:
            i += 1
            continue
    else:
        break
    
# print('\n')
# print('\n')
# for elem in espn_chances:
#     print(elem)
# print('\n')
# print('\n')
        
i = 0
while True:
    if i < len(espn_chances):
        if len(espn_chances[i]) == 2:
            chance = espn_chances[i][1][0:-1]
            chance = float(chance)
            chance = round(chance, 2)
            espn_chances[i][1] = chance
            if i == 0 or i % 2 == 0:
                o = i + 1
                opp_chance = float(100) - chance
                opp_chance = round(opp_chance, 2)
                espn_chances[o].append(opp_chance)
                i += 2
                continue
            else:
                o = i - 1
                opp_chance = float(100) - chance
                opp_chance = round(opp_chance, 2)
                espn_chances[o].append(opp_chance)
                i += 1
                continue
        else:
            i += 1
            continue
    else:
        break

espn_chances = rename(espn_chances)

# print('\n')

for elem in espn_chances:
    if len(elem) == 1:
        del elem

dict_espn_chances = {x[0]:x[1:] for x in espn_chances}
espn_keys = (dict_espn_chances.keys())

# print('\n')
# print(dict_espn_chances)
# print('\n')

def espn(lst):
    i = 0
    while True:
        if i < len(lst):
            b = i + 1
            if lst[i][0] in espn_keys and lst[b][0] in espn_keys:
                awayTeamList = dict_espn_chances[lst[i][0]]
                if len(awayTeamList) == 0:
                    i += 2
                    continue
                # print(awayTeamList)
                # print('\n')
                awayTeamChance = awayTeamList[0]
                # print(awayTeamChance)
                # print('\n')
                homeTeamList = dict_espn_chances[lst[b][0]]
                if len(homeTeamList) == 0:
                    i += 2
                    continue
                # print(homeTeamList)
                # print('\n')
                homeTeamChance = homeTeamList[0]
                # print(homeTeamChance)
                # print('\n')
                lst[i].append(awayTeamChance) #[i][19] numberfire chance
                lst[b].append(homeTeamChance) #[i][19] numberfire chance
                i += 2
                continue
            else:
                i += 2
                continue
        else:
            break  
    return lst

#[i][13] straight points [i][14] points + spread [i][15] total [i][16] calculated chance [i][17] calculated chance vs spread [18] numberfire chance
# [19] numberfire chance [20] AVERAGE CHANCE

fanduel_cbb = espn(fanduel_cbb)

draftkings_cbb = espn(draftkings_cbb)

barstool_cbb = espn(barstool_cbb)


espn_chance_time = time.perf_counter()
print('\n')
print(f'Scraped ESPN chances in {espn_chance_time - start_time:0.4f} seconds')
print('\n')

# print('\n')
# print('FANDUEL:')
# for elem in fanduel_cbb:
#     print(elem)

# print('\n')
# print('DRAFTKINGS:')
# for elem in draftkings_cbb:
#     print(elem)

# print('\n')
# print('BARSTOOL:')
# for elem in barstool_cbb:
#     print(elem)


# CALCULATE AND APPEND AVERAGE CHANCES TO _CBB LISTS / MAKES INDEX [I][19]
def avg_c(l):
    i = 0
    while True:
        if i < len(l):
            if len(l[i]) != 20:
                del l[i]
                continue
            else:
                avg = (float(l[i][15]) + float(l[i][17]) + float(l[i][18])) / 3   #[16] IS SPREAD CHANCE
                avg = round(avg, 2)
                l[i].append(avg) #[19] AVERAGE CHANCE
                i += 1
                continue
        else:
            break
    return l


fanduel_cbb = avg_c(fanduel_cbb)
draftkings_cbb = avg_c(draftkings_cbb)
barstool_cbb = avg_c(barstool_cbb)

#[i][13] straight points [i][14] points + spread [i][15] total [i][16] calculated chance [i][17] calculated chance vs spread [18] numberfire chance
# [19] numberfire chance [20] AVERAGE CHANCE [21] = total average value [22] = calculated value [23] = numberfire value [24] = espn value
# [25] spread value [26] = consensus


def vals(lst):
    i = 0
    c = 0
    n = 0
    e = 0
    while True:
        if i < len(lst):
            if lst[i][3] < 0:
                avg_chance = lst[i][19] 
                avg_chance_num = round((avg_chance / 100), 2)
                moneyline = np.nan_to_num(lst[i][3]) 
                moneyline = int(moneyline) 
                moneyline_pos = moneyline * -1
                value = round((avg_chance_num * (10 + 10 / (moneyline_pos / 10)* 10)), 3)
                lst[i].append(value) # creates [i][21] = total average value
                name = lst[i][0]
                calc_chance = lst[i][15]
                calc_chance_num = round((float(calc_chance) / 100), 2)
                nf_chance = lst[i][17]
                nf_chance_num = round((float(nf_chance) / 100), 2)
                espn_chance = lst[i][18]
                espn_chance_num = round((float(espn_chance) / 100), 2)
                calc_value = round(calc_chance_num * (10 + 10 / (moneyline_pos / 10)* 10), 3)
                lst[i].append(calc_value) # creates [i][21] = calculated value
                nf_value = round(nf_chance_num * (10 + 10 / (moneyline_pos / 10)* 10), 3)
                lst[i].append(nf_value) # creates [i][22] = numberfire value
                espn_value = round(espn_chance_num * (10 + 10 / (moneyline_pos / 10)* 10), 3)
                lst[i].append(espn_value) # creates [i][23] = espn value
                if lst[i][2] < 0:
                    spr_odds = np.nan_to_num(lst[i][2]) 
                    spr_odds = int(spr_odds) 
                    spr_odds = spr_odds * -1
                    spr_chance = lst[i][17]
                    spr_chance = round((float(spr_chance) / 100), 2)
                    spr_value = round(spr_chance * (10 + 10 / (spr_odds / 10)* 10), 3)
                    lst[i].append(spr_value) # creates [i][24] spread value
                if lst[i][2] > 0:
                    spr_odds = np.nan_to_num(lst[i][2]) 
                    spr_odds = int(spr_odds)
                    spr_chance = lst[i][17]
                    spr_chance = round((float(spr_chance) / 100), 2)
                    spr_value = round(((spr_odds / 100 * 10 + 10) * spr_chance), 3)
                    lst[i].append(spr_value) # creates [i][24] spread value
                if calc_value > 10:
                    c = '+'
                if calc_value < 10:
                    c = '-'
                if nf_value > 10:
                    n = '+'
                if nf_value < 10:
                    n = '-'
                if espn_value > 10:
                    e = '+'
                if espn_value < 10:
                    e = '-'
                lst[i].append(c + n + e) # creates [i][25] = consensus
                i += 1
                continue
            else:
                moneyline = np.nan_to_num(lst[i][3])
                moneyline = int(moneyline)
                avg_chance = lst[i][20]
                avg_chance_num = round((avg_chance / 100), 2)
                value = round(((moneyline / 100 * 10 + 10) * avg_chance_num), 3)
                lst[i].append(value) # creates [i][20] = average value
                name = lst[i][0]
                calc_chance = lst[i][16]
                calc_chance_num = round((float(calc_chance) / 100), 2)
                nf_chance = lst[i][18]
                nf_chance_num = round((float(nf_chance) / 100), 2)
                espn_chance = lst[i][19]
                espn_chance_num = round((float(espn_chance) / 100), 2)
                calc_value = round(((moneyline / 100 * 10 + 10) * calc_chance_num), 3)
                lst[i].append(calc_value) # creates [i][21] = calculated value
                nf_value = round(((moneyline / 100 * 10 + 10) * nf_chance_num), 3)
                lst[i].append(nf_value) # creates [i][22] = numberfire value
                espn_value = round(((moneyline / 100 * 10 + 10) * espn_chance_num), 3)
                lst[i].append(espn_value) # creates [i][23] = espn value
                if lst[i][2] < 0:
                    spr_odds = np.nan_to_num(lst[i][2]) 
                    spr_odds = int(spr_odds) 
                    spr_odds = spr_odds * -1
                    spr_chance = lst[i][17]
                    spr_chance = round((float(spr_chance) / 100), 2)
                    spr_value = round(spr_chance * (10 + 10 / (spr_odds / 10)* 10), 3)
                    lst[i].append(spr_value) # creates [i][24] spread value
                if lst[i][2] > 0:
                    spr_odds = np.nan_to_num(lst[i][2]) 
                    spr_odds = int(spr_odds)
                    spr_chance = lst[i][17]
                    spr_chance = round((float(spr_chance) / 100), 2)
                    spr_value = round(((spr_odds / 100 * 10 + 10) * spr_chance), 3)
                    lst[i].append(spr_value) # creates [i][24] spread value
                if calc_value > 10:
                    c = '+'
                if calc_value < 10:
                    c = '-'
                if nf_value > 10:
                    n = '+'
                if nf_value < 10:
                    n = '-'
                if espn_value > 10:
                    e = '+'
                if espn_value < 10:
                    e = '-'
                lst[i].append(c + n + e) # creates [i][25] = consensus
                i += 1
                continue
        else:
            break
    return lst



fanduel_cbb = vals(fanduel_cbb)
draftkings_cbb = vals(draftkings_cbb)
barstool_cbb = vals(barstool_cbb)

values_time = time.perf_counter()
print('\n')
print(f'Calculated values in {values_time - start_time:0.4f} seconds')
print('\n')

fd = 0
while True:
    if  fd < len(fanduel_cbb):
        del fanduel_cbb[fd][14]
        if len(fanduel_cbb[fd]) != 26:
            del fanduel_cbb[fd]
            continue
        else:
            fd += 1
            continue
    else:
        break

dk = 0
while True:
    if  dk < len(draftkings_cbb):
        del draftkings_cbb[dk][14]
        if len(draftkings_cbb[dk]) != 26:
            del draftkings_cbb[dk]
            continue
        else:
            dk += 1
            continue
    else:
        break

bs = 0
while True:
    if  bs < len(barstool_cbb):
        del barstool_cbb[bs][14]
        if len(barstool_cbb[bs]) != 26:
            del barstool_cbb[bs]
            continue
        else:
            bs += 1
            continue
    else:
        break

fanduel_cbb_sorted = sorted(fanduel_cbb, key=itemgetter(20), reverse=True)
draftkings_cbb_sorted = sorted(draftkings_cbb, key=itemgetter(20), reverse=True)
barstool_cbb_sorted = sorted(barstool_cbb, key=itemgetter(20), reverse=True)

def cln(lst):
    for elem in lst:
        del elem[6:12]
        del elem[7:9]
    return lst


fanduel_cbb_sorted = cln(fanduel_cbb_sorted)
draftkings_cbb_sorted = cln(draftkings_cbb_sorted)
barstool_cbb_sorted = cln(barstool_cbb_sorted)



#[i][0] team, [1] spread, [2] spread odds, [3] moneyline, [4] total, [5] o/u odds, [6] t_pfa, [7] h_pfa, [8] a_pfa, [9] t_paa, [10] h_paa, 
# [11] a_paa, [12] h/a, [13] straight points [i][14] total [i][15] calculated chance [i][16] calculated chance vs spread [17] numberfire chance
# [18] espn [19] AVERAGE CHANCE [20] = total average value [21] = calculated value [22] = numberfire value [23] = espn value
# [24] spread value [25] = consensus

headers = ['Team', 'Spread', 'Spr_odds', 'ML', 'Total', 'Total_odds', 'PF/G_T', 'PF/G_H',
'PF/G_A', 'PA/G_T', 'PA/G_H', 'PA/G_A', 'H/A', 'Team_Pts', 'Total_Pts', 'Calc_%', 'Spread_%', 'NF_%', 'ESPN_%',
'Avg_%', 'Avg_V', 'Calc_V', 'NF_V', 'ESPN_V', 'Spread_V', 'Consensus']


headers_sorted = ['Team', 'Spread', 'Spr_odds', 'ML', 'Total', 'Total_odds', 'H/A', 'Total_Pts', 'Calc_%', 'Spread_%', 'NF_%', 'ESPN_%',
'Src_Avg_%', 'Src_Avg_V', 'Calc_V', 'NF_V', 'ESPN_V', 'Spread_V', 'Consensus']

print('\n')
leftWidth = 23
rightWidth = 9
righterWidth = 19
rightererWidth = 14
totalWidth = (leftWidth + righterWidth + righterWidth + righterWidth + rightererWidth + rightWidth 
+ rightererWidth + righterWidth)

title = ' NCAAB '
print(title.center(totalWidth, '-'))
print('Team'.ljust(leftWidth) + 'Moneyline'.rjust(rightWidth) + 'Avg Value'.rjust(rightererWidth) 
    + 'Avg(%)'.rjust(rightererWidth) + 'Consensus(C/N/E)'.rjust(righterWidth) + 'Calculated(%)'.rjust(righterWidth) +
'Numberfire(%)'.rjust(righterWidth) + 'ESPN(%)'.rjust(righterWidth) 
)
print('\n')

def prnt(lst_sorted):
    for elem in lst_sorted:
        if elem[19] > 10 and elem[16] == 'TODAY':
            name = elem[0]
            moneyline = elem[3]
            value = elem[19]
            avg_chance = elem[18]
            consensus = elem[23] 
            calc_chance = elem[14]
            nf_chance = elem[15]
            espn_chance = elem[17]
            print((name).ljust(leftWidth) + str(moneyline).rjust(rightWidth) 
            + str(value).rjust(rightererWidth) + str(avg_chance).rjust(rightererWidth) 
            + str(consensus).rjust(righterWidth) + str(calc_chance).rjust(righterWidth) 
            + str(nf_chance).rjust(righterWidth) + str(espn_chance).rjust(righterWidth))
            continue
        else:
            continue
    return lst_sorted

# writer = pd.ExcelWriter('/Users/Hayden/OneDrive/Sports Betting/cbb.xlsx')

fanduel_cbb_df = pd.DataFrame(fanduel_cbb, columns = headers)
draftkings_cbb_df = pd.DataFrame(draftkings_cbb, columns = headers)
barstool_cbb_df = pd.DataFrame(barstool_cbb, columns = headers)
fd_cbb_sorted_df = pd.DataFrame(fanduel_cbb_sorted, columns = headers_sorted)
dk_cbb_sorted_df = pd.DataFrame(draftkings_cbb_sorted, columns = headers_sorted)
bs_cbb_sorted_df = pd.DataFrame(barstool_cbb_sorted, columns = headers_sorted)


with pd.ExcelWriter('/Users/Hayden/OneDrive/Sports Betting/cbb.xlsx') as writer:
    fanduel_cbb_df.to_excel(writer, sheet_name='Fanduel', index = False)
    fd_cbb_sorted_df.to_excel(writer, sheet_name='Fanduel_Sorted', index = False)
    draftkings_cbb_df.to_excel(writer, sheet_name='DraftKings', index = False)
    dk_cbb_sorted_df.to_excel(writer, sheet_name='DraftKings_Sorted', index = False)
    barstool_cbb_df.to_excel(writer, sheet_name='Barstool', index = False)
    bs_cbb_sorted_df.to_excel(writer, sheet_name='Barstool_Sorted', index = False)


finish_time = time.perf_counter()
print('\n')
print(f'Completed in {finish_time - start_time:0.4f} seconds')
print('\n')

# print('\n')

# fd_data = pd.DataFrame(fanduel_cbb, columns = headers)
# fd_data.head()
# fd_data.to_excel(writer, sheet_name = 'fanduel', index = False)

# dk_data = pd.DataFrame(draftkings_cbb, columns = headers)
# dk_data.head()
# dk_data.to_excel(writer, sheet_name = 'draftkings', index = False)

# bs_data = pd.DataFrame(barstool_cbb, columns = headers)
# bs_data.head()
# bs_data.to_excel(writer, sheet_name = 'barstool', index = False)

# fd_data_sorted = pd.DataFrame(fanduel_cbb_sorted, columns = headers_sorted)
# fd_data_sorted.head()
# fd_data_sorted.to_excel(writer, sheet_name = 'fanduel_sorted', index = False)

# dk_data_sorted = pd.DataFrame(draftkings_cbb_sorted, columns = headers_sorted)
# dk_data_sorted.head()
# dk_data_sorted.to_excel(writer, sheet_name = 'draftkings_sorted', index = False)

# bs_data_sorted = pd.DataFrame(barstool_cbb_sorted, columns = headers_sorted)
# bs_data_sorted.head()
# bs_data_sorted.to_excel(writer, sheet_name = 'barstool_sorted', index = False)

# writer.save()
# writer.close()

    

# conn = sqlite3.connect('NCAAB.db')

# ncaabData.to_sql(name='NCAAB values', con=conn, if_exists='replace', index=False)

# conn.commit()


# ncaab()

# schedule.every(24).hours.do(ncaab)

# while True:
#     schedule.run_pending()


