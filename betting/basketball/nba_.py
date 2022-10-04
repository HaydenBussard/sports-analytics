import sys
import os
from os import pipe
from typing import Match, Text
from urllib import request
import bs4
import pandas as pd
import numpy as np
import json
from json import scanner
import requests
import re
from datetime import date, timedelta
#import urllib  
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
import schedule


# YAHOO Stats
url_yahoo_total_against = 'https://sports.yahoo.com/nba/stats/team/?sortStatId=POINTS_PER_GAME&selectedTable=1&cutTypeIds='
url_yahoo_total_for = 'https://sports.yahoo.com/nba/stats/team/?sortStatId=POINTS_PER_GAME&selectedTable=0&cutTypeIds='
url_yahoo_home_against = 'https://sports.yahoo.com/nba/stats/team/?sortStatId=POINTS_PER_GAME&selectedTable=1&cutTypeIds=HOME'
url_yahoo_home_for = 'https://sports.yahoo.com/nba/stats/team/?sortStatId=POINTS_PER_GAME&selectedTable=0&cutTypeIds=HOME'
url_yahoo_away_against = 'https://sports.yahoo.com/nba/stats/team/?sortStatId=POINTS_PER_GAME&selectedTable=1&cutTypeIds=AWAY'
url_yahoo_away_for = 'https://sports.yahoo.com/nba/stats/team/?sortStatId=POINTS_PER_GAME&selectedTable=0&cutTypeIds=AWAY'
df_yahoo_total_against = pd.read_html(url_yahoo_total_against)
df_yahoo_total_for = pd.read_html(url_yahoo_total_for)
df_yahoo_home_against = pd.read_html(url_yahoo_home_against)
df_yahoo_home_for = pd.read_html(url_yahoo_home_for)
df_yahoo_away_against = pd.read_html(url_yahoo_away_against)
df_yahoo_away_for = pd.read_html(url_yahoo_away_for)
yahoo_total_against = df_yahoo_total_against[0].values.tolist()
yahoo_total_for = df_yahoo_total_for[0].values.tolist()
yahoo_home_against = df_yahoo_home_against[0].values.tolist()
yahoo_home_for = df_yahoo_home_for[0].values.tolist()
yahoo_away_against = df_yahoo_away_against[0].values.tolist()
yahoo_away_for = df_yahoo_away_for[0].values.tolist()

yahoo_total_against.sort(key=lambda x: x[0])
yahoo_total_for.sort(key=lambda x: x[0])
yahoo_home_against.sort(key=lambda x: x[0])
yahoo_home_for.sort(key=lambda x: x[0])
yahoo_away_against.sort(key=lambda x: x[0])
yahoo_away_for.sort(key=lambda x: x[0])


# print(yahoo_home_against)
# print('\n')
# print(yahoo_home_for)
# print('\n')
# print(yahoo_away_against)
# print('\n')
# print(yahoo_away_for)
# print('\n')
# print(len(yahoo_home_against))
# print('\n')
# print(len(yahoo_home_for))
# print('\n')
# print(len(yahoo_away_against))
# print('\n')
# print(len(yahoo_away_for))


# add name, total for average, total against average to beginning of data set: [i][0] and [i][1] and [i][2]
i = 0
y = len(yahoo_total_for)
yahoo_data = yahoo_total_for
while True:
    if i < y:
        l = yahoo_total_against[i][-1]
        yahoo_data[i].append(l)
        del yahoo_data[i][1:18]
        i += 1
        continue
    else:
        break
# print(yahoo_data)

# # name and GFA_home [i][3]
i = 0
a = 0
while True:
    if i < len(yahoo_home_for):
        if yahoo_home_for[i][0] == yahoo_data[a][0]:
            yahoo_data[a].append(yahoo_home_for[i][-1])
            i += 1
            a = 0
            continue
        else:
            a += 1
            continue
    else:
        break
i = 0
while True: # append blank indices for missing data from previous append loop
    if i < len(yahoo_data):
        if len(yahoo_data[i]) == 3:
            yahoo_data[i].append('')
            i += 1
            continue
        else:
            i += 1
            continue
    else:
        break

i = 0
a = 0
while True:
    if i < len(yahoo_home_against):
        if yahoo_home_against[i][0] in yahoo_data[a][0]:
            yahoo_data[a].append(yahoo_home_against[i][-1])
            i += 1
            a = 0
            continue
        else:
            a += 1
            continue
    else:
        break
i = 0
while True: # append blank indices for missing data from previous append loop
    if i < len(yahoo_data):
        if len(yahoo_data[i]) == 4:
            yahoo_data[i].append('')
            i += 1
            continue
        else:
            i += 1
            continue
    else:
        break

# GFA_away [i][5]
i = 0
a = 0
while True:
    if i < len(yahoo_away_for):
        if yahoo_away_for[i][0] in yahoo_data[a][0]:
            yahoo_data[a].append(yahoo_away_for[i][-1])
            i += 1
            a = 0
            continue
        else:
            a += 1
            continue
    else:
        break
i = 0
while True: # append blank indices for missing data from previous append loop
    if i < len(yahoo_data):
        if len(yahoo_data[i]) == 5:
            yahoo_data[i].append('')
            i += 1
            continue
        else:
            i += 1
            continue
    else:
        break

# GAA_away [i][6]
i = 0
a = 0
while True:
    if i < len(yahoo_away_against):
        if yahoo_away_against[i][0] in yahoo_data[a][0]:
            yahoo_data[a].append(yahoo_away_against[i][-1])
            i += 1
            a = 0
            continue
        else:
            a += 1
            continue
    else:
        break
i = 0
while True: # append blank indices for missing data from previous append loop
    if i < len(yahoo_data):
        if len(yahoo_data[i]) == 6:
            yahoo_data[i].append('')
            i += 1
            continue
        else:
            i += 1
            continue
    else:
        break

#print(yahoo_data)
# print('\n')

