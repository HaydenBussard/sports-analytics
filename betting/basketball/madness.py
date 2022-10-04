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


def ncaab():
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
            i += 1
            continue
        else:
            break
    # tr_for_table: [i][0] = teamname , [i][1] = total pfa, [i][2] = home pfa, [i][3] = away pfa , [i][1] = total paa, [i][2] = home paa, [i][3] = away paa

    i = 0
    while True:
        if i < len(tr_against_table):
            del tr_against_table[i][0]
            del tr_against_table[i][2:4]
            del tr_against_table[i][-1]
            i += 1
            continue
        else:
            break
    # tr_against_table: [i][0] = teamname , [i][1] = total paa, [i][2] = home paa, [i][3] = away paa

    tr_for_table.sort(key=lambda x: x[0])
    tr_against_table.sort(key=lambda x: x[0])


    # concat. for and against tables from teamrankings.com
    tr_data = tr_for_table
    i = 0
    while True:
        if i < len(tr_data):
            tr_data[i].append(tr_against_table[i][1])
            tr_data[i].append(tr_against_table[i][2])
            tr_data[i].append(tr_against_table[i][3])
            i += 1
            continue
        else:
            break

    # for elem in tr_data:
    #     print(elem)

    print('Team Rankings Data Scraped')

    # print('\n')
    # tr_data: [i][0] = teamname, [i][1] = total pfa, [i][2] = home pfa, [i][3] = away pfa, [i][4] = total paa
    # [i][5] = home paa, [i][6] = away paa

    url_draftKings_ncaab = 'https://sportsbook.draftkings.com/leagues/basketball/88670771'
    df_draftKings_ncaab = pd.read_html(url_draftKings_ncaab)
    draftKingsData = df_draftKings_ncaab[0].values.tolist()
    dk_length = len(df_draftKings_ncaab)
    i = 0
    draftKings_ncaab = []
    while True:
        if i < dk_length:
            x = df_draftKings_ncaab[i].values.tolist()
            draftKings_ncaab = draftKings_ncaab + x
            i += 1
            continue
        else:
            break

    # for elem in draftKings_ncaab:
    #     print(elem)

    # fix sublist index 0 with gametimes and team names
    i = 0
    a = 0 
    while True:
        if i < len(draftKings_ncaab):
            name_scraped = str(draftKings_ncaab[i][0])
            if name_scraped[5:7] == 'AM':
                m = name_scraped.index('AM')
                game_time = name_scraped[0: m + 2]
                team = name_scraped[m + 2:]
                draftKings_ncaab[i][0] = team
                draftKings_ncaab[i].append(game_time)
                i += 1
                continue
            elif name_scraped[4:6] == 'AM':
                m = name_scraped.index('AM')
                game_time = name_scraped[0: m + 2]
                team = name_scraped[m + 2:]
                draftKings_ncaab[i][0] = team
                draftKings_ncaab[i].append(game_time)
                i += 1
                continue
            elif name_scraped[5:7] == 'PM':
                m = name_scraped.index('PM')
                game_time = name_scraped[0: m + 2]
                team = name_scraped[m + 2:]
                draftKings_ncaab[i][0] = team
                draftKings_ncaab[i].append(game_time)
                i += 1
                continue
            elif name_scraped[4:6] == 'PM':
                m = name_scraped.index('PM')
                game_time = name_scraped[0: m + 2]
                team = name_scraped[m + 2:]
                draftKings_ncaab[i][0] = team
                draftKings_ncaab[i].append(game_time)
                i += 1
                continue
            elif name_scraped[4:6] == 'OT':
                m = name_scraped.index('OT')
                game_time = name_scraped[0: m + 2]
                team = name_scraped[m + 2:]
                draftKings_ncaab[i][0] = team
                draftKings_ncaab[i].append(game_time)
                i += 1
                continue
            elif name_scraped[0:15] == 'RegularTimeEnd':
                m = name_scraped.index('PM')
                game_time = name_scraped[0: 14]
                team = name_scraped[14:]
                draftKings_ncaab[i][0] = team
                draftKings_ncaab[i].append(game_time)
                i += 1
                continue
            elif 'Half' in name_scraped[7:13]:
                m = name_scraped.index('Half')
                game_time = 'LIVE'
                name_scraped = str(name_scraped[m + 4:])
                draftKings_ncaab[i][0] = name_scraped
                draftKings_ncaab[i].append(game_time)
                i += 1
                continue
            elif 'Half' in name_scraped[3:8]:
                m = name_scraped.index('Half')
                game_time = 'LIVE'
                name_scraped = str(name_scraped[m + 4:])
                draftKings_ncaab[i][0] = name_scraped
                draftKings_ncaab[i].append(game_time)
                i += 1
                continue
            # elif name_scraped[2] == ':':
            #     game_time = 'LIVE'
            #     name_scraped = str(name_scraped[16:])
            #     draftKings_ncaab[i][0] = name_scraped
            #     draftKings_ncaab[i].append(game_time)
            #     i += 1
            #     continue
            # elif name_scraped[8:15] == 'Quarter':
            #     print(name_scraped)
            #     game_time = 'LIVE'
            #     name_scraped = name_scraped[15:]
            #     draftKings_ncaab[i][0] = name_scraped
            #     draftKings_ncaab[i].append(game_time)
            #     i += 1
            #     continue
            # elif name_scraped[9:16] == 'Quarter':
            #     print(name_scraped)
            #     game_time = 'LIVE'
            #     name_scraped = name_scraped[16:]
            #     draftKings_ncaab[i][0] = name_scraped
            #     draftKings_ncaab[i].append(game_time)
            #     i += 1
            #     continue
            elif 'Overtime' in name_scraped:
                m = name_scraped.index('Overtime')
                game_time = 'LIVE'
                team = name_scraped[m + 8:]
                draftKings_ncaab[i][0] = team
                draftKings_ncaab[i].append(game_time)
                i += 1
                continue
            else:
                i += 1
                continue
        else: 
            break

    # for elem in draftKings_ncaab:
    #     print(elem)

    i = 0
    while True:
        if i < len(draftKings_ncaab):
            name_scraped = draftKings_ncaab[i][0]
            # print(name_scraped)
            if name_scraped[-1] == '0':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                # i += 1
                continue
            elif name_scraped[-1] == '1':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                # i += 1
                continue
            elif name_scraped[-1] == '2':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                # i += 1
                continue
            elif name_scraped[-1] == '3':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                # i += 1
                continue
            elif name_scraped[-1] == '4':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                # i += 1
                continue
            elif name_scraped[-1] == '5':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                # i += 1
                continue
            elif name_scraped[-1] == '6':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                # i += 1
                continue
            elif name_scraped[-1] == '7':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                # i += 1
                continue
            elif name_scraped[-1] == '8':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                # i += 1
                continue
            elif name_scraped[-1] == '9':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                # i += 1
                continue
            else:
                draftKings_ncaab[i][0] = name_scraped
                i += 1
                continue
        else: 
            break

    # print('\n')
    # print('\n')
    # print('\n')
    # print('\n')
    # for elem in draftKings_ncaab:
    #     print(elem[0])
    # print('\n')
    # print('\n')
    # print('\n')
    # print('\n')

    i = 0
    while True:
        if i < len(draftKings_ncaab):
            name_scraped = str(draftKings_ncaab[i][0])
            if name_scraped[-1] == '0':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                i += 1
                continue
            elif name_scraped[-1] == '1':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                i += 1
                continue
            elif name_scraped[-1] == '2':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                i += 1
                continue
            elif name_scraped[-1] == '3':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                i += 1
                continue
            elif name_scraped[-1] == '4':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                i += 1
                continue
            elif name_scraped[-1] == '5':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                i += 1
                continue
            elif name_scraped[-1] == '6':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                i += 1
                continue
            elif name_scraped[-1] == '7':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                i += 1
                continue
            elif name_scraped[-1] == '8':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                i += 1
                continue
            elif name_scraped[-1] == '9':
                name_scraped = name_scraped[0:-1]
                draftKings_ncaab[i][0] = name_scraped
                i += 1
                continue
            else:
                i += 1
                continue
        else: 
            break

    # print('\n')
    # print('\n')
    # for elem in draftKings_ncaab:
    #     print(elem[0])
    # print('\n')
    # print('\n')

    # # draftKings_ncaaf: [i][a][0] = team, [i][a][1] = spread, [i][a][2] = total, [i][a][3] = moneyline, 
    # # [i][a][4] = game time

    # # print(df_draftKings_ncaab)
    # # print(draftKings_ncaab)

    i = 0
    a = 0 
    alpha_dk_list = []
    while True:
        if i < dk_length:
            if draftKings_ncaab[i][0] in alpha_dk_list == True:
                i += 1
                continue
            else:
                alpha_dk_list.append(draftKings_ncaab[i][0])
                i += 1
                continue
        else: 
            break

    print('DraftKings Data Scraped')

    alpha_dk_list.sort()
    tr_data.sort(key=lambda x: x[0])
    # draftKings_ncaab.sort(key=lambda x: x[0])

    # for elem in draftKings_ncaab:
    #     print(elem[0])
        
    # print('\n')
    # print('\n')
    # print('\n')

    # for elem in tr_data:
    #     print(elem[0])

    i = 0
    a = 0
    while True:
        if i < len(tr_data):
            if 'AR Lit Rock' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Little Rock'
                i += 1
                continue
            elif 'Hampton' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Hampton'
                i += 1
                continue 
            elif 'Abl Christian' in str(tr_data[i][0]):#
                tr_data[i][0] = 'Abilene Christian'
                i += 1
                continue
            elif 'Wm & Mary' in str(tr_data[i][0]): 
                tr_data[i][0] = 'William & Mary'
                i += 1
                continue
            elif 'Air Force' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Air Force'
                i += 1
                continue
            elif 'Akron' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Akron'
                i += 1
                continue
            elif 'Alab A&M' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Alabama A&M'
                i += 1
                continue
            elif 'Alabama St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Alabama State'
                i += 1
                continue
            elif 'Prairie View' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Prairie View'
                i += 1
                continue 
            elif 'Albany' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Albany NY'
                i += 1
                continue
            elif 'Alcorn State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Alcorn'
                i += 1
                continue
            elif 'American' in str(tr_data[i][0]): 
                tr_data[i][0] = 'American'
                i += 1
                continue
            elif 'App State' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Appalachian State'
                i += 1
                continue
            elif 'N Arizona' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Northern Arizona'
                i += 1
                continue
            elif 'NC-Wilmgton' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UNCW'
                i += 1
                continue
            elif 'Arizona St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Arizona State'
                i += 1
                continue
            elif 'Arizona' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Arizona'
                i += 1
                continue
            elif 'Ark Pine Bl' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Arkansas-Pine Bluff'
                i += 1
                continue
            elif 'Arkansas St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Arkansas State'
                i += 1
                continue
            elif 'Army' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Army West Point'
                i += 1
                continue
            elif 'Auburn' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Auburn'
                i += 1
                continue
            elif 'Austin Peay' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Austin Peay'
                i += 1
                continue
            elif 'BYU' in str(tr_data[i][0]): #
                tr_data[i][0] = 'BYU'
                i += 1
                continue
            elif 'Ball State' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Ball State'
                i += 1
                continue
            elif 'Baylor' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Baylor'
                i += 1
                continue
            elif 'Bellarmine' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Bellarmine'
                i += 1
                continue
            elif 'Belmont' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Belmont'
                i += 1
                continue
            elif 'Beth-Cook' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Bethune-Cookman'
                i += 1
                continue
            elif 'Binghamton' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Binghamton'
                i += 1
                continue
            elif 'Boise State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Boise State'
                i += 1
                continue
            elif 'Boston Col' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Boston College'
                i += 1
                continue
            elif 'Boston U' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Boston University'
                i += 1
                continue
            elif 'Bowling Grn' in str(tr_data[i][0]):#
                tr_data[i][0] = 'Bowling Green'
                i += 1
                continue
            elif 'Bradley' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Bradley'
                i += 1
                continue 
            elif 'Brown' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Brown'
                i += 1
                continue
            elif 'Bryant' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Bryant'
                i += 1
                continue
            elif 'Bucknell' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Bucknell'
                i += 1
                continue
            elif 'Buffalo' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Buffalo'
                i += 1
                continue
            elif 'Butler' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Butler'
                i += 1
                continue
            elif 'CS Bakersfld' in str(tr_data[i][0]): 
                tr_data[i][0] = 'CSU Bakersfield'
                i += 1
                continue
            elif 'CS Fullerton' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Cal State Fullerton'
                i += 1
                continue
            elif 'Cal Baptist' in str(tr_data[i][0]): 
                tr_data[i][0] = 'California Baptist'
                i += 1
                continue
            elif 'Cal Poly' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Cal Poly'
                i += 1
                continue
            elif 'Cal St Nrdge' in str(tr_data[i][0]): 
                tr_data[i][0] = 'CSUN'
                i += 1
                continue
            elif 'California' in str(tr_data[i][0]): 
                tr_data[i][0] = 'California'
                i += 1
                continue
            elif 'Campbell' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Campbell'
                i += 1
                continue
            elif 'Canisius' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Canisius'
                i += 1
                continue
            elif 'Central Ark' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Central Arkansas'
                i += 1
                continue
            elif 'Arkansas' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Arkansas'
                i += 1
                continue
            elif 'Central Conn' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Central Connecticut State'
                i += 1
                continue
            elif 'Central FL' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UCF'
                i += 1
                continue
            elif 'Central Mich' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Central Michigan'
                i += 1
                continue
            elif 'Charl South' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Charleston Southern'
                i += 1
                continue
            elif 'Charlotte' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Charlotte'
                i += 1
                continue
            elif 'Chattanooga' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Chattanooga'
                i += 1
                continue
            elif 'Chicago St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Chicago State'
                i += 1
                continue 
            elif 'Cincinnati' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Cincinnati'
                i += 1
                continue
            elif 'Citadel' == str(tr_data[i][0]): #
                tr_data[i][0] = 'Citadel'
                i += 1
                continue
            elif 'Clemson' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Clemson'
                i += 1
                continue
            elif 'Cleveland St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Cleveland State'
                i += 1
                continue
            elif 'N Carolina' in str(tr_data[i][0]): 
                tr_data[i][0] = 'North Carolina'
                i += 1
                continue
            elif 'Coastal Car' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Coastal Carolina'
                i += 1
                continue
            elif 'Col Charlestn' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Charleston'
                i += 1
                continue
            elif 'Colgate' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Colgate'
                i += 1
                continue
            elif 'Colorado St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Colorado State'
                i += 1
                continue
            elif 'N Colorado' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Northern Colorado'
                i += 1
                continue
            elif 'Colorado' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Colorado'
                i += 1
                continue
            elif 'Columbia' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Columbia'
                i += 1
                continue
            elif 'Connecticut' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UConn'
                i += 1
                continue
            elif 'Coppin State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Coppin State'
                i += 1
                continue
            elif 'Cornell' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Cornell'
                i += 1
                continue 
            elif 'Creighton' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Creighton'
                i += 1
                continue
            elif 'Dartmouth' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Dartmouth'
                i += 1
                continue
            elif 'Davidson' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Davidson'
                i += 1
                continue 
            elif 'Dayton' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Dayton'
                i += 1
                continue
            elif 'DePaul' in str(tr_data[i][0]): 
                tr_data[i][0] = 'DePaul'
                i += 1
                continue
            elif 'Delaware St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Delaware State'
                i += 1
                continue
            elif 'Delaware' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Delaware'
                i += 1
                continue
            elif 'Denver' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Denver'
                i += 1
                continue
            elif 'Detroit' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Detroit Mercy'
                i += 1
                continue
            elif 'Dixie State' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Dixie State'
                i += 1
                continue
            elif 'Stetson' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Stetson'
                i += 1
                continue
            elif 'Drake' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Drake'
                i += 1
                continue
            elif 'Drexel' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Drexel'
                i += 1
                continue
            elif 'Duke' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Duke'
                i += 1
                continue
            elif 'Duquesne' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Duquesne'
                i += 1
                continue
            elif 'E Carolina' in str(tr_data[i][0]): 
                tr_data[i][0] = 'East Carolina'
                i += 1
                continue
            elif 'W Illinois' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Western Illinois'
                i += 1
                continue
            elif 'E Illinois' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Eastern Illinois'
                i += 1
                continue
            elif 'E Kentucky' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Eastern Kentucky'
                i += 1
                continue
            elif 'E Michigan' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Eastern Michigan'
                i += 1
                continue
            elif 'E Tenn St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'ETSU'
                i += 1
                continue
            elif 'E Washingtn' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Eastern Washington'
                i += 1
                continue
            elif 'Elon' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Elon'
                i += 1
                continue
            elif 'Evansville' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Evansville'
                i += 1
                continue
            elif 'F Dickinson' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Fairleigh Dickinson'
                i += 1
                continue
            elif 'Fairfield' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Fairfield'
                i += 1
                continue
            elif 'Fla Atlantic' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Florida Atlantic'
                i += 1
                continue
            elif 'Fla Gulf Cst' in str(tr_data[i][0]): 
                tr_data[i][0] = 'FGCU'
                i += 1
                continue
            elif 'Florida A&M' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Florida A&M'
                i += 1
                continue
            elif 'Florida Intl' in str(tr_data[i][0]): 
                tr_data[i][0] = 'FIU'
                i += 1
                continue
            elif 'Florida St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Florida State'
                i += 1
                continue
            elif 'N Florida' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'North Florida'
                i += 1
                continue
            elif 'S Florida' in str(tr_data[i][0]): 
                tr_data[i][0] = 'South Florida'
                i += 1
                continue 
            elif 'Florida' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Florida'
                i += 1
                continue
            elif 'Fordham' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Fordham'
                i += 1
                continue
            elif 'Fresno St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Fresno State'
                i += 1
                continue
            elif 'Furman' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Furman'
                i += 1
                continue 
            elif 'GA Southern' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Georgia Southern'
                i += 1
                continue 
            elif 'GA Tech' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Georgia Tech'
                i += 1
                continue
            elif 'Gard-Webb' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Gardner-Webb'
                i += 1
                continue
            elif 'Geo Mason' in str(tr_data[i][0]): 
                tr_data[i][0] = 'George Mason'
                i += 1
                continue 
            elif 'Geo Wshgtn' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'George Washington'
                i += 1
                continue 
            elif 'Georgetown' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Georgetown'
                i += 1
                continue 
            elif 'Georgia' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Georgia'
                i += 1
                continue 
            elif 'Georgia St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Georgia State'
                i += 1
                continue 
            elif 'Gonzaga' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Gonzaga'
                i += 1
                continue 
            elif 'Grambling St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Grambling'
                i += 1
                continue 
            elif 'Grd Canyon' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Grand Canyon'
                i += 1
                continue 
            elif 'Hartford' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Hartford'
                i += 1
                continue 
            elif 'Harvard' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Harvard'
                i += 1
                continue 
            elif 'Hawaii' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Hawaii'
                i += 1
                continue 
            elif 'High Point' in str(tr_data[i][0]): 
                tr_data[i][0] = 'High Point'
                i += 1
                continue 
            elif 'Hofstra' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Hofstra'
                i += 1
                continue 
            elif 'Holy Cross' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Holy Cross'
                i += 1
                continue 
            elif 'Houston Bap' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Houston Baptist'
                i += 1
                continue 
            elif 'Houston' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Houston'
                i += 1
                continue 
            elif 'Howard' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Howard'
                i += 1
                continue 
            elif 'IL-Chicago' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UIC'
                i += 1
                continue 
            elif 'IPFW' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Purdue Fort Wayne'
                i += 1
                continue 
            elif 'IUPUI' in str(tr_data[i][0]): 
                tr_data[i][0] = 'IUPUI'
                i += 1
                continue 
            elif 'Idaho State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Idaho State'
                i += 1
                continue 
            elif 'Idaho' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Idaho'
                i += 1
                continue 
            elif 'S Illinois' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Southern Illinois'
                i += 1
                continue 
            elif 'Illinois St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Illinois State'
                i += 1
                continue 
            elif 'Incar Word' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UIW'
                i += 1
                continue 
            elif 'Indiana St' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Indiana State'
                i += 1
                continue 
            elif 'Indiana' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Indiana'
                i += 1
                continue 
            elif 'Iona' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Iona'
                i += 1
                continue 
            elif 'N Iowa' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UNI'
                i += 1
                continue
            elif 'Iowa State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Iowa State'
                i += 1
                continue
            elif 'Iowa' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Iowa'
                i += 1
                continue 
            elif 'Jackson St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Jackson State'
                i += 1
                continue
            elif 'Jacksonville' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Jacksonville'
                i += 1
                continue
            elif 'James Mad' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'James Madison'
                i += 1
                continue
            elif 'Jksnville St' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Jacksonville State'
                i += 1
                continue
            elif 'Kansas St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Kansas State'
                i += 1
                continue
            elif 'Kansas' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Kansas'
                i += 1
                continue
            elif 'Kennesaw St' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Kennesaw State'
                i += 1
                continue
            elif 'Kent State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Kent State'
                i += 1
                continue
            elif 'LA Lafayette' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Louisiana-Lafayette'
                i += 1
                continue
            elif 'LA Monroe' in str(tr_data[i][0]): 
                tr_data[i][0] = 'ULM'
                i += 1
                continue
            elif 'LA Tech' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Louisiana Tech'
                i += 1
                continue
            elif 'LIU' in str(tr_data[i][0]): 
                tr_data[i][0] = 'LIU'
                i += 1
                continue
            elif 'LSU' in str(tr_data[i][0]): 
                tr_data[i][0] = 'LSU'
                i += 1
                continue
            elif 'La Salle' in str(tr_data[i][0]): 
                tr_data[i][0] = 'La Salle'
                i += 1
                continue
            elif 'Lafayette' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Lafayette'
                i += 1
                continue
            elif 'Lamar' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Lamar'
                i += 1
                continue
            elif 'Lehigh' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Lehigh'
                i += 1
                continue
            elif 'Lg Beach St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Long Beach State'
                i += 1
                continue
            elif 'Liberty' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Liberty'
                i += 1
                continue
            elif 'Lipscomb' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Lipscomb'
                i += 1
                continue
            elif 'Longwood' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Longwood'
                i += 1
                continue
            elif 'Louisville' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Louisville'
                i += 1
                continue
            elif 'Loyola Mymt' in str(tr_data[i][0]): 
                tr_data[i][0] = 'LMU'
                i += 1
                continue
            elif 'Loyola-Chi' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Loyola Chicago'
                i += 1
                continue
            elif 'Loyola-MD' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Loyola Maryland'
                i += 1
                continue
            elif 'Maine' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Maine'
                i += 1
                continue
            elif 'Manhattan' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Manhattan'
                i += 1
                continue
            elif 'Marist' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Marist'
                i += 1
                continue
            elif 'Marquette' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Marquette'
                i += 1
                continue 
            elif 'Marshall' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Marshall'
                i += 1
                continue
            elif 'Maryland BC' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UMBC'
                i += 1
                continue
            elif 'Maryland ES' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UMES'
                i += 1
                continue
            elif 'Maryland' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Maryland'
                i += 1
                continue
            elif 'Mass Lowell' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UMass Lowell'
                i += 1
                continue
            elif 'McNeese St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'McNeese'
                i += 1
                continue
            elif 'Memphis' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Memphis'
                i += 1
                continue
            elif 'Mercer' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Mercer'
                i += 1
                continue
            elif 'Merrimack' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Merrimack'
                i += 1
                continue
            elif 'Miami (FL)' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Miami FL'
                i += 1
                continue
            elif 'Miami (OH)' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Miami OH'
                i += 1
                continue
            elif 'W Michigan' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Western Michigan'
                i += 1
                continue
            elif 'Michigan St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Michigan State'
                i += 1
                continue
            elif 'Michigan' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Michigan'
                i += 1
                continue
            elif 'Middle Tenn' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Middle Tennessee'
                i += 1
                continue
            elif 'Minnesota' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Minnesota'
                i += 1
                continue
            elif 'Miss State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Mississippi State'
                i += 1
                continue
            elif 'Miss Val St' in str(tr_data[i][0]):
                tr_data[i][0] = 'Mississippi Valley'
                i += 1
                continue
            elif 'S Mississippi' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Southern Mississippi'
                i += 1
                continue 
            elif 'Mississippi' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Ole Miss'
                i += 1
                continue
            elif 'Missouri St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Missouri State'
                i += 1
                continue
            elif 'Monmouth' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Monmouth'
                i += 1
                continue 
            elif 'Montana St' == str(tr_data[i][0]): 
                tr_data[i][0] = 'Montana State'
                i += 1
                continue
            elif 'Montana' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Montana'
                i += 1
                continue
            elif 'Morehead St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Morehead State'
                i += 1
                continue
            elif 'Morgan St' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Morgan State'
                i += 1
                continue
            elif 'Mt St Marys' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Mount Saint Marys'
                i += 1
                continue
            elif 'St Marys' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Saint Marys'
                i += 1
                continue
            elif 'Murray St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Murray State'
                i += 1
                continue
            elif 'N Alabama' in str(tr_data[i][0]): 
                tr_data[i][0] = 'North Alabama'
                i += 1
                continue
            elif 'N Dakota St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'North Dakota State'
                i += 1
                continue
            elif 'N Hampshire' in str(tr_data[i][0]): 
                tr_data[i][0] = 'New Hampshire'
                i += 1
                continue 
            elif 'N Illinois' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Northern Illinois'
                i += 1
                continue
            elif 'Illinois' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Illinois'
                i += 1
                continue 
            elif 'N Kentucky' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Northern Kentucky'
                i += 1
                continue 
            elif 'N Mex State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'New Mexico State'
                i += 1
                continue
            elif 'NC A&T' in str(tr_data[i][0]): 
                tr_data[i][0] = 'North Carolina A&T'
                i += 1
                continue
            elif 'NC Central' in str(tr_data[i][0]): 
                tr_data[i][0] = 'North Carolina Central'
                i += 1
                continue
            elif 'NC State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'North Carolina State'
                i += 1
                continue
            elif 'NC-Asheville' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UNC Asheville'
                i += 1
                continue
            elif 'NC-Grnsboro' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UNC Greensboro'
                i += 1
                continue
            elif 'NC-Wilmgton' in str(tr_data[i][0]): #
                tr_data[i][0] = 'UNC Wilmington'
                i += 1
                continue
            elif 'NJIT' in str(tr_data[i][0]): 
                tr_data[i][0] = 'NJIT'
                i += 1
                continue
            elif 'NW State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Northwestern State'
                i += 1
                continue
            elif 'Navy' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Navy'
                i += 1
                continue
            elif 'Neb Omaha' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Omaha'
                i += 1
                continue
            elif 'Nebraska' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Nebraska'
                i += 1
                continue
            elif 'Nevada' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Nevada'
                i += 1
                continue
            elif 'New Mexico' in str(tr_data[i][0]): 
                tr_data[i][0] = 'New Mexico'
                i += 1
                continue
            elif 'New Orleans' in str(tr_data[i][0]): 
                tr_data[i][0] = 'New Orleans'
                i += 1
                continue
            elif 'Niagara' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Niagara'
                i += 1
                continue
            elif 'Nicholls St' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Nicholls State'
                i += 1
                continue
            elif 'Norfolk St' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Norfolk State'
                i += 1
                continue
            elif 'North Dakota' in str(tr_data[i][0]): 
                tr_data[i][0] = 'North Dakota'
                i += 1
                continue
            elif 'North Texas' in str(tr_data[i][0]): 
                tr_data[i][0] = 'North Texas'
                i += 1
                continue
            elif 'Northeastrn' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Northeastern'
                i += 1
                continue
            elif 'Northwestern' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Northwestern'
                i += 1
                continue
            elif 'Notre Dame' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Notre Dame'
                i += 1
                continue
            elif 'Oakland' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Oakland'
                i += 1
                continue
            elif 'Ohio State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Ohio State'
                i += 1
                continue
            elif 'Ohio' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Ohio'
                i += 1
                continue
            elif 'Oklahoma St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Oklahoma State'
                i += 1
                continue
            elif 'Oklahoma' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Oklahoma'
                i += 1
                continue
            elif 'Old Dominion' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Old Dominion'
                i += 1
                continue
            elif 'Oral Roberts' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Oral Roberts'
                i += 1
                continue 
            elif 'Oregon St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Oregon State'
                i += 1
                continue
            elif 'Oregon' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Oregon'
                i += 1
                continue 
            elif 'Pacific' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Pacific'
                i += 1
                continue
            elif 'Penn State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Penn State'
                i += 1
                continue 
            elif 'Pepperdine' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Pepperdine'
                i += 1
                continue 
            elif 'Pittsburgh' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Pittsburgh'
                i += 1
                continue 
            elif 'Portland St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Portland State'
                i += 1
                continue 
            elif 'Portland' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Portland'
                i += 1
                continue 
            elif 'Presbyterian' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Presbyterian'
                i += 1
                continue 
            elif 'Princeton' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Princeton'
                i += 1
                continue 
            elif 'Providence' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Providence'
                i += 1
                continue 
            elif 'Purdue' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Purdue'
                i += 1
                continue 
            elif 'Quinnipiac' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Quinnipiac'
                i += 1
                continue 
            elif 'Radford' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Radford'
                i += 1
                continue 
            elif 'Rhode Island' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Rhode Island'
                i += 1
                continue 
            elif 'Rice' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Rice'
                i += 1
                continue 
            elif 'Richmond' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Richmond'
                i += 1
                continue 
            elif 'Rider' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Rider'
                i += 1
                continue 
            elif 'Rob Morris' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Robert Morris'
                i += 1
                continue 
            elif 'Rutgers' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Rutgers'
                i += 1
                continue 
            elif 'S Alabama' in str(tr_data[i][0]): 
                tr_data[i][0] = 'South Alabama'
                i += 1
                continue 
            elif 'Alabama' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Alabama'
                i += 1
                continue
            elif 'S Car State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'South Carolina State'
                i += 1
                continue 
            elif 'S Carolina' in str(tr_data[i][0]): 
                tr_data[i][0] = 'South Carolina'
                i += 1
                continue 
            elif 'S Dakota St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'South Dakota State'
                i += 1
                continue 
            elif 'S Methodist' in str(tr_data[i][0]): 
                tr_data[i][0] = 'SMU'
                i += 1
                continue 
            elif 'S Utah' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Southern Utah'
                i += 1
                continue 
            elif 'SC Upstate' in str(tr_data[i][0]): 
                tr_data[i][0] = 'USC Upstate'
                i += 1
                continue 
            elif 'SE Louisiana' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Southeastern Louisiana'
                i += 1
                continue 
            elif 'SE Missouri' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Southeast Missouri State'
                i += 1
                continue 
            elif 'Missouri' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Missouri'
                i += 1
                continue
            elif 'SIU Edward' in str(tr_data[i][0]): 
                tr_data[i][0] = 'SIUE'
                i += 1
                continue
            elif 'Sac State' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Sacramento State'
                i += 1
                continue
            elif 'Sacred Hrt' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Sacred Heart'
                i += 1
                continue
            elif 'Saint Louis' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Saint Louis'
                i += 1
                continue
            elif 'Sam Hous St' in str(tr_data[i][0]):
                tr_data[i][0] = 'Sam Houston'
                i += 1
                continue
            elif 'Samford' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Samford'
                i += 1
                continue
            elif 'San Diego St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'San Diego State'
                i += 1
                continue
            elif 'UC San Diego' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UC San Diego'
                i += 1
                continue
            elif 'San Diego' in str(tr_data[i][0]): #
                tr_data[i][0] = 'San Diego'
                i += 1
                continue
            elif 'San Fransco' in str(tr_data[i][0]): 
                tr_data[i][0] = 'San Francisco'
                i += 1
                continue
            elif 'San Jose St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'San Jose State'
                i += 1
                continue
            elif 'Santa Clara' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Santa Clara'
                i += 1
                continue
            elif 'Seattle' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Seattle'
                i += 1
                continue
            elif 'Seton Hall' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Seton Hall'
                i += 1
                continue
            elif 'Siena' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Siena'
                i += 1
                continue
            elif 'South Dakota' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'South Dakota'
                i += 1
                continue
            elif 'Southern' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Southern University'
                i += 1
                continue
            elif 'St Bonavent' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Saint Bonaventure'
                i += 1
                continue
            elif 'St Fran (NY)' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Saint Francis Brooklyn'
                i += 1
                continue
            elif 'St Fran (PA)' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Saint Francis PA'
                i += 1
                continue
            elif 'St Johns' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Saint Johns'
                i += 1
                continue
            elif 'St Josephs' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Saint Josephs'
                i += 1
                continue
            elif 'St Peters' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Saint Peters'
                i += 1
                continue
            elif 'St. Thomas (MN)' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Saint Thomas MN'
                i += 1
                continue
            elif 'Stanford' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Stanford'
                i += 1
                continue
            elif 'Ste F Austin' in str(tr_data[i][0]): 
                tr_data[i][0] = 'SFA'
                i += 1
                continue
            elif 'Stony Brook' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Stony Brook'
                i += 1
                continue
            elif 'Syracuse' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Syracuse'
                i += 1
                continue
            elif 'TN Martin' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UT Martin'
                i += 1
                continue
            elif 'TN State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Tennessee State'
                i += 1
                continue 
            elif 'TN Tech' in str(tr_data[i][0]): ##
                tr_data[i][0] = 'Tennessee Tech'
                i += 1
                continue
            elif 'TX A&M-CC' in str(tr_data[i][0]): 
                tr_data[i][0] = 'A&M-Corpus Christi'
                i += 1
                continue
            elif 'TX Christian' in str(tr_data[i][0]): 
                tr_data[i][0] = 'TCU'
                i += 1
                continue
            elif 'TX El Paso' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UTEP'
                i += 1
                continue
            elif 'TX Southern' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Texas Southern'
                i += 1
                continue
            elif 'TX-Arlington' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UT Arlington'
                i += 1
                continue
            elif 'TX-Pan Am' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UTRGV'
                i += 1
                continue
            elif 'TX-San Ant' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UTSA'
                i += 1
                continue
            elif 'Tarleton State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Tarleton State'
                i += 1
                continue
            elif 'Temple' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Temple'
                i += 1
                continue
            elif 'Tennessee' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Tennessee'
                i += 1
                continue
            elif 'Texas A&M' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Texas A&M'
                i += 1
                continue
            elif 'Texas State' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Texas State'
                i += 1
                continue
            elif 'Texas Tech' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Texas Tech'
                i += 1
                continue
            elif 'Texas' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Texas'
                i += 1
                continue
            elif 'Toledo' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Toledo'
                i += 1
                continue
            elif 'Towson' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Towson'
                i += 1
                continue
            elif 'Troy' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Troy'
                i += 1
                continue
            elif 'Tulane' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Tulane'
                i += 1
                continue
            elif 'Tulsa' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Tulsa'
                i += 1
                continue
            elif 'U Mass' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Massachusetts'
                i += 1
                continue 
            elif 'U Penn' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Pennsylvania'
                i += 1
                continue
            elif 'UAB' == str(tr_data[i][0]): 
                tr_data[i][0] = 'UAB'
                i += 1
                continue
            elif 'UC Davis' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UC Davis'
                i += 1
                continue
            elif 'UC Irvine' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UC Irvine'
                i += 1
                continue
            elif 'UC Riverside' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UC Riverside'
                i += 1
                continue
            elif 'UCLA' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UCLA'
                i += 1
                continue
            elif 'UCSB' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UC Santa Barbara'
                i += 1
                continue
            elif 'UMKC' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Kansas City'
                i += 1
                continue
            elif 'UNLV' in str(tr_data[i][0]): 
                tr_data[i][0] = 'UNLV'
                i += 1
                continue
            elif 'USC' in str(tr_data[i][0]): 
                tr_data[i][0] = 'USC'
                i += 1
                continue
            elif 'Utah State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Utah State'
                i += 1
                continue 
            elif 'Utah Val St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Utah Valley'
                i += 1
                continue
            elif 'Utah' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Utah'
                i += 1
                continue
            elif 'VA Military' in str(tr_data[i][0]): 
                tr_data[i][0] = 'VMI'
                i += 1
                continue
            elif 'VA Tech' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Virginia Tech'
                i += 1
                continue 
            elif 'VCU' in str(tr_data[i][0]): 
                tr_data[i][0] = 'VCU'
                i += 1
                continue
            elif 'Valparaiso' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Valparaiso'
                i += 1
                continue
            elif 'Vanderbilt' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Vanderbilt'
                i += 1
                continue
            elif 'Vermont' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Vermont'
                i += 1
                continue
            elif 'Villanova' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Villanova'
                i += 1
                continue
            elif 'W Virginia' in str(tr_data[i][0]): 
                tr_data[i][0] = 'West Virginia'
                i += 1
                continue
            elif 'Virginia' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Virginia'
                i += 1
                continue
            elif 'W Carolina' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Western Carolina'
                i += 1
                continue
            elif 'W Kentucky' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Western Kentucky'
                i += 1
                continue
            elif 'Kentucky' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Kentucky'
                i += 1
                continue
            elif 'WI-Grn Bay' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Green Bay'
                i += 1
                continue
            elif 'WI-Milwkee' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Milwaukee'
                i += 1
                continue
            elif 'Wagner' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Wagner'
                i += 1
                continue
            elif 'Wake Forest' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Wake Forest'
                i += 1
                continue
            elif 'Wash State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Washington State'
                i += 1
                continue
            elif 'Washington' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Washington'
                i += 1
                continue
            elif 'Weber State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Weber State'
                i += 1
                continue
            elif 'Wichita St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Wichita State'
                i += 1
                continue
            elif 'Winthrop' in str(tr_data[i][0]): #
                tr_data[i][0] = 'Winthrop'
                i += 1
                continue
            elif 'Wisconsin' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Wisconsin'
                i += 1
                continue
            elif 'Wofford' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Wofford'
                i += 1
                continue
            elif 'Wright State' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Wright State'
                i += 1
                continue
            elif 'Wyoming' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Wyoming'
                i += 1
                continue
            elif str(tr_data[i][0]) == 'Xavier': 
                tr_data[i][0] = 'Xavier'
                i += 1
                continue
            elif 'Yale' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Yale'
                i += 1
                continue
            elif 'Youngs St' in str(tr_data[i][0]): 
                tr_data[i][0] = 'Youngstown State'
                i += 1
                continue
            else:
                i += 1
                continue
        else:
            break

    print('Team Rankings Names Converted')

    i = 0
    while True:
        if i < len(tr_data):
            if tr_data[i][0] == '':
                del tr_data[i]
                i = 0
                continue
            else:
                i += 1
                continue
        else:
            break

    # for elem in tr_data:
    #     print(elem)
    #     print('\n')

    # headers = ['0 - Team', '1 - Spread', '2 - Total', '3 - Moneyline', '4 - Game Time', '5 - PF/G Total', '6 - PF/G Home',
    #  '7 - PF/G Away', '8 - PA/G Total', '9 - PA/G Home', '10 - PA/G Away', '11 - Home or Away', '12 - Expected Points',
    #  '13 - Expected Total', '14 - Poisson', '14 - Calculated Chance', '14 - Numberfire Chance', '17 - Day',
    #  '18 - Average Chance', '19 - Average Value', '20 - Calculated Value', '21 - Numberfire Value', 
    #  '22 - Consensus']

    # matchupAnalysis: [i][0] = teamname, [i][1] = spread, [i][2] = total, [i][3] = moneyline,
    # [i][4] = time, [i][5] = total pfa, [i][6] = home pfa, [i][7] = away pfa , [i][8] = total paa
    # , [i][9] = home paa, [i][10] = away paa, [i][11] = home or away, [i][12] = expected points, 
    # [i][13] = expected total, [i][14] = poisson, [i][15] = calculated chance, [i][16] = numberfire chance
    # [i][17] = game day (today or not today), [i][18] = average chance, [i][19] = average value, 
    # [i][20] = calculated value, [i][21] = numberfire value, [i][22] = consensus

    dict_tr_data = {x[0]:x[1:] for x in tr_data}

    # print(dict_tr_data.keys())
    # for elem in draftKings_ncaab:
    #     print(elem[0])

    # print(dict_tr_data)
    # print(draftKings_ncaab)

    awayHome = ['A', 'H']
    y = (dict_tr_data.keys())

    # print(y)

    # for elem in draftKings_ncaab:
    #     print(elem)

    i = 0
    m = 0
    matchupAnalysis_NCAAB = []
    while True: 
        if i < len(draftKings_ncaab):
            b = i + 1
            if draftKings_ncaab[i][0] not in y or draftKings_ncaab[b][0] not in y:
                i += 2
                continue
            else:
                awayTeam = dict_tr_data[draftKings_ncaab[i][0]]
                homeTeam = dict_tr_data[draftKings_ncaab[b][0]]
                matchupAnalysis_NCAAB.append(draftKings_ncaab[i] + awayTeam + [awayHome[0]])
                matchupAnalysis_NCAAB.append(draftKings_ncaab[b] + homeTeam + [awayHome[1]])
                i += 2
                continue
        else:
            break

    print('Team Rankings and DraktKings Data Matched and combined.')

    # for elem in matchupAnalysis_NCAAB:
    #     print(elem)

    # for elem in tr_data:
    #     print(elem)

    # tr_data: [i][0] = teamname , [i][1] = total pfa, [i][2] = home pfa, [i][3] = away pfa , [i][4] = total paa
    # , [i][5] = home paa, [i][6] = away paa

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
                a = a + tr_data[i][4] # CHANGE BACK TO "6" FOR AWAY VALUES>>>    #tr_data[i][5] = Home Pts Against ..... tr_data[i][6] = Away Pts Against
                h = h + tr_data[i][4] # CHANGE BACK TO "5" FOR AWAY VALUES
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

    print('Calculated League Average Points Against' + str(leagueAvgAgainst_away))
    

    # print(len(draftKings_ncaab[0]))
    # print('\n')
    # print(draftKings_ncaaf)
    # print('\n')
    # print(matchupAnalysis_NCAAF)


    dict_matchupAnalysis = {x[0]:x[1:] for x in matchupAnalysis_NCAAB}


    # print(matchupAnalysis_NCAAF)


    # matchupAnalysis: [i][0] = teamname, [i][1] = spread, [i][2] = total, [i][3] = moneyline,
    # [i][4] = time, [i][5] = total pfa, [i][6] = home pfa, [i][7] = away pfa , [i][8] = total paa
    # , [i][9] = home paa, [i][10] = away paa

    for elem in matchupAnalysis_NCAAB:
        if elem[7] == '--':
            elem[7] = elem[5]
        if elem[6] == '--':
            elem[6] = elem[5]
        if elem[9] == '--':
            elem[9] = elem[8]
        if elem[10] == '--':
            elem[10] = elem[8]

    # Expected Points
    i = 0
    length = len(matchupAnalysis_NCAAB)
    while True: # PF/G = index 5 | GA/G = index 8 | leage avg = leagueAvgAgainst
        if i < length:
            h = i + 1
            a = (float(matchupAnalysis_NCAAB[i][5]) * float(matchupAnalysis_NCAAB[h][8]) / leagueAvgAgainst_home)  # [7] is away for, [9] is home against
            away = round(a, 2)
            matchupAnalysis_NCAAB[i].append(away)
            home = (float(matchupAnalysis_NCAAB[h][5]) * float(matchupAnalysis_NCAAB[i][8]) / leagueAvgAgainst_away)  # [6] is home for, [10] is away against
            home = round(home, 2)
            matchupAnalysis_NCAAB[h].append(home)
            i += 2
            continue
        else:
            break

    print('Calculated Each Team\'s Expected points')

    # matchupAnalysis: [i][0] = teamname, [i][1] = spread, [i][2] = total, [i][3] = moneyline,
    # [i][4] = time, [i][5] = total pfa, [i][6] = home pfa, [i][7] = away pfa , [i][8] = total paa
    # , [i][9] = home paa, [i][10] = away paa, [i][11] = home or away, [i][12] = expected points, 
    # [i][13] = expected total

    # CALCULATING EXPECTED TOTAL [i][13]
    i = 0
    while True: 
        if i < len(matchupAnalysis_NCAAB):
            h = i + 1
            blank = ''
            combinedTotal = float(matchupAnalysis_NCAAB[i][12]) + float(matchupAnalysis_NCAAB[h][12])
            matchupAnalysis_NCAAB[i].append(round(combinedTotal, 2))
            matchupAnalysis_NCAAB[h].append(blank)
            i += 2
            continue
        else:
            break

    print('Calculated All Expected Totals')

    # create list of the possible points
    possiblePoints = []
    p = 0
    while True: 
        if p < 120:
            possiblePoints.append(int(p))
            p += 1
            continue
        else: 
            break
    # print(possiblePoints)

    print('Created List of Possible Points')

    # Poisson for range for each team, EXPECTED = 12, EXP TOTAL = 13
    poissonAway = []
    poissonHome = []
    
    i = 0
    p = 0
    h = i + 1
    while True: 
        if p < len(possiblePoints) and i < len(matchupAnalysis_NCAAB):
            expectA = float(matchupAnalysis_NCAAB[i][12])
            expectH = float(matchupAnalysis_NCAAB[h][12])
            chancePerScoreAway = ((expectA**(possiblePoints[p])) * (math.exp(-expectA)) / math.factorial(possiblePoints[p]))
            poissonAway.append(chancePerScoreAway)
            chancePerScoreHome = ((expectH**(possiblePoints[p])) * (math.exp(-expectH)) / math.factorial(possiblePoints[p]))
            poissonHome.append(chancePerScoreHome)
            p += 1
            continue
        elif len(poissonAway) == len(possiblePoints):
            if h <= len(matchupAnalysis_NCAAB):
                matchupAnalysis_NCAAB[i].append(poissonAway)
                matchupAnalysis_NCAAB[h].append(poissonHome)
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

    print('Poisson Distributions Completed')

    # matchupAnalysis: [i][0] = teamname, [i][1] = spread, [i][2] = total, [i][3] = moneyline,
    # [i][4] = time, [i][5] = total pfa, [i][6] = home pfa, [i][7] = away pfa , [i][8] = total paa
    # , [i][9] = home paa, [i][10] = away paa, [i][11] = home or away, [i][12] = expected points, 
    # [i][13] = expected total, [i][14] = poisson, 

    h = 0
    a = 0
    x = 0
    y = x + 1
    while True: # poisson
        if y <= len(matchupAnalysis_NCAAB):
            for i in range (100000):
                q = np.asarray(possiblePoints)
                awayArray_poisson = np.asarray(matchupAnalysis_NCAAB[x][14])
                homeArray_poisson = np.asarray(matchupAnalysis_NCAAB[y][14])
                awayChance = random.choices((q), awayArray_poisson)
                homeChance = random.choices((q), homeArray_poisson)
                if homeChance > awayChance:
                    h += 1
                elif awayChance > homeChance:
                    a += 1
            w = round(a + h, 2)
            a = (a / w) * 100
            a = round(a, 2)
            h = (h / w) * 100
            h = round(h, 2)
            matchupAnalysis_NCAAB[x].append(a)
            matchupAnalysis_NCAAB[y].append(h)
            del matchupAnalysis_NCAAB[x][14]
            del matchupAnalysis_NCAAB[y][14]
            x += 2
            y = x + 1
            h = 0
            a = 0
            continue
        else:
            break
    print('\n')
    print('Chances Calculated for Each Team')

    for elem in matchupAnalysis_NCAAB:
        if elem[0] == 'Texas Tech' or elem[0] == 'San Diego State' or elem[0] == 'UConn' or elem[0] == 'Seton Hall':
            print(elem)
    print('\n')
    # matchupAnalysis: [i][0] = teamname, [i][1] = spread, [i][2] = total, [i][3] = moneyline,
    # [i][4] = time, [i][5] = total pfa, [i][6] = home pfa, [i][7] = away pfa , [i][8] = total paa
    # , [i][9] = home paa, [i][10] = away paa, [i][11] = home or away, [i][12] = expected points, 
    # [i][13] = expected total, [i][14] = poisson, [i][15] = calculated chance

    # NUMBERFIRE CHANCES  
    today = date.today()
    tomorrow = today + timedelta(1)
    twodays = today + timedelta(2)
    threedays = today + timedelta(3)
    fourdays = today + timedelta(4)
    fivedays = today + timedelta(5)
    url_numberfire_NCAAB = "https://www.numberfire.com/ncaab/games/" 
    resultNumberfireNCAAB = []
    i = 0
    g = 0
    s = 0
    projectedWinners = []
    resultNumberfireNCAAB_today = []
    resultNumberfireNCAAB_tomorrow = []
    resultNumberfireNCAAB_twodays = []
    resultNumberfireNCAAB_threedays = []
    resultNumberfireNCAAB_fourdays = []
    resultNumberfireNCAAB_fivedays = []
    while True: # list of Numberfire's projected winners and % chances
        if i == 0:
            url_today = url_numberfire_NCAAB + str(today)
            html_today = requests.get(url_today)
            soup_today = bs4.BeautifulSoup(html_today.content, features='html.parser') 
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_today):
                i += 1
                continue
            scrapeNumberfireNCAAB_today = soup_today.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_today):
                resultNumberfireNCAAB_today.append(str(scrapeNumberfireNCAAB_today[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_today):
                    print(resultNumberfireNCAAB_today[g])
                    print('\n')
                    teamname = resultNumberfireNCAAB_today[g][265:281] # used to be 265:275
                    print(teamname)
                    print('\n')
                    percent = resultNumberfireNCAAB_today[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    projectedWinners.append(teamname)
                    projectedWinners.append(percent)
                    projectedWinners.append('TODAY')
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    print("TODAY Numberfire Loop Complete")
                    continue
        elif i == 1:
            url_tomorrow = url_numberfire_NCAAB + str(tomorrow)
            html_tomorrow = requests.get(url_tomorrow)
            soup_tomorrow = bs4.BeautifulSoup(html_tomorrow.content, features='html.parser') 
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_tomorrow):
                i += 1
                continue
            scrapeNumberfireNCAAB_tomorrow = soup_tomorrow.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_tomorrow):
                resultNumberfireNCAAB_tomorrow.append(str(scrapeNumberfireNCAAB_tomorrow[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_tomorrow):
                    teamname = resultNumberfireNCAAB_tomorrow[g][265:275]
                    percent = resultNumberfireNCAAB_tomorrow[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    projectedWinners.append(teamname)
                    projectedWinners.append(percent)
                    projectedWinners.append('TOMORROW')
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    print("TOMORROW Numberfire Loop Complete")
                    continue
        elif i == 2:
            url_twodays = url_numberfire_NCAAB + str(twodays)
            html_twodays = requests.get(url_twodays)
            soup_twodays = bs4.BeautifulSoup(html_twodays.content, features='html.parser') 
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_twodays):
                i += 1
                continue
            scrapeNumberfireNCAAB_twodays = soup_twodays.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_twodays):
                resultNumberfireNCAAB_twodays.append(str(scrapeNumberfireNCAAB_twodays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_twodays):
                    teamname = resultNumberfireNCAAB_twodays[g][265:275]
                    percent = resultNumberfireNCAAB_twodays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    projectedWinners.append(teamname)
                    projectedWinners.append(percent)
                    projectedWinners.append(str(twodays))
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    print("TWODAYS Numberfire Loop Complete")
                    continue
        elif i == 3:
            url_threedays = url_numberfire_NCAAB + str(threedays)
            html_threedays = requests.get(url_threedays)
            soup_threedays = bs4.BeautifulSoup(html_threedays.content, features='html.parser') 
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_threedays):
                i += 1
                continue
            scrapeNumberfireNCAAB_threedays = soup_threedays.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_threedays):
                resultNumberfireNCAAB_threedays.append(str(scrapeNumberfireNCAAB_threedays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_threedays):
                    teamname = resultNumberfireNCAAB_threedays[g][265:275]
                    percent = resultNumberfireNCAAB_threedays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    projectedWinners.append(teamname)
                    projectedWinners.append(percent)
                    projectedWinners.append(str(threedays))
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    print("THREEDAYS Numberfire Loop Complete")
                    continue
        elif i == 4:
            url_fourdays = url_numberfire_NCAAB + str(fourdays)
            html_fourdays = requests.get(url_fourdays)
            soup_fourdays = bs4.BeautifulSoup(html_fourdays.content, features='html.parser') 
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_fourdays):
                i += 1
                continue
            scrapeNumberfireNCAAB_fourdays = soup_fourdays.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_fourdays):
                resultNumberfireNCAAB_fourdays.append(str(scrapeNumberfireNCAAB_fourdays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_fourdays):
                    teamname = resultNumberfireNCAAB_fourdays[g][265:275]
                    percent = resultNumberfireNCAAB_fourdays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    projectedWinners.append(teamname)
                    projectedWinners.append(percent)
                    projectedWinners.append(str(fourdays))
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    print("FOURDAYS Numberfire Loop Complete")
                    continue
        elif i == 5:
            url_fivedays = url_numberfire_NCAAB + str(fivedays)
            html_fivedays = requests.get(url_fivedays)
            soup_fivedays = bs4.BeautifulSoup(html_fivedays.content, features='html.parser')
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_fivedays):
                i += 1
                continue 
            scrapeNumberfireNCAAB_fivedays = soup_fivedays.findAll('div', attrs={'class':'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_fivedays):
                resultNumberfireNCAAB_fivedays.append(str(scrapeNumberfireNCAAB_fivedays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_fivedays):
                    teamname = resultNumberfireNCAAB_fivedays[g][265:275]
                    percent = resultNumberfireNCAAB_fivedays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    projectedWinners.append(teamname)
                    projectedWinners.append(percent)
                    projectedWinners.append(str(fivedays))
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    print("FIVEDAYS Numberfire Loop Complete")
                    continue
        else:
            break
    # print(projectedWinners)

    print('Numberfire Data Scraped')

    print('\n')
    for elem in projectedWinners:
        print('.' + str(elem) + '.')
    print('\n')
    
    # CHANGING NUMBERFIRE NAMES

    i = 0
    a = 0
    while True:
        if i < len(projectedWinners):
            if str(projectedWinners[i]) == 'ARIZ': 
                projectedWinners[i] = 'Arizona'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WIS': 
                projectedWinners[i] = 'Wisconsin'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UTAH': 
                projectedWinners[i] = 'Utah'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SMC': ##
                projectedWinners[i] = 'Saint Marys'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ASU': 
                projectedWinners[i] = 'Arizona State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UND': 
                projectedWinners[i] = 'North Dakota'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'PENN': ##
                projectedWinners[i] = 'Pennsylvania'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'VCU': 
                projectedWinners[i] = 'VCU'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'GTWN': 
                projectedWinners[i] = 'Georgetown'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'KU': 
                projectedWinners[i] = 'Kansas'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NMSU': 
                projectedWinners[i] = 'New Mexico State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MORE':
                projectedWinners[i] = 'Morehead State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'W&amp;M': 
                projectedWinners[i] = 'William & Mary'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'AMER':
                projectedWinners[i] = 'American'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UNCA': 
                projectedWinners[i] = 'UNC Asheville'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'FGCU': 
                projectedWinners[i] = 'FGCU'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LT': 
                projectedWinners[i] = 'Louisiana Tech'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'PV': 
                projectedWinners[i] = 'Prairie View'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NDSU': 
                projectedWinners[i] = 'North Dakota State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CSN': 
                projectedWinners[i] = 'CSUN'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'GB': 
                projectedWinners[i] = 'Green Bay'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'HAMP': 
                projectedWinners[i] = 'Hampton'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TENN': 
                projectedWinners[i] = 'Tennessee'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'PUR':
                projectedWinners[i] = 'Purdue'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'GCU': 
                projectedWinners[i] = 'Grand Canyon'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'GONZ': 
                projectedWinners[i] = 'Gonzaga'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LSU': 
                projectedWinners[i] = 'LSU'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ALA': 
                projectedWinners[i] = 'Alabama'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'USC': 
                projectedWinners[i] = 'USC'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'HOU':
                projectedWinners[i] = 'Houston'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BAY': 
                projectedWinners[i] = 'Baylor'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'DUKE': 
                projectedWinners[i] = 'Duke'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WYO': 
                projectedWinners[i] = 'Wyoming'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'AUB': 
                projectedWinners[i] = 'Auburn'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'VILL': 
                projectedWinners[i] = 'Villanova'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'IOWA': 
                projectedWinners[i] = 'Iowa'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TEX': 
                projectedWinners[i] = 'Texas'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CONN': 
                projectedWinners[i] = 'UConn'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'HALL': 
                projectedWinners[i] = 'Seton Hall'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MSU': 
                projectedWinners[i] = 'Michigan State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UCLA': 
                projectedWinners[i] = 'UCLA'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'VT': 
                projectedWinners[i] = 'Virginia Tech'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'FLA': 
                projectedWinners[i] = 'Florida'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BYU': ##
                projectedWinners[i] = 'BYU'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UK': 
                projectedWinners[i] = 'Kentucky'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'L-IL': ##
                projectedWinners[i] = 'Loyola Chicago'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MSST': 
                projectedWinners[i] = 'Mississippi State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UAB': 
                projectedWinners[i] = 'UAB'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'USU': 
                projectedWinners[i] = 'Utah State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UCI': ##
                projectedWinners[i] = 'UC Irvine'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SCU': 
                projectedWinners[i] = 'Santa Clara'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'MEM': 
                projectedWinners[i] = 'Memphis'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'XAV': 
                projectedWinners[i] = 'Xavier'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WSU': 
                projectedWinners[i] = 'Washington State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ISU': 
                projectedWinners[i] = 'Iowa State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CHAT': ##
                projectedWinners[i] = 'Chattanooga'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'DEP': 
                projectedWinners[i] = 'DePaul'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TTU': 
                projectedWinners[i] = 'Texas Tech'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SFNY': ##
                projectedWinners[i] = 'Saint Francis Brooklyn'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'OKLA': 
                projectedWinners[i] = 'Oklahoma'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WAG': ##
                projectedWinners[i] = 'Wagner'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MURR': 
                projectedWinners[i] = 'Murray State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'OKST': 
                projectedWinners[i] = 'Oklahoma State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CIN': 
                projectedWinners[i] = 'Cincinnati'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BEL': 
                projectedWinners[i] = 'Belmont'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'NW': 
                projectedWinners[i] = 'Northwestern'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LOU': 
                projectedWinners[i] = 'Louisville'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WICH': 
                projectedWinners[i] = 'Wichita State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'PROV': 
                projectedWinners[i] = 'Providence'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UVA': 
                projectedWinners[i] = 'Virginia'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'USA': 
                projectedWinners[i] = 'South Alabama'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MONM': 
                projectedWinners[i] = 'Monmouth'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NAVY': 
                projectedWinners[i] = 'Navy'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'IND': 
                projectedWinners[i] = 'Indiana'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'VAN': 
                projectedWinners[i] = 'Vanderbilt'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TA&M': 
                projectedWinners[i] = 'Texas A&M'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SDST': 
                projectedWinners[i] = 'South Dakota State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MICH': 
                projectedWinners[i] = 'Michigan'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'FSU': 
                projectedWinners[i] = 'Florida State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'IONA': 
                projectedWinners[i] = 'Iona'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'DAV': 
                projectedWinners[i] = 'Davidson'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'URI': 
                projectedWinners[i] = 'Rhode Island'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'OHIO': 
                projectedWinners[i] = 'Ohio'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SLU': 
                projectedWinners[i] = 'Saint Louis'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'DRKE': 
                projectedWinners[i] = 'Drake'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ILL': 
                projectedWinners[i] = 'Illinois'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'OAK': 
                projectedWinners[i] = 'Oakland'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WAKE': 
                projectedWinners[i] = 'Wake Forest'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NIAG': 
                projectedWinners[i] = 'Niagara'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LBSU': 
                projectedWinners[i] = 'Long Beach State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BSU': 
                projectedWinners[i] = 'Boise State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SDSU': 
                projectedWinners[i] = 'San Diego State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BUFF': ##
                projectedWinners[i] = 'Buffalo'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'FUR': 
                projectedWinners[i] = 'Furman'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TXST': ##
                projectedWinners[i] = 'Texas State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ACU': ##
                projectedWinners[i] = 'Abilene Christian'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UVU': ##
                projectedWinners[i] = 'Utah Valley'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WIU': ##
                projectedWinners[i] = 'Western Illinois'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CLEM': 
                projectedWinners[i] = 'Clemson'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'GMU': 
                projectedWinners[i] = 'George Mason'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'RICH': 
                projectedWinners[i] = 'Richmond'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WVU': 
                projectedWinners[i] = 'West Virginia'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SBON': ##
                projectedWinners[i] = 'Saint Bonaventure'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UNT': 
                projectedWinners[i] = 'North Texas'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MINN': 
                projectedWinners[i] = 'Minnesota'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'FRES': 
                projectedWinners[i] = 'Fresno State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UCF': 
                projectedWinners[i] = 'UCF'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'HOF': ##
                projectedWinners[i] = 'Hofstra'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'M-OH': ##
                projectedWinners[i] = 'Miami OH'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UVM': ##
                projectedWinners[i] = 'Vermont'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'MARQ': 
                projectedWinners[i] = 'Marquette'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'SJU': 
                projectedWinners[i] = 'Saint Johns'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'COR': 
                projectedWinners[i] = 'Cornell'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'NEV': 
                projectedWinners[i] = 'Nevada'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'CREI': 
                projectedWinners[i] = 'Creighton'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'MOSU': 
                projectedWinners[i] = 'Missouri State'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'OSU': 
                projectedWinners[i] = 'Ohio State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ND': 
                projectedWinners[i] = 'Notre Dame'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'DAY': 
                projectedWinners[i] = 'Dayton'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'PSU': 
                projectedWinners[i] = 'Penn State'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'TCU': 
                projectedWinners[i] = 'TCU'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'ORE': 
                projectedWinners[i] = 'Oregon'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'ETSU': 
                projectedWinners[i] = 'ETSU'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'CSF': 
                projectedWinners[i] = 'Cal State Fullerton'
                i += 1
                continue 
            elif str(projectedWinners[i]) == 'TOWS': 
                projectedWinners[i] = 'Towson'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'STAN': 
                projectedWinners[i] = 'Stanford'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'MTU': 
                projectedWinners[i] = 'Middle Tennessee'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'HAW': ##
                projectedWinners[i] = 'Hawaii'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'UMBC': 
                projectedWinners[i] = 'UMBC'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BC': 
                projectedWinners[i] = 'Boston College'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'TOL': ##
                projectedWinners[i] = 'Toledo'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'KSU': 
                projectedWinners[i] = 'Kansas State'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'UCSD': 
                projectedWinners[i] = 'UC San Diego'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'BU': 
                projectedWinners[i] = 'Boston University'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'MASS': 
                projectedWinners[i] = 'Massachusetts'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'COLG': 
                projectedWinners[i] = 'Colgate'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'UCSB': 
                projectedWinners[i] = 'UC Santa Barbara'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'COLO': 
                projectedWinners[i] = 'Colorado'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'SEA': 
                projectedWinners[i] = 'Seattle'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'RUTG': 
                projectedWinners[i] = 'Rutgers'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'GT': 
                projectedWinners[i] = 'Georgia Tech'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'SYR': 
                projectedWinners[i] = 'Syracuse'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'USD': ##
                projectedWinners[i] = 'San Diego'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'FIU': 
                projectedWinners[i] = 'FIU'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MISS': 
                projectedWinners[i] = 'Ole Miss'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NCST': 
                projectedWinners[i] = 'North Carolina State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SUU': 
                projectedWinners[i] = 'Southern Utah'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'GASO': ##
                projectedWinners[i] = 'Georgia Southern'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UNCO': 
                projectedWinners[i] = 'Northern Colorado'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LIB': 
                projectedWinners[i] = 'Liberty'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CAL': 
                projectedWinners[i] = 'California'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'YALE': 
                projectedWinners[i] = 'Yale'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WOF': 
                projectedWinners[i] = 'Wofford'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'HARV': 
                projectedWinners[i] = 'Harvard'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'PRIN': ##
                projectedWinners[i] = 'Princeton'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'JVST': ##
                projectedWinners[i] = 'Jacksonville State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CAMP': ##
                projectedWinners[i] = 'Campbell'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'COFC': 
                projectedWinners[i] = 'Charleston'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SCAR': 
                projectedWinners[i] = 'South Carolina'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WEBB': 
                projectedWinners[i] = 'Gardner-Webb'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'WEB': 
                projectedWinners[i] = 'Weber State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MIA': 
                projectedWinners[i] = 'Miami FL'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'KENT': 
                projectedWinners[i] = 'Kent State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MTST': 
                projectedWinners[i] = 'Montana State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UNH': ##
                projectedWinners[i] = 'New Hampshire'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UNM': 
                projectedWinners[i] = 'New Mexico'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WIN': ##
                projectedWinners[i] = 'Winthrop'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'STMN': ##
                projectedWinners[i] = 'Saint Thomas MN'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LIP': 
                projectedWinners[i] = 'Lipscomb'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UCRV': 
                projectedWinners[i] = 'UC Riverside'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'AMCC': 
                projectedWinners[i] = 'A&M-Corpus Christi'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CLEV': 
                projectedWinners[i] = 'Cleveland State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SFA': 
                projectedWinners[i] = 'SFA'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'DEL': 
                projectedWinners[i] = 'Delaware'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TAR': 
                projectedWinners[i] = 'Tarleton State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TEM': #
                projectedWinners[i] = 'Temple'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'JOES': 
                projectedWinners[i] = 'Saint Josephs'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'DREX': 
                projectedWinners[i] = 'Drexel'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UGA': 
                projectedWinners[i] = 'Georgia'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'APP': ##
                projectedWinners[i] = 'Appalachian State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'GAST': 
                projectedWinners[i] = 'Georgia State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TNTC': ##
                projectedWinners[i] = 'Tennessee Tech'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SMU': 
                projectedWinners[i] = 'SMU'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UNCG': 
                projectedWinners[i] = 'UNC Greensboro'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NE': 
                projectedWinners[i] = 'Northeastern'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'FOR': 
                projectedWinners[i] = 'Fordham'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MRSH': 
                projectedWinners[i] = 'Marshall'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UTEP': 
                projectedWinners[i] = 'UTEP'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'FAIR': 
                projectedWinners[i] = 'Fairfield'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CIT': ##
                projectedWinners[i] = 'Citadel'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SFPA': 
                projectedWinners[i] = 'Saint Francis PA'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'INST': ##
                projectedWinners[i] = 'Indiana State'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'BUT': 
                projectedWinners[i] = 'Butler'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NEB': 
                projectedWinners[i] = 'Nebraska'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'JMU': ##
                projectedWinners[i] = 'James Madison'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ECU': 
                projectedWinners[i] = 'East Carolina'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WKU': 
                projectedWinners[i] = 'Western Kentucky'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'RICE': ##
                projectedWinners[i] = 'Rice'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CBU': 
                projectedWinners[i] = 'California Baptist'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ALCN': 
                projectedWinners[i] = 'Alcorn'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'DET': ##
                projectedWinners[i] = 'Detroit Mercy'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'EWU': 
                projectedWinners[i] = 'Eastern Washington'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CCAR': 
                projectedWinners[i] = 'Coastal Carolina'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UML': 
                projectedWinners[i] = 'UMass Lowell'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'EKY': 
                projectedWinners[i] = 'Eastern Kentucky'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'SIU': 
                projectedWinners[i] = 'Southern Illinois'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'JAC': 
                projectedWinners[i] = 'Jacksonville'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BRWN': 
                projectedWinners[i] = 'Brown'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'UNI': 
                projectedWinners[i] = 'UNI'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UCD': 
                projectedWinners[i] = 'UC Davis'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'YSU': 
                projectedWinners[i] = 'Youngstown State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LONG': ##
                projectedWinners[i] = 'Longwood'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'EMU': ##
                projectedWinners[i] = 'Eastern Michigan'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CSB': 
                projectedWinners[i] = 'CSU Bakersfield'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'PORT': 
                projectedWinners[i] = 'Portland'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'VALP': 
                projectedWinners[i] = 'Valparaiso'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WASH': 
                projectedWinners[i] = 'Washington'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'STON': 
                projectedWinners[i] = 'Stony Brook'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BALL': ##
                projectedWinners[i] = 'Ball State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UIC': 
                projectedWinners[i] = 'UIC'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MAN': 
                projectedWinners[i] = 'Manhattan'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'PAC': 
                projectedWinners[i] = 'Pacific'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'DART': 
                projectedWinners[i] = 'Dartmouth'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'DEN': 
                projectedWinners[i] = 'Denver'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UMES': 
                projectedWinners[i] = 'UMES'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SAM': ##
                projectedWinners[i] = 'Samford'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SJSU': 
                projectedWinners[i] = 'San Jose State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NKU': 
                projectedWinners[i] = 'Northern Kentucky'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TLSA': 
                projectedWinners[i] = 'Tulsa'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TRGV': 
                projectedWinners[i] = 'UTRGV'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MRMK': 
                projectedWinners[i] = 'Merrimack'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TULN': 
                projectedWinners[i] = 'Tulane'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BELL': ##
                projectedWinners[i] = 'Bellarmine'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UNLV': 
                projectedWinners[i] = 'UNLV'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'NICH': ##
                projectedWinners[i] = 'Nicholls State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SPC': 
                projectedWinners[i] = 'Saint Peters'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'AKR': 
                projectedWinners[i] = 'Akron'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'MER': ##
                projectedWinners[i] = 'Mercer'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'NJIT': 
                projectedWinners[i] = 'NJIT'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'CHAR': 
                projectedWinners[i] = 'Charlotte'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'UMKC': 
                projectedWinners[i] = 'Kansas City'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'ORST': 
                projectedWinners[i] = 'Oregon State'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'ILST': ##
                projectedWinners[i] = 'Illinois State'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'AFA': 
                projectedWinners[i] = 'Air Force'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'KENN': ##
                projectedWinners[i] = 'Kennesaw State'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'RAD': ##
                projectedWinners[i] = 'Radford'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'LMU': 
                projectedWinners[i] = 'LMU'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'L-MD': ##
                projectedWinners[i] = 'Loyola Maryland'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'MD': 
                projectedWinners[i] = 'Maryland'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'UTA': 
                projectedWinners[i] = 'UT Arlington'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'UNA': 
                projectedWinners[i] = 'North Alabama'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'USF': 
                projectedWinners[i] = 'South Florida'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'SF': 
                projectedWinners[i] = 'San Francisco'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ORU': 
                projectedWinners[i] = 'Oral Roberts'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'NORF': ##
                projectedWinners[i] = 'Norfolk State'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'HOW': ##
                projectedWinners[i] = 'Howard'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'TROY': #
                projectedWinners[i] = 'Troy'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'ULM': 
                projectedWinners[i] = 'ULM'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'SIUE': 
                projectedWinners[i] = 'SIUE'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'COPP': 
                projectedWinners[i] = 'Coppin State'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'NAU': 
                projectedWinners[i] = 'Northern Arizona'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'TXSO': 
                projectedWinners[i] = 'Texas Southern'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'FAU': ##
                projectedWinners[i] = 'Florida Atlantic'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'PEAY': 
                projectedWinners[i] = 'Austin Peay'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'BGSU': ##
                projectedWinners[i] = 'Bowling Green'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'MONT': 
                projectedWinners[i] = 'Montana'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'DXST': ##
                projectedWinners[i] = 'Dixie State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'HP': 
                projectedWinners[i] = 'High Point'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'HART': 
                projectedWinners[i] = 'Hartford'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NCAT': 
                projectedWinners[i] = 'North Carolina A&T'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ARMY': 
                projectedWinners[i] = 'Army West Point'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SHSU': 
                projectedWinners[i] = 'Sam Houston'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BRAD': ##
                projectedWinners[i] = 'Bradley'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'DUQ': 
                projectedWinners[i] = 'Duquesne'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BRY': ##
                projectedWinners[i] = 'Bryant'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'GW': ##
                projectedWinners[i] = 'George Washington'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NEW': ##
                projectedWinners[i] = 'New Orleans'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'PRE': ##
                projectedWinners[i] = 'Presbyterian'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LIU': 
                projectedWinners[i] = 'LIU'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MIZZ': 
                projectedWinners[i] = 'Missouri'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ODU': 
                projectedWinners[i] = 'Old Dominion'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ARST': 
                projectedWinners[i] = 'Arkansas State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'PITT': 
                projectedWinners[i] = 'Pittsburgh'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CAN': 
                projectedWinners[i] = 'Canisius'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UNF': ##
                projectedWinners[i] = 'North Florida'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MRST': ##
                projectedWinners[i] = 'Marist'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'EVAN': ##
                projectedWinners[i] = 'Evansville'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WCU': ##
                projectedWinners[i] = 'Western Carolina'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ULL': 
                projectedWinners[i] = 'Louisiana-Lafayette'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'PEPP': 
                projectedWinners[i] = 'Pepperdine'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SOU': 
                projectedWinners[i] = 'Southern University'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CSUS': ##
                projectedWinners[i] = 'Sacramento State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SHU': 
                projectedWinners[i] = 'Sacred Heart'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NCCU': 
                projectedWinners[i] = 'North Carolina Central'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WRST': 
                projectedWinners[i] = 'Wright State'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'BING': ##
                projectedWinners[i] = 'Binghamton'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ALST': ##
                projectedWinners[i] = 'Alabama State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LAF': 
                projectedWinners[i] = 'Lafayette'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LEH': ##
                projectedWinners[i] = 'Lehigh'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SEMO': ##
                projectedWinners[i] = 'Southeast Missouri State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'RID': 
                projectedWinners[i] = 'Rider'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UTSA': 
                projectedWinners[i] = 'UTSA'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SDAK': ##
                projectedWinners[i] = 'South Dakota'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MSM': 
                projectedWinners[i] = 'Mount Saint Marys'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'JKST': 
                projectedWinners[i] = 'Jackson State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'RMU': 
                projectedWinners[i] = 'Robert Morris'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MCNS': 
                projectedWinners[i] = 'McNeese'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'STET': 
                projectedWinners[i] = 'Stetson'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LAS': 
                projectedWinners[i] = 'La Salle'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'VMI': 
                projectedWinners[i] = 'VMI'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MILW': 
                projectedWinners[i] = 'Milwaukee'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'COOK': 
                projectedWinners[i] = 'Bethune-Cookman'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'WMU': #
                projectedWinners[i] = 'Western Michigan'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'FDU': 
                projectedWinners[i] = 'Fairleigh Dickinson'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'GRAM': 
                projectedWinners[i] = 'Grambling'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'SCUS': 
                projectedWinners[i] = 'USC Upstate'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UNCW' == str(projectedWinners[i]): 
                projectedWinners[i] = 'UNCW'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UNC': 
                projectedWinners[i] = 'North Carolina'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CP': ##
                projectedWinners[i] = 'Cal Poly'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'LAM': 
                projectedWinners[i] = 'Lamar'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'FAMU': 
                projectedWinners[i] = 'Florida A&M'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ELON': 
                projectedWinners[i] = 'Elon'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UTM': 
                projectedWinners[i] = 'UT Martin'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'USM': 
                projectedWinners[i] = 'Southern Mississippi'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'QUIN': 
                projectedWinners[i] = 'Quinnipiac'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'BUCK': ##
                projectedWinners[i] = 'Bucknell'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'HBU': ##
                projectedWinners[i] = 'Houston Baptist'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'PRST': 
                projectedWinners[i] = 'Portland State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ARPB': 
                projectedWinners[i] = 'Arkansas-Pine Bluff'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NIU': ##
                projectedWinners[i] = 'Northern Illinois'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MORG': ##
                projectedWinners[i] = 'Morgan State'
                i += 3
                continue 
            elif str(projectedWinners[i]) == 'SIE': 
                projectedWinners[i] = 'Siena'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CMU': ##
                projectedWinners[i] = 'Central Michigan'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'UALR': 
                projectedWinners[i] = 'Little Rock'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'IPFW': 
                projectedWinners[i] = 'Purdue Fort Wayne'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ALBY': ##
                projectedWinners[i] = 'Albany NY'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'IW': ##
                projectedWinners[i] = 'Incarnate Word'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NEOM': 
                projectedWinners[i] = 'Omaha'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SELA': 
                projectedWinners[i] = 'Southeastern Louisiana'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'AAMU': 
                projectedWinners[i] = 'Alabama A&M'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'TNST': ##
                projectedWinners[i] = 'Tennessee State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'SCST': 
                projectedWinners[i] = 'South Carolina State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'NWST': 
                projectedWinners[i] = 'Northwestern State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'IUPU': 
                projectedWinners[i] = 'IUPUI'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CCSU': 
                projectedWinners[i] = 'Central Connecticut State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CSU': 
                projectedWinners[i] = 'Colorado State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CARK': ##
                projectedWinners[i] = 'Central Arkansas'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ARK': 
                projectedWinners[i] = 'Arkansas'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CLMB': 
                projectedWinners[i] = 'Columbia'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'IDHO': 
                projectedWinners[i] = 'Idaho'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'IDST': 
                projectedWinners[i] = 'Idaho State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CHSO': 
                projectedWinners[i] = 'Charleston Southern'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'CHS': 
                projectedWinners[i] = 'Chicago State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'MVSU': 
                projectedWinners[i] = 'Mississippi Valley'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'EIU': 
                projectedWinners[i] = 'Eastern Illinois'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'HC': ##
                projectedWinners[i] = 'Holy Cross'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'DSU': 
                projectedWinners[i] = 'Delaware State'
                i += 3
                continue
            elif str(projectedWinners[i]) == 'ME': 
                projectedWinners[i] = 'Maine'
                i += 3
                continue
            else:
                i += 1
                continue
        else:
            break
    # print('\n')
    print('List of Numberfire Projected Winners Generated')

    # for elem in projectedWinners:
    #     print(elem)

    # print('\n')
    # CREATE ORGANIZED LIST OF NUMBERFIRE CHANCES
    x = 3
    numberfireChances = [projectedWinners[i:i+x] for i in range(0, len(projectedWinners), x)]
    print(numberfireChances)

    i = 0
    n = 0
    while True:
        if i < len(matchupAnalysis_NCAAB):
            h = i + 1
            if str(matchupAnalysis_NCAAB[i][0]) not in projectedWinners:
                if str(matchupAnalysis_NCAAB[h][0]) not in projectedWinners:
                    del matchupAnalysis_NCAAB[h]
                    del matchupAnalysis_NCAAB[i]
                    continue
                else:
                    y = projectedWinners.index(matchupAnalysis_NCAAB[h][0])
                    winnerIndex = y
                    winnerChanceIndex = y + 1
                    gameDay = y + 2
                    awayChance = float(100) - float(projectedWinners[winnerChanceIndex])
                    awayChance = round(awayChance, 1)
                    matchupAnalysis_NCAAB[i].append(awayChance)
                    matchupAnalysis_NCAAB[h].append(projectedWinners[winnerChanceIndex])
                    matchupAnalysis_NCAAB[i].append(projectedWinners[gameDay])
                    matchupAnalysis_NCAAB[h].append(projectedWinners[gameDay])
                    del projectedWinners[y:y+2]
                    i += 2
                    continue
            elif str(matchupAnalysis_NCAAB[h][0]) not in projectedWinners:
                if str(matchupAnalysis_NCAAB[i][0]) not in projectedWinners:
                    del matchupAnalysis_NCAAB[h]
                    del matchupAnalysis_NCAAB[i]
                    continue
                else:
                    x = projectedWinners.index(matchupAnalysis_NCAAB[i][0])
                    winnerIndex = x
                    winnerChanceIndex = x + 1
                    gameDay = x + 2
                    homeChance = float(100) - float(projectedWinners[winnerChanceIndex])
                    homeChance = round(homeChance, 1)
                    matchupAnalysis_NCAAB[h].append(homeChance)
                    matchupAnalysis_NCAAB[i].append(projectedWinners[winnerChanceIndex])
                    matchupAnalysis_NCAAB[i].append(projectedWinners[gameDay])
                    matchupAnalysis_NCAAB[h].append(projectedWinners[gameDay])
                    del projectedWinners[x:x+2]
                    i += 2
                    continue
            elif projectedWinners.index(matchupAnalysis_NCAAB[i][0]) < projectedWinners.index(matchupAnalysis_NCAAB[h][0]):
                x = projectedWinners.index(matchupAnalysis_NCAAB[i][0])
                winnerIndex = x
                winnerChanceIndex = x + 1
                gameDay = x + 2
                homeChance = float(100) - float(projectedWinners[winnerChanceIndex])
                homeChance = round(homeChance, 1)
                matchupAnalysis_NCAAB[h].append(homeChance)
                matchupAnalysis_NCAAB[i].append(projectedWinners[winnerChanceIndex])
                matchupAnalysis_NCAAB[i].append(projectedWinners[gameDay])
                matchupAnalysis_NCAAB[h].append(projectedWinners[gameDay])
                del projectedWinners[x:x+2]
                i += 2
                continue
            elif projectedWinners.index(matchupAnalysis_NCAAB[h][0]) < projectedWinners.index(matchupAnalysis_NCAAB[i][0]):
                y = projectedWinners.index(matchupAnalysis_NCAAB[h][0])
                winnerIndex = y
                winnerChanceIndex = y + 1
                gameDay = y + 2
                awayChance = float(100) - float(projectedWinners[winnerChanceIndex])
                awayChance = round(awayChance, 1)
                matchupAnalysis_NCAAB[i].append(awayChance)
                matchupAnalysis_NCAAB[h].append(projectedWinners[winnerChanceIndex])
                matchupAnalysis_NCAAB[i].append(projectedWinners[gameDay])
                matchupAnalysis_NCAAB[h].append(projectedWinners[gameDay])
                del projectedWinners[y:y+2]
                i += 2
                continue
        else:
            break    
    # print('\n')
    # for elem in matchupAnalysis_NCAAB:
    #     print(elem)

    # SCRAPING ESPN CHANCES

    today = date.today()
    tomorrow = today + timedelta(1)
    twodays = today + timedelta(2)
    threedays = today + timedelta(3)
    fourdays = today + timedelta(4)
    fivedays = today + timedelta(5)
    today = today.strftime("%Y%m%d")
    tomorrow = tomorrow.strftime("%Y%m%d")
    twodays = twodays.strftime("%Y%m%d")
    threedays = threedays.strftime("%Y%m%d")
    fourdays = fourdays.strftime("%Y%m%d")
    fivedays = fivedays.strftime("%Y%m%d")
    days = [today, tomorrow, twodays, threedays, fourdays, fivedays]

    espn_data = []
    i = 0
    while True:
        if i < len(days):
            day = days[i]
            url_espn = 'http://www.espn.com/mens-college-basketball/bpi/_/view/predictions/group/50/date/' + str(day)
            html_espn = requests.get(url_espn)
            soup_espn = bs4.BeautifulSoup(html_espn.content, features='html.parser')
            if 'No games on this date.' in str(soup_espn):
                i += 1
                continue
            else:
                df_espn = pd.read_html('http://www.espn.com/mens-college-basketball/bpi/_/view/predictions/group/50/date/' + str(day))
                espn_data += df_espn[0].values.tolist()
                i += 1
                continue
        else:
            break

    for elem in espn_data:
        print(elem)

    i = 0
    j = i + 1
    while True:
        if i < len(espn_data):
            if len(espn_data[i]) > 3:
                if str(espn_data[i][0]) == 'PAC12':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ESPN':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEESPN':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ESPNN':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ACCNX':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEACCNX':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ESPN/ESPN3':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'FOX': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ESPNU/ESPN+': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEFOX': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEPAC12':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'truTV':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEtruTV':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'SECN+/ESPN+': 
                    del espn_data[i][0]
                    continue 
                elif str(espn_data[i][0]) == 'ESPNU/ESPN3': 
                    del espn_data[i][0]
                    continue 
                elif str(espn_data[i][0]) == 'ACCNX/ESPN+':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'Final':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'Final/OT':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEESPN2':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ESPN2/ESPNU': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ESPN2':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'nan':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'FS1':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ESPN+':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEFS1':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ACCN/ACCNX':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ACCN':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'TNT':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'TBS':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVETNT':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVETBS':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LHN': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEACCN':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVECBSSN':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'CBSSN':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'CBS':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVECBS':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'BTN':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEBTN':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEESPN+':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ESPN3':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'SECN/ESPN+':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'USA Net': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEESPNU':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'Canceled':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ESPNU': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'SECN+': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'FS2':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEFS2':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEESPN3':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'BIG12|ESPN+':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'SECN':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ABC':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVESECN':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'ESPN2/ESPN3':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVE':
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'Postponed': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVELHN': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEACCN/ESPN+': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVEBIG12|ESPN+': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'LIVESECN+/ESPN+': 
                    del espn_data[i][0]
                    continue
                elif str(espn_data[i][0]) == 'Forfeit': 
                    del espn_data[i]
                    continue
                elif str(espn_data[i][0]) == 'Canceled': 
                    del espn_data[i]
                    continue
                elif type(espn_data[i][1]) is float:
                    del espn_data[i][1]
                    continue
                elif str(espn_data[i][1][-1]) != '%':
                    del espn_data[i][1]
                    continue
                elif str(espn_data[i][1][-1]) == '%':
                    del espn_data[i][2:]
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
        if i < len(espn_data):
            if len(espn_data[i]) == 3:
                del espn_data[i][1:]
                i += 1
                continue
            else:
                i += 1
                continue
        else:
            break
        
    i = 0
    while True:
        if i < len(espn_data):
            name = espn_data[i][0]
            if name[-1] == '-':
                name = name[0:-1]
                espn_data[i][0] = name
                continue
            elif name[-1] == '0':
                name = name[0:-1]
                espn_data[i][0] = name
                continue
            elif name[-1] == '1':
                name = name[0:-1]
                espn_data[i][0] = name
                continue
            elif name[-1] == '2':
                name = name[0:-1]
                espn_data[i][0] = name
                continue
            elif name[-1] == '3':
                name = name[0:-1]
                espn_data[i][0] = name
                continue
            elif name[-1] == '4':
                name = name[0:-1]
                espn_data[i][0] = name
                continue
            elif name[-1] == '5':
                name = name[0:-1]
                espn_data[i][0] = name
                continue
            elif name[-1] == '6':
                name = name[0:-1]
                espn_data[i][0] = name
                continue
            elif name[-1] == '7':
                name = name[0:-1]
                espn_data[i][0] = name
                continue
            elif name[-1] == '8':
                name = name[0:-1]
                espn_data[i][0] = name
                continue
            elif name[-1] == '9':
                name = name[0:-1]
                espn_data[i][0] = name
                continue
            else:
                i += 1
                continue
        else:
            break
        
    print('\n')
    print('\n')
    for elem in espn_data:
        print(elem)
    print('\n')
    print('\n')
            
    i = 0
    while True:
        if i < len(espn_data):
            if len(espn_data[i]) == 2:
                chance = espn_data[i][1][0:-1]
                chance = float(chance)
                chance = round(chance, 2)
                espn_data[i][1] = chance
                if i == 0 or i % 2 == 0:
                    o = i + 1
                    opp_chance = float(100) - chance
                    opp_chance = round(opp_chance, 2)
                    espn_data[o].append(opp_chance)
                    i += 2
                    continue
                else:
                    o = i - 1
                    opp_chance = float(100) - chance
                    opp_chance = round(opp_chance, 2)
                    espn_data[o].append(opp_chance)
                    i += 1
                    continue
            else:
                i += 1
                continue
        else:
            break

    # print('\n')
    # print('\n')
    # for elem in espn_data:
    #     print(elem)
    # print('\n')
    # print('\n')
        
    i = 0
    a = 0
    while True:
        if i < len(espn_data):
            if str(espn_data[i][0]) == 'ArizonaARIZ': 
                espn_data[i][0] = 'Arizona'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Grand CanyonGCU': 
                espn_data[i][0] = 'Grand Canyon'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'UMBCUMBC': 
                espn_data[i][0] = 'UMBC'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'MarshallMRSH': 
                espn_data[i][0] = 'Marshall'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'South AlabamaUSA': 
                espn_data[i][0] = 'South Alabama'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'North DakotaUND': 
                espn_data[i][0] = 'North Dakota'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'IndianaIU': 
                espn_data[i][0] = 'Indiana'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'KentuckyUK': 
                espn_data[i][0] = 'Kentucky'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Texas TechTTU': 
                espn_data[i][0] = 'Texas Tech'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'South DakotaSDAK': 
                espn_data[i][0] = 'South Dakota'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Tennessee StateTNST': 
                espn_data[i][0] = 'Tennessee State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Northern ArizonaNAU': 
                espn_data[i][0] = 'Northern Arizona'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'AuburnAUB': 
                espn_data[i][0] = 'Auburn'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Rhode IslandURI': 
                espn_data[i][0] = 'Rhode Island'
                i += 1
                continue 
            elif str(espn_data[i][0]) == "Saint Mary'sSMC": 
                espn_data[i][0] = 'Saint Marys'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'RiderRID': 
                espn_data[i][0] = 'Rider'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Mississippi StateMSST': 
                espn_data[i][0] = 'Mississippi State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'MaineMAINE': 
                espn_data[i][0] = 'Maine'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'MerrimackMRMK': 
                espn_data[i][0] = 'Merrimack'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'NebraskaNEB': 
                espn_data[i][0] = 'Nebraska'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'DePaulDEP': 
                espn_data[i][0] = 'DePaul'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'PennsylvaniaPENN': 
                espn_data[i][0] = 'Pennsylvania'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'UtahUTAH': 
                espn_data[i][0] = 'Utah'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'DukeDUKE': 
                espn_data[i][0] = 'Duke'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'UT Rio Grande ValleyRGV': 
                espn_data[i][0] = 'UTRGV'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Texas SouthernTXSO': 
                espn_data[i][0] = 'Texas Southern'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Charleston SouthernCHSO': 
                espn_data[i][0] = 'Charleston Southern'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'North Dakota StateNDSU': 
                espn_data[i][0] = 'North Dakota State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'CharlotteCLT': 
                espn_data[i][0] = 'Charlotte'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'American UniversityAMER': 
                espn_data[i][0] = 'American'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'South FloridaUSF': 
                espn_data[i][0] = 'South Florida'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'CreightonCREI': 
                espn_data[i][0] = 'Creighton'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'WisconsinWISC': 
                espn_data[i][0] = 'Wisconsin'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'North CarolinaUNC': 
                espn_data[i][0] = 'North Carolina'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Eastern WashingtonEWU': 
                espn_data[i][0] = 'Eastern Washington'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'HarvardHARV': 
                espn_data[i][0] = 'Harvard'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Southern UtahSUU': 
                espn_data[i][0] = 'Southern Utah'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UNC GreensboroUNCG': 
                espn_data[i][0] = 'UNC Greensboro'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'North Carolina CentralNCCU': 
                espn_data[i][0] = 'North Carolina Central'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'MemphisMEM': 
                espn_data[i][0] = 'Memphis'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'UC DavisUCD': 
                espn_data[i][0] = 'UC Davis'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Gardner-WebbGWEB': 
                espn_data[i][0] = 'Gardner-Webb'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'UABUAB': 
                espn_data[i][0] = 'UAB'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'LSULSU': 
                espn_data[i][0] = 'LSU'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'South Carolina StateSCST': 
                espn_data[i][0] = 'South Carolina State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'HoustonHOU':
                espn_data[i][0] = 'Houston'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'MonmouthMONM': 
                espn_data[i][0] = 'Monmouth'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Wake ForestWAKE': 
                espn_data[i][0] = 'Wake Forest'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'BrownBRWN':
                espn_data[i][0] = 'Brown'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'UC IrvineUCI': 
                espn_data[i][0] = 'UC Irvine'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'RutgersRUTG': 
                espn_data[i][0] = 'Rutgers'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Utah StateUSU': 
                espn_data[i][0] = 'Utah State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Austin PeayAPSU': 
                espn_data[i][0] = 'Austin Peay'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Seton HallHALL': 
                espn_data[i][0] = 'Seton Hall'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'VCUVCU': 
                espn_data[i][0] = 'VCU'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'ClemsonCLEM': 
                espn_data[i][0] = 'Clemson'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'TroyTROY': 
                espn_data[i][0] = 'Troy'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'PurduePUR':
                espn_data[i][0] = 'Purdue'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Montana StateMTST': 
                espn_data[i][0] = 'Montana State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Michigan StateMSU': 
                espn_data[i][0] = 'Michigan State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'ColumbiaCLMB': 
                espn_data[i][0] = 'Columbia'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'East Tennessee StateETSU': 
                espn_data[i][0] = 'ETSU'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'AlabamaALA': 
                espn_data[i][0] = 'Alabama'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'BaylorBAY': 
                espn_data[i][0] = 'Baylor'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Seattle USEA': 
                espn_data[i][0] = 'Seattle'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'USCUSC': 
                espn_data[i][0] = 'USC'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Ohio StateOSU': 
                espn_data[i][0] = 'Ohio State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'St. Francis (PA)SFPA': 
                espn_data[i][0] = 'Saint Francis PA'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'ProvidencePROV': 
                espn_data[i][0] = 'Providence'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Wichita StateWICH': 
                espn_data[i][0] = 'Wichita State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Louisiana TechLT': 
                espn_data[i][0] = 'Louisiana Tech'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'FloridaFLA': 
                espn_data[i][0] = 'Florida'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'LouisvilleLOU': 
                espn_data[i][0] = 'Louisville'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Florida StateFSU': 
                espn_data[i][0] = 'Florida State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Stony BrookSTBK': 
                espn_data[i][0] = 'Stony Brook'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Incarnate WordUIW': 
                espn_data[i][0] = 'UIW'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'South Dakota StateSDST': 
                espn_data[i][0] = 'South Dakota State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Santa ClaraSCU':
                espn_data[i][0] = 'Santa Clara'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Virginia TechVT': 
                espn_data[i][0] = 'Virginia Tech'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'HamptonHAMP': ##
                espn_data[i][0] = 'Hampton'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UC San DiegoUCSD': 
                espn_data[i][0] = 'UC San Diego'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'GramblingGRAM': 
                espn_data[i][0] = 'Grambling'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'OregonORE': 
                espn_data[i][0] = 'Oregon'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Indiana StateINST': 
                espn_data[i][0] = 'Indiana State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'JacksonvilleJAX': 
                espn_data[i][0] = 'Jacksonville'
                i += 1
                continue
            elif str(espn_data[i][0]) == "Mount St. Mary'sMSM": 
                espn_data[i][0] = 'Mount Saint Marys'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'CaliforniaCAL': 
                espn_data[i][0] = 'California'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Missouri StateMOST':
                espn_data[i][0] = 'Missouri State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Central ConnecticutCCSU': 
                espn_data[i][0] = 'Central Connecticut State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UICUIC': 
                espn_data[i][0] = 'UIC'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'PacificPAC': 
                espn_data[i][0] = 'Pacific'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'New Mexico StateNMSU': 
                espn_data[i][0] = 'New Mexico State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'North TexasUNT': 
                espn_data[i][0] = 'North Texas'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'LafayetteLAF': 
                espn_data[i][0] = 'Lafayette'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Georgia StateGAST': 
                espn_data[i][0] = 'Georgia State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Alcorn StateALCN': 
                espn_data[i][0] = 'Alcorn'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'UC RiversideUCR': 
                espn_data[i][0] = 'UC Riverside'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'XavierXAV': 
                espn_data[i][0] = 'Xavier'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'North AlabamaUNA': 
                espn_data[i][0] = 'North Alabama'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'CincinnatiCIN': 
                espn_data[i][0] = 'Cincinnati'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Alabama StateALST': 
                espn_data[i][0] = 'Alabama State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'LamarLAM': 
                espn_data[i][0] = 'Lamar'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'FurmanFUR': 
                espn_data[i][0] = 'Furman'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'DavidsonDAV': 
                espn_data[i][0] = 'Davidson'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'McNeeseMCNS':
                espn_data[i][0] = 'McNeese'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'OhioOHIO': 
                espn_data[i][0] = 'Ohio'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'TowsonTOW': 
                espn_data[i][0] = 'Towson'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'HartfordHART': 
                espn_data[i][0] = 'Hartford'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'FairfieldFAIR': 
                espn_data[i][0] = 'Fairfield'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UCFUCF': 
                espn_data[i][0] = 'UCF'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'West VirginiaWVU': 
                espn_data[i][0] = 'West Virginia'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Boise StateBSU': 
                espn_data[i][0] = 'Boise State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Kansas StateKSU': 
                espn_data[i][0] = 'Kansas State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'California BaptistCBU': 
                espn_data[i][0] = 'California Baptist'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'StanfordSTAN': 
                espn_data[i][0] = 'Stanford'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'SE LouisianaSELA': 
                espn_data[i][0] = 'Southeastern Louisiana'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Little RockUALR':
                espn_data[i][0] = 'Little Rock'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Penn StatePSU': 
                espn_data[i][0] = 'Penn State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'New MexicoUNM': 
                espn_data[i][0] = 'New Mexico'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Houston BaptistHBU': 
                espn_data[i][0] = 'Houston Baptist'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'CSU NorthridgeCSUN': 
                espn_data[i][0] = 'CSUN'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Arkansas-Pine BluffUAPB': 
                espn_data[i][0] = 'Arkansas-Pine Bluff'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Northern IowaUNI': 
                espn_data[i][0] = 'UNI'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'MinnesotaMINN': 
                espn_data[i][0] = 'Minnesota'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'VillanovaVILL': 
                espn_data[i][0] = 'Villanova'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'DenverDEN': 
                espn_data[i][0] = 'Denver'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'ArkansasARK': 
                espn_data[i][0] = 'Arkansas'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Coastal CarolinaCCU': 
                espn_data[i][0] = 'Coastal Carolina'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Chicago StateCHIC': 
                espn_data[i][0] = 'Chicago State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Kent StateKENT': 
                espn_data[i][0] = 'Kent State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Coppin StateCOPP': 
                espn_data[i][0] = 'Coppin State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'PittsburghPITT': 
                espn_data[i][0] = 'Pittsburgh'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Alabama A&MAAMU': 
                espn_data[i][0] = 'Alabama A&M'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'DrexelDREX': 
                espn_data[i][0] = 'Drexel'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Illinois StateILST': 
                espn_data[i][0] = 'Illinois State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Oregon StateORST': 
                espn_data[i][0] = 'Oregon State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Arizona StateASU': 
                espn_data[i][0] = 'Arizona State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Kansas CityKC': 
                espn_data[i][0] = 'Kansas City'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Sam HoustonSHSU': 
                espn_data[i][0] = 'Sam Houston'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'YaleYALE': 
                espn_data[i][0] = 'Yale'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'MarylandMD': 
                espn_data[i][0] = 'Maryland'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'SyracuseSYR': 
                espn_data[i][0] = 'Syracuse'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'GeorgetownGTWN': 
                espn_data[i][0] = 'Georgetown'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Fresno StateFRES': 
                espn_data[i][0] = 'Fresno State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'VMIVMI': 
                espn_data[i][0] = 'VMI'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'CSU BakersfieldCSUB': 
                espn_data[i][0] = 'CSU Bakersfield'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'DaytonDAY': 
                espn_data[i][0] = 'Dayton'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'NC StateNCST':
                espn_data[i][0] = 'North Carolina State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Mississippi Valley StateMVSU': 
                espn_data[i][0] = 'Mississippi Valley'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'StetsonSTET': 
                espn_data[i][0] = 'Stetson'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'FordhamFOR': 
                espn_data[i][0] = 'Fordham'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UMass LowellUML': 
                espn_data[i][0] = 'UMass Lowell'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'South Carolina UpstateSCUP': 
                espn_data[i][0] = 'USC Upstate'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UTSAUTSA': 
                espn_data[i][0] = 'UTSA'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Central ArkansasCARK': 
                espn_data[i][0] = 'Central Arkansas'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Jackson StateJKST': 
                espn_data[i][0] = 'Jackson State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'LibertyLIB': 
                espn_data[i][0] = 'Liberty'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Ole MissMISS': 
                espn_data[i][0] = 'Ole Miss'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Robert MorrisRMU': 
                espn_data[i][0] = 'Robert Morris'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Northwestern StateNWST': 
                espn_data[i][0] = 'Northwestern State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'ButlerBUT': 
                espn_data[i][0] = 'Butler'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Arkansas StateARST':
                espn_data[i][0] = 'Arkansas State'
                i += 1
                continue
            elif str(espn_data[i][0]) == "St. John'sSJU": 
                espn_data[i][0] = 'Saint Johns'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Florida Gulf CoastFGCU': 
                espn_data[i][0] = 'FGCU'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Long Beach StateLBSU': 
                espn_data[i][0] = 'Long Beach State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Florida A&MFAMU': 
                espn_data[i][0] = 'Florida A&M'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Middle TennesseeMTSU': 
                espn_data[i][0] = 'Middle Tennessee'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Western CarolinaWCU': 
                espn_data[i][0] = 'Western Carolina'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Old DominionODU': 
                espn_data[i][0] = 'Old Dominion'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'New OrleansUNO': 
                espn_data[i][0] = 'New Orleans'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'SIU EdwardsvilleSIUE': 
                espn_data[i][0] = 'SIUE'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'PrincetonPRIN': ##
                espn_data[i][0] = 'Princeton'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Southeast Missouri StateSEMO': 
                espn_data[i][0] = 'Southeast Missouri State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Prairie View A&MPV':
                espn_data[i][0] = 'Prairie View'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Boston UniversityBU': 
                espn_data[i][0] = 'Boston University'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Oral RobertsORU': 
                espn_data[i][0] = 'Oral Roberts'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'ElonELON': 
                espn_data[i][0] = 'Elon'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UTEPUTEP': 
                espn_data[i][0] = 'UTEP'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UNC WilmingtonUNCW':
                espn_data[i][0] = 'UNCW'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Western KentuckyWKU': 
                espn_data[i][0] = 'Western Kentucky'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'CSU FullertonCSUF': 
                espn_data[i][0] = 'Cal State Fullerton'
                i += 1
                continue  
            elif str(espn_data[i][0]) == 'Loyola MarymountLMU': 
                espn_data[i][0] = 'LMU'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Southern MissUSM': 
                espn_data[i][0] = 'Southern Mississippi'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'New HampshireUNH': ##
                espn_data[i][0] = 'New Hampshire'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'MissouriMIZ': 
                espn_data[i][0] = 'Missouri'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UNC AshevilleUNCA': 
                espn_data[i][0] = 'UNC Asheville'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'MiamiMIA': 
                espn_data[i][0] = 'Miami FL'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'WoffordWOF': 
                espn_data[i][0] = 'Wofford'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'North Carolina A&TNCAT': 
                espn_data[i][0] = 'North Carolina A&T'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UT MartinUTM': 
                espn_data[i][0] = 'UT Martin'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'South CarolinaSC': 
                espn_data[i][0] = 'South Carolina'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'LouisianaULL': 
                espn_data[i][0] = 'Louisiana-Lafayette'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Bethune-CookmanBCU': 
                espn_data[i][0] = 'Bethune-Cookman'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'NortheasternNE': 
                espn_data[i][0] = 'Northeastern'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'DuquesneDUQ': 
                espn_data[i][0] = 'Duquesne'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UMassMASS': 
                espn_data[i][0] = 'Massachusetts'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Loyola ChicagoLUC': 
                espn_data[i][0] = 'Loyola Chicago'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'William & MaryW&M': 
                espn_data[i][0] = 'William & Mary'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Green BayGB': 
                espn_data[i][0] = 'Green Bay'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'TennesseeTENN': 
                espn_data[i][0] = 'Tennessee'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'St. Francis (BKN)SFBK': ##
                espn_data[i][0] = 'Saint Francis Brooklyn'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'GonzagaGONZ': 
                espn_data[i][0] = 'Gonzaga'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'WyomingWYO': 
                espn_data[i][0] = 'Wyoming'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'IowaIOWA': 
                espn_data[i][0] = 'Iowa'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'TexasTEX': 
                espn_data[i][0] = 'Texas'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UConnCONN': 
                espn_data[i][0] = 'UConn'
                i += 1
                continue
            elif 'UCLA' in str(espn_data[i][0]): 
                espn_data[i][0] = 'UCLA'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'BYUBYU': ##
                espn_data[i][0] = 'BYU'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Washington StateWSU': 
                espn_data[i][0] = 'Washington State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Iowa StateISU': 
                espn_data[i][0] = 'Iowa State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'ChattanoogaUTC': ##
                espn_data[i][0] = 'Chattanooga'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'San FranciscoSF': ##
                espn_data[i][0] = 'San Francisco'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'OklahomaOU': 
                espn_data[i][0] = 'Oklahoma'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'WagnerWAG': ##
                espn_data[i][0] = 'Wagner'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Murray StateMUR': 
                espn_data[i][0] = 'Murray State'
                i += 1
                continue
            elif 'CSU' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Colorado State'
                i += 1
                continue
            elif 'Oklahoma StateOKST' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Oklahoma State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Weber StateWEB': 
                espn_data[i][0] = 'Weber State'
                i += 1
                continue
            elif 'BelmontBEL' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Belmont'
                i += 1
                continue 
            elif 'UVA' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Virginia'
                i += 1
                continue
            elif 'NAVY' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Navy'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'VanderbiltVAN': 
                espn_data[i][0] = 'Vanderbilt'
                i += 1
                continue
            elif 'TA&M' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Texas A&M'
                i += 1
                continue
            elif 'MICH' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Michigan'
                i += 1
                continue 
            elif 'IONA' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Iona'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Saint LouisSLU': 
                espn_data[i][0] = 'Saint Louis'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'DrakeDRKE': 
                espn_data[i][0] = 'Drake'
                i += 1
                continue
            elif 'ILL' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Illinois'
                i += 1
                continue
            elif 'OAK' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Oakland'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'NiagaraNIAG': 
                espn_data[i][0] = 'Niagara'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'San Diego StateSDSU': 
                espn_data[i][0] = 'San Diego State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'BuffaloBUFF': ##
                espn_data[i][0] = 'Buffalo'
                i += 1
                continue
            elif 'Texas StateTXST' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Texas State'
                i += 1
                continue
            elif 'ACU' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Abilene Christian'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Utah ValleyUVU': ##
                espn_data[i][0] = 'Utah Valley'
                i += 1
                continue
            elif 'Western IllinoisWIU' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Western Illinois'
                i += 1
                continue
            elif 'GMU' in str(espn_data[i][0]): 
                espn_data[i][0] = 'George Mason'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'RichmondRICH': 
                espn_data[i][0] = 'Richmond'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'St. BonaventureSBU': ##
                espn_data[i][0] = 'Saint Bonaventure'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'HofstraHOF': ##
                espn_data[i][0] = 'Hofstra'
                i += 1
                continue
            elif 'M-OH' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Miami OH'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'VermontUVM': ##
                espn_data[i][0] = 'Vermont'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'MarquetteMARQ': 
                espn_data[i][0] = 'Marquette'
                i += 1
                continue 
            elif 'MORE' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Morehead State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'CornellCOR': 
                espn_data[i][0] = 'Cornell'
                i += 1
                continue 
            elif 'NEV' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Nevada'
                i += 1
                continue 
            elif 'ND' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Notre Dame'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'TCUTCU': 
                espn_data[i][0] = 'TCU'
                i += 1
                continue 
            elif str(espn_data[i][0]) == "Hawai'iHAW": ##
                espn_data[i][0] = 'Hawaii'
                i += 1
                continue 
            elif 'BC' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Boston College'
                i += 1
                continue 
            elif 'TOL' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Toledo'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'ColgateCOLG': 
                espn_data[i][0] = 'Colgate'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'UC Santa BarbaraUCSB': 
                espn_data[i][0] = 'UC Santa Barbara'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'ColoradoCOLO': 
                espn_data[i][0] = 'Colorado'
                i += 1
                continue 
            elif 'Georgia TechGT' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Georgia Tech'
                i += 1
                continue 
            elif 'San DiegoUSD' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'San Diego'
                i += 1
                continue
            elif 'FIU' in str(espn_data[i][0]): 
                espn_data[i][0] = 'FIU'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Georgia SouthernGASO': ##
                espn_data[i][0] = 'Georgia Southern'
                i += 1
                continue
            elif 'UNCO' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Northern Colorado'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Jacksonville StateJVST': ##
                espn_data[i][0] = 'Jacksonville State'
                i += 1
                continue
            elif 'CAMP' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Campbell'
                i += 1
                continue
            elif 'COFC' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Charleston'
                i += 1
                continue
            elif 'WIN' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Winthrop'
                i += 1
                continue
            elif 'St. Thomas - MinnesotaSTMN' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Saint Thomas MN'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'LipscombLIP': 
                espn_data[i][0] = 'Lipscomb'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Texas A&M-CCAMCC': 
                espn_data[i][0] = 'A&M-Corpus Christi'
                i += 1
                continue
            elif 'CLEV' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Cleveland State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Stephen F. AustinSFA': 
                espn_data[i][0] = 'SFA'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'DelawareDEL': 
                espn_data[i][0] = 'Delaware'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'TarletonTAR': 
                espn_data[i][0] = 'Tarleton State'
                i += 1
                continue
            elif 'TEM' in str(espn_data[i][0]): #
                espn_data[i][0] = 'Temple'
                i += 1
                continue
            elif str(espn_data[i][0]) == "Saint Joseph'sJOES": 
                espn_data[i][0] = 'Saint Josephs'
                i += 1
                continue
            elif 'UGA' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Georgia'
                i += 1
                continue
            elif 'APP' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Appalachian State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Tennessee TechTNTC': 
                espn_data[i][0] = 'Tennessee Tech'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'SMUSMU': 
                espn_data[i][0] = 'SMU'
                i += 1
                continue
            elif 'CIT' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Citadel'
                i += 1
                continue
            elif 'JMU' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'James Madison'
                i += 1
                continue
            elif 'ECU' in str(espn_data[i][0]): 
                espn_data[i][0] = 'East Carolina'
                i += 1
                continue
            elif 'RICE' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Rice'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Detroit MercyDET': ##
                espn_data[i][0] = 'Detroit Mercy'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Eastern KentuckyEKU': ##
                espn_data[i][0] = 'Eastern Kentucky'
                i += 1
                continue
            elif 'Southern IllinoisSIU' in str(espn_data[i][0]): #
                espn_data[i][0] = 'Southern Illinois'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Youngstown StateYSU': 
                espn_data[i][0] = 'Youngstown State'
                i += 1
                continue
            elif 'LONG' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Longwood'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Eastern MichiganEMU': ##
                espn_data[i][0] = 'Eastern Michigan'
                i += 1
                continue
            elif 'NC-Wilmgton' in str(espn_data[i][0]): 
                espn_data[i][0] = 'UNCW'
                i += 1
                continue
            elif 'PORT' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Portland'
                i += 1
                continue
            elif 'ValparaisoVALP' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Valparaiso'
                i += 1
                continue
            elif 'WASH' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Washington'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Ball StateBALL': ##
                espn_data[i][0] = 'Ball State'
                i += 1
                continue
            elif 'ManhattanMAN' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Manhattan'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'DartmouthDART': ##
                espn_data[i][0] = 'Dartmouth'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Maryland-Eastern ShoreUMES': 
                espn_data[i][0] = 'UMES'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'SamfordSAM': ##
                espn_data[i][0] = 'Samford'
                i += 1
                continue
            elif 'SJSU' in str(espn_data[i][0]): 
                espn_data[i][0] = 'San Jose State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Northern KentuckyNKU': 
                espn_data[i][0] = 'Northern Kentucky'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'TulsaTLSA': 
                espn_data[i][0] = 'Tulsa'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'TulaneTULN': 
                espn_data[i][0] = 'Tulane'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'BellarmineBELL': ##
                espn_data[i][0] = 'Bellarmine'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'UNLVUNLV': 
                espn_data[i][0] = 'UNLV'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'NichollsNICH': ##
                espn_data[i][0] = 'Nicholls State'
                i += 1
                continue
            elif str(espn_data[i][0]) == "Saint Peter'sSPU": 
                espn_data[i][0] = 'Saint Peters'
                i += 1
                continue 
            elif 'AKR' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Akron'
                i += 1
                continue 
            elif 'MER' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Mercer'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'NJITNJIT': 
                espn_data[i][0] = 'NJIT'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Air ForceAFA': 
                espn_data[i][0] = 'Air Force'
                i += 1
                continue 
            elif 'Kennesaw StateKENN' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Kennesaw State'
                i += 1
                continue 
            elif 'Radford' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Radford'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Loyola (MD)L-MD': ##
                espn_data[i][0] = 'Loyola Maryland'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'UT ArlingtonUTA': ##
                espn_data[i][0] = 'UT Arlington'
                i += 1
                continue 
            elif 'NORF' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Norfolk State'
                i += 1
                continue 
            elif 'HOW' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Howard'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'UL MonroeULM': 
                espn_data[i][0] = 'ULM'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'Florida AtlanticFAU': ##
                espn_data[i][0] = 'Florida Atlantic'
                i += 1
                continue 
            elif 'BGSU' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Bowling Green'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'MontanaMONT': ##
                espn_data[i][0] = 'Montana'
                i += 1
                continue 
            elif 'DXST' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Dixie State'
                i += 1
                continue
            elif 'HP' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'High Point'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'ArmyARMY': 
                espn_data[i][0] = 'Army West Point'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'BradleyBRAD': ##
                espn_data[i][0] = 'Bradley'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'BryantBRY': ##
                espn_data[i][0] = 'Bryant'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'George WashingtonGW': ##
                espn_data[i][0] = 'George Washington'
                i += 1
                continue
            elif 'PRE' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Presbyterian'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Long Island UniversityLIU': 
                espn_data[i][0] = 'LIU'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'CanisiusCAN': 
                espn_data[i][0] = 'Canisius'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'North FloridaUNF': ##
                espn_data[i][0] = 'North Florida'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'MaristMRST': ##
                espn_data[i][0] = 'Marist'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'EvansvilleEVAN': ##
                espn_data[i][0] = 'Evansville'
                i += 1
                continue
            elif 'PEPP' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Pepperdine'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'SouthernSOU': 
                espn_data[i][0] = 'Southern University'
                i += 1
                continue
            elif 'Sacramento StateSAC' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Sacramento State'
                i += 1
                continue
            elif 'Sacred HeartSHU' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Sacred Heart'
                i += 1
                continue
            elif 'WRST' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Wright State'
                i += 1
                continue 
            elif str(espn_data[i][0]) == 'BinghamtonBING':
                espn_data[i][0] = 'Binghamton'
                i += 1
                continue
            elif 'LEH' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Lehigh'
                i += 1
                continue
            elif 'LAS' in str(espn_data[i][0]): 
                espn_data[i][0] = 'La Salle'
                i += 1
                continue
            elif 'MILW' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Milwaukee'
                i += 1
                continue
            elif 'Western MichiganWMU' in str(espn_data[i][0]): #
                espn_data[i][0] = 'Western Michigan'
                i += 1
                continue
            elif 'FDU' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Fairleigh Dickinson'
                i += 1
                continue
            elif 'Cal PolyCP' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Cal Poly'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'QuinnipiacQUIN': 
                espn_data[i][0] = 'Quinnipiac'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'BucknellBUCK': ##
                espn_data[i][0] = 'Bucknell'
                i += 1
                continue
            elif 'PRST' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Portland State'
                i += 1
                continue
            elif 'NIU' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Northern Illinois'
                i += 1
                continue
            elif 'MORG' in str(espn_data[i][0]): ##
                espn_data[i][0] = 'Morgan State'
                i += 1
                continue 
            elif 'SienaSIE' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Siena'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Central MichiganCMU': ##
                espn_data[i][0] = 'Central Michigan'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Purdue Fort WaynePFW': 
                espn_data[i][0] = 'Purdue Fort Wayne'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'AlbanyALB': ##
                espn_data[i][0] = 'Albany NY'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'OmahaOMA': 
                espn_data[i][0] = 'Omaha'
                i += 1
                continue
            elif 'NorthwesternNU' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Northwestern'
                i += 1
                continue
            elif 'IUPU' in str(espn_data[i][0]): 
                espn_data[i][0] = 'IUPUI'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'IdahoIDHO': 
                espn_data[i][0] = 'Idaho'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Idaho StateIDST': ##
                espn_data[i][0] = 'Idaho State'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Eastern IllinoisEIU': 
                espn_data[i][0] = 'Eastern Illinois'
                i += 1
                continue
            elif str(espn_data[i][0]) == 'Holy CrossHC': ##
                espn_data[i][0] = 'Holy Cross'
                i += 1
                continue
            elif 'DSU' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Delaware State'
                i += 1
                continue
            elif 'KU' in str(espn_data[i][0]): 
                espn_data[i][0] = 'Kansas'
                i += 1
                continue
            else:
                i += 1
                continue
        else:
            break

    # print('\n')

    # for elem in espn_data:
    #     print(elem)
        
    # print('\n')

    for elem in espn_data:
        if len(elem) == 1:
            del elem

    dict_espn_data = {x[0]:x[1:] for x in espn_data}
    y = (dict_espn_data.keys())

    # print('\n')
    # print(dict_espn_data)
    # print('\n')

    i = 0
    while True: 
        if i < len(matchupAnalysis_NCAAB):
            b = i + 1
            if matchupAnalysis_NCAAB[i][0] in y and matchupAnalysis_NCAAB[b][0] in y:
                awayTeamList = dict_espn_data[matchupAnalysis_NCAAB[i][0]]
                if len(awayTeamList) == 0:
                    i += 2
                    continue
                # print(awayTeamList)
                # print('\n')
                awayTeamChance = awayTeamList[0]
                # print(awayTeamChance)
                # print('\n')
                homeTeamList = dict_espn_data[matchupAnalysis_NCAAB[b][0]]
                if len(homeTeamList) == 0:
                    i += 2
                    continue
                # print(homeTeamList)
                # print('\n')
                homeTeamChance = homeTeamList[0]
                # print(homeTeamChance)
                # print('\n')
                matchupAnalysis_NCAAB[i].append(awayTeamChance)
                matchupAnalysis_NCAAB[b].append(homeTeamChance)
                i += 2
                continue
            else:
                i += 2
                continue
        else:
            break
        
    for elem in matchupAnalysis_NCAAB:
        # print(elem)
        # print(len(elem))
        if len(elem) != 18:
            del elem
        # print('\n')
        
    # for elem in matchupAnalysis_NCAAB:
    #     if len(elem) == 17:
    #         del elem
    #         continue

    # matchupAnalysis: [i][0] = teamname, [i][1] = spread, [i][2] = total, [i][3] = moneyline,
    # [i][4] = time, [i][5] = total pfa, [i][6] = home pfa, [i][7] = away pfa , [i][8] = total paa
    # , [i][9] = home paa, [i][10] = away paa, [i][11] = home or away, [i][12] = expected points, 
    # [i][13] = expected total, [i][14] = calculated chance, [i][15] = numberfire chance
    # [i][16] = game day (today or not today), [i][17] = ESPN Chance, [i][18] = average source chance

    # CALCULATE AND APPEND AVERAGE CHANCES TO MATCHUPANALYSIS_NHL / INDEX [I][18]
    i = 0
    while True:
        if i < len(matchupAnalysis_NCAAB):
            if len(matchupAnalysis_NCAAB[i]) == 17:
                del matchupAnalysis_NCAAB[i]
                continue
            else:
                # print(matchupAnalysis[i][0])
                avg = (float(matchupAnalysis_NCAAB[i][15]) + float(matchupAnalysis_NCAAB[i][17]) + float(matchupAnalysis_NCAAB[i][14])) / 3   
                avg = round(avg, 2)
                matchupAnalysis_NCAAB[i].append(avg)
                i += 1
                continue
        else:
            break

    # matchupAnalysis: [i][0] = teamname, [i][1] = spread, [i][2] = total, [i][3] = moneyline,
    # [i][4] = time, [i][5] = total pfa, [i][6] = home pfa, [i][7] = away pfa , [i][8] = total paa
    # , [i][9] = home paa, [i][10] = away paa, [i][11] = home or away, [i][12] = expected points, 
    # [i][13] = expected total, [i][14] = calculated chance, [i][15] = numberfire chance
    # [i][16] = game day (today or not today), [i][17] = ESPN Chance, [i][18] = average source chance
    
    # matchupAnalysis: [i][0] = teamname, [i][1] = spread, [i][2] = total, [i][3] = moneyline,
    # [i][4] = time, [i][5] = home or away, [i][6] = expected points, 
    # [i][7] = expected total, [i][8] = calculated chance, [i][9] = numberfire chance
    # [i][10] = game day (today or not today), [i][11] = ESPN Chance, [i][12] = average chance, [13] = avg value, [14] = calc val
    # [15] = nf val, [16] = espn val, [17] consensus

    print('\n')
    leftWidth = 23
    rightWidth = 9
    righterWidth = 19
    rightererWidth = 14
    totalWidth = (leftWidth + righterWidth + righterWidth + righterWidth + rightererWidth + rightWidth 
    + rightererWidth + righterWidth)

    title = " IT'S MADNESS SZN "
    print(title.center(totalWidth, '-'))
    print('Team'.ljust(leftWidth) + 'Moneyline'.rjust(rightWidth) + 'Avg Value'.rjust(rightererWidth) 
        + 'Avg(%)'.rjust(rightererWidth) + 'Consensus(C/N/E)'.rjust(righterWidth) + 'Calculated(%)'.rjust(righterWidth) +
    'Numberfire(%)'.rjust(righterWidth) + 'ESPN(%)'.rjust(righterWidth) 
    )
    
    headers = ['Team', 'Spread', 'Total', 'ML', 'Game Time', 'PF/G_T', 'PF/G_H',
    'PF/G_A', 'PA/G_T', 'PA/G_H', 'PA/G_A', 'H/A', 'Team_Pts',
    'Total_Pts', 'Calc_%', 'NF_%', 'Day', 'ESPN_%',
    'Src_Avg_%', 'Src_Avg_V', 'Calc_V', 'NF_V', 
    'ESPN_V', 'Consensus']

    i = 0
    while True:
        if i < len(matchupAnalysis_NCAAB):
            if matchupAnalysis_NCAAB[i][3] < 0:
                avg_chance = matchupAnalysis_NCAAB[i][18] # includes calculated chance
                avg_chance_num = round((avg_chance / 100), 2)
                moneyline = np.nan_to_num(matchupAnalysis_NCAAB[i][3]) 
                moneyline = int(moneyline) 
                moneyline_pos = moneyline * -1
                value = round((avg_chance_num * (10 + 10 / (moneyline_pos / 10)* 10)), 3)
                matchupAnalysis_NCAAB[i].append(value) # creates [i][19] = total average value
                name = matchupAnalysis_NCAAB[i][0]
                calc_chance = matchupAnalysis_NCAAB[i][14]
                calc_chance_num = round((float(calc_chance) / 100), 2)
                nf_chance = matchupAnalysis_NCAAB[i][15]
                nf_chance_num = round((float(nf_chance) / 100), 2)
                espn_chance = matchupAnalysis_NCAAB[i][17]
                espn_chance_num = round((float(espn_chance) / 100), 2)
                calc_value = round(calc_chance_num * (10 + 10 / (moneyline_pos / 10)* 10), 3)
                # print('Calculated Value: ' + str(calc_value))
                matchupAnalysis_NCAAB[i].append(calc_value) # creates [i][20] = calculated value
                nf_value = round(nf_chance_num * (10 + 10 / (moneyline_pos / 10)* 10), 3)
                # print('NF Value: ' + str(nf_value))
                matchupAnalysis_NCAAB[i].append(nf_value) # creates [i][21] = numberfire value
                espn_value = round(espn_chance_num * (10 + 10 / (moneyline_pos / 10)* 10), 3)
                # print('ESPN Value: ' + str(espn_value))
                matchupAnalysis_NCAAB[i].append(espn_value) # creates [i][22] = espn value
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
                c = str(c)
                n = str(n)
                e = str(e)
                matchupAnalysis_NCAAB[i].append(c + n + e) # creates [i][23] = consensus
                if matchupAnalysis_NCAAB[i][19] > 10:
                    consensus = matchupAnalysis_NCAAB[i][23] 
                    i += 1
                    continue
                else:
                    i += 1
                    continue
            else:
                moneyline = np.nan_to_num(matchupAnalysis_NCAAB[i][3])
                moneyline = int(moneyline)
                avg_chance = matchupAnalysis_NCAAB[i][18]
                avg_chance_num = round((avg_chance / 100), 2)
                value = round(((moneyline / 100 * 10 + 10) * avg_chance_num), 3)
                matchupAnalysis_NCAAB[i].append(value) # creates [i][19] = average value
                name = matchupAnalysis_NCAAB[i][0]
                calc_chance = matchupAnalysis_NCAAB[i][14]
                calc_chance_num = round((float(calc_chance) / 100), 2)
                nf_chance = matchupAnalysis_NCAAB[i][15]
                nf_chance_num = round((float(nf_chance) / 100), 2)
                espn_chance = matchupAnalysis_NCAAB[i][17]
                espn_chance_num = round((float(espn_chance) / 100), 2)
                calc_value = round(((moneyline / 100 * 10 + 10) * calc_chance_num), 3)
                # print('Calculated Value: ' + str(calc_value))
                matchupAnalysis_NCAAB[i].append(calc_value) # creates [i][20] = calculated value
                nf_value = round(((moneyline / 100 * 10 + 10) * nf_chance_num), 3)
                # print('NF Value: ' + str(nf_value))
                matchupAnalysis_NCAAB[i].append(nf_value) # creates [i][21] = numberfire value
                espn_value = round(((moneyline / 100 * 10 + 10) * espn_chance_num), 3)
                # print('ESPN Value: ' + str(espn_value))
                matchupAnalysis_NCAAB[i].append(espn_value) # creates [i][22] = espn value
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
                c = str(c)
                n = str(n)
                e = str(e)
                matchupAnalysis_NCAAB[i].append(c + n + e) # creates [i][23] = consensus
                i += 1
                continue
        else:
            break
    
    matchupAnalysis_NCAAB_sorted = sorted(matchupAnalysis_NCAAB, key=itemgetter(19), reverse=True)
    
    for elem in matchupAnalysis_NCAAB_sorted:
        del elem[5:11]
        del elem[10]
        
    headers_sorted = ['Team', 'Spread', 'Total', 'ML', 'Game Time', 'H/A', 'Team_Pts',
    'Total_Pts', 'Calc_%', 'NF_%', 'ESPN_%',
    'Avg_%', 'Avg_V', 'Calc_V', 'NF_V', 
    'ESPN_V', 'Consensus']

    for elem in matchupAnalysis_NCAAB_sorted:
        if elem[12] > 10:
            name = elem[0]
            moneyline = elem[3]
            value = elem[12]
            avg_chance = elem[11]
            consensus = elem[16] 
            calc_chance = elem[8]
            nf_chance = elem[9]
            espn_chance = elem[10]
            print((name).ljust(leftWidth) + str(moneyline).rjust(rightWidth) 
            + str(value).rjust(rightererWidth) + str(avg_chance).rjust(rightererWidth) 
            + str(consensus).rjust(righterWidth) + str(calc_chance).rjust(righterWidth) 
            + str(nf_chance).rjust(righterWidth) + str(espn_chance).rjust(righterWidth))
            continue
        else:
            continue


    print('\n')
    ncaabData = pd.DataFrame(matchupAnalysis_NCAAB_sorted, columns = headers_sorted) #matchupAnalysis_NCAAB_sorted, matchupAnalysis_NCAAB
    ncaabData.head()
    ncaabData.to_excel('/Users/Hayden/OneDrive/Sports Betting/Basketball/madness_040422.xlsx', sheet_name = 'cbb', index=False)

    conn = sqlite3.connect('madness.db')

    ncaabData.to_sql(name='cbb', con=conn, if_exists='replace', index=False)

    conn.commit()

ncaab()

# schedule.every(2.5).hours.do(ncaab)
 
# while True:
#     schedule.run_pending()

