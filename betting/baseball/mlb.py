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
import scipy
from scipy.stats import poisson
import matplotlib.pyplot as plt
import math
import random
import sqlite3
from operator import itemgetter
import schedule
from sqlalchemy import column
from sympy import continued_fraction_reduce
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from webdriver_auto_update import check_driver
import copy


def mlb():
    # change to https://www.espn.com/mlb/stats/parkfactor when data is ready
    url_parkFactor = 'https://baseballsavant.mlb.com/leaderboard/statcast-park-factors?type=year&year=2021&batSide=&stat=index_wOBA&condition=All&rolling=&sort=6&sortDir=desc'
    url_pitching = 'https://www.mlb.com/stats/team/pitching?sortState=asc'
    url_rpg = 'https://www.teamrankings.com/mlb/stat/runs-per-game'
    url_o_rpg = 'https://www.teamrankings.com/mlb/stat/opponent-runs-per-game'
    url_o_fir = 'https://www.teamrankings.com/mlb/stat/opponent-1st-inning-scored-percentage'
    url_fir = 'https://www.teamrankings.com/mlb/stat/1st-inning-scored-percentage'
    url_soa = 'https://www.teamrankings.com/mlb/stat/strikeouts-per-game'
    url_pitchers = 'https://www.cbssports.com/fantasy/baseball/probable-pitchers/'  # + date
    url_matchups = 'https://www.espn.com/mlb/scoreboard/_/date/'  # + date
    url_bullpen_ERAs = 'https://www.espn.com/mlb/stats/team/_/view/pitching/table/pitching'
    url_innings_avg = 'https://www.espn.com/mlb/team/stats/_/type/pitching/name/'
    url_nf = 'https://www.numberfire.com/mlb/games/'
    url_relievers = 'https://www.mlb.com/stats/team/pitching?split=rp&sortState=asc'
    # Check_Chromedriver('/Users/Hayden/opt/anaconda3/bin/')

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
    # days = [today, tomorrow, twodays, threedays, fourdays, fivedays]
    days = [today, tomorrow, twodays]  # , threedays, fourdays, fivedays]

    def rename(teamName):
        if teamName == 'Houston' or teamName == 'HOU' or teamName == 'Houston Astros' or teamName == 'null(Houston, Texas)' or teamName == 'Astros Minute Maid Park' or teamName == 'HOUAstros' or 'HOU Astros' in teamName or teamName == 'Astros' or 'Astros' in teamName:
            teamName = 'HOU Astros'
            return teamName
        if teamName == 'Tampa Bay' or teamName == 'TB' or teamName == 'Tampa Bay Rays' or teamName == 'null(St. Petersburg, Florida)' or teamName == 'Rays Tropicana Field' or teamName == 'TBRays' or 'TB Rays' in teamName or teamName == 'Rays' or 'Rays' in teamName:
            teamName = 'TB Rays'
            return teamName
        if teamName == 'Toronto' or teamName == 'TOR' or teamName == 'Toronto Blue Jays' or teamName == 'Rogers Centre(Toronto, Ontario)' or teamName == 'Blue Jays Rogers Centre' or teamName == 'TORBlue Jays' or 'TOR Blue Jays' in teamName or teamName == 'Blue Jays' or 'Blue Jays' in teamName:
            teamName = 'TOR Blue Jays'
            return teamName
        if teamName == 'Boston' or teamName == 'BOS' or teamName == 'Boston Red Sox' or teamName == 'null(Boston, Massachusetts)' or teamName == 'Red Sox Fenway Park' or teamName == 'BOSRed Sox' or 'BOS Red Sox' in teamName or teamName == 'Red Sox' or 'Red Sox' in teamName:
            teamName = 'BOS Red Sox'
            return teamName
        if teamName == 'LA Dodgers' or teamName == 'LAD' or teamName == 'Los Angeles Dodgers' or teamName == 'null(Los Angeles, California)' or teamName == 'Dodgers Dodger Stadium' or teamName == 'LADDodgers' or 'LA Dodgers' in teamName or teamName == 'Dodgers' or 'Dodgers' in teamName:
            teamName = 'LA Dodgers'
            return teamName
        if teamName == 'Chi Sox' or teamName == 'Chicago White Sox' or teamName == 'CHW' or teamName == 'White Sox Guaranteed Rate Field' or teamName == 'White Sox Guaranteed Rate Field' or teamName == 'CHWWhite Sox' or 'CHI White Sox' in teamName or teamName == 'White Sox' or 'White Sox' in teamName:
            teamName = 'CHI White Sox'
            return teamName
        # SF Giants
        if teamName == 'SF Giants' or teamName == 'SF' or teamName == 'San Francisco Giants' or teamName == 'null(San Francisco, California)' or teamName == 'Giants Oracle Park' or teamName == 'SFGiants' or 'SF Giants' in teamName or teamName == 'Giants' or 'Giants' in teamName:
            teamName = 'SF Giants'
            return teamName
        if teamName == 'Cincinnati' or teamName == 'CIN' or teamName == 'Cincinnati Reds' or teamName == 'null(Cincinnati, Ohio)' or teamName == 'Reds Great American Ball Park' or teamName == 'CINReds' or 'CIN Reds' in teamName or teamName == 'Reds' or 'Reds' in teamName:
            teamName = 'CIN Reds'
            return teamName
        if teamName == 'Atlanta' or teamName == 'ATL' or teamName == 'Atlanta Braves' or teamName == 'null(Atlanta, Georgia)' or teamName == 'Braves Truist Park' or teamName == 'ATLBraves' or 'ATL Braves' in teamName or teamName == 'Braves' or 'Braves' in teamName:
            teamName = 'ATL Braves'
            return teamName
        if teamName == 'Colorado' or teamName == 'COL' or teamName == 'Colorado Rockies' or teamName == 'null(Denver, Colorado)' or teamName == 'Rockies Coors Field' or teamName == 'COLRockies' or 'COL Rockies' in teamName or teamName == 'Rockies' or 'Rockies' in teamName:
            teamName = 'COL Rockies'
            return teamName
        if teamName == 'Oakland' or teamName == 'OAK' or teamName == 'Oakland Athletics' or teamName == 'null(Oakland, California)' or teamName == 'Athletics Oakland Coliseum' or teamName == 'OAKAthletics' or 'OAK Athletics' in teamName or teamName == 'Athletics' or 'Athletics' in teamName:
            teamName = 'OAK Athletics'
            return teamName
        if teamName == 'Philadelphia' or teamName == 'PHI' or teamName == 'Philadelphia Phillies' or teamName == 'null(Philadelphia, Pennsylvania)' or teamName == 'Phillies Citizens Bank Park' or teamName == 'PHIPhillies' or 'PHI Phillies' in teamName or teamName == 'Phillies' or 'Phillies' in teamName:
            teamName = 'PHI Phillies'
            return teamName
        if teamName == 'San Diego' or teamName == 'SD' or teamName == 'San Diego Padres' or teamName == 'null(San Diego, California)' or teamName == 'Padres Petco Park' or teamName == 'SDPadres' or 'SD Padres' in teamName or teamName == 'Padres' or 'Padres' in teamName:
            teamName = 'SD Padres'
            return teamName
        if teamName == 'Minnesota' or teamName == 'MIN' or teamName == 'Minnesota Twins' or teamName == 'null(Minneapolis, Minnesota)' or teamName == 'Twins Target Field' or teamName == 'MINTwins' or 'MIN Twins' in teamName or teamName == 'Twins' or 'Twins' in teamName:
            teamName = 'MIN Twins'
            return teamName
        if teamName == 'Milwaukee' or teamName == 'MIL' or teamName == 'Milwaukee Brewers' or teamName == 'Miller Park(Milwaukee, Wisconsin)' or teamName == 'Brewers American Family Field' or teamName == 'MILBrewers' or 'MIL Brewers' in teamName or teamName == 'Brewers' or 'Brewers' in teamName:
            teamName = 'MIL Brewers'
            return teamName
        if teamName == 'Washington' or teamName == 'WSH' or teamName == 'WAS' or teamName == 'Washington Nationals' or teamName == 'null(Washington, District of Columbia)' or teamName == 'Nationals Nationals Park' or teamName == 'WSHNationals' or 'WAS Nationals' in teamName or teamName == 'Nationals' or 'Nationals' in teamName:
            teamName = 'WAS Nationals'
            return teamName
        if teamName == 'LA Angels' or teamName == 'LAA' or teamName == 'Los Angeles Angels' or teamName == 'null(Anaheim, California)' or teamName == 'Angels Angel Stadium' or teamName == 'LAAAngels' or 'LA Angels' in teamName or teamName == 'Angels' or 'Angels' in teamName:
            teamName = 'LA Angels'
            return teamName
        if teamName == 'Cleveland' or teamName == 'CLE' or teamName == 'Cleveland Guardians' or teamName == 'Cleveland Indians' or teamName == 'null(Cleveland, Ohio)' or teamName == 'Indians Progressive Field' or teamName == 'Guardians Progressive Field' or teamName == 'CLEGuardians' or 'CLE Guardians' in teamName or teamName == 'Guardians' or teamName == 'Indians' or 'Guardians' in teamName:
            teamName = 'CLE Guardians'
            return teamName
        if teamName == 'NY Yankees' or teamName == 'NYY' or teamName == 'New York Yankees' or teamName == 'null(Bronx, New York)' or teamName == 'Yankees Yankee Stadium' or teamName == 'NYYYankees' or 'NY Yankees' in teamName or teamName == 'Yankees' or 'Yankees' in teamName:
            teamName = 'NY Yankees'
            return teamName
        if teamName == 'Chi Cubs' or teamName == 'Chicago Cubs' or teamName == 'CHC' or teamName == 'Cubs Wrigley Field' or teamName == 'CHCCubs' or 'CHI Cubs' in teamName or teamName == 'Cubs' or 'Cubs' in teamName:
            teamName = 'CHI Cubs'
            return teamName
        if teamName == 'St. Louis' or teamName == 'STL' or teamName == 'St. Louis Cardinals' or teamName == 'null(St. Louis, Missouri)' or teamName == 'Cardinals Busch Stadium' or teamName == 'STLCardinals' or 'STL Cardinals' in teamName or teamName == 'Cardinals' or 'Cardinals' in teamName:
            teamName = 'STL Cardinals'
            return teamName
        if teamName == 'Detroit' or teamName == 'DET' or teamName == 'Detroit Tigers' or teamName == 'null(Detroit, Michigan)' or teamName == 'Tigers Comerica Park' or teamName == 'DETTigers' or 'DET Tigers' in teamName or teamName == 'Tigers' or 'Tigers' in teamName:
            teamName = 'DET Tigers'
            return teamName
        if teamName == 'Seattle' or teamName == 'SEA' or teamName == 'Seattle Mariners' or teamName == 'null(Seattle, Washington)' or teamName == 'Mariners T-Mobile Park' or teamName == 'SEAMariners' or 'SEA Mariners' in teamName or teamName == 'Mariners' or 'Mariners' in teamName:
            teamName = 'SEA Mariners'
            return teamName
        if teamName == 'Kansas City' or teamName == 'KC' or teamName == 'Kansas City Royals' or teamName == 'null(Kansas City, Missouri)' or teamName == 'Royals Kauffman Stadium' or teamName == 'KCRoyals' or 'KC Royals' in teamName or teamName == 'Royals' or 'Royals' in teamName:
            teamName = 'KC Royals'
            return teamName
        if teamName == 'Arizona' or teamName == 'ARI' or teamName == 'Arizona Diamondbacks' or teamName == 'null(Phoenix, Arizona)' or teamName == 'D-backs Chase Field' or teamName == 'ARIDiamondbacks' or 'ARI Diamondbacks' in teamName or teamName == 'Diamondbacks' or 'Diamondbacks' in teamName:
            teamName = 'ARI Diamondbacks'
            return teamName
        if teamName == 'Baltimore' or teamName == 'BAL' or teamName == 'Baltimore Orioles' or teamName == 'null(Baltimore, Maryland)' or teamName == 'Orioles Oriole Park at Camden Yards' or teamName == 'BALOrioles' or 'BAL Orioles' in teamName or teamName == 'Orioles' or 'Orioles' in teamName:
            teamName = 'BAL Orioles'
            return teamName
        if teamName == 'NY Mets' or teamName == 'NYM' or teamName == 'New York Mets' or teamName == 'null(Queens, New York)' or teamName == 'Mets Citi Field' or teamName == 'NYMMets' or 'NY Mets' in teamName or teamName == 'Mets' or 'Mets' in teamName:
            teamName = 'NY Mets'
            return teamName
        if teamName == 'Texas' or teamName == 'TEX' or teamName == 'Texas Rangers' or teamName == 'null(Arlington, Texas)' or teamName == 'TEXRangers' or 'TEX Rangers' in teamName or teamName == 'Rangers' or 'Rangers' in teamName:
            teamName = 'TEX Rangers'
            return teamName
        if teamName == 'Miami' or teamName == 'MIA' or teamName == 'Miami Marlins' or teamName == 'Marlins Park(Miami, Florida)' or teamName == 'Marlins loanDepot park' or teamName == 'MIAMarlins' or 'MIA Marlins' in teamName or teamName == 'Marlins' or 'Marlins' in teamName:
            teamName = 'MIA Marlins'
            return teamName
        if teamName == 'Pittsburgh' or teamName == 'PIT' or teamName == 'Pittsburgh Pirates' or teamName == 'null(Pittsburgh, Pennsylvania)' or teamName == 'Pirates PNC Park' or teamName == 'PITPirates' or 'PIT Pirates' in teamName or teamName == 'Pirates' or 'Pirates' in teamName:
            teamName = 'PIT Pirates'
            return teamName
        else:
            return teamName

    def espn(teamName, player):
        if teamName == 'HOU Astros':
            teamName = 'hou'
        if teamName == 'TB Rays':
            teamName = 'tb'
        if teamName == 'TOR Blue Jays':
            teamName = 'tor'
        if teamName == 'BOS Red Sox':
            teamName = 'bos'
        if teamName == 'LA Dodgers':
            teamName = 'lad'
        if teamName == 'CHI White Sox':
            teamName = 'chw'
        if teamName == 'SF Giants':
            teamName = 'sf'
        if teamName == 'CIN Reds':
            teamName = 'cin'
        if teamName == 'ATL Braves':
            teamName = 'atl'
        if teamName == 'COL Rockies':
            teamName = 'col'
        if teamName == 'OAK Athletics':
            teamName = 'oak'
        if teamName == 'PHI Phillies':
            teamName = 'phi'
        if teamName == 'SD Padres':
            teamName = 'sd'
        if teamName == 'MIN Twins':
            teamName = 'min'
        if teamName == 'MIL Brewers':
            teamName = 'mil'
        if teamName == 'WAS Nationals':
            teamName = 'wsh'
        if teamName == 'LA Angels':
            teamName = 'laa'
        if teamName == 'CLE Guardians':
            teamName = 'cle'
        if teamName == 'NY Yankees':
            teamName = 'nyy'
        if teamName == 'CHI Cubs':
            teamName = 'chc'
        if teamName == 'STL Cardinals':
            teamName = 'stl'
        if teamName == 'DET Tigers':
            teamName = 'det'
        if teamName == 'SEA Mariners':
            teamName = 'sea'
        if teamName == 'KC Royals':
            teamName = 'kc'
        if teamName == 'ARI Diamondbacks':
            teamName = 'ari'
        if teamName == 'BAL Orioles':
            teamName = 'bal'
        if teamName == 'NY Mets':
            teamName = 'nym'
        if teamName == 'TEX Rangers':
            teamName = 'tex'
        if teamName == 'MIA Marlins':
            teamName = 'mia'
        if teamName == 'PIT Pirates':
            teamName = 'pit'
        print(str(url_innings_avg) + str(teamName))
        df_innings = pd.read_html(url_innings_avg + teamName)
        innings_name = df_innings[0].values.tolist()
        innings_stats = df_innings[1].values.tolist()
        pitchers = []
        i = 0
        while True:
            if i < len(innings_name):
                lgth = len(str(innings_name[i][0])) - 3
                name = str(innings_name[i][0])
                name = name[:lgth]
                name = [name]
                stat = innings_stats[i]
                # print(stat)
                y = 0
                while True:
                    if y < len(stat):
                        if stat[y] == '---' or stat[y] == '--' or stat[y] == '-':
                            y += 1
                            continue
                        # print(stat[y])
                        stat[y] = float(stat[y])
                        y += 1
                        continue
                    else:
                        break
                lst = name + stat
                pitchers.append(lst)
                i += 1
                continue
            else:
                break
        i = 0
        while True:
            if i < len(pitchers):
                gp = pitchers[i][1]
                inn = pitchers[i][8]
                ipg = round(inn / gp, 3)
                pitchers[i].append(ipg)
                i += 1
                continue
            else:
                break
        dict_pitchers = {x[0]: x[1:] for x in pitchers}
        keys_pitchers = (dict_pitchers.keys())
        if player in keys_pitchers:
            player_stats = dict_pitchers[player]
            del player_stats[3:5]
            del player_stats[5]
            del player_stats[8:10]
            # should give 'games_played', 'starts', 'qual_starts', 'saves', 'holds', 'hits', 'earned_runs', 'homers', 'ks_per_9', 'pitches_per_start', 'WAR', 'ipg'
            del player_stats[11:13]
            return player_stats
        else:
            lst = ['use bullpen avg', '-', '-', '-',
                   '-', '-', '-', '-', '-', '-', '-', '-']
            return lst

    def get_index_positions(list_of_elems, element):
        ''' Returns the indexes of all occurrences of give element in
        the list- listOfElements '''
        index_pos_list = []
        index_pos = 0
        while True:
            try:
                # Search for item in list from indexPos to the end of list
                index_pos = list_of_elems.index(element, index_pos)
                # Add the index position in list
                index_pos_list.append(index_pos)
                index_pos += 1
            except ValueError as e:
                break
        return index_pos_list

    # test = espn('PIT Pirates', 'Zach Thompson')
    # print(test)

    html_pf = requests.get(url_parkFactor)
    soup_pf = bs4.BeautifulSoup(html_pf.content, features='html.parser')
    scrapeNumberfireNCAAB_today = soup_pf.findAll(
        'tr', attrs={'class': 'default-table-row'})

    # CREATING PARK FACTOR LIST

    pf_browser = webdriver.Chrome()
    pf_browser.get(url_parkFactor)
    time.sleep(20)
    pf = pf_browser.find_elements(By.CLASS_NAME, 'default-table-row  ')

    pf_mlb = []
    for elem in pf:
        txt = elem.text
        txt = txt.split('\n')
        lng = len(txt)
        end = lng - 1
        a = 0
        while True:
            if a < lng:
                pf_mlb.append(txt[a])
                a += 1
                continue
            else:
                break

    pf = []
    pf_val = 0
    wOBACon = 0
    bacon = 0
    r = 0
    obp = 0
    h = 0
    one_b = 0
    two_b = 0
    three_b = 0
    hr = 0
    bb = 0
    so = 0
    pa = 0
    for elem in pf_mlb:
        ind0 = elem.index('-202')
        ind1 = ind0 - 5
        name = elem[:ind1]
        spaces = name.count(' ')
        inds = name.index(' ') + 1
        name = rename(name[inds:])
        name = [name]
        # print('.' + name + '.')
        # print(spaces)
        # print(elem)
        stat = elem[ind0 + 6:]
        stat = stat.split(' ')
        i = 0
        while True:
            if i < len(stat):
                stat[i] = stat[i].replace(',', '')
                stat[i] = float(stat[i])
                i += 1
                continue
            else:
                break
        lst = name + stat
        pf_val = pf_val + lst[1]
        wOBACon = wOBACon + lst[2]
        bacon = bacon + lst[3]
        r = r + lst[4]
        obp = obp + lst[5]
        h = h + lst[6]
        one_b = one_b + lst[7]
        two_b = two_b + lst[8]
        three_b = three_b + lst[9]
        hr = hr + lst[10]
        bb = bb + lst[11]
        so = so + lst[12]
        pa = pa + lst[13]
        pf.append(lst)

    pf_browser.quit()

    # TEX RANGERS NOT IN PF LIST ON WEBSITE. HAVE TO MANUALLY CALCULATE BASED ON SITE AVERAGES

    print('r = ' + str(round(r / 29, 4)))
    print('TEX Rangers PF = ' + str(round((100 * 30) - r, 4)))
    pf_val = round((100 * 30) - pf_val, 4)
    wOBACon = round((100 * 30) - wOBACon, 4)
    bacon = round((100 * 30) - bacon, 4)
    r = round((100 * 30) - r, 4)
    obp = round((100 * 30) - obp, 4)
    h = round((100 * 30) - h, 4)
    one_b = round((100 * 30) - one_b, 4)
    two_b = round((100 * 30) - two_b, 4)
    three_b = round((100 * 30) - three_b, 4)
    hr = round((100 * 30) - hr, 4)
    bb = round((100 * 30) - bb, 4)
    so = round((100 * 30) - so, 4)
    pa = round((15000 * 30) - pf_val, 4)
    lst = ['TEX Rangers', pf_val, wOBACon, bacon, r,
           obp, h, one_b, two_b, three_b, hr, bb, so, pa]
    pf.append(lst)
    print('\n')
    print('PARK FACTORS')
    for elem in pf:
        print(elem)
    print('\n')

    # CREATE DICTIONARY OF MLB PARK FACTORS

    dict_pf = {x[0]: x[1:] for x in pf}
    keys_pf = (dict_pf.keys())

    # Step 1: Get Average Runs For
    # Avg Runs For = Average Runs Scored (total/home/away)

    # Step 2: Get Runs Against (using pitcher ERA's)
    # How to Calculate Runs Against
    # Runs Against = ((1 - starter average innings) * Bullpen ERA) + (Starter average innings * Starter ERA)

    # Step 3: Get Ballpark Factor
    # How to Calculate Ballpark Factor
    # Average BPF for this year and the last 4 years (2022 - 2018)
    # only applies to away team for expected Runs

    # How to Calculate Expected Runs
    # Expected Runs Away Team = Away Avg Runs For * Home Runs Against * Ballpark Factor / Home Runs Against
    # Expected Runs Home Team = Home Avg Runs For * Away Runs Against / Away Runs Against

    # CREATING DICTIONARY FOR RUNS PER GAME

    df_rpg = pd.read_html(url_rpg)
    tr_rpg = df_rpg[0].values.tolist()

    mlb_rpg = []
    for elem in tr_rpg:
        team = str(elem[1])
        team = rename(team)
        # print(elem)
        lastYear_avg = float(elem[7])
        if elem[2] == '--':
            neutral_avg = lastYear_avg
        if elem[5] == '--':
            if elem[2] != '--':
                home_avg = float(elem[2])
            else:
                home_avg = lastYear_avg
        if elem[6] == '--':
            if elem[2] != '--':
                away_avg = float(elem[2])
            else:
                away_avg = lastYear_avg
        if elem[2] != '--':
            neutral_avg = float(elem[2])
        if elem[5] != '--':
            home_avg = float(elem[5])
        if elem[6] != '--':
            away_avg = float(elem[6])
        lst = [team, neutral_avg, home_avg, away_avg, lastYear_avg]
        # print(lst)
        mlb_rpg.append(lst)

    # MLB_RPG: [0] = TEAM NAME, [1] = NEUTRAL RUNS AVG, [2] = HOME RUNS AVG, [3] = AWAY RUNS AVG, [4] = LAST YEAR RUNS AVG
    # for elem in mlb_rpg:
    #     print(elem)

    # GETTING OPPONENT POINTS PER GAME STATS

    df_o_rpg = pd.read_html(url_o_rpg)
    tr_o_rpg = df_o_rpg[0].values.tolist()

    mlb_o_rpg = []

    for elem in tr_o_rpg:
        team = str(elem[1])
        team = rename(team)
        # print(elem)
        lastYear_avg = float(elem[7])
        if elem[2] == '--':
            neutral_avg = lastYear_avg
        if elem[5] == '--':
            if elem[2] != '--':
                home_avg = float(elem[2])
            else:
                home_avg = lastYear_avg
        if elem[6] == '--':
            if elem[2] != '--':
                away_avg = float(elem[2])
            else:
                away_avg = lastYear_avg
        if elem[2] != '--':
            neutral_avg = float(elem[2])
        if elem[5] != '--':
            home_avg = float(elem[5])
        if elem[6] != '--':
            away_avg = float(elem[6])
        lst = [team, neutral_avg, home_avg, away_avg, lastYear_avg]
        mlb_o_rpg.append(lst)

    dict_o_rpg = {x[0]: x[1:] for x in mlb_o_rpg}
    keys_o_rpg = (dict_o_rpg.keys())

    # CALCULATING TEAM AVERAGE RUNS FOR/AGAINST AND LEAGUE AVERAGE RUNS FOR/AGAINST, W/ AND W/O SPLITS AND MERGING FOR AND AGAINST STATS

    league_runs_against_total = []
    league_runs_against_away = []
    league_runs_against_home = []
    league_runs_for_total = []
    league_runs_for_away = []
    league_runs_for_home = []
    tr_data = []
    i = 0
    while True:
        if i < len(mlb_rpg):
            name = mlb_rpg[i][0]
            lst = dict_o_rpg[name]
            lst = mlb_rpg[i] + lst
            league_runs_for_total.append(lst[1])
            league_runs_for_home.append(lst[2])
            league_runs_for_away.append(lst[3])
            league_runs_against_total.append(lst[5])
            league_runs_against_home.append(lst[6])
            league_runs_against_away.append(lst[7])
            tr_data.append(lst)
            i += 1
            continue
        else:
            break

    print('\n')
    print('TEAM RANKINGS STATS')
    for elem in tr_data:
        print(elem)
    print('\n')

    league_runs_against_total = round(
        statistics.mean(league_runs_against_total), 4)
    league_runs_against_away = round(
        statistics.mean(league_runs_against_away), 4)
    league_runs_against_home = round(
        statistics.mean(league_runs_against_home), 4)
    league_runs_for_total = round(statistics.mean(league_runs_for_total), 4)
    league_runs_for_away = round(statistics.mean(league_runs_for_away), 4)
    league_runs_for_home = round(statistics.mean(league_runs_for_home), 4)
    print('\n')
    print('League Average Runs For (total) = ' + str(league_runs_for_total))
    print('League Average Runs For (home) = ' + str(league_runs_for_home))
    print('League Average Runs For (away) = ' + str(league_runs_for_away))
    print('League Average Runs Against (total) = ' +
          str(league_runs_against_total))
    print('League Average Runs Against (home) = ' +
          str(league_runs_against_home))
    print('League Average Runs Against (away) = ' +
          str(league_runs_against_away))
    print('\n')

    # for elem in mlb:
    #     print(elem)

    # CREATING DICTIONARY OF MLB LIST WITH NEUTRAL, HOME, AWAY RUNS FOR AND NEUTRAL, HOME, AWAY RUNS AGAINST AVERAGES FOR EVERY TEAM (CURRENT "MLB" LIST)

    dict_tr_data = {x[0]: x[1:] for x in tr_data}
    keys_tr_data = (dict_tr_data.keys())

    # FINDING THE PROBABLE STARTING PITCHERS FOR EACH GAME IN THE NEXT 5 DAYS

    dfPitchers = []
    y = 0
    for elem in days:
        url = str(url_pitchers) + str(elem)
        print(url)
        html_strt = requests.get(url_pitchers + str(elem))
        soup_strt = bs4.BeautifulSoup(
            html_strt.content, features='html.parser')
        # scrape_strt = soup_pf.findAll('tr', attrs={'class':'default-table-row'})
        if 'No pitching matchups available.' in str(soup_strt):
            continue
        else:
            df_pitchers = pd.read_html(url_pitchers + str(elem))
            # print(len(df_pitchers))
            i = 0
            while True:
                if i < len(df_pitchers):
                    dfPitchers.append(df_pitchers[i].values.tolist())
                    dfPitchers[y].append(str(elem))
                    i += 1
                    y += 1
                    continue
                else:
                    break

    i = 0
    y = 0
    while True:
        if i < len(dfPitchers):
            if y < 2:
                # print(dfPitchers[i][y])
                # SKIPS ENTRIES WITHOUT A LISTED PROBABLE PITCHER
                if str(dfPitchers[i][y][0]) == 'TBD  TBD':
                    y += 1
                    continue
                # print(dfPitchers[i][y])
                lst = str(dfPitchers[i][y][0])
                # print(dfPitchers[i][y][1])
                # IF THAT PITCHER HAS PAST STATS, INDEX [I][Y][1] WILL NOT = '-'
                if dfPitchers[i][y][1] != '—':
                    wins = float(dfPitchers[i][y][1])
                    losses = float(dfPitchers[i][y][2])
                    innings_pitched = float(dfPitchers[i][y][3])
                    era = float(dfPitchers[i][y][4])
                    if era > 5.5:
                        era = float(5.5)
                    babw = float(dfPitchers[i][y][5])
                    so = float(dfPitchers[i][y][6])
                    whip = float(dfPitchers[i][y][7])
                    lst_stats = [wins, losses,
                                 innings_pitched, era, babw, so, whip]
                # IF THE PITCHER HAS NO EXISTING STATS, INDEX [I][Y][1] WILL = '-', REPLACING WITH EMPTY INDICIES WHICH WILL BE USED TO TRIGGER THE USE OF BULLPEN AVERAGES
                if str(dfPitchers[i][y][1]) == '—':
                    lst_stats = ['-', '-', '-', '-', '-', '-', '-']
                if 'RHP' in lst:
                    ind = lst.index('RHP') + 5
                if 'LHP' in lst:
                    ind = lst.index('LHP') + 5
                # print(lst)
                lst = lst[ind:]
                lst = lst.split('  ')
                lst = lst + lst_stats
                lst[1] = rename(lst[1])  # LST[1] IS THE TEAM NAME
                # print(lst)
                # GETS TEAM STATS FROM MLB DICTIONARY
                team_stats = dict_tr_data[lst[1]]
                team_name = [lst[1]]
                pitcher = [lst[0]]
                pitcher_stats = lst[2:]
                # team_name + team_stats + pitcher + pitcher_stats
                dfPitchers[i][y] = team_name + pitcher + pitcher_stats
                # print(dfPitchers[i][y])
                y += 1
                continue
            else:
                y = 0
                i += 1
                continue
        else:
            break

    pitchers = dfPitchers

    print('\n')
    print('Pitchers List:')
    for elem in pitchers:
        print(elem)
    print('\n')

    # dict_pitchers = {x[0]:x[1:] for x in pitchers}
    # keys_pitchers = (dict_pitchers.keys())
    numList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # CREATING LIST 'MLB MATCHUPS' TO SIMPLY LIST EVERY MATCHUP, AND THE DATE, WITHIN THE NEXT 5 DAYS, NO RISK OF ERROR SUCH RESULTING FROM MISSING DATA LIKE WE CAN SEE IN SPORTSBOOKS, OTHER PREDRICTION SOURCES
    print('CREATING LIST MLB MATCHUPS TO SIMPLY LIST EVERY MATCHUP')
    mlb_matchups = []
    for elem in days:
        print(str(url_matchups) + str(elem))
        html_matchups = requests.get(url_matchups + str(elem))
        print(html_matchups)
        soup_matchups = bs4.BeautifulSoup(
            html_matchups.content, features='html.parser')
        # print('\n')
        data1 = soup_matchups.find_all(
            'ul', class_='ScoreboardScoreCell__Competitors')
        for el in data1:
            # print(el.text)
            matchup = str(el.text)
            print('\n')
            print(matchup)
            print('\n')
            if 'Away)' in matchup:
                matchup = matchup.split('Away)')
                ind_arec = matchup[0].index('(')
                matchup[0] = matchup[0][:ind_arec]
                if matchup[0][0] in numList:
                    i = 0
                    while True:
                        if i < len(str(matchup[0][0])):
                            if matchup[0][i] in numList:
                                i += 1
                                continue
                            else:
                                i += 1
                                matchup[0] = matchup[0][i:]
                                break
                        else:
                            break
                print(matchup[1])
                ind_hrec = matchup[1].index('(')
                matchup[1] = matchup[1][:ind_hrec]
                if matchup[1][0] in numList:
                    i = 0
                    while True:
                        if i < len(str(matchup[1][0])):
                            if matchup[1][i] in numList:
                                i += 1
                                continue
                            else:
                                i += 1
                                matchup[1] = matchup[1][i:]
                                break
                        else:
                            break
            else:
                matchup = matchup.split(')')
                ind_arec = matchup[0].index('(')
                matchup[0] = matchup[0][:ind_arec]
                if matchup[0][0] in numList:
                    i = 0
                    while True:
                        if i < len(str(matchup[0][0])):
                            if matchup[0][i] in numList:
                                i += 1
                                continue
                            else:
                                i += 1
                                matchup[0] = matchup[0][i:]
                                break
                        else:
                            break
                print(matchup[1])
                ind_hrec = matchup[1].index('(')
                matchup[1] = matchup[1][:ind_hrec]
                if matchup[1][0] in numList:
                    i = 0
                    while True:
                        if i < len(str(matchup[1][0])):
                            if matchup[1][i] in numList:
                                i += 1
                                continue
                            else:
                                i += 1
                                matchup[1] = matchup[1][i:]
                                break
                        else:
                            break
            aName = matchup[0]
            aName = rename(aName)
            matchup[0] = aName
            hName = matchup[1]
            hName = rename(hName)
            matchup[1] = hName
            matchup.append(str(elem))
            mlb_matchups.append(matchup)
        # # ind = matchups.index('","competitions":[{"') - 50
        # while True:
        #     if '","competitions":[{"' in matchups:
        #         print('string matches matchups soup')
        #         ind = matchups.index('","competitions":[{"') - 80
        #         game = matchups[ind: ind + 500]
        #         start = game.index('","name":"') + 10
        #         end = game.index('","competitions":[{"')
        #         matchup = game[start: end]
        #         matchup = matchup.split(' at ')
        #         matchup[0] = rename(matchup[0])
        #         matchup[1] = rename(matchup[1])
        #         matchup.append(str(elem))
        #         print(matchup)
        #         mlb_matchups.append(matchup)
        #         matchups = matchups[ind + 500:]
        #         continue
        #     else:
        #         print('\n')
        #         print('STRING DOES NOT MATCH MATCHUPS SOUP')
        #         break
    print('\n')
    mlb = copy.deepcopy(mlb_matchups)
    print('after deep copy of mlb_matchups')
    print(str(len(mlb)))
    print(mlb)
    print('\n')
    # CREATING ESPN LIST WITH EACH TEAMS BULLPEN AVERAGE PITCHING STATS

    df_espn_ERA = pd.read_html(url_bullpen_ERAs)
    espn_ERA_names = df_espn_ERA[0].values.tolist()
    espn_ERA_stats = df_espn_ERA[1].values.tolist()

    espn_ERA = []

    i = 0
    while True:
        if i < len(espn_ERA_names):
            lst = espn_ERA_names[i] + espn_ERA_stats[i]
            del lst[0]
            lst[0] = rename(lst[0])
            y = 1
            while True:
                if y < len(lst):
                    lst[y] = float(lst[y])
                    y += 1
                    continue
                else:
                    break
            espn_ERA.append(lst)
            i += 1
            continue
        else:
            break

    print('\n')
    print('espn_ERA list:')
    # print('\n')
    for elem in espn_ERA:
        print(elem)
        # print('\n')
    print('\n')
    dict_era = {x[0]: x[1:] for x in espn_ERA}
    keys_era = (dict_era.keys())
    print('ERA KEYS')
    print(keys_era)
    print('\n')

    rl_browser = webdriver.Chrome()
    rl_browser.get(url_relievers)
    time.sleep(120)
    pf_row = rl_browser.find_elements(By.TAG_NAME, 'tr')

    print('\n')

    mlb_relievers = []
    for elem in pf_row:
        txt = elem.text
        txt = txt.split('\n')
        lng = len(txt)
        end = lng - 1
        a = 0
        while True:
            if a < lng:
                mlb_relievers.append(str(txt[a]))
                a += 1
                continue
            else:
                break

    rl_browser.quit()

    reliever_stats = []
    i = mlb_relievers.index('1')
    t = i + 1
    d = i + 2
    while True:
        if i < len(mlb_relievers):
            team = mlb_relievers[t]
            team = rename(team)
            stat = mlb_relievers[d]
            stat = stat.split(' ')
            del stat[5:8]
            stat = stat[1:]
            z = 0
            while True:
                if z < len(stat):
                    if '.' in stat[z]:
                        if stat[z][0] == '−':
                            stat[z] = stat[z][1:]
                            stat[z] = float(stat[z])
                            stat[z] = round(-1 * stat[z], 2)
                        stat[z] = float(stat[z])
                        z += 1
                        continue
                    else:
                        if stat[z][0] == '−':
                            stat[z] = stat[z][1:]
                            stat[z] = float(stat[z])
                            stat[z] = round(-1 * stat[z], 2)
                        stat[z] = int(stat[z])
                        z += 1
                        continue
                else:
                    break
            # lst = [team, stat]
            lst = [team] + stat
            reliever_stats.append(lst)
            i += 3
            t = i + 1
            d = i + 2
            continue
        else:
            break

    for elem in reliever_stats:
        print(elem)

    dict_relievers = {x[0]: x[1:] for x in reliever_stats}
    keys_relievers = (dict_relievers.keys())
    print('\n')

    # CURRENT LISTS:
    # ESPN_ERA - LIST WITH TEAM BULLPEN AVGS
    # PARK FACTORS - LIST WITH PARK FACTORS AND OTHER DATA NAMED BY HOME TEAM NAME, NOT STADIUM NAME
    # TR_DATA - STATS FROM TEAM RANKINGS (RUNS FOR/ AGAINST)
    # GOAL: TO USE MLB MATCHUPS LIST WITH DATES TO ADD DATA TO
    # PITCHERS - LIST WITH AWAY PROBABLE PITCHER STATS, HOME PROBABLE PITCHER STATS, FOLLOWED BY THE DATE OF THE GAME
    # .
    print('\n')
    print('MLB MATCHUPS LIST - PRE MERGING:')
    for elem in mlb:
        print(elem)
    print('\n')

    # THIS TAKES THE LIST OF GAMES FOR THE NEXT 5 DAYS (MLB_MATCHUPS LIST) AND ADDS TEAM RANKINGS RUNS DATA, PARK FACTOR DATA, AND BULLPEN DATA
    i = 0
    while True:
        if i < len(mlb_matchups):
            awayTeam = mlb_matchups[i][0]
            homeTeam = mlb_matchups[i][1]
            day = mlb_matchups[i][2]
            runs_away = dict_tr_data[awayTeam]
            runs_home = dict_tr_data[homeTeam]
            pf = dict_pf[homeTeam]
            away_era = dict_relievers[awayTeam]
            home_era = dict_relievers[homeTeam]
            away_stats = [awayTeam] + runs_away + pf + away_era
            home_stats = [homeTeam] + runs_home + pf + home_era
            mlb_matchups[i][0] = away_stats
            mlb_matchups[i][1] = home_stats
            i += 1
            continue
        else:
            break

    print('\n')
    print('MLB MATCHUPS LIST - PRE MERGING:')
    for elem in mlb:
        print(elem)
    print('\n')
    print('\n')
    # THIS GOES THROUGH THE PITCHERS LIST AND MATCHES THE TEAM NAMES AND GAME DATES TO THE MLB_MATCHUPS LIST, THEN ADDS THOSE PROBABLE PITCHERS TO MLB_MATCHUPS
    double_header = []
    i = 0
    while True:
        if i < len(pitchers):
            awayTeam = pitchers[i][0][0]
            homeTeam = pitchers[i][1][0]
            day = str(pitchers[i][2])
            lst = [awayTeam, homeTeam, day]
            print(lst)
            # y = 0
            # while True:
            #     if y < len
            if lst in mlb:
                c = 0
                c = mlb.count(lst)
                print('lst is in "mlb" ' + str(c) + ' time(s).')
                if c > 1:
                    if lst in double_header:
                        i += 1
                        continue
                    inds = get_index_positions(mlb, lst)
                    print('repeated list index positions:')
                    print(inds)
                    s = 0
                    while True:
                        if inds[s] in double_header:
                            s += 1
                            continue
                        else:
                            x = inds[s]
                            break
                    print('PITCHERS INDEX MATCHED AN ITEM IN THE MLB MATCHUPS LIST')
                    away_pitcher = pitchers[i][0][1]
                    away_ipg = espn(awayTeam, away_pitcher)
                    pitchers[i][0] = pitchers[i][0] + away_ipg
                    away_starter_stats = pitchers[i][0][1:]
                    home_pitcher = pitchers[i][1][1]
                    home_ipg = espn(homeTeam, home_pitcher)
                    pitchers[i][1] = pitchers[i][1] + home_ipg
                    home_starter_stats = pitchers[i][1][1:]
                    print(mlb_matchups[x])
                    mlb_matchups[x][0] = mlb_matchups[x][0] + \
                        away_starter_stats
                    mlb_matchups[x][1] = mlb_matchups[x][1] + \
                        home_starter_stats
                    print(mlb_matchups[x])
                    double_header.append(x)
                    i += 1
                    continue
                print('PITCHERS INDEX MATCHED AN ITEM IN THE MLB MATCHUPS LIST')
                x = mlb.index(lst)
                away_pitcher = pitchers[i][0][1]
                away_ipg = espn(awayTeam, away_pitcher)
                pitchers[i][0] = pitchers[i][0] + away_ipg
                away_starter_stats = pitchers[i][0][1:]
                home_pitcher = pitchers[i][1][1]
                home_ipg = espn(homeTeam, home_pitcher)
                pitchers[i][1] = pitchers[i][1] + home_ipg
                home_starter_stats = pitchers[i][1][1:]
                print(mlb_matchups[x])
                mlb_matchups[x][0] = mlb_matchups[x][0] + away_starter_stats
                mlb_matchups[x][1] = mlb_matchups[x][1] + home_starter_stats
                print(mlb_matchups[x])
                i += 1
                continue
            else:
                i += 1
                continue
        else:
            break
    print('\n')

    for elem in mlb_matchups:
        for el in elem:
            print(el)

    ######################################################################################################
    ###################################### fixing draftkings #############################################
    ######################################################################################################

    dk_df_0 = pd.DataFrame(pd.read_html(
        'https://sportsbook.draftkings.com/leagues/baseball/88670847')[0])
    dk_df_1 = pd.DataFrame(pd.read_html(
        'https://sportsbook.draftkings.com/leagues/baseball/88670847')[1])
    # dk_df_2 = pd.DataFrame(pd.read_html('https://sportsbook.draftkings.com/leagues/baseball/88670847')[2])

    def today_or_tomorrow(col):
        if 'AM' in col and ':' in col:
            day = 'Today'
        else:
            day = 'Tomorrow'
        return day

    dk_df_0['Day'] = dk_df_1.apply(lambda x: 'Today', axis=1)
    dk_df_1['Day'] = dk_df_1.apply(
        lambda x: today_or_tomorrow(x['Tomorrow']), axis=1)

    dk_df_1.rename(columns={'Tomorrow': 'Today'}, inplace=True)
    cond = dk_df_1.Day == 'Today'
    rows = dk_df_1.loc[cond, :]
    dk_df_0 = dk_df_0.append(rows)
    dk_df_1.drop(rows.index, inplace=True)

    dk_df = dk_df_0.append(dk_df_1)

    dk_df['Today'] = dk_df.apply(lambda x: rename(x['Today']), axis=1)
    dk_df.rename(columns={'Today': 'Team'}, inplace=True)
    print(dk_df)

    ######################################################################################################
    ###################################### fixing draftkings #############################################
    ######################################################################################################

    mlb_draftkings = pd.read_html(
        'https://sportsbook.draftkings.com/leagues/baseball/88670847')
    # mlb_DK = mlb_draftkings[0].values.tolist()
    # mlb_DK_cols = mlb_draftkings[0].columns.tolist()
    mlbDk = []
    i = 0
    while True:
        if i < len(mlb_draftkings):
            x = [mlb_draftkings[i].columns.tolist()]
            y = mlb_draftkings[i].values.tolist()  # to_numpy
            # z = mlb_draftkings[i].index.tolist()
            mlbDk = mlbDk + x + y
            i += 1
            continue
        else:
            break

    dict_dk = {x[0]: x[1:] for x in mlbDk}
    keys_dk = (dict_dk.keys())

    # print('\n')
    # for elem in mlbDk:
    #     print(elem)
    # print('\n')

    dk_today = 0
    dk_tomorrow = 0
    dk_late_today = 0
    today_ind = 0
    i = 0
    while True:
        if i < len(mlbDk):
            if mlbDk[i][1] == 'RUN LINE' or mlbDk[i][2] == 'TOTAL' or mlbDk[i][3] == 'MONEYLINE':
                if mlbDk[i][0] == 'Today':
                    dk_today += 1
                    i += 1
                    continue
                elif mlbDk[i][0] == 'Tomorrow':
                    tomorrow_index = i
                    dk_tomorrow += 1
                    i += 1
                    continue
                elif ':' in str(mlbDk[i][0]) and 'AM' in str(mlbDk[i][0]):
                    gametime = mlbDk[i][0]
                    ind = gametime.index(':') + 3
                    gametime = gametime[:ind]
                    gametime = gametime.replace(':', '')
                    gametime = int(gametime)
                    if gametime < 900:  # USED TO BE 400
                        dk_late_today += 1
                    continue
                else:
                    dk_today += 1
                    dk_tomorrow += 1
                    i += 1
                    continue
            else:
                name = rename(mlbDk[i][0])
                mlbDk[i][0] = name
                if str(mlbDk[i][1]) != 'nan':
                    len_spread = len(mlbDk[i][1])
                    spread_odds = mlbDk[i][1]
                    if '.' in str(spread_odds):
                        dot = spread_odds.index('.') + 2
                        spread = float(spread_odds[:dot])
                        spr_odds = spread_odds[dot:]
                        if '−' in spr_odds:
                            spr_odds = spr_odds[1:]
                            spr_odds = int(spr_odds)
                            spr_odds = round(-1 * spr_odds, 2)
                        spr_odds = int(spr_odds)
                    if '.' not in str(spread_odds):
                        pm = spread_odds[0]
                        spread_odds = spread_odds[1:]
                        if '-' in spread_odds:
                            ind = spread_odds.index('-')
                            if pm == '-':
                                spr_odds = int(spread_odds[ind:])
                                spread = float(spread_odds[:ind]) * -1
                            if pm == '+':
                                spr_odds = int(spread_odds[ind:])
                                spread = float(spread_odds[:ind])
                        if '+' in spread_odds:
                            ind = spread_odds.index('+')
                            if pm == '-':
                                spr_odds = int(spread_odds[ind:])
                                spread = float(spread_odds[:ind]) * -1
                            if pm == '+':
                                spr_odds = int(spread_odds[ind:])
                                spread = float(spread_odds[:ind])
                    # spr_odds = int(spread_odds[len_spread - 4:])
                    # spread = float(spread_odds[:len_spread - 4])
                    if str(mlbDk[i][2]) != 'nan':
                        if 'O' in mlbDk[i][2]:
                            lg_over = len(mlbDk[i][2])
                            over_odds = mlbDk[i][2]
                            o_odds = over_odds[lg_over - 4:]
                            # print(over_odds)
                            if o_odds[0] == '−':
                                o_odds = o_odds[1:]
                                o_odds = float(o_odds)
                                o_odds = round(-1 * o_odds, 2)
                            o_odds = int(o_odds)
                            over = float(over_odds[2: lg_over - 4])
                            if str(mlbDk[i][3]) != 'nan':
                                ml = mlbDk[i][3]
                                if mlbDk[i][3][0] == '−':
                                    ml = mlbDk[i][3][1:]
                                    ml = float(ml)
                                    ml = round(-1 * ml, 2)
                                mlbDk[i][3] = int(ml)
                            if str(mlbDk[i][3]) == 'nan':
                                ml = 'n/a'
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(today)
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(tomorrow)
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(tomorrow)
                            if dk_tomorrow == 0 and dk_today == 1:
                                gameday = str(today)
                            if mlbDk[i][0] == 'Tomorrow':
                                today_ind = tomorrow_index + dk_late_today + 1
                                if dk_tomorrow == 1 and dk_today == 1 and i < today_ind:
                                    gameday = str(today)
                            # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 1:
                            #     gameday = str(tomorrow)
                            # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 'NA':
                            #     gameday = str(tomorrow)
                            # if dk_tomorrow == 0 and dk_today == 1 and dk_late_today == 'NA':
                            #     gameday = str(today)
                            name = str(name) + ' ' + str(gameday)
                            lst = [name, spread, spr_odds, over, o_odds, ml]
                            mlbDk[i] = lst
                            i += 1
                            continue
                        else:
                            lg_under = len(mlbDk[i][2])
                            under_odds = mlbDk[i][2]
                            under = float(under_odds[2: lg_under - 4])
                            under_odds = under_odds[lg_under - 4:]
                            # print(under_odds)
                            if under_odds[0] == '−':
                                under_odds = under_odds[1:]
                                under_odds = float(under_odds)
                                under_odds = round(-1 * under_odds, 2)
                            u_odds = int(under_odds)
                            if str(mlbDk[i][3]) != 'nan':
                                if mlbDk[i][3][0] == '−':
                                    ml = mlbDk[i][3][1:]
                                    ml = float(ml)
                                    ml = round(-1 * ml, 2)
                                mlbDk[i][3] = int(ml)
                                ml = int(mlbDk[i][3])
                            if str(mlbDk[i][3]) == 'nan':
                                ml = 'n/a'
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(today)
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(tomorrow)
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(tomorrow)
                            if dk_tomorrow == 0 and dk_today == 1:
                                gameday = str(today)
                            if dk_tomorrow == 1 and dk_today == 1 and i < today_ind:
                                gameday = str(today)
                            # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 1:
                            #     gameday = str(tomorrow)
                            # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 'NA':
                            #     gameday = str(tomorrow)
                            # if dk_tomorrow == 0 and dk_today == 1 and dk_late_today == 'NA':
                            #     gameday = str(today)
                            name = str(name) + ' ' + str(gameday)
                            lst = [name, spread, spr_odds, under, u_odds, ml]
                            mlbDk[i] = lst
                            i += 1
                            continue
                    if str(mlbDk[i][2]) == 'nan':
                        if str(mlbDk[i][3]) != 'nan':
                            if mlbDk[i][3][0] == '−':
                                ml = mlbDk[i][3][1:]
                                ml = float(ml)
                                ml = round(-1 * ml, 2)
                                mlbDk[i][3] = ml
                            ml = int(mlbDk[i][3])
                        if str(mlbDk[i][3]) == 'nan':
                            ml = 'n/a'
                        ou = 'n/a'
                        ou_odds = 'n/a'
                        if dk_tomorrow == 1 and dk_today == 1:
                            gameday = str(today)
                        if dk_tomorrow == 1 and dk_today == 1:
                            gameday = str(tomorrow)
                        if dk_tomorrow == 1 and dk_today == 1:
                            gameday = str(tomorrow)
                        if dk_tomorrow == 0 and dk_today == 1:
                            gameday = str(today)
                        if dk_tomorrow == 1 and dk_today == 1 and i < today_ind:
                            gameday = str(today)
                        # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 1:
                        #     gameday = str(tomorrow)
                        # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 'NA':
                        #     gameday = str(tomorrow)
                        # if dk_tomorrow == 0 and dk_today == 1 and dk_late_today == 'NA':
                        #     gameday = str(today)
                        name = str(name) + ' ' + str(gameday)
                        lst = [name, spread, spr_odds, ou, ou_odds, ml]
                        mlbDk[i] = lst
                        i += 1
                        continue
                if str(mlbDk[i][1]) == 'nan':
                    spr_odds = 'n/a'
                    spread = 'n/a'
                    if str(mlbDk[i][2]) != 'nan':
                        if 'O' in mlbDk[i][2]:
                            lg_over = len(mlbDk[i][2])
                            over_odds = mlbDk[i][2]
                            # print(over_odds)
                            o_odds = int(over_odds[lg_over - 4:])
                            over = float(over_odds[2: lg_over - 4])
                            if str(mlbDk[i][3]) != 'nan':
                                if mlbDk[i][3][0] == '−':
                                    ml = mlbDk[i][3][1:]
                                    ml = float(ml)
                                    ml = round(-1 * ml, 2)
                                    mlbDk[i][3] = ml
                                ml = int(mlbDk[i][3])
                            if str(mlbDk[i][3]) == 'nan':
                                ml = 'n/a'
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(today)
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(tomorrow)
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(tomorrow)
                            if dk_tomorrow == 0 and dk_today == 1:
                                gameday = str(today)
                            if dk_tomorrow == 1 and dk_today == 1 and i < today_ind:
                                gameday = str(today)
                            # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 1:
                            #     gameday = str(tomorrow)
                            # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 'NA':
                            #     gameday = str(tomorrow)
                            # if dk_tomorrow == 0 and dk_today == 1 and dk_late_today == 'NA':
                            #     gameday = str(today)
                            name = str(name) + ' ' + str(gameday)
                            lst = [name, spread, spr_odds, over, o_odds, ml]
                            mlbDk[i] = lst
                            i += 1
                            continue
                        else:
                            lg_under = len(mlbDk[i][2])
                            under_odds = mlbDk[i][2]
                            # print(under_odds)
                            u_odds = int(under_odds[lg_under - 4:])
                            under = float(under_odds[2: lg_under - 4])
                            if str(mlbDk[i][3]) != 'nan':
                                if mlbDk[i][3][0] == '−':
                                    ml = mlbDk[i][3][1:]
                                    ml = float(ml)
                                    ml = round(-1 * ml, 2)
                                    mlbDk[i][3] = ml
                                ml = int(mlbDk[i][3])
                            if str(mlbDk[i][3]) == 'nan':
                                ml = 'n/a'
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(today)
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(tomorrow)
                            if dk_tomorrow == 1 and dk_today == 1:
                                gameday = str(tomorrow)
                            if dk_tomorrow == 0 and dk_today == 1:
                                gameday = str(today)
                            if dk_tomorrow == 1 and dk_today == 1 and i < today_ind:
                                gameday = str(today)
                            # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 1:
                            #     gameday = str(tomorrow)
                            # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 'NA':
                            #     gameday = str(tomorrow)
                            # if dk_tomorrow == 0 and dk_today == 1 and dk_late_today == 'NA':
                            #     gameday = str(today)
                            name = str(name) + ' ' + str(gameday)
                            lst = [name, spread, spr_odds, under, u_odds, ml]
                            mlbDk[i] = lst
                            i += 1
                            continue
                    if str(mlbDk[i][2]) == 'nan':
                        if str(mlbDk[i][3]) != 'nan':
                            if mlbDk[i][3][0] == '−':
                                ml = mlbDk[i][3][1:]
                                ml = float(ml)
                                ml = round(-1 * ml, 2)
                                mlbDk[i][3] = ml
                            ml = int(mlbDk[i][3])
                        if str(mlbDk[i][3]) == 'nan':
                            ml = 'n/a'
                        ou = 'n/a'
                        ou_odds = 'n/a'
                        if dk_tomorrow == 1 and dk_today == 1:
                            gameday = str(today)
                        if dk_tomorrow == 1 and dk_today == 1:
                            gameday = str(tomorrow)
                        if dk_tomorrow == 1 and dk_today == 1:
                            gameday = str(tomorrow)
                        if dk_tomorrow == 0 and dk_today == 1:
                            gameday = str(today)
                        if dk_tomorrow == 1 and dk_today == 1 and i < today_ind:
                            gameday = str(today)
                        # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 1:
                        #     gameday = str(tomorrow)
                        # if dk_tomorrow == 1 and dk_today == 1 and dk_late_today == 'NA':
                        #     gameday = str(tomorrow)
                        # if dk_tomorrow == 0 and dk_today == 1 and dk_late_today == 'NA':
                        #     gameday = str(today)
                        name = str(name) + ' ' + str(gameday)
                        lst = [name, spread, spr_odds, ou, ou_odds, ml]
                        mlbDk[i] = lst
                        i += 1
                        continue
        else:
            break

    dict_dk_data = {x[0]: x[1:] for x in mlbDk}
    keys_dk_data = (dict_dk_data.keys())

    # for elem in mlbDk:
    #     print(elem)

    # print('\n')
    # print('DraftKings List:')
    # print(mlbDk)
    # print('\n')

    # MLB MATCHUPS NOW HAS EVERY GAME IN NEXT 5 DAYS WITH TEAM NAMES, RUNS DATA FROM TEAM RANKINGS, PARK FACTORS, BULLPEN STATS, AND THE PROBABLE STARTER
    # AND THAT PITCHER'S STATS.
    # print('\n')
    # print('MLB_MATCHUPS LIST WITH ALL NEEDED DATA')
    # for elem in mlb_matchups:
    #     for el in elem:
    #         print(el)
    #     print('\n')
    # print('\n')

    # print('MATCHUP STATS LIST:')

    # for elem in matchup_stats:
    #     print(elem)
    #     for el in elem:
    #         print(el)
    #         # print('\n')
    #     print('\n')

    # pitcher avg innings index [18], preceded by Pitcher stats, followed by Bullpen stats (bullpen avg era is index [22])

    # headers_park = ['Park Factor', 'wOBACon', 'BACON', 'R', 'OBP', 'H', '1B', '2B', '3B', 'HR', 'BB', 'SO', 'PA']

    mlb = []

    # Expected Points
    i = 0
    length = len(mlb_matchups)
    while True:
        if i < len(mlb_matchups):
            if len(mlb_matchups[i][0]) != 59 or len(mlb_matchups[i][1]) != 59:
                del mlb_matchups[i]
                continue
            print(mlb_matchups[i])
            # print('\n')
            # print('\n')
            day = mlb_matchups[i][2]
            away_name = mlb_matchups[i][0][0]  # STARTING PITCHER = [38]
            home_name = mlb_matchups[i][1][0]
            away_for_avg = mlb_matchups[i][0][3]
            home_for_avg = mlb_matchups[i][1][2]
            print('Length of mlb_matchups[' + str(i) + ']:')
            print(len(mlb_matchups[i][0]))
            away_starter_ERA = mlb_matchups[i][0][43]
            if away_starter_ERA == 0.0 or away_starter_ERA == '-':
                # relievers ERA = [24]
                away_starter_ERA = mlb_matchups[i][0][24]
            home_starter_ERA = mlb_matchups[i][1][43]
            if home_starter_ERA == 0.0 or home_starter_ERA == '-':
                home_starter_ERA = mlb_matchups[i][1][24]
            away_bp_ERA = mlb_matchups[i][0][24]
            home_bp_ERA = mlb_matchups[i][1][24]
            away_starter_avg_innings = mlb_matchups[i][0][58]
            home_starter_avg_innings = mlb_matchups[i][1][58]
            park_run_factor = round(mlb_matchups[i][0][12] / 100, 3)
            if away_starter_avg_innings == 'use bullpen avg' or away_starter_avg_innings == '-':
                # print('\n')
                # print('away starter not listed for ' + str(away_name))
                mlb_matchups[i][0][43] = away_bp_ERA
                away_runs_against = away_bp_ERA
                away_starter_ERA = away_bp_ERA
                away_starter_avg_innings = 5
            if away_starter_avg_innings != 'use bullpen avg' and away_starter_avg_innings != '-':
                # print('\n')
                # print(away_starter_ERA)
                # print(away_starter_avg_innings)
                # print(away_bp_ERA)
                away_runs_against = round(away_starter_ERA * (away_starter_avg_innings / 9) + (
                    (9 - away_starter_avg_innings) / 9) * away_bp_ERA, 3)
            if home_starter_avg_innings == 'use bullpen avg' or home_starter_avg_innings == '-':
                # print('home starter not listed for ' + str(home_name))
                # print('\n')
                mlb_matchups[i][1][43] = home_bp_ERA
                home_runs_against = home_bp_ERA
                home_starter_ERA = home_bp_ERA
                home_starter_avg_innings = 5
            if home_starter_avg_innings != 'use bullpen avg' and home_starter_avg_innings != '-':
                home_runs_against = round(home_starter_ERA * (home_starter_avg_innings / 9) + (
                    (9 - home_starter_avg_innings) / 9) * home_bp_ERA, 3)
            # league_runs_against_total, league_runs_against_home     ##
            away_runs = round(away_for_avg * home_runs_against *
                              park_run_factor / league_runs_against_total, 3)
            # league_runs_against_total, league_runs_against_away                       ##
            home_runs = round(home_for_avg * away_runs_against /
                              league_runs_against_total, 3)
            total_runs = round(away_runs + home_runs, 3)
            lst_a = [away_runs_against, away_runs, total_runs]
            lst_h = [home_runs_against, home_runs, total_runs]
            mlb_matchups[i][0] = mlb_matchups[i][0] + lst_a
            mlb_matchups[i][1] = mlb_matchups[i][1] + lst_h
            # print(lst)
            # mlb.append(lst)
            i += 1
            continue
        else:
            break

    print('Calculated Each Team\'s Expected points')

    mlb = mlb_matchups

    # for elem in mlb:
    #     for el in elem:
    #         print(el)
    #         # print('\n')
    #     print('\n')

    # matchupAnalysis: [i][0] = teamname, [i][1] = spread, [i][2] = total, [i][3] = moneyline,
    # [i][4] = time, [i][5] = total pfa, [i][6] = home pfa, [i][7] = away pfa , [i][8] = total paa
    # , [i][9] = home paa, [i][10] = away paa, [i][11] = home or away, [i][12] = expected points,
    # [i][13] = expected total

    # create list of the possible points

    possiblePoints = []
    p = 0
    while True:
        if p < 21:
            possiblePoints.append(int(p))
            p += 1
            continue
        else:
            break

    print(possiblePoints)

    print('Created List of Possible Points')

    # Poisson for range for each team, EXPECTED = 12, EXP TOTAL = 13
    poissonAway = []
    poissonHome = []

    i = 0
    p = 0
    h = i + 1
    while True:
        if p < len(possiblePoints) and i < len(mlb):
            # print(mlb[i][0])
            # print(len(mlb[i][0]))
            expectA = float(mlb[i][0][60])  # was 49
            # print(mlb[i][1])
            # print(len(mlb[i][1]))
            expectH = float(mlb[i][1][60])
            # print(expectA)
            # print(expectH)
            # print(possiblePoints[p])
            chancePerScoreAway = (
                (expectA**(possiblePoints[p])) * (math.exp(-expectA)) / math.factorial(possiblePoints[p]))
            poissonAway.append(chancePerScoreAway)
            # print(poissonAway)
            chancePerScoreHome = (
                (expectH**(possiblePoints[p])) * (math.exp(-expectH)) / math.factorial(possiblePoints[p]))
            poissonHome.append(chancePerScoreHome)
            # print(poissonHome)
            p += 1
            continue
        elif len(poissonAway) == len(possiblePoints):
            if i < len(mlb):
                mlb[i][0].append(poissonAway)  # temporary index [62]
                # print('length of away team list = ' + str(len(mlb[i][0])))
                # print(mlb[i][0])
                mlb[i][1].append(poissonHome)
                # print('length of home team list = ' + str(len(mlb[i][1])))
                # print(print(mlb[i][1]))
                p = 0
                i += 1
                poissonAway = []
                poissonHome = []
                continue
            else:
                break
        else:
            break

    print('Poisson Distributions Completed')

    h = 0
    a = 0
    x = 0
    while True:  # poisson
        if x < len(mlb):
            for i in range(100000):
                q = np.asarray(possiblePoints)
                # print(mlb[x][0][51])
                # print(mlb[x][1][51])
                awayArray_poisson = np.asarray(mlb[x][0][62])
                homeArray_poisson = np.asarray(mlb[x][1][62])
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
            mlb[x][0].append(a)  # CALC Chance = new index [62]
            mlb[x][1].append(h)
            del mlb[x][0][62]  # delete poisson array from lists
            del mlb[x][1][62]
            x += 1
            h = 0
            a = 0
            continue
        else:
            break
    print('\n')
    print('Chances Calculated for Each Team')
    print('length of MLB list after calculating chances is ' + str(len(mlb)))

    # print('\n')
    # for elem in mlb:
    #     for el in elem:
    #         print(el)
    #         # print('\n')
    #     print('\n')

    # Need to scrape chances from FTE and NF

    today_nf = date.today()
    tomorrow_nf = today_nf + timedelta(1)
    twodays_nf = today_nf + timedelta(2)
    threedays_nf = today_nf + timedelta(3)
    fourdays_nf = today_nf + timedelta(4)
    fivedays_nf = today_nf + timedelta(5)
    i = 0
    g = 0
    s = 0
    nf_MLB = []
    nf_MLB_today = []
    nf_MLB_tomorrow = []
    nf_MLB_twodays = []
    nf_MLB_threedays = []
    nf_MLB_fourdays = []
    nf_MLB_fivedays = []
    while True:  # list of Numberfire's projected winners and % chances
        if i == 0:
            url_today = url_nf + str(today_nf)
            html_today = requests.get(url_today)
            soup_today = bs4.BeautifulSoup(
                html_today.content, features='html.parser')
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_today):
                i += 1
                continue
            scrapeNumberfireNCAAB_today = soup_today.findAll(
                'div', attrs={'class': 'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_today):
                nf_MLB_today.append(str(scrapeNumberfireNCAAB_today[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_today):
                    # print(nf_MLB_today[g])
                    # print('\n')
                    teamname = nf_MLB_today[g][265:281]  # used to be 265:275
                    # print(teamname)
                    # print('\n')
                    percent = nf_MLB_today[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    teamname = rename(teamname)
                    nf_MLB.append(teamname)
                    nf_MLB.append(percent)
                    nf_MLB.append(str(today))
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    # print("TODAY Numberfire Loop Complete")
                    continue
        elif i == 1:
            url_tomorrow = url_nf + str(tomorrow_nf)
            html_tomorrow = requests.get(url_tomorrow)
            soup_tomorrow = bs4.BeautifulSoup(
                html_tomorrow.content, features='html.parser')
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_tomorrow):
                i += 1
                continue
            scrapeNumberfireNCAAB_tomorrow = soup_tomorrow.findAll(
                'div', attrs={'class': 'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_tomorrow):
                nf_MLB_tomorrow.append(str(scrapeNumberfireNCAAB_tomorrow[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_tomorrow):
                    teamname = nf_MLB_tomorrow[g][265:275]
                    percent = nf_MLB_tomorrow[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    teamname = rename(teamname)
                    nf_MLB.append(teamname)
                    nf_MLB.append(percent)
                    nf_MLB.append(str(tomorrow))
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    # print("TOMORROW Numberfire Loop Complete")
                    continue
        elif i == 2:
            url_twodays = url_nf + str(twodays_nf)
            html_twodays = requests.get(url_twodays)
            soup_twodays = bs4.BeautifulSoup(
                html_twodays.content, features='html.parser')
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_twodays):
                i += 1
                continue
            scrapeNumberfireNCAAB_twodays = soup_twodays.findAll(
                'div', attrs={'class': 'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_twodays):
                nf_MLB_twodays.append(str(scrapeNumberfireNCAAB_twodays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_twodays):
                    teamname = nf_MLB_twodays[g][265:275]
                    percent = nf_MLB_twodays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    teamname = rename(teamname)
                    nf_MLB.append(teamname)
                    nf_MLB.append(percent)
                    nf_MLB.append(str(twodays))
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    # print("TWODAYS Numberfire Loop Complete")
                    continue
        elif i == 3:
            url_threedays = url_nf + str(threedays_nf)
            html_threedays = requests.get(url_threedays)
            soup_threedays = bs4.BeautifulSoup(
                html_threedays.content, features='html.parser')
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_threedays):
                i += 1
                continue
            scrapeNumberfireNCAAB_threedays = soup_threedays.findAll(
                'div', attrs={'class': 'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_threedays):
                nf_MLB_threedays.append(
                    str(scrapeNumberfireNCAAB_threedays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_threedays):
                    teamname = nf_MLB_threedays[g][265:275]
                    percent = nf_MLB_threedays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    teamname = rename(teamname)
                    nf_MLB.append(teamname)
                    nf_MLB.append(percent)
                    nf_MLB.append(str(threedays))
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    # print("THREEDAYS Numberfire Loop Complete")
                    continue
        elif i == 4:
            url_fourdays = url_nf + str(fourdays_nf)
            html_fourdays = requests.get(url_fourdays)
            soup_fourdays = bs4.BeautifulSoup(
                html_fourdays.content, features='html.parser')
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_fourdays):
                i += 1
                continue
            scrapeNumberfireNCAAB_fourdays = soup_fourdays.findAll(
                'div', attrs={'class': 'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_fourdays):
                nf_MLB_fourdays.append(str(scrapeNumberfireNCAAB_fourdays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_fourdays):
                    teamname = nf_MLB_fourdays[g][265:275]
                    percent = nf_MLB_fourdays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    teamname = rename(teamname)
                    nf_MLB.append(teamname)
                    nf_MLB.append(percent)
                    nf_MLB.append(str(fourdays))
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    # print("FOURDAYS Numberfire Loop Complete")
                    continue
        elif i == 5:
            url_fivedays = url_nf + str(fivedays_nf)
            html_fivedays = requests.get(url_fivedays)
            soup_fivedays = bs4.BeautifulSoup(
                html_fivedays.content, features='html.parser')
            if 'Game projections for today are not yet available. Check back soon.' in str(soup_fivedays):
                i += 1
                continue
            scrapeNumberfireNCAAB_fivedays = soup_fivedays.findAll(
                'div', attrs={'class': 'win-probability-wrap'})
            if s < len(scrapeNumberfireNCAAB_fivedays):
                nf_MLB_fivedays.append(str(scrapeNumberfireNCAAB_fivedays[s]))
                s += 1
                continue
            else:
                if g < len(scrapeNumberfireNCAAB_fivedays):
                    teamname = nf_MLB_fivedays[g][265:275]
                    percent = nf_MLB_fivedays[g][200:215]
                    teamname = teamname.replace(' ', '')
                    percent = percent.replace(' ', '')
                    percent = percent[0:4]
                    percent = float(percent)
                    teamname = rename(teamname)
                    nf_MLB.append(teamname)
                    nf_MLB.append(percent)
                    nf_MLB.append(str(fivedays))
                    g += 1
                    continue
                else:
                    s = 0
                    g = 0
                    i += 1
                    # print("FIVEDAYS Numberfire Loop Complete")
                    continue
        else:
            break
    print('\n')
    # for elem in nf_MLB:
    #     print(elem)
    # print('\n')

    mlb_nf = []
    i = 0
    while True:
        if i < len(nf_MLB):
            team = nf_MLB[i]
            chance = float(nf_MLB[i + 1])
            day = str(nf_MLB[i + 2])
            team_and_day_string = str(team) + ' ' + str(day)
            lst = [team_and_day_string, chance]
            mlb_nf.append(lst)
            del nf_MLB[0]
            del nf_MLB[0]
            del nf_MLB[0]
            continue
        else:
            break

    # print('\n')
    # print('NUMBERFIRE CHANCES')
    # for elem in mlb_nf:
    #     print(elem)
    # print('\n')

    dict_nf = {x[0]: x[1:] for x in mlb_nf}
    keys_nf = (dict_nf.keys())
    # print('NUMBERFIRE KEYS')
    # print(keys_nf)
    # print('\n')

    # print('about to add numberfire chances to MLB')
    # print('current length of mlb list is ' + str(len(mlb)))
    i = 0
    while True:
        if i < len(mlb):
            awayTeam = mlb[i][0][0]
            homeTeam = mlb[i][1][0]
            day = str(mlb[i][2])
            away = str(awayTeam) + ' ' + str(day)
            home = str(homeTeam) + ' ' + str(day)
            if away in keys_nf:
                awayChance = dict_nf[away]
                awayChance = float(awayChance[0])
                homeChance = float(round(100 - awayChance, 2))
                mlb[i][0].append(awayChance)
                mlb[i][1].append(homeChance)
                i += 1
                continue
            elif home in keys_nf:
                homeChance = dict_nf[home]
                homeChance = float(homeChance[0])
                awayChance = float(round(100 - homeChance, 2))
                mlb[i][0].append(awayChance)
                mlb[i][1].append(homeChance)
                i += 1
                continue
            else:
                awayChance = 'n/a'
                homeChance = 'n/a'
                mlb[i][0].append(awayChance)
                mlb[i][1].append(homeChance)
                i += 1
                continue
        else:
            break

    # print('beginning to read FTE')

    df_fte = pd.read_html(
        'https://projects.fivethirtyeight.com/2022-mlb-predictions/games/')
    fte_mlb = df_fte[0].values.tolist()
    # print('got FTE dataframe')
    # for elem in fte_mlb:
    # print(elem)
    # print('\n')
    i = 0
    while True:
        if i < len(fte_mlb):
            if 'Monday' in fte_mlb[i][0]:
                day = str(fte_mlb[i][0])
                ind = day.index('Monday')
                backslash = day.index('/')
                m = day[:backslash]
                if int(m) >= 4:
                    y = '2022'
                if int(m) < 4:
                    y = '2023'
                if len(m) == 1:
                    m = '0' + str(m)
                d = day[backslash + 1: ind]
                if len(d) == 1:
                    d = '0' + str(d)
                game_date = str(y) + str(m) + str(d)
                team = rename(fte_mlb[i][1])
                chance = fte_mlb[i][7]
                percent_index = chance.index('%')
                chance = chance[:percent_index]
                chance = float(chance)
                team_and_date = str(team) + ' ' + str(game_date)
                lst = [team_and_date, chance]
                fte_mlb[i] = lst
                i += 1
                continue
            if 'Tuesday' in fte_mlb[i][0]:
                day = str(fte_mlb[i][0])
                ind = day.index('Tuesday')
                backslash = day.index('/')
                m = day[:backslash]
                if int(m) >= 4:
                    y = '2022'
                if int(m) < 4:
                    y = '2023'
                if len(m) == 1:
                    m = '0' + str(m)
                d = day[backslash + 1: ind]
                if len(d) == 1:
                    d = '0' + str(d)
                game_date = str(y) + str(m) + str(d)
                team = rename(fte_mlb[i][1])
                chance = fte_mlb[i][7]
                percent_index = chance.index('%')
                chance = chance[:percent_index]
                chance = float(chance)
                team_and_date = str(team) + ' ' + str(game_date)
                lst = [team_and_date, chance]
                fte_mlb[i] = lst
                i += 1
                continue
            if 'Wednesday' in fte_mlb[i][0]:
                day = str(fte_mlb[i][0])
                ind = day.index('Wednesday')
                backslash = day.index('/')
                m = day[:backslash]
                if int(m) >= 4:
                    y = '2022'
                if int(m) < 4:
                    y = '2023'
                if len(m) == 1:
                    m = '0' + str(m)
                d = day[backslash + 1: ind]
                if len(d) == 1:
                    d = '0' + str(d)
                game_date = str(y) + str(m) + str(d)
                team = rename(fte_mlb[i][1])
                chance = fte_mlb[i][7]
                percent_index = chance.index('%')
                chance = chance[:percent_index]
                chance = float(chance)
                team_and_date = str(team) + ' ' + str(game_date)
                lst = [team_and_date, chance]
                fte_mlb[i] = lst
                i += 1
                continue
            if 'Thursday' in fte_mlb[i][0]:
                day = str(fte_mlb[i][0])
                ind = day.index('Thursday')
                backslash = day.index('/')
                m = day[:backslash]
                if int(m) >= 4:
                    y = '2022'
                if int(m) < 4:
                    y = '2023'
                if len(m) == 1:
                    m = '0' + str(m)
                d = day[backslash + 1: ind]
                if len(d) == 1:
                    d = '0' + str(d)
                game_date = str(y) + str(m) + str(d)
                team = rename(fte_mlb[i][1])
                chance = fte_mlb[i][7]
                percent_index = chance.index('%')
                chance = chance[:percent_index]
                chance = float(chance)
                team_and_date = str(team) + ' ' + str(game_date)
                lst = [team_and_date, chance]
                fte_mlb[i] = lst
                i += 1
                continue
            if 'Friday' in fte_mlb[i][0]:
                day = str(fte_mlb[i][0])
                ind = day.index('Friday')
                backslash = day.index('/')
                m = day[:backslash]
                if int(m) >= 4:
                    y = '2022'
                if int(m) < 4:
                    y = '2023'
                if len(m) == 1:
                    m = '0' + str(m)
                d = day[backslash + 1: ind]
                if len(d) == 1:
                    d = '0' + str(d)
                game_date = str(y) + str(m) + str(d)
                team = rename(fte_mlb[i][1])
                chance = fte_mlb[i][7]
                percent_index = chance.index('%')
                chance = chance[:percent_index]
                chance = float(chance)
                team_and_date = str(team) + ' ' + str(game_date)
                lst = [team_and_date, chance]
                fte_mlb[i] = lst
                i += 1
                continue
            if 'Saturday' in fte_mlb[i][0]:
                day = str(fte_mlb[i][0])
                ind = day.index('Saturday')
                backslash = day.index('/')
                m = day[:backslash]
                if int(m) >= 4:
                    y = '2022'
                if int(m) < 4:
                    y = '2023'
                if len(m) == 1:
                    m = '0' + str(m)
                d = day[backslash + 1: ind]
                if len(d) == 1:
                    d = '0' + str(d)
                game_date = str(y) + str(m) + str(d)
                team = rename(fte_mlb[i][1])
                chance = fte_mlb[i][7]
                percent_index = chance.index('%')
                chance = chance[:percent_index]
                chance = float(chance)
                team_and_date = str(team) + ' ' + str(game_date)
                lst = [team_and_date, chance]
                fte_mlb[i] = lst
                i += 1
                continue
            if 'Sunday' in fte_mlb[i][0]:
                day = str(fte_mlb[i][0])
                ind = day.index('Sunday')
                backslash = day.index('/')
                m = day[:backslash]
                if int(m) >= 4:
                    y = '2022'
                if int(m) < 4:
                    y = '2023'
                if len(m) == 1:
                    m = '0' + str(m)
                d = day[backslash + 1: ind]
                if len(d) == 1:
                    d = '0' + str(d)
                game_date = str(y) + str(m) + str(d)
                team = rename(fte_mlb[i][1])
                chance = fte_mlb[i][7]
                percent_index = chance.index('%')
                chance = chance[:percent_index]
                chance = float(chance)
                team_and_date = str(team) + ' ' + str(game_date)
                lst = [team_and_date, chance]
                fte_mlb[i] = lst
                i += 1
                continue
        else:
            break

    dict_fte = {x[0]: x[1:] for x in fte_mlb}
    # print(dict_fte)
    # print('\n')
    keys_fte = (dict_fte.keys())

    # print('adding FTE chances to list:')
    # print('i = 0 is less than the length of the mlb list @ ' + str(len(mlb)))
    i = 0
    while True:
        if i < len(mlb):
            awayTeam = mlb[i][0][0]
            homeTeam = mlb[i][1][0]
            day = str(mlb[i][2])
            away = str(awayTeam) + ' ' + str(day)
            home = str(homeTeam) + ' ' + str(day)
            if away in keys_fte and home in keys_fte:
                awayChance = dict_fte[away]
                awayChance = float(awayChance[0])
                homeChance = dict_fte[home]
                homeChance = float(homeChance[0])
                mlb[i][0].append(awayChance)  # index [71]
                mlb[i][1].append(homeChance)
                # print(mlb[i][0])
                # print(mlb[i][1])
                i += 1
                continue
            else:
                awayChance = 'n/a'
                homeChance = 'n/a'
                mlb[i][0].append(awayChance)
                mlb[i][1].append(homeChance)
                # print(mlb[i][0])
                # print(mlb[i][1])
                i += 1
                continue
        else:
            break

    i = 0
    while True:
        if i < len(mlb):
            # print('mlb[i][0]')
            # print(mlb[i][0])
            # print('mlb[i][1]')
            # print(mlb[i][1])
            away_calc_chance = mlb[i][0][62]
            # print('away_calc_chance = ' + str(away_calc_chance))
            away_nf_chance = mlb[i][0][63]
            # print('away_nf_chance = ' + str(away_nf_chance))
            away_fte_chance = mlb[i][0][64]
            # print('away_fte_chance = ' + str(away_fte_chance))
            home_calc_chance = mlb[i][1][62]
            # print('home_calc_chance = ' + str(home_calc_chance))
            home_nf_chance = mlb[i][1][63]
            # print('home_nf_chance = ' + str(home_nf_chance))
            home_fte_chance = mlb[i][1][64]
            # print('home_fte_chance = ' + str(home_fte_chance))
            if away_nf_chance == 'n/a' and away_fte_chance == 'n/a':
                away_avg = away_calc_chance
            if away_nf_chance == 'n/a' and away_fte_chance != 'n/a':
                away_avg = round((float(away_calc_chance) +
                                 float(away_fte_chance)) / 2, 2)
            if away_nf_chance != 'n/a' and away_fte_chance == 'n/a':
                away_avg = round((float(away_calc_chance) +
                                 float(away_nf_chance)) / 2, 2)
            if away_nf_chance != 'n/a' and away_fte_chance != 'n/a':
                # (float(away_calc_chance) + float(away_nf_chance) + float(away_fte_chance)) / 3
                away_avg = round(
                    (float(away_calc_chance) + float(away_nf_chance) + float(away_fte_chance)) / 3, 2)
            if home_nf_chance == 'n/a' and home_fte_chance == 'n/a':
                home_avg = home_calc_chance
            if home_nf_chance == 'n/a' and home_fte_chance != 'n/a':
                home_avg = round((float(home_calc_chance) +
                                 float(home_fte_chance)) / 2, 2)
            if home_nf_chance != 'n/a' and home_fte_chance == 'n/a':
                home_avg = round((float(home_calc_chance) +
                                 float(home_nf_chance)) / 2, 2)
            if home_nf_chance != 'n/a' and home_fte_chance != 'n/a':
                # (float(home_calc_chance) + float(home_nf_chance) + float(home_fte_chance)) / 3
                home_avg = round(
                    (float(home_calc_chance) + float(home_nf_chance) + float(home_fte_chance)) / 3, 2)
            mlb[i][0].append(away_avg)  # index [65]
            mlb[i][1].append(home_avg)
            i += 1
            continue
        else:
            break

    i = 0
    while True:
        if i < len(mlb):
            awayTeam = mlb[i][0][0]
            homeTeam = mlb[i][1][0]
            day = str(mlb[i][2])
            away = str(awayTeam) + ' ' + str(day)
            home = str(homeTeam) + ' ' + str(day)
            # home_team = dk_df.loc[dk_df['Team'] == homeTeam, 'homeTeam'].iloc[0]
            if away in keys_dk_data and home in keys_dk_data:
                awayOdds = dict_dk_data[away]
                homeOdds = dict_dk_data[home]
                mlb[i][0] = mlb[i][0] + awayOdds
                mlb[i][1] = mlb[i][1] + homeOdds
                print(mlb[i])
                i += 1
                continue
            else:
                i += 1
                continue
        else:
            break

    temp_headers = ['team', 'pts_for', 'pts_ag', 'runs', 'total',
                    'calc%', 'nf%', 'fte%', 'avg%']  # 66     67     68        69     70
    temp_headers_1 = ['team', 'pts_for', 'pts_ag', 'runs', 'total',
                      'calc%', 'nf%', 'fte%', 'avg%', 'spr', 'spr_o', 'o/u', 'o/u_o', 'ml']
    temp_headers_2 = ['team', 'pts_for', 'pts_ag', 'runs', 'total', 'calc%', 'nf%', 'fte%', 'avg%',
                      'spr', 'spr_o', 'o/u', 'o/u_o', 'ml', 'avg_V', 'calc_V', 'nf_V', 'fte_V', 'consensus']

    headers = ['Team', 'Avg_Runs', 'Home_Avg_Runs', 'Away_Avg_Runs', 'Last_Yr_Avg_Runs',
               'Opp_Runs', 'Home_Opp_Runs', 'Away_Opp_Runs', 'Last_Yr_Opp_Runs', 'Park_Factor',
               'wOBACon', 'BACON', 'R', 'OBP', 'H',
               '1B', '2B', '3B', 'HR', 'BB',
               'SO', 'PA', 'RL_Wins', 'RL_Losses', 'RL_ERA',
               'RL_Games', 'RL_Saves', 'RL_Save_Opps', 'RL_Innings_Pitched', 'RL_Hits',
               'RL_Runs', 'RL_Earned_Runs', 'RL_Homers', 'RL_Hit_Batters', 'RL_BB',
               'RL_Ks', 'RL_WHIP', 'RL_Hits_per_At_Bat', 'Starter', 'RHP/LHP',
               'Wins', 'Losses', 'Innings Pitched', 'ERA', 'BB/Walks',
               "K's", 'WHIP', 'games_played', 'starts', 'qual_starts',
               'saves', 'holds', 'hits', 'earned_runs', 'homers',
               'ks_per_9', 'pitches_per_start', 'WAR', 'ipg', 'runs_against',
               'calc_runs', 'calc_total', 'calc%', 'nf%', 'fte%',
               'avg%', 'spr', 'spr_o', 'o/u', 'o/u_o',
               'ml', 'avg_V', 'calc_V', 'nf_V', 'fte_V',
               'consensus']

    mlb_df = []
    mlb_today = []
    mlb_tomorrow = []
    mlb_twodays = []
    mlb_threedays = []
    mlb_fourdays = []
    mlb_fivedays = []

    i = 0
    while True:
        if i < len(mlb):
            if str(mlb[i][2]) == str(today):
                awayTeam = mlb[i][0]
                homeTeam = mlb[i][1]
                mlb_today.append(awayTeam)
                mlb_today.append(homeTeam)
                mlb_df.append(awayTeam)
                mlb_df.append(homeTeam)
                i += 1
                continue
            if str(mlb[i][2]) == str(tomorrow):
                awayTeam = mlb[i][0]
                homeTeam = mlb[i][1]
                mlb_tomorrow.append(awayTeam)
                mlb_tomorrow.append(homeTeam)
                mlb_df.append(awayTeam)
                mlb_df.append(homeTeam)
                i += 1
                continue
            if str(mlb[i][2]) == str(twodays):
                awayTeam = mlb[i][0]
                homeTeam = mlb[i][1]
                mlb_twodays.append(awayTeam)
                mlb_twodays.append(homeTeam)
                mlb_df.append(awayTeam)
                mlb_df.append(homeTeam)
                i += 1
                continue
            if str(mlb[i][2]) == str(threedays):
                awayTeam = mlb[i][0]
                homeTeam = mlb[i][1]
                mlb_threedays.append(awayTeam)
                mlb_threedays.append(homeTeam)
                mlb_df.append(awayTeam)
                mlb_df.append(homeTeam)
                i += 1
                continue
            if str(mlb[i][2]) == str(fourdays):
                awayTeam = mlb[i][0]
                homeTeam = mlb[i][1]
                mlb_fourdays.append(awayTeam)
                mlb_fourdays.append(homeTeam)
                mlb_df.append(awayTeam)
                mlb_df.append(homeTeam)
                i += 1
                continue
            if str(mlb[i][2]) == str(fivedays):
                awayTeam = mlb[i][0]
                homeTeam = mlb[i][1]
                mlb_fivedays.append(awayTeam)
                mlb_fivedays.append(homeTeam)
                mlb_df.append(awayTeam)
                mlb_df.append(homeTeam)
                i += 1
                continue
        else:
            break

    def value(lst):
        i = 0
        c = 0
        while True:
            if i < len(lst):
                if len(lst[i]) == 71:  # was == 14
                    print(lst[i][70])
                    if int(lst[i][70]) < 0:
                        print(lst[i])
                        print('\n')
                        avg_chance = lst[i][65]
                        avg_chance_num = avg_chance / 100
                        avg_chance_num = round(avg_chance_num, 2)
                        moneyline = np.nan_to_num(lst[i][70])
                        moneyline = int(moneyline)
                        moneyline_pos = moneyline * -1
                        value = avg_chance_num * \
                            (10 + 10 / (moneyline_pos / 10) * 10)
                        value = round(value, 3)
                        lst[i].append(value)  # creates [i][71] = avg value
                        name = lst[i][0]
                        calc_chance = lst[i][62]
                        calc_chance_num = calc_chance / 100
                        calc_chance_num = round(calc_chance_num, 2)
                        nf_chance = lst[i][63]
                        nf_chance_num = float(nf_chance) / 100
                        nf_chance_num = round(nf_chance_num, 2)
                        fte_chance = lst[i][64]
                        fte_chance_num = fte_chance / 100
                        fte_chance_num = round(fte_chance_num, 2)
                        calc_value = calc_chance_num * \
                            (10 + 10 / (moneyline_pos / 10) * 10)
                        calc_value = round(calc_value, 3)
                        # creates [i][72] = calculated value
                        lst[i].append(calc_value)
                        nf_value = nf_chance_num * \
                            (10 + 10 / (moneyline_pos / 10) * 10)
                        nf_value = round(nf_value, 3)
                        # creates [i][73] = numberfire value
                        lst[i].append(nf_value)
                        fte_value = fte_chance_num * \
                            (10 + 10 / (moneyline_pos / 10) * 10)
                        fte_value = round(fte_value, 3)
                        lst[i].append(fte_value)  # creates [i][74] = fte value
                        if calc_value > 10:
                            c = '+'
                        if calc_value < 10:
                            c = '-'
                        if calc_value == 10:
                            c = '='
                        if nf_value > 10:
                            n = '+'
                        if nf_value < 10:
                            n = '-'
                        if nf_value == 10:
                            n = '='
                        if fte_value > 10:
                            f = '+'
                        if fte_value < 10:
                            f = '-'
                        if fte_value == 10:
                            f = '='
                        lst[i].append(c + n + f)  # creates [i][75] = consensus
                        i += 1
                        continue
                    else:
                        moneyline = np.nan_to_num(lst[i][70])
                        moneyline = int(moneyline)
                        avg_chance = lst[i][65]
                        avg_chance_num = avg_chance / 100
                        avg_chance_num = round(avg_chance_num, 2)
                        value = (moneyline / 100 * 10 + 10) * avg_chance_num
                        value = round(value, 3)
                        lst[i].append(value)  # creates [i][71] = avg value
                        name = lst[i][0]
                        calc_chance = lst[i][62]
                        calc_chance_num = calc_chance / 100
                        calc_chance_num = round(calc_chance_num, 2)
                        nf_chance = lst[i][63]
                        nf_chance_num = float(nf_chance) / 100
                        nf_chance_num = round(nf_chance_num, 2)
                        fte_chance = lst[i][64]
                        fte_chance_num = fte_chance / 100
                        fte_chance_num = round(fte_chance_num, 2)
                        calc_value = (moneyline / 100 * 10 +
                                      10) * calc_chance_num
                        calc_value = round(calc_value, 3)
                        # creates [i][72] = calculated value
                        lst[i].append(calc_value)
                        nf_value = (moneyline / 100 * 10 + 10) * nf_chance_num
                        nf_value = round(nf_value, 3)
                        # creates [i][73] = numberfire value
                        lst[i].append(nf_value)
                        fte_value = (moneyline / 100 * 10 + 10) * \
                            fte_chance_num
                        fte_value = round(fte_value, 3)
                        lst[i].append(fte_value)  # creates [i][74] = fte value
                        if calc_value > 10:
                            c = '+'
                        if calc_value < 10:
                            c = '-'
                        if calc_value == 10:
                            c = '='
                        if nf_value > 10:
                            n = '+'
                        if nf_value < 10:
                            n = '-'
                        if nf_value == 10:
                            n = '='
                        if fte_value > 10:
                            f = '+'
                        if fte_value < 10:
                            f = '-'
                        if fte_value == 10:
                            f = '='
                        lst[i].append(c + n + f)  # creates [i][75] = consensus
                        i += 1
                        continue
                else:
                    i += 1
                    continue
            else:
                break
        return lst

    def mlb_spreadsheet_prep(lst):
        i = 0
        while True:
            if i < len(lst):
                if len(lst[i]) < 76:
                    x = len(lst[i])
                    fill = 76 - x
                    hash_list = []
                    b = 0
                    while True:
                        if b < fill:
                            hash_list = hash_list + [0]
                            b += 1
                            continue
                        else:
                            break
                    lst[i] = lst[i] + hash_list
                    i += 1
                    continue
                else:
                    i += 1
                    continue
            else:
                break
        return lst

    mlb_today = value(mlb_today)
    # for elem in mlb_today:
    #     print(elem)
    mlb_tomorrow = value(mlb_tomorrow)
    mlb_twodays = value(mlb_twodays)
    mlb_threedays = value(mlb_threedays)
    mlb_fourdays = value(mlb_fourdays)
    mlb_fivedays = value(mlb_fivedays)
    mlb_df = value(mlb_df)

    mlb_today = mlb_spreadsheet_prep(mlb_today)
    mlb_tomorrow = mlb_spreadsheet_prep(mlb_tomorrow)
    mlb_twodays = mlb_spreadsheet_prep(mlb_twodays)
    mlb_threedays = mlb_spreadsheet_prep(mlb_threedays)
    mlb_fourdays = mlb_spreadsheet_prep(mlb_fourdays)
    mlb_fivedays = mlb_spreadsheet_prep(mlb_fivedays)
    mlb_df = mlb_spreadsheet_prep(mlb_df)

    mlb_today = sorted(mlb_today, key=itemgetter(71), reverse=True)
    mlb_tomorrow = sorted(mlb_tomorrow, key=itemgetter(71), reverse=True)
    mlb_twodays = sorted(mlb_twodays, key=itemgetter(71), reverse=True)
    mlb_threedays = sorted(mlb_threedays, key=itemgetter(71), reverse=True)
    mlb_fourdays = sorted(mlb_fourdays, key=itemgetter(71), reverse=True)
    mlb_fivedays = sorted(mlb_fivedays, key=itemgetter(71), reverse=True)

    # headers = ['Team', 'Avg_Runs', 'Home_Avg_Runs', 'Away_Avg_Runs', 'Last_Yr_Avg_Runs',
    #         'Opp_Runs', 'Home_Opp_Runs', 'Away_Opp_Runs', 'Last_Yr_Opp_Runs', 'Park_Factor',
    #         'wOBACon', 'BACON', 'R', 'OBP', 'H',
    #         '1B', '2B', '3B', 'HR', 'BB',
    #         'SO', 'PA', 'Bullpen_Games_Played', 'Bullpen_Wins', 'Bullpen_Losses',
    #         'Bullpen_ERA', 'Bullpen_Saves', 'Bullpen_Complete_Games', 'Bullpen_Shutouts', 'BP_Quality_Starts',
    #         'BP_Innings_Pitched', 'BP_Hits', 'BP_Earned_Runs', 'BP_HRs', 'BP_Walks',
    #         'BP_Ks', 'BP_Opponent_Batting_Avg', 'BP_WHIP', 'Starter', 'RHP/LHP',
    #         'Wins', 'Losses', 'Innings Pitched', 'ERA', 'BB/Walks',
    #         "K's", 'WHIP', 'games_played', 'starts', 'qual_starts',
    #         'saves', 'holds', 'hits', 'earned_runs', 'homers',
    #         'ks_per_9', 'pitches_per_start', 'WAR', 'ipg', 'runs_against',
    #         'calc_runs', 'calc_total', 'calc%', 'nf%', 'fte%',
    #         'avg%', 'spr', 'spr_o', 'o/u', 'o/u_o',
    #         'ml', 'avg_V', 'calc_V', 'nf_V', 'fte_V',
    #         'consensus']

    df_mlb_today = pd.DataFrame(mlb_today, columns=headers)
    df_mlb_tomorrow = pd.DataFrame(mlb_tomorrow, columns=headers)
    df_mlb_twodays = pd.DataFrame(mlb_twodays, columns=headers)
    df_mlb_threedays = pd.DataFrame(mlb_threedays, columns=headers)
    df_mlb_fourdays = pd.DataFrame(mlb_fourdays, columns=headers)
    df_mlb_fivedays = pd.DataFrame(mlb_fivedays, columns=headers)
    df_mlb = pd.DataFrame(mlb_df, columns=headers)

    lst = ['Team', 'Starter', 'RHP/LHP', 'calc_runs', 'calc_total', 'ml', 'calc%',
           'nf%', 'fte%', 'avg%', 'avg_V', 'calc_V', 'nf_V', 'fte_V', 'consensus']

    df_mlb_today = df_mlb_today[lst]
    df_mlb_tomorrow = df_mlb_tomorrow[lst]
    df_mlb_twodays = df_mlb_twodays[lst]
    df_mlb_threedays = df_mlb_threedays[lst]
    df_mlb_fourdays = df_mlb_fourdays[lst]
    df_mlb_fivedays = df_mlb_fivedays[lst]

    with pd.ExcelWriter('/Users/Hayden/OneDrive/Sports Betting/Baseball/MLB.xlsx') as writer:  # doctest: +SKIP
        df_mlb_today.to_excel(writer, sheet_name=str(today), index=False)
        df_mlb_tomorrow.to_excel(writer, sheet_name=str(tomorrow), index=False)
        df_mlb_twodays.to_excel(writer, sheet_name=str(twodays), index=False)
        df_mlb_threedays.to_excel(
            writer, sheet_name=str(threedays), index=False)
        df_mlb_fourdays.to_excel(writer, sheet_name=str(fourdays), index=False)
        df_mlb_fivedays.to_excel(writer, sheet_name=str(fivedays), index=False)
        df_mlb.to_excel(writer, sheet_name='MLB')

    conn = sqlite3.connect('MLB.db')

    df_mlb.to_sql(name='MLB', con=conn, if_exists='replace', index=False)

    conn.commit()

    return


mlb()


# schedule.every(6).hours.do(mlb)

# while True:
#     schedule.run_pending()