i = 0
while True: # MATCHING TEAM NAMES FROM BOTH SOURCES
    if i < len(yahoo_data):
        if 'Atlanta' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'ATL Hawks'
            i += 1
            continue
        elif 'Boston' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'BOS Celtics'
            i += 1
            continue
        elif 'Brooklyn' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'BKN Nets'
            i += 1
            continue
        elif 'Charlotte' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'CHA Hornets'
            i += 1
            continue
        elif 'Chicago' in str(yahoo_data[i][0]):  
            yahoo_data[i][0] = 'CHI Bulls'
            i += 1
            continue
        elif 'Cleveland' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'CLE Cavaliers'
            i += 1
            continue
        elif 'Dallas' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'DAL Mavericks'
            i += 1
            continue
        elif 'Denver' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'DEN Nuggets'
            i += 1
            continue
        elif 'Detroit' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'DET Pistons'
            i += 1
            continue
        elif 'Golden State' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'GS Warriors'
            i += 1
            continue
        elif 'Houston' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'HOU Rockets'
            i += 1
            continue
        elif 'Indiana' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'IND Pacers'
            i += 1
            continue
        elif 'LA Clippers' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'LA Clippers'
            i += 1
            continue
        elif 'LA Lakers' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'LA Lakers'
            i += 1
            continue
        elif 'Memphis' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'MEM Grizzlies'
            i += 1
            continue
        elif 'Miami' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'MIA Heat'
            i += 1
            continue
        elif 'Milwaukee' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'MIL Bucks'
            i += 1
            continue
        elif 'Minnesota' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'MIN Timberwolves'
            i += 1
            continue
        elif 'New Orleans' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'NO Pelicans'
            i += 1
            continue
        elif 'New York' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'NY Knicks'
            i += 1
            continue
        elif 'Oklahoma City' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'OKC Thunder'
            i += 1
            continue
        elif 'Orlando' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'ORL Magic'
            i += 1
            continue
        elif 'Philadelphia' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'PHI 76ers'
            i += 1
            continue
        elif 'Phoenix' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'PHO Suns'
            i += 1
            continue
        elif 'Portland' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'POR Trail Blazers'
            i += 1
            continue
        elif 'Sacramento' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'SAC Kings'
            i += 1
            continue
        elif 'San Antonio' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'SA Spurs'
            i += 1
            continue
        elif 'Toronto' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'TOR Raptors'
            i += 1
            continue
        elif 'Utah' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'UTA Jazz'
            i += 1
            continue
        elif 'Washington' in str(yahoo_data[i][0]):
            yahoo_data[i][0] = 'WAS Wizards'
            i += 1
            continue
        else:
            break
    else:
        break
yahoo_data.sort(key=lambda x: x[0])

# for elem in yahoo_data:
#     print(elem)

df_DraftKings = pd.read_html('https://sportsbook.draftkings.com/leagues/basketball/88670846?category=game-lines&subcategory=game')
draftKingsData = df_DraftKings[0].values.tolist()
# print(df_DraftKings)
i = 1
while True:
    if i < len(df_DraftKings):
        x = df_DraftKings[i].values.tolist()
        draftKingsData = draftKingsData + x
        i += 1
        continue
    else:
        break
# print(draftKingsData)

# fix sublist index 0 with gametimes and team names
i = 0
a = 0 
while True:
    if i < len(draftKingsData): # if a < len(draftKingsData[i]):
        name_scraped = draftKingsData[i][0]
        if 'AM' in name_scraped[0:7]:
            m = name_scraped.index('AM')
            game_time = name_scraped[0: m + 2]
            team = name_scraped[m + 2:]
            draftKingsData[i][0] = team
            draftKingsData[i].append(game_time)
            i += 1
            continue
        elif 'PM' in name_scraped[0:7]:
            m = name_scraped.index('PM')
            game_time = name_scraped[0: m + 2]
            team = name_scraped[m + 2:]
            draftKingsData[i][0] = team
            draftKingsData[i].append(game_time)
            i += 1
            continue
        elif 'Quarter' in name_scraped[0:16]:
            m = name_scraped.index('Quarter')
            game_time = name_scraped[0: m + 7]
            team = name_scraped[m + 7:]
            team = ''.join((x for x in team if not x.isdigit()))
            draftKingsData[i][0] = team
            draftKingsData[i].append(game_time)
            i += 1
            continue
        elif 'st' in name_scraped[0:8] == True or 'nd' in name_scraped[0:8] == True or 'rd' in name_scraped[0:8] == True or 'th' in name_scraped[0:8] == True:
            game_time = 'LIVE'
            draftKingsData[i].append(game_time)
            i += 1
            continue
        else:
            i += 1
            continue
    else: 
        break

# print('\n')
# print(draftKingsData)
# print('\n')

# # matchupAnalysis [i][0] = name, [i][3] = moneyline, [i][14] = calculated chance, [i][15] = numberfire chance 
# # [i][16] = FiveThirtyEight chance, [i][17] = avg chance, [i][18] = value, [i][18] = calculated value
# # [i][19] = numberfire value, [i][20] = fivethirtyeight value, [i][21] = consensus

dict_yahoo_data = {x[0]:x[1:] for x in yahoo_data}

awayHome = ['A', 'H']
y = (dict_yahoo_data.keys())
# print(y)
# print('\n')
# print(len(draftKingsData))
# print('\n')
i = 0
matchupAnalysis_NBA = []
while True: 
    if i < len(draftKingsData):
        if draftKingsData[i][0] not in y:
            i += 2
            continue
        else:
            b = i + 1
            awayTeam = dict_yahoo_data[draftKingsData[i][0]]
            homeTeam = dict_yahoo_data[draftKingsData[b][0]]
            matchupAnalysis_NBA.append(draftKingsData[i] + awayTeam + [awayHome[0]])
            matchupAnalysis_NBA.append(draftKingsData[b] + homeTeam + [awayHome[1]])
            i += 2
            continue
    else:
        break

# print('\n')
# for elem in matchupAnalysis_NBA:
#     print(elem)
# print('\n')

# get League Avg Points Against
i = 0
a = 0
while True:
    if i < len(yahoo_data):
        a = a + yahoo_data[i][4]
        i += 1
        continue
    else:
        a = a / len(yahoo_data)
        leagueAvgAgainst_home = round(a, 2)
        break
# print(leagueAvgAgainst_home)

# get League Avg Points Against
i = 0
a = 0
while True:
    if i < len(yahoo_data):
        a = a + yahoo_data[i][6]
        i += 1
        continue
    else:
        a = a / len(yahoo_data)
        leagueAvgAgainst_away = round(a, 2)
        break
# print(leagueAvgAgainst_away)

# Expected Points
i = 0
length = len(matchupAnalysis_NBA)
while True: # GF/G = index 5 | GA/G = index 6 | leage avg = leagueAvgAgainst | 
    if i < length:
        h = i + 1
        a = (float(matchupAnalysis_NBA[i][7]) * float(matchupAnalysis_NBA[h][6])) / leagueAvgAgainst_home
        away = round(a, 2)
        matchupAnalysis_NBA[i].append(away)
        home = (float(matchupAnalysis_NBA[h][5]) * float(matchupAnalysis_NBA[i][6])) / leagueAvgAgainst_away
        home = round(home, 2)
        matchupAnalysis_NBA[h].append(home)
        i += 2
        continue
    else:
        break

