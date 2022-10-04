import sys
import os
import datetime
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
import lxml
import schedule
import pyderman as dr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
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

def firstFG():
    start_time = time.perf_counter()

    #class="sportsbook-outcome-cell__label"
    dk_browser0 = webdriver.Chrome() # dk_browser0.quit()
    dk_browser0.get('https://sportsbook.draftkings.com/leagues/basketball/88670846?category=player-props&subcategory=first-fg')
    time.sleep(20)
    dkplayers = dk_browser0.find_elements(By.CLASS_NAME, 'sportsbook-outcome-body-wrapper')
    # sportsbook-outcome-body-wrapper


    # dk_ffg = []
    # for elem in dkplayers:
    #     txt = elem.text
    #     txt = txt.split('\n')
    #     dk_ffg.append(txt)

    dk_ffg = []
    for elem in dkplayers:
        txt = elem.text
        txt = txt.split('\n')
        lng = len(txt)
        end = lng - 1
        a = 0
        while True:
            if a < lng:
                dk_ffg.append(txt[a])
                a += 1
                continue
            else:
                break


    dk_firstFG = []
    i = 0
    h = i + 1
    while True:
        if h < len(dk_ffg):
            print('name = ' + str(dk_ffg[i]))
            name = dk_ffg[i]
            print('odds = ' + str(dk_ffg[h]))
            odds = int(dk_ffg[h])
            player = [name, odds]
            dk_firstFG.append(player)
            i += 2
            h = i + 1
            continue
        else:
            break

    # for elem in dk_ffg:
    #     print(elem)
        
    dict_dk_firstFG = {x[0]:x[1:] for x in dk_firstFG}
    ffg_odds_keys = (dict_dk_firstFG.keys())

    print(dict_dk_firstFG)
    print('\n')
    print(ffg_odds_keys)

    dk_browser0.quit()

    # First 2021/22 NBA Game ID - 401358773
    today = date.today()
    tomorrow = today + timedelta(1)
    day_zero = datetime.date(2021, 10, 19)



    game_ids = []
    x = 0
    while True:
        day = day_zero + timedelta(x)
        if day < today:
            day = str(day)
            day = day.replace('-', '')
            url_espn_scoreboard = 'https://www.espn.com/nba/scoreboard/_/date/' + str(day)
            #print(url_espn_scoreboard)
            html_espn_scoreboard = requests.get(url_espn_scoreboard)
            soup_espn_scoreboard = bs4.BeautifulSoup(html_espn_scoreboard.content, features='html.parser')
            for sectiontag in soup_espn_scoreboard.findAll('div', {'class': 'Scoreboard__Callouts flex flex-column ph4 mv4 items-center'}):
                tag = str(sectiontag)
                ind_0 = 198
                ind_1 = ind_0 + 9
                game_id = tag[ind_0:ind_1]
                game_ids.append(game_id) 
            x += 1
            continue
        else:
            break

    #print(soup_espn_scoreboard)

    # for elem in game_ids:
    #     print(elem)

    length_game_ids = len(game_ids)

    # <div class="ScoreCell__Link" data-game-link="true"><div class="ScoreCell__Link__Event__Detail"><a href="/nba/game/_/gameId/401358773" class="ScoreCell__CompetitorDetails"><ul class="ScoreCell__Competitors"><li class="ScoreCell__Item ScoreCell__Item--away ScoreCell__Item--loser"><img alt="" class="Image Logo ScoreCell__Logo mr3 Logo__sm" data-mptype="image" src="https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/scoreboard/bkn.png&amp;scale=crop&amp;cquality=40&amp;location=origin&amp;w=40&amp;h=40"><div class="ScoreCell__Team"><div class="ScoreCell__Truncate clr-gray-01 h5"><div class="ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db">Nets</div></div><div class="ScoreCell__Score h5 clr-gray-01 fw-heavy tar">104</div></div></li><li class="ScoreCell__Item ScoreCell__Item--home ScoreCell__Item--winner"><img alt="" class="Image Logo ScoreCell__Logo mr3 Logo__sm" data-mptype="image" src="https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/scoreboard/mil.png&amp;scale=crop&amp;cquality=40&amp;location=origin&amp;w=40&amp;h=40"><div class="ScoreCell__Team"><div class="ScoreCell__Truncate clr-gray-01 h5"><div class="ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db">Bucks</div></div><div class="ScoreCell__Score h5 clr-gray-01 fw-heavy tar">127</div></div><svg aria-hidden="true" class="ScoreCell__WinnerIcon icon__svg" viewBox="0 0 24 24"><use xlink:href="#icon__arrow__winner_left"></use></svg></li></ul></a><div class="ScoreCell__Overview"><div class="ScoreCell__Time h9 clr-gray-01">Final</div><div class="ScrollSpy_container ScoreCell__Btn mt2"><span></span><button class="Button Button--sm Button--alt ScoreCell__Btn mt2" tabindex="0"><div>HIGHLIGHTS<div class="espn-video-player-placeholder"></div></div></button></div></div></div></div>


    ###
    test_list = []
    html_espn_pbp_test = requests.get('https://www.espn.com/nba/scoreboard/_/date/20220303')#  https://www.espn.com/nba/scoreboard
    soup_espn_pbp_test = bs4.BeautifulSoup(html_espn_pbp_test.content, features='html.parser') 


    first_team_scorers = []
    first_game_scorers = [] 
    all_starters = []


    url_espn_pbp = 'https://www.espn.com/nba/playbyplay/_/gameId/'#401360116
    url_espn_starters = 'https://www.espn.com/nba/boxscore/_/gameId/'
    h = 0
    b = 0
    i = 0
    while True:
        if i < length_game_ids:
            id = game_ids[i]
            print(id)
            html_espn_pbp = requests.get(url_espn_pbp + str(id))
            soup_espn_pbp = bs4.BeautifulSoup(html_espn_pbp.content, features='html.parser') 
            for ultag in soup_espn_pbp.find_all('ul', {'class': 'shots away-team'}):
                for litag in ultag.find('li', {'class': 'made'}):
                    tag = str(litag)
                    name_start = tag.index('style="display:none;">')
                    name_start = name_start + 22
                    name_end = tag.index(' makes')
                    name = tag[name_start:name_end]
                    # print(str(id) + ' ' + str(name))
                    first_team_scorers.append(name)
                    h += 1
            for ultag in soup_espn_pbp.find_all('ul', {'class': 'shots home-team'}):
                for litag in ultag.find('li', {'class': 'made'}):
                    tag = str(litag)
                    name_start = tag.index('style="display:none;">')
                    name_start = name_start + 22
                    name_end = tag.index(' makes')
                    name = tag[name_start:name_end]
                    # print(str(id) + ' ' + str(name))
                    first_team_scorers.append(name)
                    h += 1
            b += 2
            if h != b:
                h = 0
                b = 0
                i += 1
                continue
            print('\n')
            print('SEARCH THIS URL')
            print(url_espn_pbp + str(id))
            df_espn = pd.read_html(url_espn_pbp + str(id))
            espn_data = df_espn[1].values.tolist()
            espn_data = espn_data[0:-1]
            s = 0
            while True:
                if s < len(espn_data):
                    del espn_data[s][1]
                    del espn_data[s][2:]
                    if type(espn_data[s][1]) != str:
                        del espn_data[s]
                        continue
                    # print(espn_data[s][1])
                    if 'makes' in espn_data[s][1]:
                        if 'free throw' in espn_data[s][1]:
                            del espn_data[s]
                            continue
                        else:
                            ind = espn_data[s][1].index(' makes')
                            name = espn_data[s][1][0:ind]
                            espn_data[s].append(name)
                            del espn_data[s][1]
                            s += 1
                            continue
                    else:
                        del espn_data[s]
                        continue
                else:
                    break 
            first_game_scorers.append(espn_data[0][1])
            print(first_game_scorers)
            html_espn_starters = requests.get(url_espn_starters + str(id))
            print(url_espn_starters + str(id))
            print('SEARCHING FOR GAME STARTERS')
            soup_espn_starters = bs4.BeautifulSoup(html_espn_starters.content, features='html.parser') 
            # print('TD TAGS:')
            tables = []
            names = []
            # i = 0
            for tabletag in soup_espn_starters.find_all('td', {'class': 'name'}):#('table', {'class': 'mod-data'})
                tables.append(tabletag.text)
                print('GOT TEXT FROM TABLE WITH STARTERS FOR GAME')
            # print('\n')
            new_tables = []
            for elem in tables:
                if '.' not in elem:
                    elem = 'split here'
                    new_tables.append(elem)
                    # continue
                else:
                    if elem[3] == '.':
                        elem = elem[5:]
                        # print(elem)
                        ind = elem.index('.')
                        ind -= 1
                        elem = elem[ind:]
                        # print(elem)
                        ind += 5
                        elem = elem[:ind]
                        # print(elem)
                        new_tables.append(elem)
                        # print('\n')
                    else:
                        # print(elem)
                        elem = elem[3:]
                        # print(elem)
                        ind = elem.index('.')
                        ind -= 1
                        elem = elem[ind:]
                        # print(elem)
                        ind += 3
                        elem = elem[:ind]
                        # print(elem)
                        new_tables.append(elem)
                        # print('\n')
            away_starters = new_tables[0:5]
            print(' away starters = ')
            print(away_starters)
            print(new_tables[0:5])
            print('\n')
            print(new_tables)
            print('\n')
            del new_tables[0:5]
            ind = new_tables.index('split here')
            print('split table index')
            print(ind)
            while True:
                print('split tables index = ' + str(ind))
                print(new_tables[ind])
                if new_tables[ind] == 'split here':
                    ind += 1
                    continue
                else:
                    print('split index not working')
                    del new_tables[:ind]
                    if 'split here' in new_tables[0:4]:
                        split_ind = new_tables.index('split here')
                        print('new split index')
                        print(split_ind)
                        a = 0
                        # split_ind = 69
                        while True:
                            if a < 5:
                                if new_tables[a] == 'split here':
                                    split_ind = a
                                    a += 1
                                    continue
                                else:
                                    a += 1
                                    continue
                            else:
                                del new_tables[:split_ind + 1]    
                                break   
                    del new_tables[5:]
                    home_starters = new_tables
                    break
            game_starters = away_starters + home_starters
            print('got game starters')
            print(game_starters)
            all_starters.append(game_starters)
            # print('\n')
            # for elem in game_starters:
            #     print(elem)
            i += 1
            continue
        else:
            break
    print('\n')
    print('ALL STRTERS:')
    print(all_starters)
    print('\n')

    url_celtics = 'https://www.espn.com/nba/team/roster/_/name/bos/boston-celtics'
    url_nets = 'https://www.espn.com/nba/team/roster/_/name/bkn/brooklyn-nets'
    url_knicks = 'https://www.espn.com/nba/team/roster/_/name/ny/new-york-knicks'
    url_76ers = 'https://www.espn.com/nba/team/roster/_/name/phi/philadelphia-76ers'
    url_raptors = 'https://www.espn.com/nba/team/roster/_/name/tor/toronto-raptors'
    url_warriors = 'https://www.espn.com/nba/team/roster/_/name/gs/golden-state-warriors'
    url_clippers = 'https://www.espn.com/nba/team/roster/_/name/lac/la-clippers'
    url_lakers = 'https://www.espn.com/nba/team/roster/_/name/lal/los-angeles-lakers'
    url_suns = 'https://www.espn.com/nba/team/roster/_/name/phx/phoenix-suns'
    url_kings = 'https://www.espn.com/nba/team/roster/_/name/sac/sacramento-kings'
    url_bulls = 'https://www.espn.com/nba/team/roster/_/name/chi/chicago-bulls'
    url_cavaliers = 'https://www.espn.com/nba/team/roster/_/name/cle/cleveland-cavaliers'
    url_pistons = 'https://www.espn.com/nba/team/roster/_/name/det/detroit-pistons'
    url_pacers = 'https://www.espn.com/nba/team/roster/_/name/ind/indiana-pacers'
    url_bucks = 'https://www.espn.com/nba/team/roster/_/name/mil/milwaukee-bucks'
    url_hawks = 'https://www.espn.com/nba/team/roster/_/name/atl/atlanta-hawks'
    url_hornets = 'https://www.espn.com/nba/team/roster/_/name/cha/charlotte-hornets'
    url_heat = 'https://www.espn.com/nba/team/roster/_/name/mia/miami-heat'
    url_magic = 'https://www.espn.com/nba/team/roster/_/name/orl/orlando-magic'
    url_wizards = 'https://www.espn.com/nba/team/roster/_/name/wsh/washington-wizards'
    url_nuggets = 'https://www.espn.com/nba/team/roster/_/name/den/denver-nuggets'
    url_timberwolves = 'https://www.espn.com/nba/team/roster/_/name/min/minnesota-timberwolves'
    url_thunder = 'https://www.espn.com/nba/team/roster/_/name/okc/oklahoma-city-thunder'
    url_trailblazers = 'https://www.espn.com/nba/team/roster/_/name/por/portland-trail-blazers'
    url_jazz = 'https://www.espn.com/nba/team/roster/_/name/utah/utah-jazz'
    url_mavericks = 'https://www.espn.com/nba/team/roster/_/name/dal/dallas-mavericks'
    url_rockets = 'https://www.espn.com/nba/team/roster/_/name/hou/houston-rockets'
    url_grizzlies = 'https://www.espn.com/nba/team/roster/_/name/mem/memphis-grizzlies'
    url_pelicans = 'https://www.espn.com/nba/team/roster/_/name/no/new-orleans-pelicans'
    url_spurs = 'https://www.espn.com/nba/team/roster/_/name/sa/san-antonio-spurs'
    df_celtics = pd.read_html(url_celtics)
    df_nets = pd.read_html(url_nets)
    df_knicks = pd.read_html(url_knicks)
    df_76ers = pd.read_html(url_76ers)
    df_raptors = pd.read_html(url_raptors)
    df_warriors = pd.read_html(url_warriors)
    df_clippers = pd.read_html(url_clippers)
    df_lakers = pd.read_html(url_lakers)
    df_suns = pd.read_html(url_suns)
    df_kings = pd.read_html(url_kings)
    df_bulls = pd.read_html(url_bulls)
    df_cavaliers = pd.read_html(url_cavaliers)
    df_pistons = pd.read_html(url_pistons)
    df_pacers = pd.read_html(url_pacers)
    df_bucks = pd.read_html(url_bucks)
    df_hawks = pd.read_html(url_hawks)
    df_hornets = pd.read_html(url_hornets)
    df_heat = pd.read_html(url_heat)
    df_magic = pd.read_html(url_magic)
    df_wizards = pd.read_html(url_wizards)
    df_nuggets = pd.read_html(url_nuggets)
    df_timberwolves = pd.read_html(url_timberwolves)
    df_thunder = pd.read_html(url_thunder)
    df_trailblazers = pd.read_html(url_trailblazers)
    df_jazz = pd.read_html(url_jazz)
    df_mavericks = pd.read_html(url_mavericks)
    df_rockets = pd.read_html(url_rockets)
    df_grizzlies = pd.read_html(url_grizzlies)
    df_pelicans = pd.read_html(url_pelicans)
    df_spurs = pd.read_html(url_spurs)
    celtics = df_celtics[0].values.tolist()
    nets = df_nets[0].values.tolist()
    knicks = df_knicks[0].values.tolist()
    phi76ers = df_76ers[0].values.tolist()
    raptors = df_raptors[0].values.tolist()
    warriors = df_warriors[0].values.tolist()
    clippers = df_clippers[0].values.tolist()
    lakers = df_lakers[0].values.tolist()
    suns = df_suns[0].values.tolist()
    kings = df_kings[0].values.tolist()
    bulls = df_bulls[0].values.tolist()
    cavaliers = df_cavaliers[0].values.tolist()
    pistons = df_pistons[0].values.tolist()
    pacers = df_pacers[0].values.tolist()
    bucks = df_bucks[0].values.tolist()
    hawks = df_hawks[0].values.tolist()
    hornets = df_hornets[0].values.tolist()
    heat = df_heat[0].values.tolist()
    magic = df_magic[0].values.tolist()
    wizards = df_wizards[0].values.tolist()
    nuggets = df_nuggets[0].values.tolist()
    timberwolves = df_timberwolves[0].values.tolist()
    thunder = df_thunder[0].values.tolist()
    trailblazers = df_trailblazers[0].values.tolist()
    jazz = df_jazz[0].values.tolist()
    mavericks = df_mavericks[0].values.tolist()
    rockets = df_rockets[0].values.tolist()
    grizzlies = df_grizzlies[0].values.tolist()
    pelicans = df_pelicans[0].values.tolist()
    spurs = df_spurs[0].values.tolist()

    print(first_game_scorers)
    
    def roster(team):
        for elem in team:
            del elem[0]
            del elem[1:]
        roster_length = len(team)
        i = 0
        while True:
            if i < roster_length:
                name = team[i][0]
                if name[-1] == '-':
                    name = name[0:-1]
                    team[i][0] = name
                    continue
                elif name[-1] == '0':
                    name = name[0:-1]
                    team[i][0] = name
                    continue
                elif name[-1] == '1':
                    name = name[0:-1]
                    team[i][0] = name
                    continue
                elif name[-1] == '2':
                    name = name[0:-1]
                    team[i][0] = name
                    continue
                elif name[-1] == '3':
                    name = name[0:-1]
                    team[i][0] = name
                    continue
                elif name[-1] == '4':
                    name = name[0:-1]
                    team[i][0] = name
                    continue
                elif name[-1] == '5':
                    name = name[0:-1]
                    team[i][0] = name
                    continue
                elif name[-1] == '6':
                    name = name[0:-1]
                    team[i][0] = name
                    continue
                elif name[-1] == '7':
                    name = name[0:-1]
                    team[i][0] = name
                    continue
                elif name[-1] == '8':
                    name = name[0:-1]
                    team[i][0] = name
                    continue
                elif name[-1] == '9':
                    name = name[0:-1]
                    team[i][0] = name
                    continue
                else:
                    i += 1
                    continue
            else:
                break
        team = [player for sublist in team for player in sublist]
        return team

    celtics = roster(celtics)
    nets = roster(nets)
    knicks = roster(knicks)
    phi76ers = roster(phi76ers)
    raptors = roster(raptors)
    warriors = roster(warriors)
    clippers = roster(clippers)
    lakers = roster(lakers)
    suns = roster(suns)
    kings = roster(kings)
    bulls = roster(bulls)
    cavaliers = roster(cavaliers)
    pistons = roster(pistons)
    pacers = roster(pacers)
    bucks = roster(bucks)
    hawks = roster(hawks)
    hornets = roster(hornets)
    heat = roster(heat)
    magic = roster(magic)
    wizards = roster(wizards)
    nuggets = roster(nuggets)
    timberwolves = roster(timberwolves)
    thunder = roster(thunder)
    trailblazers = roster(trailblazers)
    jazz = roster(jazz)
    mavericks = roster(mavericks)
    rockets = roster(rockets)
    grizzlies = roster(grizzlies)
    pelicans = roster(pelicans)
    spurs = roster(spurs)

    # FOT = First of Team
    # FOG = First of Game
    # FT = First Team (to score a FG)

    celtics_FOG = []
    celtics_FOT = []
    nets_FOG = []
    nets_FOT = []
    knicks_FOG = []
    knicks_FOT = []
    phi76ers_FOG = []
    phi76ers_FOT = []
    raptors_FOG = []
    raptors_FOT = []
    warriors_FOG = []
    warriors_FOT = []
    clippers_FOG = []
    clippers_FOT = []
    lakers_FOG = []
    lakers_FOT = []
    suns_FOG = []
    suns_FOT = []
    kings_FOG = []
    kings_FOT = []
    bulls_FOG = []
    bulls_FOT = []
    cavaliers_FOG = []
    cavaliers_FOT = []
    pistons_FOG = []
    pistons_FOT = []
    pacers_FOG = []
    pacers_FOT = []
    bucks_FOG = []
    bucks_FOT = []
    hawks_FOG = []
    hawks_FOT = []
    hornets_FOG = []
    hornets_FOT = []
    heat_FOG = []
    heat_FOT = []
    magic_FOG = []
    magic_FOT = []
    wizards_FOG = []
    wizards_FOT = []
    nuggets_FOG = []
    nuggets_FOT = []
    timberwolves_FOG = []
    timberwolves_FOT = []
    thunder_FOG = []
    thunder_FOT = []
    trailblazers_FOG = []
    trailblazers_FOT = []
    jazz_FOG = []
    jazz_FOT = []
    mavericks_FOG = []
    mavericks_FOT = []
    rockets_FOG = []
    rockets_FOT = []
    grizzlies_FOG = []
    grizzlies_FOT = []
    pelicans_FOG = []
    pelicans_FOT = []
    spurs_FOG = []
    spurs_FOT = []


    def fog(team_FOG, roster):
        # global first_game_scorers
        for elem in first_game_scorers:
            if elem in roster:
                team_FOG.append(elem)
                continue
            else:
                continue
        return team_FOG

    def fot(team_FOT, roster):
        # global first_team_scorers
        for elem in first_team_scorers:
            if elem in roster:
                team_FOT.append(elem)
                continue
            else:
                continue
        return team_FOT


    celtics_FOG = fog(celtics_FOG, celtics)
    celtics_FOT = fot(celtics_FOT, celtics)
    nets_FOG = fog(nets_FOG, nets)
    nets_FOT = fot(nets_FOT, nets)
    knicks_FOG = fog(knicks_FOG, knicks)
    knicks_FOT = fot(knicks_FOT, knicks)
    phi76ers_FOG = fog(phi76ers_FOG, phi76ers)
    phi76ers_FOT = fot(phi76ers_FOT, phi76ers)
    raptors_FOG = fog(raptors_FOG, raptors)
    raptors_FOT = fot(raptors_FOT, raptors)
    warriors_FOG = fog(warriors_FOG, warriors)
    warriors_FOT = fot(warriors_FOT, warriors)
    clippers_FOG = fog(clippers_FOG, clippers)
    clippers_FOT = fot(clippers_FOT, clippers)
    lakers_FOG = fog(lakers_FOG, lakers)
    lakers_FOT = fot(lakers_FOT, lakers)
    suns_FOG = fog(suns_FOG, suns)
    suns_FOT = fot(suns_FOT, suns)
    kings_FOG = fog(kings_FOG, kings)
    kings_FOT = fot(kings_FOT, kings)
    bulls_FOG = fog(bulls_FOG, bulls)
    bulls_FOT = fot(bulls_FOT, bulls)
    cavaliers_FOG = fog(cavaliers_FOG, cavaliers)
    cavaliers_FOT = fot(cavaliers_FOT, cavaliers)
    pistons_FOG = fog(pistons_FOG, pistons)
    pistons_FOT = fot(pistons_FOT, pistons)
    pacers_FOG = fog(pacers_FOG, pacers)
    pacers_FOT = fot(pacers_FOT, pacers)
    bucks_FOG = fog(bucks_FOG, bucks)
    bucks_FOT = fot(bucks_FOT, bucks)
    hawks_FOG = fog(hawks_FOG, hawks)
    hawks_FOT = fot(hawks_FOT, hawks)
    hornets_FOG = fog(hornets_FOG, hornets)
    hornets_FOT = fot(hornets_FOT, hornets)
    heat_FOG = fog(heat_FOG, heat)
    heat_FOT = fot(heat_FOT, heat)
    magic_FOG = fog(magic_FOG, magic)
    magic_FOT = fot(magic_FOT, magic)
    wizards_FOG = fog(wizards_FOG, wizards)
    wizards_FOT = fot(wizards_FOT, wizards)
    nuggets_FOG = fog(nuggets_FOG, nuggets)
    nuggets_FOT = fot(nuggets_FOT, nuggets)
    timberwolves_FOG = fog(timberwolves_FOG, timberwolves)
    timberwolves_FOT = fot(timberwolves_FOT, timberwolves)
    thunder_FOG = fog(thunder_FOG, thunder)
    thunder_FOT = fot(thunder_FOT, thunder)
    trailblazers_FOG = fog(trailblazers_FOG, trailblazers)
    trailblazers_FOT = fot(trailblazers_FOT, trailblazers)
    jazz_FOG = fog(jazz_FOG, jazz)
    jazz_FOT = fot(jazz_FOT, jazz)
    mavericks_FOG = fog(mavericks_FOG, mavericks)
    mavericks_FOT = fot(mavericks_FOT, mavericks)
    rockets_FOG = fog(rockets_FOG, rockets)
    rockets_FOT = fot(rockets_FOT, rockets)
    grizzlies_FOG = fog(grizzlies_FOG, grizzlies)
    grizzlies_FOT = fot(grizzlies_FOT, grizzlies)
    pelicans_FOG = fog(pelicans_FOG, pelicans)
    pelicans_FOT = fot(pelicans_FOT, pelicans)
    spurs_FOG = fog(spurs_FOG, spurs)
    spurs_FOT = fot(spurs_FOT, spurs)

    print('\n')
    print(celtics_FOG)
    print('\n')
    print(celtics_FOT)

    celtics_FT = len(celtics_FOG)
    celtics_num_games = len(celtics_FOT)
    celtics_FT_percent = float(celtics_FT / celtics_num_games)
    celtics_FT_percent = round(celtics_FT_percent, 3)

    nets_FT = len(nets_FOG)
    nets_num_games = len(nets_FOT)
    nets_FT_percent = float(nets_FT / nets_num_games)
    nets_FT_percent = round(nets_FT_percent, 3)

    knicks_FT = len(knicks_FOG)
    knicks_num_games = len(knicks_FOT)
    knicks_FT_percent = float(knicks_FT / knicks_num_games)
    knicks_FT_percent = round(knicks_num_games, 3)

    phi76ers_FT = len(phi76ers_FOG)
    phi76ers_num_games = len(phi76ers_FOT)
    phi76ers_FT_percent = float(phi76ers_FT / phi76ers_num_games)
    phi76ers_FT_percent = round(phi76ers_FT_percent, 3)

    raptors_FT = len(raptors_FOG)
    raptors_num_games = len(raptors_FOT)
    raptors_FT_percent = float(raptors_FT / raptors_num_games)
    raptors_FT_percent = round(raptors_FT_percent, 3)

    warriors_FT = len(warriors_FOG)
    warriors_num_games = len(warriors_FOT)
    warriors_FT_percent = float(warriors_FT / warriors_num_games)
    warriors_FT_percent = round(warriors_FT_percent, 3)

    clippers_FT = len(clippers_FOG)
    clippers_num_games = len(clippers_FOT)
    clippers_FT_percent = float(clippers_FT / clippers_num_games)
    clippers_FT_percent = round(clippers_FT_percent, 3)

    lakers_FT = len(lakers_FOG)
    lakers_num_games = len(lakers_FOT)
    lakers_FT_percent = float(lakers_FT / lakers_num_games)
    lakers_FT_percent = round(lakers_FT_percent, 3)

    suns_FT = len(suns_FOG)
    suns_num_games = len(suns_FOT)
    suns_FT_percent = float(suns_FT / suns_num_games)
    suns_FT_percent = round(suns_FT_percent, 3)

    kings_FT = len(kings_FOG)
    kings_num_games = len(kings_FOT)
    kings_FT_percent = float(kings_FT / kings_num_games)
    kings_FT_percent = round(kings_FT_percent, 3)

    bulls_FT = len(bulls_FOG)
    bulls_num_games = len(bulls_FOT)
    bulls_FT_percent = float(bulls_FT / bulls_num_games)
    bulls_FT_percent = round(bulls_FT_percent, 3)

    cavaliers_FT = len(cavaliers_FOG)
    cavaliers_num_games = len(cavaliers_FOT)
    cavaliers_FT_percent = float(cavaliers_FT / cavaliers_num_games)
    cavaliers_FT_percent = round(cavaliers_FT_percent, 3)

    pistons_FT = len(pistons_FOG)
    pistons_num_games = len(pistons_FOT)
    pistons_FT_percent = float(pistons_FT / pistons_num_games)
    pistons_FT_percent = round(pistons_FT_percent, 3)

    pacers_FT = len(pacers_FOG)
    pacers_num_games = len(pacers_FOT)
    pacers_FT_percent = float(pacers_FT / pacers_num_games)
    pacers_FT_percent = round(pacers_FT_percent, 3)

    bucks_FT = len(bucks_FOG)
    bucks_num_games = len(bucks_FOT)
    bucks_FT_percent = float(bucks_FT / bucks_num_games)
    bucks_FT_percent = round(bucks_FT_percent, 3)

    hawks_FT = len(hawks_FOG)
    hawks_num_games = len(hawks_FOT)
    hawks_FT_percent = float(hawks_FT / hawks_num_games)
    hawks_FT_percent = round(hawks_FT_percent, 3)

    hornets_FT = len(hornets_FOG)
    hornets_num_games = len(hornets_FOT)
    hornets_FT_percent = float(hornets_FT / hornets_num_games)
    hornets_FT_percent = round(hornets_FT_percent, 3)

    heat_FT = len(heat_FOG)
    heat_num_games = len(heat_FOT)
    heat_FT_percent = float(heat_FT / heat_num_games)
    heat_FT_percent = round(heat_FT_percent, 3)

    magic_FT = len(magic_FOG)
    magic_num_games = len(magic_FOT)
    magic_FT_percent = float(magic_FT / magic_num_games)
    magic_FT_percent = round(magic_FT_percent, 3)

    wizards_FT = len(wizards_FOG)
    wizards_num_games = len(wizards_FOT)
    wizards_FT_percent = float(wizards_FT / wizards_num_games)
    wizards_FT_percent = round(wizards_FT_percent, 3)

    nuggets_FT = len(nuggets_FOG)
    nuggets_num_games = len(nuggets_FOT)
    nuggets_FT_percent = float(nuggets_FT / nuggets_num_games)
    nuggets_FT_percent = round(nuggets_FT_percent, 3)

    timberwolves_FT = len(timberwolves_FOG)
    timberwolves_num_games = len(timberwolves_FOT)
    timberwolves_FT_percent = float(timberwolves_FT / timberwolves_num_games)
    timberwolves_FT_percent = round(timberwolves_FT_percent, 3)

    thunder_FT = len(thunder_FOG)
    thunder_num_games = len(thunder_FOT)
    thunder_FT_percent = float(thunder_FT / thunder_num_games)
    thunder_FT_percent = round(thunder_FT_percent, 3)

    trailblazers_FT = len(trailblazers_FOG)
    trailblazers_num_games = len(trailblazers_FOT)
    trailblazers_FT_percent = float(trailblazers_FT / trailblazers_num_games)
    trailblazers_FT_percent = round(trailblazers_FT_percent, 3)

    jazz_FT = len(jazz_FOG)
    jazz_num_games = len(jazz_FOT)
    jazz_FT_percent = float(jazz_FT / jazz_num_games)
    jazz_FT_percent = round(jazz_FT_percent, 3)

    mavericks_FT = len(mavericks_FOG)
    mavericks_num_games = len(mavericks_FOT)
    mavericks_FT_percent = float(mavericks_FT / mavericks_num_games)
    mavericks_FT_percent = round(mavericks_FT_percent, 3)

    rockets_FT = len(rockets_FOG)
    rockets_num_games = len(rockets_FOT)
    rockets_FT_percent = float(rockets_FT / rockets_num_games)
    rockets_FT_percent = round(rockets_FT_percent, 3)

    grizzlies_FT = len(grizzlies_FOG)
    grizzlies_num_games = len(grizzlies_FOT)
    grizzlies_FT_percent = float(grizzlies_FT / grizzlies_num_games)
    grizzlies_FT_percent = round(grizzlies_FT_percent, 3)

    pelicans_FT = len(pelicans_FOG)
    pelicans_num_games = len(pelicans_FOT)
    pelicans_FT_percent = float(pelicans_FT / pelicans_num_games)
    pelicans_FT_percent = round(pelicans_FT_percent, 3)

    spurs_FT = len(spurs_FOG)
    spurs_num_games = len(spurs_FOT)
    spurs_FT_percent = float(spurs_FT / spurs_num_games)
    spurs_FT_percent = round(spurs_FT_percent, 3)

    # CREATING ROSTER LISTS WITH THE PLAYERS AND THEIR INDIVIDUAL CHANCES ... pc = "player chances"


    def pc(roster, num_games):
        # global first_game_scorers
        res = []
        for el in roster:
            sub = el.split(', ')
            res.append(sub)
            continue
        for elem in res:
            name = elem[0]
            fgs = first_game_scorers.count(name)
            per = float(fgs / num_games)
            per = round(per, 3)
            elem.append(per)
            continue
        return(res)

    celtics = pc(celtics, celtics_num_games)
    nets = pc(nets, nets_num_games)
    knicks = pc(knicks, knicks_num_games)
    phi76ers = pc(phi76ers, phi76ers_num_games)
    raptors = pc(raptors, raptors_num_games)
    warriors = pc(warriors, warriors_num_games)
    clippers = pc(clippers, clippers_num_games)
    lakers = pc(lakers, lakers_num_games)
    suns = pc(suns, suns_num_games)
    kings = pc(kings, kings_num_games)
    bulls = pc(bulls, bulls_num_games)
    cavaliers = pc(cavaliers, cavaliers_num_games)
    pistons = pc(pistons, pistons_num_games)
    pacers = pc(pacers, pacers_num_games)
    bucks = pc(bucks, bucks_num_games)
    hawks = pc(hawks, hawks_num_games)
    hornets = pc(hornets, hornets_num_games)
    heat = pc(heat, heat_num_games)
    magic = pc(magic, magic_num_games)
    wizards = pc(wizards, wizards_num_games)
    nuggets = pc(nuggets, nuggets_num_games)
    timberwolves = pc(timberwolves, timberwolves_num_games)
    thunder = pc(thunder, thunder_num_games)
    trailblazers = pc(trailblazers, trailblazers_num_games)
    jazz = pc(jazz, jazz_num_games)
    mavericks = pc(mavericks, mavericks_num_games)
    rockets = pc(rockets, rockets_num_games)
    grizzlies = pc(grizzlies, grizzlies_num_games)
    pelicans = pc(pelicans, pelicans_num_games)
    spurs = pc(spurs, spurs_num_games)

    print(heat)

    def game(away_team, home_team):
        if away_team == 'Boston':
            away_roster = celtics
            away_chance = celtics_FT_percent
        if away_team == 'Brooklyn':
            away_roster = nets
            away_chance = nets_FT_percent
        if away_team == 'New York':
            away_roster = knicks
            away_chance = knicks_FT_percent
        if away_team == 'Philadelphia':
            away_roster = phi76ers
            away_chance = phi76ers_FT_percent
        if away_team == 'Toronto':
            away_roster = raptors
            away_chance = raptors_FT_percent
        if away_team == 'Golden State':
            away_roster = warriors
            away_chance = warriors_FT_percent
        if away_team == 'LA':
            away_roster = clippers
            away_chance = clippers_FT_percent
        if away_team == 'Los Angeles':
            away_roster = lakers
            away_chance = lakers_FT_percent
        if away_team == 'Phoenix':
            away_roster = suns
            away_chance = suns_FT_percent
        if away_team == 'Sacramento':
            away_roster = kings
            away_chance = kings_FT_percent
        if away_team == 'Chicago':
            away_roster = bulls
            away_chance = bulls_FT_percent
        if away_team == 'Cleveland':
            away_roster = cavaliers
            away_chance = cavaliers_FT_percent
        if away_team == 'Detroit':
            away_roster = pistons
            away_chance = pistons_FT_percent
        if away_team == 'Indiana':
            away_roster = pacers
            away_chance = pacers_FT_percent
        if away_team == 'Milwaukee': 
            away_roster = bucks
            away_chance = bucks_FT_percent
        if away_team == 'Atlanta':
            away_roster = hawks
            away_chance = hawks_FT_percent
        if away_team == 'Charlotte':
            away_roster = hornets
            away_chance = hornets_FT_percent
        if away_team == 'Miami':
            away_roster = heat
            away_chance = heat_FT_percent
        if away_team == 'Orlando':
            away_roster = magic
            away_chance = magic_FT_percent
        if away_team == 'Washington':
            away_roster = wizards
            away_chance = wizards_FT_percent
        if away_team == 'Denver':
            away_roster = nuggets
            away_chance = nuggets_FT_percent
        if away_team == 'Minnesota':
            away_roster = timberwolves
            away_chance = timberwolves_FT_percent
        if away_team == 'Oklahoma City':
            away_roster = thunder
            away_chance = thunder_FT_percent
        if away_team == 'Portland':
            away_roster = trailblazers
            away_chance = trailblazers_FT_percent
        if away_team == 'Utah':
            away_roster = jazz
            away_chance = jazz_FT_percent
        if away_team == 'Dallas':
            away_roster = mavericks
            away_chance = mavericks_FT_percent
        if away_team == 'Houston':
            away_roster = rockets
            away_chance = rockets_FT_percent
        if away_team == 'Memphis':
            away_roster = grizzlies
            away_chance = grizzlies_FT_percent
        if away_team == 'New Orleans':
            away_roster = pelicans
            away_chance = pelicans_FT_percent
        if away_team == 'San Antonio':
            away_roster = spurs
            away_chance = spurs_FT_percent
        if home_team == 'Boston':
            home_roster = celtics
            home_chance = celtics_FT_percent
        if home_team == 'Brooklyn':
            home_roster = nets
            home_chance = nets_FT_percent
        if home_team == 'New York':
            home_roster = knicks
            home_chance = knicks_FT_percent
        if home_team == 'Philadelphia':
            home_roster = phi76ers
            home_chance = phi76ers_FT_percent
        if home_team == 'Toronto':
            home_roster = raptors
            home_chance = raptors_FT_percent
        if home_team == 'Golden State':
            home_roster = warriors
            home_chance = warriors_FT_percent
        if home_team == 'LA':
            home_roster = clippers
            home_chance = clippers_FT_percent
        if home_team == 'Los Angeles':
            home_roster = lakers
            home_chance = lakers_FT_percent
        if home_team == 'Phoenix':
            home_roster = suns
            home_chance = suns_FT_percent
        if home_team == 'Sacramento':
            home_roster = kings
            home_chance = kings_FT_percent
        if home_team == 'Chicago':
            home_roster = bulls
            home_chance = bulls_FT_percent
        if home_team == 'Cleveland':
            home_roster = cavaliers
            home_chance = cavaliers_FT_percent
        if home_team == 'Detroit':
            home_roster = pistons
            home_chance = pistons_FT_percent
        if home_team == 'Indiana':
            home_roster = pacers
            home_chance = pacers_FT_percent
        if home_team == 'Milwaukee': 
            home_roster = bucks
            home_chance = bucks_FT_percent
        if home_team == 'Atlanta':
            home_roster = hawks
            home_chance = hawks_FT_percent
        if home_team == 'Charlotte':
            home_roster = hornets
            home_chance = hornets_FT_percent
        if home_team == 'Miami':
            home_roster = heat
            home_chance = heat_FT_percent
        if home_team == 'Orlando':
            home_roster = magic
            home_chance = magic_FT_percent
        if home_team == 'Washington':
            home_roster = wizards
            home_chance = wizards_FT_percent
        if home_team == 'Denver':
            home_roster = nuggets
            home_chance = nuggets_FT_percent
        if home_team == 'Minnesota':
            home_roster = timberwolves
            home_chance = timberwolves_FT_percent
        if home_team == 'Oklahoma City':
            home_roster = thunder
            home_chance = thunder_FT_percent
        if home_team == 'Portland':
            home_roster = trailblazers
            home_chance = trailblazers_FT_percent
        if home_team == 'Utah':
            home_roster = jazz
            home_chance = jazz_FT_percent
        if home_team == 'Dallas':
            home_roster = mavericks
            home_chance = mavericks_FT_percent
        if home_team == 'Houston':
            home_roster = rockets
            home_chance = rockets_FT_percent
        if home_team == 'Memphis':
            home_roster = grizzlies
            home_chance = grizzlies_FT_percent
        if home_team == 'New Orleans':
            home_roster = pelicans
            home_chance = pelicans_FT_percent
        if home_team == 'San Antonio':
            home_roster = spurs
            home_chance = spurs_FT_percent
        print(str(away_team))
        away_blend = float(away_chance / (away_chance + home_chance))
        away_blend = round(away_blend, 3)
        home_blend = float(home_chance / (home_chance + away_chance))
        home_blend = round(home_blend, 3)
        for elem in away_roster:
            away_player_chance = float(elem[1])
            away_player_chance = float(away_player_chance * away_blend)
            away_player_chance = round(away_player_chance, 3)
            elem.append(away_player_chance)
            continue
        for elem in home_roster:
            home_player_chance = float(elem[1])
            home_player_chance = float(home_player_chance * home_blend)
            home_player_chance = round(home_player_chance, 3)
            elem.append(home_player_chance)
            continue
        matchup = []
        matchup.append(away_roster)
        matchup.append(home_roster)
        return matchup

    url_nba_sched = 'https://www.espn.com/nba/schedule'
    df_nba_sched = pd.read_html(url_nba_sched)
    nba_sched = df_nba_sched[0].values.tolist()
    for elem in nba_sched:
        print(elem)
        
    i = 0
    while True:
        if i < len(nba_sched):
            if 'East' in nba_sched[i][0]:
                ind = nba_sched[i][0].index('East')
                name = nba_sched[i][0]
                name = name[:ind]
                nba_sched[i][0] = name
                i += 1
                continue
            elif 'West' in nba_sched[i][0]:
                ind = nba_sched[i][0].index('West')
                name = nba_sched[i][0]
                name = name[:ind]
                nba_sched[i][0] = name
                i += 1
                continue
            else:
                i += 1
                continue
        else:
            break
        


    # print('Doesn Fanduel have a First Basket promo? (Y / N)')
    # fanduel = input()
    # print('Doesn DraftKings have a First Basket promo? (Y / N)')
    # draftkings = input()
    # print('Doesn Barstool have a First Basket promo? (Y / N)')
    # barstool = input()

    # awayTeamList = dict_espn_data[matchupAnalysis_NCAAB[i][0]]
    #                 if len(awayTeamList) == 0:
    #                     i += 2
    #                     continue
    #                 # print(awayTeamList)
    #                 # print('\n')
    #                 awayTeamChance = awayTeamList[0]
    #
    #
    #
    # ffg_odds_keys
    
    print('\n')
    print('DRAFTKINGS KEYS - PLAYER NAMES:')
    print(dict_dk_firstFG)
    print('\n')
    
    for elem in nba_sched:
        away_teamname = str(elem[0])
        print('AWAY TEAM NAME:')
        print('.' + away_teamname + '.')
        home_teamname = str(elem[1])
        home_teamname = str(home_teamname[2:])
        print('HOME TEAM NAME:')
        print('.' + home_teamname + '.')
        lst = game(away_teamname, home_teamname)
        away_roster = lst[0]
        for player in away_roster:
            player_name = player[0]
            player_blended_chance = float(player[2])
            if player_name in ffg_odds_keys:
                player_odds_lst = dict_dk_firstFG[player_name]
                player_odds = player_odds_lst[0]
                player.append(int(player_odds))
                fd_value = float((player_odds / 100 * 10 + 10) * player_blended_chance)
                fd_value = round(fd_value, 3)
                player.append(fd_value)
            else:
                del player
                continue
            player.append(away_teamname)
        home_roster = lst[1]
        for player in home_roster:
            player_name = player[0]
            player_blended_chance = float(player[2])
            if player_name in ffg_odds_keys:
                player_odds_lst = dict_dk_firstFG[player_name]
                player_odds = player_odds_lst[0]
                player.append(int(player_odds))
                fd_value = float((player_odds / 100 * 10 + 10) * player_blended_chance)
                fd_value = round(fd_value, 3)
                player.append(fd_value)
            else:
                del player
                continue
            player.append(home_teamname)
        elem.append(away_roster)
        elem.append(home_roster)
        del elem[0:6]
        print(elem)
        print('\n')
        continue

    print('\n')
    print('MAYBE A GOOD LIST OF FIRST SCORERS????')
    for elem in nba_sched:
        print(elem)
    print('\n')

    first_FG_picks = []
    for matchup in nba_sched:
        for team in matchup:
            for player in team:
                print(player)
                first_FG_picks.append(player)
                continue

    # for elem in first_FG_picks:
    #     if len(elem) != 6:
    #         del elem
    #         continue

    headers = ['Name', 'chance(%)', 'blend(%)', 'dk_odds', 'dk_val', 'team']

    leftWidth = 23
    rightWidth = 9
    totalWidth = (leftWidth + rightWidth + rightWidth + rightWidth + rightWidth)

    print('\n')
    for elem in first_FG_picks:
        print(elem)
    print('\n')
    
    i = 0
    while True:
        if i < len(first_FG_picks):
            l = len(first_FG_picks[i])
            if l != 6:
                del first_FG_picks[i]
                continue
            else:
                i += 1
                continue
        else:
            break
    
    title = ' First FG '
    print(title.center(totalWidth, '-'))
    print('Name'.ljust(leftWidth) + 'chance(%)'.rjust(rightWidth) + 'blend(%)'.rjust(rightWidth)  
        + 'dk_odds'.rjust(rightWidth) + 'dk_val'.rjust(rightWidth) + 'team'.rjust(rightWidth)
        )

    # Robert Williams +750

    for elem in first_FG_picks:
        name = elem[0]
        chance = round((float(elem[1])) * 100, 2)
        blend = round((float(elem[2])) * 100, 2)
        dk_odds = elem[3]
        dk_val = elem[4]
        team_nm = elem[5]
        print(str(name).ljust(leftWidth) + str(chance).rjust(rightWidth) + str(blend).rjust(rightWidth) 
            + str(dk_odds).rjust(rightWidth) + str(dk_val).rjust(rightWidth) + str(team_nm).rjust(rightWidth))
        
    firstFGs = pd.DataFrame(first_FG_picks, columns = headers)
    firstFGs.head()
    firstFGs.to_excel('/Users/Hayden/OneDrive/Sports Betting/Basketball/FirstFG.xlsx', index=False)

    finished_time = time.perf_counter()
    print('\n')
    print(f'Finished FFG in {finished_time - start_time:0.4f} seconds.')
    print('\n')

    conn = sqlite3.connect('First_FG.db')

    firstFGs.to_sql(name='First FG', con=conn, if_exists='replace', index=False)

    conn.commit()


firstFG()

# schedule.every(25).hours.do(firstFG)

# while True:
#     schedule.run_pending()