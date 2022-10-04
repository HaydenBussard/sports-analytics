import sys
import os
from os import pipe
from typing import Match, Text
from urllib import request
import bs4
import pandas as pd
import sqlite3
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
import pymysql
import mysql.connector 
from operator import itemgetter
import schedule

def nhl():
    # Get the current working directory
    # cwd = os.getcwd()

    # Print the current working directory
    # print("Current working directory: {0}".format(cwd))

    # Print the type of the returned object
    # print("os.getcwd() returns an object of type: {0}".format(type(cwd)))

    # YAHOO Stats
    url_yahoo_total_against = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=1&sortStatId=GOALS_AGAINST_AVERAGE&cutTypeIds='
    url_yahoo_total_for = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=0&sortStatId=GOALS_FOR_AVERAGE&cutTypeIds='
    url_yahoo_home_against = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=1&sortStatId=GOALS_AGAINST&cutTypeIds=HOME'
    url_yahoo_home_for = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=0&sortStatId=GOALS_AGAINST&cutTypeIds=HOME'
    url_yahoo_away_against = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=1&sortStatId=GOALS_AGAINST&cutTypeIds=AWAY'
    url_yahoo_away_for = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=0&sortStatId=GOALS_AGAINST&cutTypeIds=AWAY'
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



    # CREATES YAHOO LIST: NAME, TOTAL AVERAGE FOR,  TOTAL AVERAGE AGAINST
    i = 0
    y = len(yahoo_total_for)
    yahoo_data = yahoo_total_for
    while True:
        if i < y:
            l = yahoo_total_against[i][5]
            yahoo_data[i].append(l)
            del yahoo_data[i][1:5]
            del yahoo_data[i][2:10]
            i += 1
            continue
        else:
            break
    

    # ADDS TO YAHOO LIST: NAME, TOTAL AVERAGE FOR, TOTAL AVERAGE AGAINST, 'HOME AVERAGE FOR' ### CHANGE BACK TO [I][5]
    i = 0
    a = 0
    while True:
        if i < len(yahoo_home_for):
            if yahoo_home_for[i][0] in yahoo_data[a][0]:
                yahoo_data[a].append(yahoo_home_for[i][5])
                i += 1
                a = 0
                continue
            else:
                a += 1
                continue
        else:
            break
        

    
    i = 0
    while True: 
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

    # ADDS TO YAHOO LIST: NAME, TOTAL AVERAGE FOR, TOTAL AVERAGE AGAINST, HOME AVERAGE FOR, 'HOME AVERAGE AGAINST' ### CHANGE BACK TO [I][5]
    i = 0
    a = 0
    while True:
        if i < len(yahoo_home_against):
            if yahoo_home_against[i][0] in yahoo_data[a][0]:
                yahoo_data[a].append(yahoo_home_against[i][5])
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
    

    # ADDS TO YAHOO LIST: NAME, TOTAL AVERAGE FOR, TOTAL AVERAGE AGAINST, HOME AVERAGE FOR, HOME AVERAGE AGAINST, 'AWAY AVERAGE FOR' ### CHANGE BACK TO [I][5]
    i = 0
    a = 0
    while True:
        if i < len(yahoo_away_for):
            if yahoo_away_for[i][0] in yahoo_data[a][0]:
                yahoo_data[a].append(yahoo_away_for[i][5])
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

    # ADDS TO YAHOO LIST: NAME, TOTAL AVERAGE FOR, TOTAL AVERAGE AGAINST, HOME AVERAGE FOR, HOME AVERAGE AGAINST, AWAY AVERAGE FOR, AWAY AVERAGE AGAINST ### CHANGE BACK TO [I][5]
    i = 0
    a = 0
    while True:
        if i < len(yahoo_away_against):
            if yahoo_away_against[i][0] in yahoo_data[a][0]:
                yahoo_data[a].append(yahoo_away_against[i][5])
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

    # for elem in yahoo_data:
    #     print(elem)
    
    i = 0
    while True: # MATCHING TEAM NAMES FROM BOTH SOURCES
        if i < len(yahoo_data):
            if 'Anaheim' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Anaheim Ducks'
                i += 1
                continue
            elif 'Arizona' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Arizona Coyotes'
                i += 1
                continue
            elif 'Boston' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Boston Bruins'
                i += 1
                continue
            elif 'Buffalo' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Buffalo Sabres'
                i += 1
                continue
            elif 'Calgary' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Calgary Flames'
                i += 1
                continue
            elif 'Carolina' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Carolina Hurricanes'
                i += 1
                continue
            elif 'Chicago' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Chicago Blackhawks'
                i += 1
                continue
            elif 'Colorado' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Colorado Avalanche'
                i += 1
                continue
            elif 'Columbus' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Columbus Blue Jackets'
                i += 1
                continue
            elif 'Dallas' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Dallas Stars'
                i += 1
                continue
            elif 'Detroit' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Detroit Red Wings'
                i += 1
                continue
            elif 'Edmonton' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Edmonton Oilers'
                i += 1
                continue
            elif 'Florida' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Florida Panthers'
                i += 1
                continue
            elif 'Los Angeles' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Los Angeles Kings'
                i += 1
                continue
            elif 'Minnesota' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Minnesota Wild'
                i += 1
                continue
            elif 'Montreal' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Montreal Canadiens'
                i += 1
                continue
            elif 'Nashville' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Nashville Predators'
                i += 1
                continue
            elif 'New Jersey' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'New Jersey Devils'
                i += 1
                continue
            elif 'NY Islanders' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'New York Islanders'
                i += 1
                continue
            elif 'NY Rangers' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'New York Rangers'
                i += 1
                continue
            elif 'Ottawa' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Ottawa Senators'
                i += 1
                continue
            elif 'Philadelphia' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Philadelphia Flyers'
                i += 1
                continue
            elif 'Pittsburgh' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Pittsburgh Penguins'
                i += 1
                continue
            elif 'San Jose' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'San Jose Sharks'
                i += 1
                continue
            elif 'Seattle' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Seattle Kraken'
                i += 1
                continue
            elif 'St. Louis' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'St. Louis Blues'
                i += 1
                continue
            elif 'Tampa Bay' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Tampa Bay Lightning'
                i += 1
                continue
            elif 'Toronto' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Toronto Maple Leafs'
                i += 1
                continue
            elif 'Vancouver' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Vancouver Canucks'
                i += 1
                continue
            elif 'Vegas' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Vegas Golden Knights'
                i += 1
                continue
            elif 'Washington' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Washington Capitals'
                i += 1
                continue
            elif 'Winnipeg' in str(yahoo_data[i][0]):
                yahoo_data[i][0] = 'Winnipeg Jets'
                i += 1
                continue
            else:
                break
        else:
            break
    yahoo_data.sort(key=lambda x: x[0])
    # for elem in yahoo_data:
    #     print(elem)

    # url_DraftKings = 'https://sportsbook.draftkings.com/leagues/hockey/88670853?category=game-lines&subcategory=game'
    df_DraftKings = pd.read_html('https://sportsbook.draftkings.com/leagues/hockey/88670853?category=game-lines&subcategory=game')
    draftKingsData = df_DraftKings[0].values.tolist()
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

    i = 0
    while True: # MATCHING TEAM NAMES FROM BOTH SOURCES
        if i < len(draftKingsData):
            if 'Ducks' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Anaheim Ducks'
                i += 1
                continue
            elif 'Coyotes' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Arizona Coyotes'
                i += 1
                continue
            elif 'Bruins' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Boston Bruins'
                i += 1
                continue
            elif 'Sabres' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Buffalo Sabres'
                i += 1
                continue
            elif 'Flames' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Calgary Flames'
                i += 1
                continue
            elif 'Hurricanes' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Carolina Hurricanes'
                i += 1
                continue
            elif 'Blackhawks' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Chicago Blackhawks'
                i += 1
                continue
            elif 'Avalanche' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Colorado Avalanche'
                i += 1
                continue
            elif 'Jackets' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Columbus Blue Jackets'
                i += 1
                continue
            elif 'Stars' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Dallas Stars'
                i += 1
                continue
            elif 'Wings' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Detroit Red Wings'
                i += 1
                continue
            elif 'Oilers' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Edmonton Oilers'
                i += 1
                continue
            elif 'Panthers' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Florida Panthers'
                i += 1
                continue
            elif 'Kings' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Los Angeles Kings'
                i += 1
                continue
            elif 'Wild' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Minnesota Wild'
                i += 1
                continue
            elif 'Canadiens' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Montreal Canadiens'
                i += 1
                continue
            elif 'Predators' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Nashville Predators'
                i += 1
                continue
            elif 'Devils' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'New Jersey Devils'
                i += 1
                continue
            elif 'Islanders' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'New York Islanders'
                i += 1
                continue
            elif 'Rangers' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'New York Rangers'
                i += 1
                continue
            elif 'Senators' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Ottawa Senators'
                i += 1
                continue
            elif 'Flyers' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Philadelphia Flyers'
                i += 1
                continue
            elif 'Penguins' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Pittsburgh Penguins'
                i += 1
                continue
            elif 'Sharks' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'San Jose Sharks'
                i += 1
                continue
            elif 'Kraken' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Seattle Kraken'
                i += 1
                continue
            elif 'Blues' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'St. Louis Blues'
                i += 1
                continue
            elif 'Lightning' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Tampa Bay Lightning'
                i += 1
                continue
            elif 'Leafs' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Toronto Maple Leafs'
                i += 1
                continue
            elif 'Canucks' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Vancouver Canucks'
                i += 1
                continue
            elif 'Knights' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Vegas Golden Knights'
                i += 1
                continue
            elif 'Capitals' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Washington Capitals'
                i += 1
                continue
            elif 'Jets' in str(draftKingsData[i][0]):
                draftKingsData[i][0] = 'Winnipeg Jets'
                i += 1
                continue
            else:
                break
        else:
            break
    # print(draftKingsData)

    # matchupAnalysis [i][0] = name, [i][3] = moneyline, [i][14] = calculated chance, [i][15] = numberfire chance 
    # [i][16] = FiveThirtyEight chance, [i][17] = avg chance, [i][18] = value, [i][18] = calculated value
    # [i][19] = numberfire value, [i][20] = fivethirtyeight value, [i][21] = consensus

    headers = ['Team', 'PL', 'Total', 'ML', 'GF/G_T', 'GA/G_T', 'GF/G_H', 'GA/G_H', 
    'GF/G_A', 'GA/G_A', 'H/A', 'Team_Pts', 'Total_Pts', 'Calc %', 
    'NF_%', 'Day', 'FTE_%', 'Avg_%', 'Avg_V', 'Calc_V', 'NF_V', 
    'FTE_V', 'Consensus']

    dict_yahoo_data = {x[0]:x[1:] for x in yahoo_data}

    awayHome = ['A', 'H']
    y = (dict_yahoo_data.keys())
    # print(y)
    i = 0
    matchupAnalysis_NHL = []
    while True: 
        if i < len(draftKingsData):
            if draftKingsData[i][0] not in y:
                i += 1
                continue
            else:
                b = i + 1
                awayTeam = dict_yahoo_data[draftKingsData[i][0]]
                homeTeam = dict_yahoo_data[draftKingsData[b][0]]
                matchupAnalysis_NHL.append(draftKingsData[i] + awayTeam + [awayHome[0]])
                matchupAnalysis_NHL.append(draftKingsData[b] + homeTeam + [awayHome[1]])
                i += 2
        else:
            break
    # print(matchupAnalysis_NHL)

    # for elem in matchupAnalysis_NHL:
    #     print(elem)
        
    
    # get League Avg Points Against Home
    i = 0
    h = 0
    hf = 0
    while True:
        if i < len(yahoo_data):
            if yahoo_data[i][4] != '':
                h = h + yahoo_data[i][4]
                hf = hf + yahoo_data[i][3]
                i += 1
                continue
            else:
                h = h + yahoo_data[i][2]
                hf = hf + yahoo_data[i][1]
                i += 1
                continue
        else:
            # print(len(yahoo_data))
            h = h / len(yahoo_data)
            hf = hf / len(yahoo_data)
            leagueAvgAgainst_home = round(h, 2)
            leagueAvgForHome = round(hf, 2)
            break
    # print('league avg against home:')
    # print(leagueAvgAgainst_home)

    # get League Avg Points Against Away
    i = 0
    a = 0
    af = 0
    while True:
        if i < len(yahoo_data):
            if yahoo_data[i][6] != '':
                a = a + yahoo_data[i][6]
                af = af + yahoo_data[i][5]
                i += 1
                continue
            else:
                a = a + yahoo_data[i][2]
                af = af + yahoo_data[i][1]
                i += 1
                continue
        else:
            # print(len(yahoo_data))
            a = a / len(yahoo_data)
            af = af / len(yahoo_data)
            leagueAvgAgainst_away = round(a, 2)
            leagueAvgForAway = round(af, 2)
            break
    print('\n')
    print('league avg against away: ' + str(leagueAvgAgainst_away))
    print('league avg against home: ' + str(leagueAvgAgainst_home))
    # print('See ' + str(url_yahoo_total_against) + ' for team averages.')
    print('\n')
    print('league avg for away: ' + str(leagueAvgForAway))
    print('league avg for home: ' + str(leagueAvgForHome))

    for elem in matchupAnalysis_NHL:
        print(elem)
    #     print('\n')
        
    # Expected Points
    i = 0
    length = len(matchupAnalysis_NHL)
    while True: # GF/G = index 4 | GA/G = index 5 | leage avg = leagueAvgAgainst
        if i < length:
            h = i + 1
            if matchupAnalysis_NHL[h][7] == '':
                print('error')
                matchupAnalysis_NHL[h][7] = matchupAnalysis_NHL[h][5]
            if matchupAnalysis_NHL[h][6] == '':
                print('error')
                matchupAnalysis_NHL[h][6] = matchupAnalysis_NHL[h][4]
            a = round(float(matchupAnalysis_NHL[i][8]) * float(matchupAnalysis_NHL[h][7]), 2) 
            away = round(a / leagueAvgAgainst_home, 2)
            matchupAnalysis_NHL[i].append(away)
            home = round(float(matchupAnalysis_NHL[h][6]) * float(matchupAnalysis_NHL[i][9]), 2) 
            home = round(home / leagueAvgAgainst_away, 2)
            matchupAnalysis_NHL[h].append(home)
            i += 2
            continue
        else:
            break

    # CALCULATING EXPECTED TOTAL [i][12]
    i = 0
    while True: 
        if i < len(matchupAnalysis_NHL):
            h = i + 1
            blank = ''
            combinedTotal = matchupAnalysis_NHL[i][11] + matchupAnalysis_NHL[h][11]
            matchupAnalysis_NHL[i].append(round(combinedTotal, 2))
            matchupAnalysis_NHL[h].append(blank)
            i += 2
            continue
        else:
            break

    # create list of the possible points
    possiblePoints = []
    p = 0
    while True: 
        if p < 10:
            possiblePoints.append(int(p))
            p += 1
            continue
        else: 
            break
    # print(possiblePoints)

    # Poisson for range for each team, 7 = 11, 8 = 12
    poissonAway = []
    poissonHome = []
    i = 0
    p = 0
    h = i + 1
    while True: 
        if p < len(possiblePoints) and i < len(matchupAnalysis_NHL):
            expectA = float(matchupAnalysis_NHL[i][11])
            expectH = float(matchupAnalysis_NHL[h][11])
            chancePerScoreAway = ((expectA**(possiblePoints[p])) * (math.exp(-expectA)) / math.factorial(possiblePoints[p]))
            poissonAway.append(chancePerScoreAway)
            chancePerScoreHome = ((expectH**(possiblePoints[p])) * (math.exp(-expectH)) / math.factorial(possiblePoints[p]))
            poissonHome.append(chancePerScoreHome)
            p += 1
            continue
        elif len(poissonAway) == len(possiblePoints):
            if h <= len(matchupAnalysis_NHL):
                matchupAnalysis_NHL[i].append(poissonAway)
                matchupAnalysis_NHL[h].append(poissonHome)
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

    h = 0
    a = 0
    x = 0
    y = x + 1
    while True: # poisson
        if y <= len(matchupAnalysis_NHL):
            for i in range (10000):
                q = np.asarray(possiblePoints)
                awayArray_poisson = np.asarray(matchupAnalysis_NHL[x][13])
                homeArray_poisson = np.asarray(matchupAnalysis_NHL[y][13])
                awayChance = random.choices(q, awayArray_poisson)
                homeChance = random.choices(q, homeArray_poisson)
                if homeChance > awayChance:
                    h += 1
                elif awayChance > homeChance:
                    a += 1
            # d = 10000 - (a + h) # regulation
            w = round(a + h, 2) #
            a = (a / w) * 100 # including OT
            # a = (a / 10000) * 100 #
            a = round(a, 2)
            h = (h / w) * 100 #
            # h = (h / 10000) * 100 #
            h = round(h, 2)
            matchupAnalysis_NHL[x].append(a)
            matchupAnalysis_NHL[y].append(h)
            x += 2
            y = x + 1
            h = 0
            a = 0
            continue
        else:
            break
    # print('\n')
    # print(matchupAnalysis_NHL)
    # print('\n')

    # NUMBERFIRE CHANCES  
    today = date.today()
    tomorrow = today + timedelta(1)
    twodays = today + timedelta(2)
    threedays = today + timedelta(3)
    fourdays = today + timedelta(4)
    fivedays = today + timedelta(5)
    url_numberfire_NHL = "https://www.numberfire.com/nhl/games/" 
    resultNumberfireNHL = []
    i = 0
    g = 0
    s = 0
    projectedWinners = []
    resultNumberfireNHL_today = []
    resultNumberfireNHL_tomorrow = []
    resultNumberfireNHL_twodays = []
    resultNumberfireNHL_threedays = []
    resultNumberfireNHL_fourdays = []
    resultNumberfireNHL_fivedays = []
    while True: # list of Numberfire's projected winners and % chances
        if i == 0:
            url_today = url_numberfire_NHL + str(today)
            html_today = requests.get(url_today)
            soup_today = bs4.BeautifulSoup(html_today.content, features='html.parser') 
            scrapeNumberfireNHL_today = soup_today.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNHL_today):
                resultNumberfireNHL_today.append(str(scrapeNumberfireNHL_today[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNHL_today):
                    teamname = resultNumberfireNHL_today[g][265:275]
                    percent = resultNumberfireNHL_today[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
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
            url_tomorrow = url_numberfire_NHL + str(tomorrow)
            html_tomorrow = requests.get(url_tomorrow)
            soup_tomorrow = bs4.BeautifulSoup(html_tomorrow.content, features='html.parser') 
            scrapeNumberfireNHL_tomorrow = soup_tomorrow.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNHL_tomorrow):
                resultNumberfireNHL_tomorrow.append(str(scrapeNumberfireNHL_tomorrow[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNHL_tomorrow):
                    teamname = resultNumberfireNHL_tomorrow[g][265:275]
                    percent = resultNumberfireNHL_tomorrow[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
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
            url_twodays = url_numberfire_NHL + str(twodays)
            html_twodays = requests.get(url_twodays)
            soup_twodays = bs4.BeautifulSoup(html_twodays.content, features='html.parser') 
            scrapeNumberfireNHL_twodays = soup_twodays.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNHL_twodays):
                resultNumberfireNHL_twodays.append(str(scrapeNumberfireNHL_twodays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNHL_twodays):
                    teamname = resultNumberfireNHL_twodays[g][265:275]
                    percent = resultNumberfireNHL_twodays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
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
            url_threedays = url_numberfire_NHL + str(threedays)
            html_threedays = requests.get(url_threedays)
            soup_threedays = bs4.BeautifulSoup(html_threedays.content, features='html.parser') 
            scrapeNumberfireNHL_threedays = soup_threedays.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNHL_threedays):
                resultNumberfireNHL_threedays.append(str(scrapeNumberfireNHL_threedays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNHL_threedays):
                    teamname = resultNumberfireNHL_threedays[g][265:275]
                    percent = resultNumberfireNHL_threedays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
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
            url_fourdays = url_numberfire_NHL + str(fourdays)
            html_fourdays = requests.get(url_fourdays)
            soup_fourdays = bs4.BeautifulSoup(html_fourdays.content, features='html.parser') 
            scrapeNumberfireNHL_fourdays = soup_fourdays.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNHL_fourdays):
                resultNumberfireNHL_fourdays.append(str(scrapeNumberfireNHL_fourdays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNHL_fourdays):
                    teamname = resultNumberfireNHL_fourdays[g][265:275]
                    percent = resultNumberfireNHL_fourdays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
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
            url_fivedays = url_numberfire_NHL + str(fivedays)
            html_fivedays = requests.get(url_fivedays)
            soup_fivedays = bs4.BeautifulSoup(html_fivedays.content, features='html.parser') 
            scrapeNumberfireNHL_fivedays = soup_fivedays.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNHL_fivedays):
                resultNumberfireNHL_fivedays.append(str(scrapeNumberfireNHL_fivedays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNHL_fivedays):
                    teamname = resultNumberfireNHL_fivedays[g][265:275]
                    percent = resultNumberfireNHL_fivedays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
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
            if 'ANA' in str(projectedWinners[i]):
                projectedWinners[i] = 'Anaheim Ducks'
                i += 1
                continue
            elif 'ARI' in str(projectedWinners[i]):
                projectedWinners[i] = 'Arizona Coyotes'
                i += 1
                continue
            elif 'BOS' in str(projectedWinners[i]):
                projectedWinners[i] = 'Boston Bruins'
                i += 1
                continue
            elif 'BUF' in str(projectedWinners[i]):
                projectedWinners[i] = 'Buffalo Sabres'
                i += 1
                continue
            elif 'CGY' in str(projectedWinners[i]):
                projectedWinners[i] = 'Calgary Flames'
                i += 1
                continue
            elif 'CAR' in str(projectedWinners[i]):
                projectedWinners[i] = 'Carolina Hurricanes'
                i += 1
                continue
            elif 'CHI' in str(projectedWinners[i]):
                projectedWinners[i] = 'Chicago Blackhawks'
                i += 1
                continue
            elif 'COL' in str(projectedWinners[i]):
                projectedWinners[i] = 'Colorado Avalanche'
                i += 1
                continue
            elif 'CBJ' in str(projectedWinners[i]):
                projectedWinners[i] = 'Columbus Blue Jackets'
                i += 1
                continue
            elif 'DAL' in str(projectedWinners[i]):
                projectedWinners[i] = 'Dallas Stars'
                i += 1
                continue
            elif 'DET' in str(projectedWinners[i]):
                projectedWinners[i] = 'Detroit Red Wings'
                i += 1
                continue
            elif 'EDM' in str(projectedWinners[i]):
                projectedWinners[i] = 'Edmonton Oilers'
                i += 1
                continue
            elif 'FLA' in str(projectedWinners[i]):
                projectedWinners[i] = 'Florida Panthers'
                i += 1
                continue
            elif 'LA' in str(projectedWinners[i]):
                projectedWinners[i] = 'Los Angeles Kings'
                i += 1
                continue
            elif 'MIN' in str(projectedWinners[i]):
                projectedWinners[i] = 'Minnesota Wild'
                i += 1
                continue
            elif 'MTL' in str(projectedWinners[i]):
                projectedWinners[i] = 'Montreal Canadiens'
                i += 1
                continue
            elif 'NSH' in str(projectedWinners[i]):
                projectedWinners[i] = 'Nashville Predators'
                i += 1
                continue
            elif 'NJ' in str(projectedWinners[i]):
                projectedWinners[i] = 'New Jersey Devils'
                i += 1
                continue
            elif 'NYI' in str(projectedWinners[i]):
                projectedWinners[i] = 'New York Islanders'
                i += 1
                continue
            elif 'NYR' in str(projectedWinners[i]):
                projectedWinners[i] = 'New York Rangers'
                i += 1
                continue
            elif 'OTT' in str(projectedWinners[i]):
                projectedWinners[i] = 'Ottawa Senators'
                i += 1
                continue
            elif 'PHI' in str(projectedWinners[i]):
                projectedWinners[i] = 'Philadelphia Flyers'
                i += 1
                continue 
            elif 'PIT' in str(projectedWinners[i]):
                projectedWinners[i] = 'Pittsburgh Penguins'
                i += 1
                continue
            elif 'SJ' in str(projectedWinners[i]):
                projectedWinners[i] = 'San Jose Sharks'
                i += 1
                continue
            elif 'SEA' in str(projectedWinners[i]):
                projectedWinners[i] = 'Seattle Kraken'
                i += 1
                continue
            elif 'STL' in str(projectedWinners[i]):
                projectedWinners[i] = 'St. Louis Blues'
                i += 1
                continue
            elif 'TB' in str(projectedWinners[i]):
                projectedWinners[i] = 'Tampa Bay Lightning'
                i += 1
                continue
            elif 'TOR' in str(projectedWinners[i]):
                projectedWinners[i] = 'Toronto Maple Leafs'
                i += 1
                continue
            elif 'VAN' in str(projectedWinners[i]):
                projectedWinners[i] = 'Vancouver Canucks'
                i += 1
                continue
            elif 'VGS' in str(projectedWinners[i]):
                projectedWinners[i] = 'Vegas Golden Knights'
                i += 1
                continue
            elif 'WSH' in str(projectedWinners[i]):
                projectedWinners[i] = 'Washington Capitals'
                i += 1
                continue
            elif 'WPG' in str(projectedWinners[i]):
                projectedWinners[i] = 'Winnipeg Jets'
                i += 1
                continue
            else:
                i += 1
        else:
            break
    #print('\n')
    # prit('\n')
    # CREATE ORGANIZED LIST OF NUMBERFIRE CHANCES
    x = 3
    numberfireChances = [projectedWinners[i:i+x] for i in range(0, len(projectedWinners), x)]
    # print(numberfireChances)

    i = 0
    n = 0
    while True:
        if i < len(matchupAnalysis_NHL):
            h = i + 1
            if str(matchupAnalysis_NHL[i][0]) not in projectedWinners:
                y = projectedWinners.index(matchupAnalysis_NHL[h][0])
                winnerIndex = y
                winnerChanceIndex = y + 1
                gameDay = y + 2
                awayChance = float(100) - float(projectedWinners[winnerChanceIndex])
                awayChance = round(awayChance, 1)
                matchupAnalysis_NHL[i].append(awayChance)
                matchupAnalysis_NHL[h].append(projectedWinners[winnerChanceIndex])
                matchupAnalysis_NHL[i].append(projectedWinners[gameDay])
                matchupAnalysis_NHL[h].append(projectedWinners[gameDay])
                del projectedWinners[y:y+2]
                i += 2
                continue
            elif str(matchupAnalysis_NHL[h][0]) not in projectedWinners:
                x = projectedWinners.index(matchupAnalysis_NHL[i][0])
                winnerIndex = x
                winnerChanceIndex = x + 1
                gameDay = x + 2
                homeChance = float(100) - float(projectedWinners[winnerChanceIndex])
                homeChance = round(homeChance, 1)
                matchupAnalysis_NHL[h].append(homeChance)
                matchupAnalysis_NHL[i].append(projectedWinners[winnerChanceIndex])
                matchupAnalysis_NHL[i].append(projectedWinners[gameDay])
                matchupAnalysis_NHL[h].append(projectedWinners[gameDay])
                del projectedWinners[x:x+2]
                i += 2
                continue
            elif projectedWinners.index(matchupAnalysis_NHL[i][0]) < projectedWinners.index(matchupAnalysis_NHL[h][0]):
                x = projectedWinners.index(matchupAnalysis_NHL[i][0])
                winnerIndex = x
                winnerChanceIndex = x + 1
                gameDay = x + 2
                homeChance = float(100) - float(projectedWinners[winnerChanceIndex])
                homeChance = round(homeChance, 1)
                matchupAnalysis_NHL[h].append(homeChance)
                matchupAnalysis_NHL[i].append(projectedWinners[winnerChanceIndex])
                matchupAnalysis_NHL[i].append(projectedWinners[gameDay])
                matchupAnalysis_NHL[h].append(projectedWinners[gameDay])
                del projectedWinners[x:x+2]
                i += 2
                continue
            elif projectedWinners.index(matchupAnalysis_NHL[h][0]) < projectedWinners.index(matchupAnalysis_NHL[i][0]):
                y = projectedWinners.index(matchupAnalysis_NHL[h][0])
                winnerIndex = y
                winnerChanceIndex = y + 1
                gameDay = y + 2
                awayChance = float(100) - float(projectedWinners[winnerChanceIndex])
                awayChance = round(awayChance, 1)
                matchupAnalysis_NHL[i].append(awayChance)
                matchupAnalysis_NHL[h].append(projectedWinners[winnerChanceIndex])
                matchupAnalysis_NHL[i].append(projectedWinners[gameDay])
                matchupAnalysis_NHL[h].append(projectedWinners[gameDay])
                del projectedWinners[y:y+2]
                i += 2
                continue
        else:
            break    
    # print('\n')
    # for elem in matchupAnalysis_NHL:
    #     print(elem)

    # print('\n')
    # print(len(projectedWinners))
    # print('\n')
    fivethirtyeight_referenceLength = int(len(matchupAnalysis_NHL)) 
    df_fivethirtyeight = pd.read_html('https://projects.fivethirtyeight.com/2022-nhl-predictions/games/')
    # print('\n')
    # for elem in df_fivethirtyeight:
    #     print(elem)
    #     print('\n')
    # print(df_fivethirtyeight[3] / 2)
    # print('\n')
    lastTable_fivethirtyeight = 0 + fivethirtyeight_referenceLength
    # print('\n')
    # print(lastTable_fivethirtyeight)
    # print('\n')
    i = 0
    matchups_fivethirtyeight_NHL = []
    while True:
        if i < lastTable_fivethirtyeight:
            matchups_fivethirtyeight_NHL.append(df_fivethirtyeight[i].values.tolist())
            i += 2
            continue
        else:
            break
    print(matchups_fivethirtyeight_NHL)
    print(len(matchups_fivethirtyeight_NHL))
    for elem in matchups_fivethirtyeight_NHL:
        print(elem)
        print('\n')
    # print(type(matchups_fivethirtyeight_NHL[0][0][2]))

    i = 0
    m = 0
    while True: # MATCHING TEAM NAMES FIVETHIRTYEIGHT
        if i < len(matchups_fivethirtyeight_NHL):
            if m < 2:
                if '✓' in str(matchups_fivethirtyeight_NHL[i][m][2]): # if '%' in str(matchups_fivethirtyeight_NHL[i][m][1]) or '✓' in matchups_fivethirtyeight_NHL[i][m][2]:
                    del matchups_fivethirtyeight_NHL[i]
                    continue
                elif 'Ducks' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Anaheim Ducks'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Coyotes' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Arizona Coyotes'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Bruins' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Boston Bruins'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Sabres' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Buffalo Sabres'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Flames' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Calgary Flames'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Hurricanes' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Carolina Hurricanes'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Blackhawks' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Chicago Blackhawks'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Avalanche' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Colorado Avalanche'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Blue Jackets' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Columbus Blue Jackets'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Stars' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Dallas Stars'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Red Wings' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Detroit Red Wings'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Oilers' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Edmonton Oilers'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Panthers' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Florida Panthers'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Kings' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Los Angeles Kings'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Wild' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Minnesota Wild'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Canadiens' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Montreal Canadiens'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Predators' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Nashville Predators'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Devils' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'New Jersey Devils'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Islanders' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'New York Islanders'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Rangers' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'New York Rangers'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Senators' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Ottawa Senators'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Flyers' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Philadelphia Flyers'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue 
                elif 'Penguins' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Pittsburgh Penguins'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Sharks' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'San Jose Sharks'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Kraken' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Seattle Kraken'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Blues' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'St. Louis Blues'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Lightning' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Tampa Bay Lightning'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Maple Leafs' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Toronto Maple Leafs'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Canucks' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Vancouver Canucks'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Golden Knights' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Vegas Golden Knights'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Capitals' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Washington Capitals'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
                    m += 1
                    continue
                elif 'Jets' in str(matchups_fivethirtyeight_NHL[i][m][0]):
                    matchups_fivethirtyeight_NHL[i][m][0] = 'Winnipeg Jets'
                    x = str(matchups_fivethirtyeight_NHL[i][m][1])
                    x = x.translate({ord(i):None for i in '%'})
                    matchups_fivethirtyeight_NHL[i][m][1] = int(x)
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
    print('FIVETHIRTYEIGHT LENGTH = ' + str(len(matchups_fivethirtyeight_NHL)))
    print('MATCHUP ANALYSIS LENGTH = ' + str(len(matchupAnalysis_NHL)))
    print('\n')
    print(matchups_fivethirtyeight_NHL)
    print('\n')
    print(matchupAnalysis_NHL)
    print('\n')
    
    nhl_fte = []
    for elem in matchups_fivethirtyeight_NHL:
        for el in elem:
            nhl_fte.append(el)
    
    nhl = []
    i = 0
    while True:
        if i < len(matchupAnalysis_NHL):
            awayTeam = matchupAnalysis_NHL[i]
            homeTeam = matchupAnalysis_NHL[i + 1]
            lst = [awayTeam, homeTeam]
            nhl.append(lst)
            i += 2
            continue
        else:
            break
    
    dict_fte = {x[0]:x[1:] for x in nhl_fte}
    keys_fte = (dict_fte.keys())
    
    i = 0
    while True:
        if i < len(nhl):
            awayTeam = nhl[i][0][0]
            print(awayTeam)
            homeTeam = nhl[i][1][0]
            print(homeTeam)
            # day = str(nhl[i][2])
            away = str(awayTeam) # + ' ' + str(day)
            home = str(homeTeam) # + ' ' + str(day)s
            if away in keys_fte and home in keys_fte:
                awayChance = dict_fte[away]
                awayChance = float(awayChance[0])
                homeChance = dict_fte[home]
                homeChance = float(homeChance[0])
                nhl[i][0].append(awayChance)
                nhl[i][1].append(homeChance)
                i += 1
                continue
            else:
                awayChance = 'n/a'
                homeChance = 'n/a'
                nhl[i][0].append(awayChance)
                nhl[i][1].append(homeChance)
                i += 1
                continue
        else:
            break
    
    # fte_len = len(matchups_fivethirtyeight_NHL)
    # fte = 0
    # i = 0
    # m = 0
    # r = 0
    # while True:
    #     if i < len(matchupAnalysis_NHL):
    #         print(i)
    #         if r < 2:
    #             print(r)
    #             if str(matchupAnalysis_NHL[i][0]) == str(matchups_fivethirtyeight_NHL[m][r][0]):
    #                 if i == 0 or i % 2 == 0:
    #                     h = i + 1
    #                     d = r + 1
    #                     if str(matchupAnalysis_NHL[h][0]) == str(matchups_fivethirtyeight_NHL[m][d][0]):
    #                         if fte < fte_len:
    #                             matchupAnalysis_NHL[i].append(matchups_fivethirtyeight_NHL[m][r][2])
    #                             matchupAnalysis_NHL[h].append(matchups_fivethirtyeight_NHL[m][d][2])
    #                             del matchups_fivethirtyeight_NHL[m]
    #                             fte += 1
    #                             m = 0
    #                             r = 0
    #                             i += 2
    #                             continue
    #                         else:
    #                             break
    #                     else:
    #                         r += 1
    #                         continue
    #                 else:
    #                     r += 1
    #                     continue
    #             else:
    #                 r += 1
    #                 continue
    #         else:
    #             r = 0
    #             m += 1
    #             continue
    #     else:
    #         break

    print('\n')
    # print(matchupAnalysis_NHL)
    # print('\n')
    
    nhl_reorg = []
    for elem in nhl:
        away = elem[0]
        home = elem[1]
        nhl_reorg.append(away)
        nhl_reorg.append(home)
    
    
    matchupAnalysis_NHL = nhl_reorg
    # CALCULATE AND APPEND AVERAGE CHANCES TO MATCHUPANALYSIS_NHL / INDEX [I][17]
    i = 0
    while True:
        if i < len(matchupAnalysis_NHL):
            if matchupAnalysis_NHL[i][17] == 'n/a':
                avg = (float(matchupAnalysis_NHL[i][15]) + float(matchupAnalysis_NHL[i][14])) / 2
                avg = round(avg, 2)
                matchupAnalysis_NHL[i].append(avg)
                i += 1
                continue
            if matchupAnalysis_NHL[i][15] == 'n/a':
                avg = (float(matchupAnalysis_NHL[i][17]) + float(matchupAnalysis_NHL[i][14])) / 2
                avg = round(avg, 2)
                matchupAnalysis_NHL[i].append(avg)
                i += 1
                continue
            else:
                avg = (float(matchupAnalysis_NHL[i][15]) + float(matchupAnalysis_NHL[i][17]) + float(matchupAnalysis_NHL[i][14])) / 3
                avg = round(avg, 2)
                matchupAnalysis_NHL[i].append(avg)
                i += 1
                continue
        else:
            break
    # print(len(matchupAnalysis_NHL[0]))


    print('\n')
    leftWidth = 23
    rightWidth = 9
    righterWidth = 19
    rightererWidth = 14
    totalWidth = (leftWidth + righterWidth + righterWidth + righterWidth + rightererWidth + rightWidth 
    + rightererWidth + righterWidth)

    title = ' NHL '
    print(title.center(totalWidth, '-'))
    print('Team'.ljust(leftWidth) + 'Moneyline'.rjust(rightWidth) + 'Avg Value'.rjust(rightererWidth) 
        + 'Avg(%)'.rjust(rightererWidth) + 'Consensus(C/N/F)'.rjust(righterWidth) + 'Calculated(%)'.rjust(righterWidth) +
    'Numberfire(%)'.rjust(righterWidth) + 'FTE(%)'.rjust(righterWidth) 
    )
    print('\n')



    # matchupAnalysis [i][0] = name, [i][3] = moneyline, [i][14] = calculated chance, [i][15] = numberfire chance 
    # [i][16] = FiveThirtyEight chance, [i][17] = avg chance, [i][18] = value, [i][18] = calculated value
    # [i][19] = numberfire value, [i][20] = fivethirtyeight value, [i][21] = consensus

    #Fanduel

    for elem in matchupAnalysis_NHL:
        del elem[13]

    i = 0
    c = 0
    n = 0
    f = 0
    while True:
        if i < len(matchupAnalysis_NHL):
            if matchupAnalysis_NHL[i][3] < 0:
                avg_chance = matchupAnalysis_NHL[i][17]
                avg_chance_num = avg_chance / 100
                avg_chance_num = round(avg_chance_num, 2)
                moneyline = np.nan_to_num(matchupAnalysis_NHL[i][3]) 
                moneyline_pos = moneyline * -1
                value = avg_chance_num * (10 + 10 / (moneyline_pos / 10)* 10)
                value = round(value, 3)
                matchupAnalysis_NHL[i].append(value) # [i][18]
                name = matchupAnalysis_NHL[i][0]
                calc_chance = matchupAnalysis_NHL[i][13]
                calc_chance_num = calc_chance / 100
                calc_chance_num = round(calc_chance_num, 2)
                calc_value = calc_chance_num * (10 + 10 / (moneyline_pos / 10)* 10)
                calc_value = round(calc_value, 3)
                if calc_value > 10:
                    c = '+'
                if calc_value < 10:
                    c = '-'
                if matchupAnalysis_NHL[i][14] != 'n/a':
                    nf_chance = matchupAnalysis_NHL[i][14]
                    nf_chance_num = float(nf_chance) / 100
                    nf_chance_num = round(nf_chance_num, 2)
                    nf_value = nf_chance_num * (10 + 10 / (moneyline_pos / 10)* 10)
                    nf_value = round(nf_value, 3)
                    if nf_value > 10:
                        n = '+'
                    if nf_value < 10:
                        n = '-'
                if matchupAnalysis_NHL[i][14] == 'n/a':
                    nf_chance = matchupAnalysis_NHL[i][14]
                    nf_value = 'n/a'
                    n = '*'
                if matchupAnalysis_NHL[i][16] != 'n/a':
                    fte_chance = matchupAnalysis_NHL[i][16]
                    fte_chance_num = fte_chance / 100
                    fte_chance_num = round(fte_chance_num, 2)
                    fte_value = fte_chance_num * (10 + 10 / (moneyline_pos / 10)* 10)
                    fte_value = round(fte_value, 3)
                    if fte_value > 10:
                        f = '+'
                    if fte_value < 10:
                        f = '-'
                if matchupAnalysis_NHL[i][16] == 'n/a':
                    fte_chance = matchupAnalysis_NHL[i][14]
                    fte_value = 'n/a'
                    f = '*'
                matchupAnalysis_NHL[i].append(calc_value) # [i][19]
                matchupAnalysis_NHL[i].append(nf_value) # [i][20]
                matchupAnalysis_NHL[i].append(fte_value) # [i][21]
                matchupAnalysis_NHL[i].append(c + n + f) # creates [i][22] = consensus
                i += 1
                continue
            else:
                moneyline = np.nan_to_num(matchupAnalysis_NHL[i][3])
                moneyline = int(moneyline)
                avg_chance = matchupAnalysis_NHL[i][17]
                avg_chance_num = avg_chance / 100
                avg_chance_num = round(avg_chance_num, 2)
                value = (moneyline / 100 * 10 + 10) * avg_chance_num
                value = round(value, 3)
                matchupAnalysis_NHL[i].append(value) # [i][18]
                #if matchupAnalysis_NHL[i][18] > 10 and matchupAnalysis_NHL[i][15] == 'Today':
                name = matchupAnalysis_NHL[i][0]
                calc_chance = matchupAnalysis_NHL[i][13]
                calc_chance_num = calc_chance / 100
                calc_chance_num = round(calc_chance_num, 2)
                calc_value = (moneyline / 100 * 10 + 10) * calc_chance_num
                calc_value = round(calc_value, 3)
                if calc_value > 10:
                    c = '+'
                if calc_value < 10:
                    c = '-'
                if matchupAnalysis_NHL[i][14] != 'n/a':
                    nf_chance = matchupAnalysis_NHL[i][14]
                    nf_chance_num = float(nf_chance) / 100
                    nf_chance_num = round(nf_chance_num, 2)
                    nf_value = (moneyline / 100 * 10 + 10) * nf_chance_num
                    nf_value = round(nf_value, 3)
                    if nf_value > 10:
                        n = '+'
                    if nf_value < 10:
                        n = '-'
                if matchupAnalysis_NHL[i][14] == 'n/a':
                    nf_chance = matchupAnalysis_NHL[i][14]
                    nf_value = 'n/a'
                    n = '*'
                if matchupAnalysis_NHL[i][16] != 'n/a':
                    fte_chance = matchupAnalysis_NHL[i][16]
                    fte_chance_num = fte_chance / 100
                    fte_chance_num = round(fte_chance_num, 2)
                    fte_value = (moneyline / 100 * 10 + 10) * fte_chance_num
                    fte_value = round(fte_value, 3)
                    if fte_value > 10:
                        f = '+'
                    if fte_value < 10:
                        f = '-'
                if matchupAnalysis_NHL[i][16] == 'n/a':
                    fte_chance = matchupAnalysis_NHL[i][16]
                    fte_value = 'n/a'
                    f = '*'
                matchupAnalysis_NHL[i].append(calc_value) # [i][19]
                matchupAnalysis_NHL[i].append(nf_value) # [i][20]
                matchupAnalysis_NHL[i].append(fte_value) # [i][21]
                matchupAnalysis_NHL[i].append(c + n + f) # creates [i][22] = consensus
                i += 1
                continue
        else:
            break

    matchupAnalysis_NHL_sorted = sorted(matchupAnalysis_NHL, key=itemgetter(18), reverse=True)
    
    headers_sorted = ['Team', 'PL', 'Total', 'ML', 'H/A', 'Team_Pts', 'Total_Pts', 'Calc %', 
    'NF_%', 'FTE_%', 'Avg_%', 'Avg_V', 'Calc_V', 'NF_V', 
    'FTE_V', 'Consensus']

    for elem in matchupAnalysis_NHL_sorted:
        if elem[18] > 10 and elem[15] == 'Today':
            name = elem[0]
            moneyline = elem[3]
            value = elem[18]
            avg_chance = elem[17]
            consensus = elem[22] 
            calc_chance = elem[13]
            nf_chance = elem[14]
            fte_chance = elem[16]
            print((name).ljust(leftWidth) + str(moneyline).rjust(rightWidth) 
            + str(value).rjust(rightererWidth) + str(avg_chance).rjust(rightererWidth) 
            + str(consensus).rjust(righterWidth) + str(calc_chance).rjust(righterWidth) 
            + str(nf_chance).rjust(righterWidth) + str(fte_chance).rjust(righterWidth))
            continue
        else:
            continue

    for elem in matchupAnalysis_NHL_sorted:
        del elem[4:10]
        del elem[9]
    
    
    
        
        
        
    print('\n')
    nhlData = pd.DataFrame(matchupAnalysis_NHL_sorted, columns = headers_sorted)
    nhlData.head()
    nhlData.to_excel('/Users/Hayden/OneDrive/Sports Betting/Hockey/NHL.xlsx', index=False)

    conn = sqlite3.connect('NHL.db')

    nhlData.to_sql(name='NHL values', con=conn, if_exists='replace', index=False)

    conn.commit()

nhl()

# schedule.every(12).hours.do(nhl)

# while True:
#     schedule.run_pending()