# print(matchupAnalysis_NBA)
# # matchupAnalysis [i][0] = name, [i][1] = spread, [i][2] = total,  [i][3] = moneyline, [i][4] = game time, 
# [i][5] = PF/G Total, [i][6] = PA/G Total, [i][7] PF/G Home, [i][8] = PA/G Home, [i][9] = PA/G Away,
# [i][10] = PA/G Away, [i][11] = Home or Away, [i][12] = Expected Points, [i][13] = Expected Total, 
# [i][14] = poisson, [i][15] = calculated chance, [i][16] = numberfire chance, [i][16] = Today or Not Today, 
# [i][17] = FTE Chance, [i][18] = avg chance, [i][19] = value, [i][20] = calculated value, [i][21] = numberfire value, 
# [i][22] = fivethirtyeight value, [i][23] = consensus

# print(matchupAnalysis_NBA[0][12])
# print(matchupAnalysis_NBA[1][12])

# CALCULATING EXPECTED TOTAL [i][13]
i = 0
while True: 
    if i < length:
        h = i + 1
        combinedTotal = float(matchupAnalysis_NBA[i][12]) + float(matchupAnalysis_NBA[h][12])
        combinedTotal = round(combinedTotal, 2)
        matchupAnalysis_NBA[i].append(combinedTotal)
        blank = '_'
        matchupAnalysis_NBA[h].append('')
        i += 2
        continue
    else:
        break
    
# print(matchupAnalysis_NBA)

# create list of the possible points
possiblePoints = []
p = 0
while True: 
    if p < 100:
        possiblePoints.append(int(p))
        p += 1
        continue
    else: 
        break
# print(len(possiblePoints))

# Poisson for range for each team, 7 = 11, 8 = 12
poissonAway = []
poissonHome = []
i = 0
p = 0
h = i + 1
while True: 
    if p < len(possiblePoints) and i < len(matchupAnalysis_NBA):
        expectA = float(matchupAnalysis_NBA[i][12])
        expectH = float(matchupAnalysis_NBA[h][12])
        chancePerScoreAway = ((expectA**(possiblePoints[p])) * (math.exp(-expectA)) / math.factorial(possiblePoints[p]))
        poissonAway.append(chancePerScoreAway)
        chancePerScoreHome = ((expectH**(possiblePoints[p])) * (math.exp(-expectH)) / math.factorial(possiblePoints[p]))
        poissonHome.append(chancePerScoreHome)
        p += 1
        continue
    elif len(poissonAway) == len(possiblePoints):
        if h <= len(matchupAnalysis_NBA):
            matchupAnalysis_NBA[i].append(poissonAway)
            matchupAnalysis_NBA[h].append(poissonHome)
            p = 0
            i += 2
            h = i + 1
            poissonAway = []
            poissonHome = []
            continue
        else:
            break
    else:
        break

# print(matchupAnalysis_NBA)

h = 0
a = 0
x = 0
y = x + 1
while True: # poisson
    if y <= len(matchupAnalysis_NBA):
        for i in range (100000):
            q = np.asarray(possiblePoints)
            awayArray_poisson = np.asarray(matchupAnalysis_NBA[x][14])
            homeArray_poisson = np.asarray(matchupAnalysis_NBA[y][14])
            awayChance = random.choices(q, awayArray_poisson)
            homeChance = random.choices(q, homeArray_poisson)
            if homeChance > awayChance:
                h += 1
            elif awayChance > homeChance:
                a += 1
        w = round(a + h, 2)
        a = (a / w) * 100
        a = round(a, 2)
        h = (h / w) * 100
        h = round(h, 2)
        matchupAnalysis_NBA[x].append(a)
        matchupAnalysis_NBA[y].append(h)
        x += 2
        y = x + 1
        h = 0
        a = 0
        continue
    else:
        break

# print(matchupAnalysis_NBA)

# NUMBERFIRE CHANCES  
today = date.today()
tomorrow = today + timedelta(1)
twodays = today + timedelta(2)
threedays = today + timedelta(3)
fourdays = today + timedelta(4)
fivedays = today + timedelta(5)
url_numberfire_NBA = "https://www.numberfire.com/nba/games" 
resultNumberfireNBA = []
i = 0
g = 0
s = 0
projectedWinners = []
resultNumberfireNBA_today = []
resultNumberfireNBA_tomorrow = []
resultNumberfireNBA_twodays = []
resultNumberfireNBA_threedays = []
resultNumberfireNBA_fourdays = []
resultNumberfireNBA_fivedays = []
while True: # list of Numberfire's projected winners and % chances
    if i == 0:
        url_today = url_numberfire_NBA # + str(today)
        html_today = requests.get(url_today)
        soup_today = bs4.BeautifulSoup(html_today.content, features='html.parser') 
        scrapeNumberfireNBA_today = soup_today.findAll('div', attrs={'class':'win-probability-wrap'})
        if len(scrapeNumberfireNBA_today) == 0:
            i += 1
            continue
        elif s < len(scrapeNumberfireNBA_today):
            resultNumberfireNBA_today.append(str(scrapeNumberfireNBA_today[s]))
            s += 1
            continue
        else:
            if g < len(scrapeNumberfireNBA_today):
                teamname = resultNumberfireNBA_today[g][265:275]
                percent = resultNumberfireNBA_today[g][200:215]
                teamname = teamname.replace(' ', '')
                percent = percent.replace(' ', '')
                percent = percent[0:4]
                projectedWinners.append(teamname)
                projectedWinners.append(percent)
                projectedWinners.append('Today')
                g += 1
                continue
            else:
                s = 0
                g = 0
                i += 1
                continue
    elif i == 1:
        url_tomorrow = url_numberfire_NBA + str(tomorrow)
        html_tomorrow = requests.get(url_tomorrow)
        soup_tomorrow = bs4.BeautifulSoup(html_tomorrow.content, features='html.parser') 
        scrapeNumberfireNBA_tomorrow = soup_tomorrow.findAll('div', attrs={'class':'win-probability-wrap'})
        if len(scrapeNumberfireNBA_tomorrow) == 0:
            i += 1
            continue
        elif s < len(scrapeNumberfireNBA_tomorrow):
            resultNumberfireNBA_tomorrow.append(str(scrapeNumberfireNBA_tomorrow[s]))
            s += 1
            continue
        else:
            if g < len(scrapeNumberfireNBA_tomorrow):
                teamname = resultNumberfireNBA_tomorrow[g][265:275]
                percent = resultNumberfireNBA_tomorrow[g][200:215]
                teamname = teamname.replace(' ', '')
                percent = percent.replace(' ', '')
                percent = percent[0:4]
                projectedWinners.append(teamname)
                projectedWinners.append(percent)
                projectedWinners.append('Not Today')
                g += 1
                continue
            else:
                s = 0
                g = 0
                i += 1
                continue
    elif i == 2:
        url_twodays = url_numberfire_NBA + str(twodays)
        html_twodays = requests.get(url_twodays)
        soup_twodays = bs4.BeautifulSoup(html_twodays.content, features='html.parser') 
        scrapeNumberfireNBA_twodays = soup_twodays.findAll('div', attrs={'class':'win-probability-wrap'})
        if len(scrapeNumberfireNBA_twodays) == 0:
            i += 1
            continue
        elif s < len(scrapeNumberfireNBA_twodays):
            resultNumberfireNBA_twodays.append(str(scrapeNumberfireNBA_twodays[s]))
            s += 1
            continue
        else:
            if g < len(scrapeNumberfireNBA_twodays):
                teamname = resultNumberfireNBA_twodays[g][265:275]
                percent = resultNumberfireNBA_twodays[g][200:215]
                teamname = teamname.replace(' ', '')
                percent = percent.replace(' ', '')
                percent = percent[0:4]
                projectedWinners.append(teamname)
                projectedWinners.append(percent)
                projectedWinners.append('Not Today')
                g += 1
                continue
            else:
                s = 0
                g = 0
                i += 1
                continue
    elif i == 3:
        url_threedays = url_numberfire_NBA + str(threedays)
        html_threedays = requests.get(url_threedays)
        soup_threedays = bs4.BeautifulSoup(html_threedays.content, features='html.parser') 
        scrapeNumberfireNBA_threedays = soup_threedays.findAll('div', attrs={'class':'win-probability-wrap'})
        if len(scrapeNumberfireNBA_threedays) == 0:
            i += 1
            continue
        elif s < len(scrapeNumberfireNBA_threedays):
            resultNumberfireNBA_threedays.append(str(scrapeNumberfireNBA_threedays[s]))
            s += 1
            continue
        else:
            if g < len(scrapeNumberfireNBA_threedays):
                teamname = resultNumberfireNBA_threedays[g][265:275]
                percent = resultNumberfireNBA_threedays[g][200:215]
                teamname = teamname.replace(' ', '')
                percent = percent.replace(' ', '')
                percent = percent[0:4]
                projectedWinners.append(teamname)
                projectedWinners.append(percent)
                projectedWinners.append('Not Today')
                g += 1
                continue
            else:
                s = 0
                g = 0
                i += 1
                continue
    elif i == 4:
        url_fourdays = url_numberfire_NBA + str(fourdays)
        html_fourdays = requests.get(url_fourdays)
        soup_fourdays = bs4.BeautifulSoup(html_fourdays.content, features='html.parser') 
        scrapeNumberfireNBA_fourdays = soup_fourdays.findAll('div', attrs={'class':'win-probability-wrap'})
        if len(scrapeNumberfireNBA_fourdays) == 0:
            i += 1
            continue
        elif s < len(scrapeNumberfireNBA_fourdays):
            resultNumberfireNBA_fourdays.append(str(scrapeNumberfireNBA_fourdays[s]))
            s += 1
            continue
        else:
            if g < len(scrapeNumberfireNBA_fourdays):
                teamname = resultNumberfireNBA_fourdays[g][265:275]
                percent = resultNumberfireNBA_fourdays[g][200:215]
                teamname = teamname.replace(' ', '')
                percent = percent.replace(' ', '')
                percent = percent[0:4]
                projectedWinners.append(teamname)
                projectedWinners.append(percent)
                projectedWinners.append('Not Today')
                g += 1
                continue
            else:
                s = 0
                g = 0
                i += 1
                continue
    elif i == 5:
        url_fivedays = url_numberfire_NBA + str(fivedays)
        html_fivedays = requests.get(url_fivedays)
        soup_fivedays = bs4.BeautifulSoup(html_fivedays.content, features='html.parser') 
        scrapeNumberfireNBA_fivedays = soup_fivedays.findAll('div', attrs={'class':'win-probability-wrap'})
        if len(scrapeNumberfireNBA_fivedays) == 0:
            i += 1
            continue
        elif s < len(scrapeNumberfireNBA_fivedays):
            resultNumberfireNBA_fivedays.append(str(scrapeNumberfireNBA_fivedays[s]))
            s += 1
            continue
        else:
            if g < len(scrapeNumberfireNBA_fivedays):
                teamname = resultNumberfireNBA_fivedays[g][265:275]
                percent = resultNumberfireNBA_fivedays[g][200:215]
                teamname = teamname.replace(' ', '')
                percent = percent.replace(' ', '')
                percent = percent[0:4]
                projectedWinners.append(teamname)
                projectedWinners.append(percent)
                projectedWinners.append('Not Today')
                g += 1
                continue
            else:
                s = 0
                g = 0
                i += 1
                continue
    else:
        break

# print(projectedWinners)

i = 0
while True: # MATCHING TEAM NAMES FROM BOTH SOURCES
    if i < len(projectedWinners):
        if 'ATL' in str(projectedWinners[i]):
            projectedWinners[i] = 'ATL Hawks'
            i += 1
            continue
        elif 'BOS' in str(projectedWinners[i]):
            projectedWinners[i] = 'BOS Celtics'
            i += 1
            continue
        elif 'BKN' in str(projectedWinners[i]):
            projectedWinners[i] = 'BKN Nets'
            i += 1
            continue
        elif 'CHA' in str(projectedWinners[i]):
            projectedWinners[i] = 'CHA Hornets'
            i += 1
            continue
        elif 'CHI' in str(projectedWinners[i]):  
            projectedWinners[i] = 'CHI Bulls'
            i += 1
            continue
        elif 'CLE' in str(projectedWinners[i]):
            projectedWinners[i] = 'CLE Cavaliers'
            i += 1
            continue
        elif 'DAL' in str(projectedWinners[i]):
            projectedWinners[i] = 'DAL Mavericks'
            i += 1
            continue
        elif 'DEN' in str(projectedWinners[i]):
            projectedWinners[i] = 'DEN Nuggets'
            i += 1
            continue
        elif 'DET' in str(projectedWinners[i]):
            projectedWinners[i]= 'DET Pistons'
            i += 1
            continue
        elif 'GS' in str(projectedWinners[i]):
            projectedWinners[i] = 'GS Warriors'
            i += 1
            continue
        elif 'HOU' in str(projectedWinners[i]):
            projectedWinners[i] = 'HOU Rockets'
            i += 1
            continue
        elif 'IND' in str(projectedWinners[i]):
            projectedWinners[i] = 'IND Pacers'
            i += 1
            continue
        elif 'LAC' in str(projectedWinners[i]):
            projectedWinners[i] = 'LA Clippers'
            i += 1
            continue
        elif 'LAL' in str(projectedWinners[i]):
            projectedWinners[i] = 'LA Lakers'
            i += 1
            continue
        elif 'MEM' in str(projectedWinners[i]):
            projectedWinners[i] = 'MEM Grizzlies'
            i += 1
            continue
        elif 'MIA' in str(projectedWinners[i]):
            projectedWinners[i] = 'MIA Heat'
            i += 1
            continue
        elif 'MIL' in str(projectedWinners[i]):
            projectedWinners[i] = 'MIL Bucks'
            i += 1
            continue
        elif 'MIN' in str(projectedWinners[i]):
            projectedWinners[i] = 'MIN Timberwolves'
            i += 1
            continue
        elif 'NO' in str(projectedWinners[i]):
            projectedWinners[i] = 'NO Pelicans'
            i += 1
            continue
        elif 'NY' in str(projectedWinners[i]):
            projectedWinners[i] = 'NY Knicks'
            i += 1
            continue
        elif 'OKC' in str(projectedWinners[i]):
            projectedWinners[i] = 'OKC Thunder'
            i += 1
            continue
        elif 'ORL' in str(projectedWinners[i]):
            projectedWinners[i] = 'ORL Magic'
            i += 1
            continue
        elif 'PHI' in str(projectedWinners[i]):
            projectedWinners[i] = 'PHI 76ers'
            i += 1
            continue
        elif 'PHX' in str(projectedWinners[i]):
            projectedWinners[i] = 'PHO Suns'
            i += 1
            continue
        elif 'POR' in str(projectedWinners[i]):
            projectedWinners[i] = 'POR Trail Blazers'
            i += 1
            continue
        elif 'SAC' in str(projectedWinners[i]):
            projectedWinners[i] = 'SAC Kings'
            i += 1
            continue
        elif 'SA' in str(projectedWinners[i]):
            projectedWinners[i] = 'SA Spurs'
            i += 1
            continue
        elif 'TOR' in str(projectedWinners[i]):
            projectedWinners[i] = 'TOR Raptors'
            i += 1
            continue
        elif 'UTAH' in str(projectedWinners[i]):
            projectedWinners[i] = 'UTA Jazz'
            i += 1
            continue
        elif 'WSH' in str(projectedWinners[i]):
            projectedWinners[i] = 'WAS Wizards'
            i += 1
            continue
        else:
            i += 1
            continue
    else:
        break

# print(projectedWinners)

# CREATE ORGANIZED LIST OF NUMBERFIRE CHANCES
x = 3
numberfireChances = [projectedWinners[i:i+x] for i in range(0, len(projectedWinners), x)]
# print('\n')
# print(numberfireChances)
# print('\n')

i = 0
n = 0
while True:
    if i < len(matchupAnalysis_NBA):
        h = i + 1
        if str(matchupAnalysis_NBA[i][0]) not in projectedWinners:
            if str(matchupAnalysis_NBA[h][0]) not in projectedWinners:
                i += 2
                continue
            else:
                y = projectedWinners.index(matchupAnalysis_NBA[h][0])
                winnerIndex = y
                winnerChanceIndex = y + 1
                teamIndex = y + 2
                awayChance = float(100) - float(projectedWinners[winnerChanceIndex])
                awayChance = round(awayChance, 1)
                matchupAnalysis_NBA[i].append(awayChance)
                matchupAnalysis_NBA[h].append(projectedWinners[winnerChanceIndex])
                matchupAnalysis_NBA[i].append(projectedWinners[teamIndex])
                matchupAnalysis_NBA[h].append(projectedWinners[teamIndex])
                del projectedWinners[y:y+2]
                i += 2
                continue
        elif str(matchupAnalysis_NBA[h][0]) not in projectedWinners:
            if str(matchupAnalysis_NBA[i][0]) not in projectedWinners:
                i += 2
                continue
            else:
                x = projectedWinners.index(matchupAnalysis_NBA[i][0])
                winnerIndex = x
                winnerChanceIndex = x + 1
                teamIndex = x + 2
                homeChance = float(100) - float(projectedWinners[winnerChanceIndex])
                homeChance = round(homeChance, 1)
                matchupAnalysis_NBA[h].append(homeChance)
                matchupAnalysis_NBA[i].append(projectedWinners[winnerChanceIndex])
                matchupAnalysis_NBA[i].append(projectedWinners[teamIndex])
                matchupAnalysis_NBA[h].append(projectedWinners[teamIndex])
                del projectedWinners[x:x+2]
                i += 2
                continue
        elif projectedWinners.index(matchupAnalysis_NBA[i][0]) < projectedWinners.index(matchupAnalysis_NBA[h][0]):
            x = projectedWinners.index(matchupAnalysis_NBA[i][0])
            winnerIndex = x
            winnerChanceIndex = x + 1
            teamIndex = x + 2
            homeChance = float(100) - float(projectedWinners[winnerChanceIndex])
            homeChance = round(homeChance, 1)
            matchupAnalysis_NBA[h].append(homeChance)
            matchupAnalysis_NBA[i].append(projectedWinners[winnerChanceIndex])
            matchupAnalysis_NBA[i].append(projectedWinners[teamIndex])
            matchupAnalysis_NBA[h].append(projectedWinners[teamIndex])
            del projectedWinners[x:x+2]
            i += 2
            continue
        elif projectedWinners.index(matchupAnalysis_NBA[h][0]) < projectedWinners.index(matchupAnalysis_NBA[i][0]):
            y = projectedWinners.index(matchupAnalysis_NBA[h][0])
            winnerIndex = y
            winnerChanceIndex = y + 1
            teamIndex = y + 2
            awayChance = float(100) - float(projectedWinners[winnerChanceIndex])
            awayChance = round(awayChance, 1)
            matchupAnalysis_NBA[i].append(awayChance)
            matchupAnalysis_NBA[h].append(projectedWinners[winnerChanceIndex])
            matchupAnalysis_NBA[i].append(projectedWinners[teamIndex])
            matchupAnalysis_NBA[h].append(projectedWinners[teamIndex])
            del projectedWinners[y:y+2]
            i += 2
            continue
    else:
        break    
print('\n')
for elem in matchupAnalysis_NBA:
    print(elem)
    print(len(elem))
print('\n')


i = 0
while True:
    if i < len(matchupAnalysis_NBA):
        if len(matchupAnalysis_NBA[i]) == 17:
            matchupAnalysis_NBA[i].append('')
            i += 1
            continue
        else:
            i += 1
            continue
    else:
        break

# # matchupAnalysis [i][0] = name, [i][1] = spread, [i][2] = total,  [i][3] = moneyline, [i][4] = game time, 
# [i][5] = PF/G Total, [i][6] = PF/G Home, [i][7] PF/G Away, [i][8] = PA/G Total, [i][9] = PA/G Home,
# [i][10] = PA/G Away, [i][11] = Home or Away, [i][12] = Expected Points, [i][13] = Expected Total, 
# [i][14] = poisson, [i][15] = calculated chance, [i][16] = numberfire chance, [i][16] = Today or Not Today, 
# [i][17] = FTE Chance, [i][18] = avg chance, [i][19] = value, [i][20] = calculated value, [i][21] = numberfire value, 
# [i][22] = fivethirtyeight value, [i][23] = consensus

for elem in matchupAnalysis_NBA:
    print(elem)

fivethirtyeight_referenceLength = int(len(numberfireChances)) * 2
df_fivethirtyeight = pd.read_html('https://projects.fivethirtyeight.com/2022-nba-predictions/games/')
# print(df_fivethirtyeight)
lastTable_fivethirtyeight = 2 + fivethirtyeight_referenceLength
i = 2
matchups_fivethirtyeight_NBA = []
while True:
    if i < lastTable_fivethirtyeight:
        matchups_fivethirtyeight_NBA.append(df_fivethirtyeight[i].values.tolist())
        i += 2
        continue
    else:
        break

i = 0 
m = 0
while True:
    if i < len(matchups_fivethirtyeight_NBA):
        if m < 2:
            del matchups_fivethirtyeight_NBA[i][m][0:2]
            del matchups_fivethirtyeight_NBA[i][m][1]
            del matchups_fivethirtyeight_NBA[i][m][2:]
            x = str(matchups_fivethirtyeight_NBA[i][m][1])
            x = x.translate({ord(i):None for i in '%'})
            matchups_fivethirtyeight_NBA[i][m][1] = float(x)
            m += 1
            continue
        else: 
            del matchups_fivethirtyeight_NBA[i][2]
            i += 1
            m = 0
            continue
    else:
        break

i = 0
m = 0
matchups_fte_NBA = []
while True: # MATCHING TEAM NAMES FIVETHIRTYEIGHT
    if i < len(matchups_fivethirtyeight_NBA):
        if m < 2:
            if 'Hawks' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'ATL Hawks'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Celtics' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'BOS Celtics'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Nets' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'BKN Nets'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Hornets' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'CHA Hornets'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Bulls' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'CHI Bulls'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Cavaliers' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'CLE Cavaliers'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Mavericks' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'DAL Mavericks'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Nuggets' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'DEN Nuggets'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Pistons' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'DET Pistons'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Warriors' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'GS Warriors'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Rockets' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'HOU Rockets'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Pacers' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'IND Pacers'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Clippers' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'LA Clippers'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Lakers' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'LA Lakers'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Grizzlies' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'MEM Grizzlies'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Heat' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'MIA Heat'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Bucks' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'MIL Bucks'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Timberwolves' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'MIN Timberwolves'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Pelicans' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'NO Pelicans'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Knicks' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'NY Knicks'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Thunder' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'OKC Thunder'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Magic' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'ORL Magic'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue 
            elif '76ers' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'PHI 76ers'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Suns' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'PHO Suns'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Trail Blazers' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'POR Trail Blazers'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Kings' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'SAC Kings'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Spurs' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'SA Spurs'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Raptors' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'TOR Raptors'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Jazz' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'UTA Jazz'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            elif 'Wizards' in str(matchups_fivethirtyeight_NBA[i][m][0]):
                matchups_fivethirtyeight_NBA[i][m][0] = 'WAS Wizards'
                matchups_fte_NBA.append(matchups_fivethirtyeight_NBA[i][m])
                m += 1
                continue
            else:
                m += 1
                continue
        else:
            m = 0
            i += 1
            continue
    else:
        break
print('\n')
print(matchups_fte_NBA)
print('\n')

i = 0
r = 0
while True:
    if i < len(matchupAnalysis_NBA):
        if len(matchups_fte_NBA) == 0:
            break
        if len(matchups_fte_NBA) == 2:
            if str(matchupAnalysis_NBA[i][0]) == str(matchups_fte_NBA[r][0]):
                if i == 0 or i % 2 == 0:
                    h = i + 1
                    d = r + 1
                    if str(matchupAnalysis_NBA[h][0]) == str(matchups_fte_NBA[d][0]):
                        matchupAnalysis_NBA[i].append(float(matchups_fte_NBA[r][1]))
                        matchupAnalysis_NBA[h].append(float(matchups_fte_NBA[d][1]))
                        del matchups_fte_NBA[d]
                        del matchups_fte_NBA[r]
                        r = 0
                        i += 2
                        continue
                    else:
                        i += 2
                        continue
                else:
                    i += 1
                    continue
            else:
                i += 2
                continue
        elif str(matchupAnalysis_NBA[i][0]) == str(matchups_fte_NBA[r][0]):
            if i == 0 or i % 2 == 0:
                h = i + 1
                d = r + 1
                if str(matchupAnalysis_NBA[h][0]) == str(matchups_fte_NBA[d][0]):
                    matchupAnalysis_NBA[i].append(float(matchups_fte_NBA[r][1]))
                    matchupAnalysis_NBA[h].append(float(matchups_fte_NBA[d][1]))
                    del matchups_fte_NBA[d]
                    del matchups_fte_NBA[r]
                    r = 0
                    i += 2
                    continue
                else:
                    r += 2
                    continue
            else:
                r += 2
                continue
        else:
            r += 2
            continue
    else:
        break

i = 0
matchup_Analysis_NBA = []
while True:
    if i < len(matchupAnalysis_NBA):
        if len(matchupAnalysis_NBA[i]) == 19:
            matchup_Analysis_NBA.append(matchupAnalysis_NBA[i])
            i += 1
            continue
        else:
            i += 1
            continue
    else:
        break

matchupAnalysis_NBA = matchup_Analysis_NBA

# print(matchupAnalysis_NBA)

# # matchupAnalysis(wrong order, see above) [i][0] = name, [i][1] = spread, [i][2] = total,  [i][3] = moneyline, [i][4] = game time, 
# [i][5] = PF/G Total, [i][6] = PF/G Home, [i][7] PF/G Away, [i][8] = PA/G Total, [i][9] = PA/G Home,
# [i][10] = PA/G Away, [i][11] = Home or Away, [i][12] = Expected Points, [i][13] = Expected Total, 
# [i][14] = poisson, [i][15] = calculated chance, [i][16] = numberfire chance, [i][17] = Today or Not Today, 
# [i][18] = FTE Chance, [i][19] = avg chance, [i][20] = value, [i][21] = calculated value, [i][22] = numberfire value, 
# [i][23] = fivethirtyeight value, [i][24] = consensus

# CALCULATE AND APPEND AVERAGE CHANCES TO MATCHUPANALYSIS_NBA
i = 0
while True:
    if i < len(matchupAnalysis_NBA):
        avg = float(float(matchupAnalysis_NBA[i][16]) + float(matchupAnalysis_NBA[i][18]) + float(matchupAnalysis_NBA[i][15])) / 3
        avg = round(avg, 2)
        matchupAnalysis_NBA[i].append(avg)
        i += 1
        continue
    else:
        break
# print(len(matchupAnalysis_NBA[0]))

print('\n')
leftWidth = 23
rightWidth = 9
righterWidth = 19
rightererWidth = 14
totalWidth = (leftWidth + righterWidth + righterWidth + righterWidth + rightererWidth + rightWidth 
+ rightererWidth + rightererWidth)

title = ' NBA '
print(title.center(totalWidth, '-'))
print('Team'.ljust(leftWidth) + 'Moneyline'.rjust(rightWidth) + 'Chance(%)'.rjust(righterWidth) +
'Numberfire(%)'.rjust(righterWidth) + 'FiveThirtyEight(%)'.rjust(righterWidth) + 'Average(%)'.rjust(rightererWidth) 
+ 'Value'.rjust(rightererWidth) + 'Consensus'.rjust(rightererWidth))
print('\n')

# # matchupAnalysis [i][0] = name, [i][1] = spread, [i][2] = total,  [i][3] = moneyline, [i][4] = game time, 
# [i][5] = PF/G Total, [i][6] = PF/G Home, [i][7] PF/G Away, [i][8] = PA/G Total, [i][9] = PA/G Home,
# [i][10] = PA/G Away, [i][11] = Home or Away, [i][12] = Expected Points, [i][13] = Expected Total, 
# [i][14] = poisson, [i][15] = calculated chance, [i][16] = numberfire chance, [i][17] = Today or Not Today, 
# [i][18] = FTE Chance, [i][19] = avg chance, [i][20] = value, [i][21] = calculated value, [i][22] = numberfire value, 
# [i][23] = fivethirtyeight value, [i][24] = consensus

headers = ['0 - Name', '1 - Spread', '2 - Total', '3 - Moneyline', '4 - Gametime', '5 - PF/G Total', 
'6 - PF/G Home', '7 - PF/G Away', '8 - PA/G Total', '9 - PA/G Home', '10 - PA/G Away', '11 - Home or Away', 
'12 - Expected Points', '13 - Expected Total', '14 - Calc Chance', '15 - NF Chance', 
'16 - Today or Not Today', '17 - FTE Chance', '18 - Avg Chance', '19 - Avg Value', '20 - Calc Value', 
'21 - NF Value', '22 - FTE Value', '23 - Consensus']

for elem in matchupAnalysis_NBA:
    del elem[14]

i = 0
c = 0
while True:
    if i < len(matchupAnalysis_NBA):
        if matchupAnalysis_NBA[i][3] < 0:
            avg_chance = matchupAnalysis_NBA[i][18]
            avg_chance_num = avg_chance / 100
            avg_chance_num = round(avg_chance_num, 2)
            # print('What is the FanDuel Moneyline for the ' + matchupAnalysis_NBA[i][0] + '?') # fanduel 
            # matchupAnalysis_NBA[i][3] = int(input()) # fanduel 
            moneyline = np.nan_to_num(matchupAnalysis_NBA[i][3])
            moneyline = int(moneyline)
            moneyline_pos = moneyline * -1
            value = avg_chance_num * (10 + 10 / (moneyline_pos / 10)* 10)
            value = round(value, 3)
            matchupAnalysis_NBA[i].append(value) # creates [i][19] = avg value
            if matchupAnalysis_NBA[i][19] > 10:
                name = matchupAnalysis_NBA[i][0]
                calc_chance = matchupAnalysis_NBA[i][14]
                calc_chance_num = calc_chance / 100
                calc_chance_num = round(calc_chance_num, 2)
                nf_chance = matchupAnalysis_NBA[i][15]
                nf_chance_num = float(nf_chance) / 100
                nf_chance_num = round(nf_chance_num, 2)
                fte_chance = matchupAnalysis_NBA[i][17]
                fte_chance_num = fte_chance / 100
                fte_chance_num = round(fte_chance_num, 2)
                calc_value = calc_chance_num * (10 + 10 / (moneyline_pos / 10)* 10)
                calc_value = round(calc_value, 3)
                matchupAnalysis_NBA[i].append(calc_value) # creates [i][21] = calculated value
                nf_value = nf_chance_num * (10 + 10 / (moneyline_pos / 10)* 10)
                nf_value = round(nf_value, 3)
                matchupAnalysis_NBA[i].append(nf_value) # creates [i][22] = numberfire value
                fte_value = fte_chance_num * (10 + 10 / (moneyline_pos / 10)* 10)
                fte_value = round(fte_value, 3)
                matchupAnalysis_NBA[i].append(fte_value) # creates [i][23] = fte value
                if calc_value > 10:
                    c += 1
                if nf_value > 10:
                    c += 1
                if fte_value > 10:
                    c += 1 
                if c == 0:
                    matchupAnalysis_NBA[i].append('-') # creates [i][24] = consensus
                    consensus = matchupAnalysis_NBA[i][23]
                    print(name.ljust(leftWidth)+ str(moneyline).rjust(rightWidth) 
                    + str(calc_chance).rjust(righterWidth) + str(nf_chance).rjust(righterWidth) 
                    + str(fte_chance).rjust(righterWidth) + str(avg_chance).rjust(rightererWidth) 
                    + str(value).rjust(rightererWidth) + str(consensus).rjust(rightererWidth))
                    i += 1
                    continue
                if c == 1:
                    matchupAnalysis_NBA[i].append('+') # creates [i][24] = consensus
                    consensus = matchupAnalysis_NBA[i][23]
                    print(name.ljust(leftWidth)+ str(moneyline).rjust(rightWidth) 
                    + str(calc_chance).rjust(righterWidth) + str(nf_chance).rjust(righterWidth) 
                    + str(fte_chance).rjust(righterWidth) + str(avg_chance).rjust(rightererWidth) 
                    + str(value).rjust(rightererWidth) + str(consensus).rjust(rightererWidth))
                    c = 0
                    i += 1
                    continue
                if c == 2:
                    matchupAnalysis_NBA[i].append('++') # creates [i][24] = consensus
                    consensus = matchupAnalysis_NBA[i][23]
                    print(name.ljust(leftWidth)+ str(moneyline).rjust(rightWidth) 
                    + str(calc_chance).rjust(righterWidth) + str(nf_chance).rjust(righterWidth) 
                    + str(fte_chance).rjust(righterWidth) + str(avg_chance).rjust(rightererWidth) 
                    + str(value).rjust(rightererWidth) + str(consensus).rjust(rightererWidth))
                    c = 0
                    i += 1
                    continue
                if c == 3:
                    matchupAnalysis_NBA[i].append('+++') # creates [i][24] = consensus
                    consensus = matchupAnalysis_NBA[i][23]
                    print(name.ljust(leftWidth)+ str(moneyline).rjust(rightWidth) 
                    + str(calc_chance).rjust(righterWidth) + str(nf_chance).rjust(righterWidth) 
                    + str(fte_chance).rjust(righterWidth) + str(avg_chance).rjust(rightererWidth) 
                    + str(value).rjust(rightererWidth) + str(consensus).rjust(rightererWidth))
                    c = 0
                    i += 1
                    continue
            else:
                i += 1
                continue
        else:
            # print('What is the FanDuel Moneyline for the ' + matchupAnalysis_NBA[i][0] + '?') # fanduel 
            # matchupAnalysis_NBA[i][3] = int(input()) # fanduel 
            moneyline = np.nan_to_num(matchupAnalysis_NBA[i][3])
            moneyline = int(moneyline)
            avg_chance = matchupAnalysis_NBA[i][18]
            avg_chance_num = avg_chance / 100
            avg_chance_num = round(avg_chance_num, 2)
            value = (moneyline / 100 * 10 + 10) * avg_chance_num
            value = round(value, 3)
            matchupAnalysis_NBA[i].append(value) # creates [i][19] = avg value
            if matchupAnalysis_NBA[i][19] > 10:
                name = matchupAnalysis_NBA[i][0]
                calc_chance = matchupAnalysis_NBA[i][14]
                calc_chance_num = calc_chance / 100
                calc_chance_num = round(calc_chance_num, 2)
                nf_chance = matchupAnalysis_NBA[i][15]
                nf_chance_num = float(nf_chance) / 100
                nf_chance_num = round(nf_chance_num, 2)
                fte_chance = matchupAnalysis_NBA[i][17]
                fte_chance_num = fte_chance / 100
                fte_chance_num = round(fte_chance_num, 2)
                calc_value = (moneyline / 100 * 10 + 10) * calc_chance_num
                calc_value = round(calc_value, 3)
                matchupAnalysis_NBA[i].append(calc_value) # creates [i][20] = calculated value
                nf_value = (moneyline / 100 * 10 + 10) * nf_chance_num
                nf_value = round(nf_value, 3)
                matchupAnalysis_NBA[i].append(nf_value) # creates [i][21] = numberfire value
                fte_value = (moneyline / 100 * 10 + 10) * fte_chance_num
                fte_value = round(fte_value, 3)
                matchupAnalysis_NBA[i].append(fte_value) # creates [i][22] = fte value
                if calc_value > 10:
                    c += 1
                if nf_value > 10:
                    c += 1
                if fte_value > 10:
                    c += 1 
                if c == 0:
                    matchupAnalysis_NBA[i].append('-') # creates [i][23] = consensus
                    consensus = matchupAnalysis_NBA[i][23]
                    print(name.ljust(leftWidth)+ ('+' + str(moneyline)).rjust(rightWidth) 
                    + str(calc_chance).rjust(righterWidth) + str(nf_chance).rjust(righterWidth) 
                    + str(fte_chance).rjust(righterWidth) + str(avg_chance).rjust(rightererWidth) 
                    + str(value).rjust(rightererWidth) + str(consensus).rjust(rightererWidth))
                    i += 1
                    continue
                if c == 1:
                    matchupAnalysis_NBA[i].append('+') # creates [i][23] = consensus
                    consensus = matchupAnalysis_NBA[i][23]
                    print(name.ljust(leftWidth)+ ('+' + str(moneyline)).rjust(rightWidth) 
                    + str(calc_chance).rjust(righterWidth) + str(nf_chance).rjust(righterWidth) 
                    + str(fte_chance).rjust(righterWidth) + str(avg_chance).rjust(rightererWidth) 
                    + str(value).rjust(rightererWidth) + str(consensus).rjust(rightererWidth))
                    c = 0
                    i += 1
                    continue
                if c == 2:
                    matchupAnalysis_NBA[i].append('++') # creates [i][23] = consensus
                    consensus = matchupAnalysis_NBA[i][23]
                    print(name.ljust(leftWidth)+ ('+' + str(moneyline)).rjust(rightWidth) 
                    + str(calc_chance).rjust(righterWidth) + str(nf_chance).rjust(righterWidth) 
                    + str(fte_chance).rjust(righterWidth) + str(avg_chance).rjust(rightererWidth) 
                    + str(value).rjust(rightererWidth) + str(consensus).rjust(rightererWidth))
                    c = 0
                    i += 1
                    continue
                if c == 3:
                    matchupAnalysis_NBA[i].append('+++') # creates [i][23] = consensus
                    consensus = matchupAnalysis_NBA[i][23]
                    print(name.ljust(leftWidth)+ ('+' + str(moneyline)).rjust(rightWidth) 
                    + str(calc_chance).rjust(righterWidth) + str(nf_chance).rjust(righterWidth) 
                    + str(fte_chance).rjust(righterWidth) + str(avg_chance).rjust(rightererWidth) 
                    + str(value).rjust(rightererWidth) + str(consensus).rjust(rightererWidth))
                    c = 0
                    i += 1
                    continue
            else:
                i += 1
                continue
    else:
        break
print('\n')
nbaData = pd.DataFrame(matchupAnalysis_NBA, columns = headers)
nbaData.head()
nbaData.to_excel('/Users/Hayden/OneDrive/Sports Betting/NBA.xlsx', index=False)

conn = sqlite3.connect('NBA.db')

nbaData.to_sql(name='NBA values', con=conn, if_exists='replace', index=False)

conn.commit()
    