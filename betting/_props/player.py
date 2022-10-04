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

def onePlayer(league, team, player, stat, value, bet_type):
    if league == 'NBA':
        if team == 'Boston':
            team_url = 'bos/boston-celtics'
        if team == 'Brooklyn':
            team_url = 'bkn/brooklyn-nets'
        if team == 'New York':
            team_url = 'ny/new-york-knicks'
        if team == 'Philly':
            team_url = 'phi/philadelphia-76ers'
        if team == 'Toronto':
            team_url = 'tor/toronto-raptors'
        if team == 'Golden State':
            team_url = 'gs/golden-state-warriors'
        if team == 'LAC':
            team_url = 'lac/la-clippers'
        if team == 'LAL':
            team_url = 'lal/los-angeles-lakers'
        if team == 'Phoenix':
            team_url = 'phx/phoenix-suns'
        if team == 'Sacramento':
            team_url = 'sac/sacramento-kings'
        if team == 'Chicago':
            team_url = 'chi/chicago-bulls'
        if team == 'Cleveland':
            team_url = 'cle/cleveland-cavaliers'
        if team == 'Detroit':
            team_url = 'det/detroit-pistons'
        if team == 'Indiana':
            team_url = 'ind/indiana-pacers'
        if team == 'Milwaukee':
            team_url = 'mil/milwaukee-bucks'
        if team == 'Atlanta':
            team_url = 'atl/atlanta-hawks'
        if team == 'Charlotte':
            team_url = 'cha/charlotte-hornets'
        if team == 'Miami':
            team_url = 'mia/miami-heat'
        if team == 'Orlando':
            team_url = 'orl/orlando-magic'
        if team == 'Washington':
            team_url = 'wsh/washington-wizards'
        if team == 'Denver':
            team_url = 'den/denver-nuggets'
        if team == 'Minnesota':
            team_url = 'min/minnesota-timberwolves'
        if team == 'OKC':
            team_url = 'okc/oklahoma-city-thunder'
        if team == 'Portland':
            team_url = 'por/portland-trail-blazers'
        if team == 'Utah':
            team_url = 'utah/utah-jazz'
        if team == 'Dallas':
            team_url = 'dal/dallas-mavericks'
        if team == 'Houston':
            team_url = 'hou/houston-rockets'
        if team == 'Memphis':
            team_url = 'mem/memphis-grizzlies'
        if team == 'New Orleans':
            team_url = 'no/new-orleans-pelicans'
        if team == 'San Antonio':
            team_url = 'sa/san-antonio-spurs'
            
        ###
        
        url_roster = 'https://www.espn.com/nba/team/roster/_/name/'
        html_hornets = requests.get(url_roster + team_url)
        soup_hornets = bs4.BeautifulSoup(html_hornets.content, features='html.parser')
        ids_hornets = soup_hornets.find_all('a', {'class': 'AnchorLink'})

        new = []

        for elem in ids_hornets:
            if 'div' not in str(elem):
                if '/player/_/id/' in str(elem):
                    new.append(str(elem))

        # for elem in new:
        #     print(elem)
        #     print('\n')

        team_ids = []

        i = 0
        while True:
            if i < len(new):
                elem = new[i]
                name_index = elem.index('"0">')
                name_end_index = elem.index('</a>')
                id_index = elem.index('/id/')
                id_end_index = elem.index('" tabindex=')
                player_name = elem[name_index + 4: name_end_index]
                player_id = elem[id_index + 4: id_end_index]
                lst = [player_name, player_id]
                team_ids.append(lst)
                i += 1
                continue
            else:
                break
            
        # for elem in team_ids:
        #     print(elem)
            
        dict_team_ids = {x[0]:x[1:] for x in team_ids}
        team_ids_keys = (dict_team_ids.keys())
        if player in team_ids_keys:
            player_id = dict_team_ids[player]
            player_id = player_id[0]
        else:
            return('Wrong player name.')
        
        
        
        ###
        
        # TESTING WIHT LAMELO BALL'S GAME BY GAME PAGE

        url_gbg = 'https://www.espn.com/nba/player/gamelog/_/id/'
        html_gbg = requests.get(url_gbg + player_id)
        soup_gbg = bs4.BeautifulSoup(html_gbg.content, features='html.parser')

        new = []

        for elem in soup_gbg:
            if 'Regular Season' in str(elem):
                new.append(str(elem))
                
        meloBall = new[0]
        
        print('\n')
        # print(meloBall)
        print('\n')

        # game = meloBall.index('"groups":[{"name":"2021-22 Regular Season","tbls":[{"name":') # 
        game = meloBall.index('{"name":"Postseason","tbls":')
        meloBall = meloBall[game:]
        preseason_index = meloBall.index(',["Totals","')
        meloBall = meloBall[:preseason_index]
        if '"allStar":"*"},' in meloBall:
            ind = meloBall.index('"allStar":"*"},')
            ind_end = meloBall.index('4th quarter untimed')
            meloBall = meloBall[:ind] + meloBall[ind_end:]
        melo_ball = meloBall.split('"stats":[')
        # print(meloBall[game:game + 700])

        i = 0
        while True:
            if i < len(melo_ball):
                if ']' in str(melo_ball[i]):
                    ind = melo_ball[i].index(']')
                    melo_ball[i] = melo_ball[i][:ind]
                    melo_ball[i] = melo_ball[i].split(',')
                    if '.' in melo_ball[i][0]:
                        del melo_ball[i]
                        continue
                    lst = melo_ball[i]
                    a = 0
                    while True:
                        if a < len(melo_ball[i]):
                            melo_ball[i][a] = melo_ball[i][a][1:-1]
                            a += 1
                            continue
                        else:
                            break
                    i += 1
                    continue
                else:
                    del melo_ball[i]
                    continue
            else:
                break

        # for elem in melo_ball:
        #     print(elem)
        
        player_stats = [['minutes'],
                        ['field goals'],
                        ['field goal percentage'],
                        ['threes'], 
                        ['three percentage'], 
                        ['free throws'], 
                        ['free throw percentage'], 
                        ['rebounds'],
                        ['assists'],
                        ['blocks'],
                        ['steals'], 
                        ['fouls'],
                        ['turn overs'],
                        ['points']
                        ]
        
        i = 0
        a = 0
        while True:
            if i < len(melo_ball):
                if a < len(player_stats):
                    if '-' in melo_ball[i][a]:
                        ind = melo_ball[i][a].index('-')
                        melo_ball[i][a] = melo_ball[i][a][:ind]
                    if player_stats[a][0] == 'free throw percentage' or player_stats[a][0] == 'three percentage' or player_stats[a][0] == 'field goal percentage':
                        melo_ball[i][a] = float(melo_ball[i][a])
                        player_stats[a].append(melo_ball[i][a])
                    if player_stats[a][0] != 'free throw percentage' and player_stats[a][0] != 'three percentage' and player_stats[a][0] != 'field goal percentage':
                        melo_ball[i][a] = int(melo_ball[i][a])
                        player_stats[a].append(melo_ball[i][a])
                    a += 1
                    continue
                else:
                    a = 0
                    i += 1
                    continue
            else:
                break
        
        # for elem in player_stats:
        #     print(elem)
            
        dict_player_stats = {x[0]:x[1:] for x in player_stats}
        player_stats_keys = (dict_player_stats.keys())
        
        if bet_type == 1:    
            if stat in player_stats_keys:
                stat_list = dict_player_stats[stat]
                print(stat_list)
            else:
                return('Wrong stat.')
            
            # print('\n')
            # print(stat_list)
            # print('\n')
            
            avg = statistics.mean(stat_list)
            std = statistics.pstdev(stat_list)
            # team, player, stat
            print('\n')
            print(str(player) + "'s average " + str(stat) + ' = ' + str(avg))
            print(str(player) + "'s " + str(stat) + ' standard deviation = ' + str(std))
            player_chance = scipy.stats.norm.cdf(value, avg, std)
            player_chance = round(1 - player_chance, 6)
            player_chance = round(player_chance * 100, 4)
            print(str(player) + ' has a ' + str(player_chance) + '% chance of ' + str(value) + '+ ' + str(stat) + '.')
            print('\n')
            return
        if bet_type == 2:
            ind = stat.index('+')
            stat0 = str(stat[:ind])
            stat1 = str(stat[ind + 1:])
            
            if stat0 in player_stats_keys:
                stat0_list = dict_player_stats[stat0]
            else:
                return('Wrong stat.')
            if stat1 in player_stats_keys:
                stat1_list = dict_player_stats[stat1]
            else:
                return('Wrong stat.')
            
            avg0 = statistics.mean(stat0_list)
            std0 = statistics.pstdev(stat0_list)
            avg1 = statistics.mean(stat1_list)
            std1 = statistics.pstdev(stat1_list)
            avg = avg0 + avg1
            std = std = math.sqrt(round((std0 * std0) + (std1 * std1), 6))
            # team, player, stat
            print('\n')
            # print(str(player) + "'s average " + str(stat) + ' = ' + str(avg))
            # print(str(player) + "'s " + str(stat) + ' standard deviation = ' + str(std))
            player_chance = scipy.stats.norm.cdf(value, avg, std)
            player_chance = round(1 - player_chance, 6)
            player_chance = round(player_chance * 100, 4)
            print(str(player) + ' has a ' + str(player_chance) + '% chance of ' + str(value) + '+ ' + str(stat0) + ' + ' + str(stat1) + '.')
            print('\n')
            return
    if league == 'NHL':
        if team == 'Boston':
            team_url = 'bos/boston-bruins'
        if team == 'Buffalo':
            team_url = 'buf/buffalo-sabres'
        if team == 'NYI':
            team_url = 'nyi/new-york-islanders'
        if team == 'Philly':
            team_url = 'phi/philadelphia-flyers'
        if team == 'Toronto':
            team_url = 'tor/toronto-maple-leafs'
        if team == 'Montreal':
            team_url = 'mtl/montreal-canadiens'
        if team == 'Ottawa':
            team_url = 'ott/ottawa-senators'
        if team == 'LA':
            team_url = 'la/los-angeles-kings'
        if team == 'Arizona':
            team_url = 'ari/arizona-coyotes'
        if team == 'New Jersey':
            team_url = 'nj/new-jersey-devils'
        if team == 'Chicago':
            team_url = 'chi/chicago-blackhawks'
        if team == 'Seattle':
            team_url = 'sea/seattle-kraken'
        if team == 'Vancouver':
            team_url = 'van/vancouver-canucks'
        if team == 'Vegas':
            team_url = 'vgk/vegas-golden-knights'
        if team == 'Colombus':
            team_url = 'cbj/columbus-blue-jackets'
        if team == 'Detroit':
            team_url = 'det/detroit-red-wings'
        if team == 'Pittsburgh':
            team_url = 'pit/pittsburgh-penguins'
        if team == 'San Jose':
            team_url = 'sj/san-jose-sharks'
        if team == 'Edmonton':
            team_url = 'edm/edmonton-oilers'
        if team == 'Carolina':
            team_url = 'car/carolina-hurricanes'
        if team == 'Florida':
            team_url = 'fla/florida-panthers'
        if team == 'NYR':
            team_url = 'nyr/new-york-rangers'
        if team == 'Washington':
            team_url = 'wsh/washington-capitals'
        if team == 'Colorado':
            team_url = 'col/colorado-avalanche'
        if team == 'Minnesota':
            team_url = 'min/minnesota-wild'
        if team == 'Calgary':
            team_url = 'cgy/calgary-flames'
        if team == 'Anaheim':
            team_url = 'ana/anaheim-ducks'
        if team == 'Dallas':
            team_url = 'dal/dallas-stars'
        if team == 'Winnipeg':
            team_url = 'wpg/winnipeg-jets'
        if team == 'Tampa Bay':
            team_url = 'tb/tampa-bay-lightning'
        if team == 'Nashville':
            team_url = 'nsh/nashville-predators'
        if team == 'St. Louis':
            team_url = 'stl/st-louis-blues'
            
        ###
        
        url_roster = 'https://www.espn.com/nhl/team/roster/_/name/'
        html_roster = requests.get(url_roster + team_url)
        soup_roster = bs4.BeautifulSoup(html_roster.content, features='html.parser')
        ids_roster = soup_roster.find_all('a', {'class': 'AnchorLink'})

        roster = []
        for elem in ids_roster:
            if 'div' not in str(elem):
                if '/player/_/id/' in str(elem):
                    roster.append(str(elem))

        # for elem in roster:
        #     print(elem)
        #     print('\n')

        team_ids = []
        i = 0
        while True:
            if i < len(roster):
                elem = roster[i]
                # print(elem)
                name_index = elem.index('"0">')
                name_end_index = elem.index('</a>')
                id_index = elem.index('/id/')
                id_end_index = elem.index('" tabindex=')
                player_name = elem[name_index + 4: name_end_index]
                player_id = elem[id_index + 4: id_end_index]
                lst = [player_name, player_id]
                team_ids.append(lst)
                i += 1
                continue
            else:
                break
            
        # for elem in team_ids:
        #     print(elem)
            
        dict_team_ids = {x[0]:x[1:] for x in team_ids}
        team_ids_keys = (dict_team_ids.keys())
        if player in team_ids_keys:
            player_id = dict_team_ids[player]
            player_id = player_id[0]
        else:
            return('Wrong player name.')
        
        
        
        ###
        
        # TESTING WIHT LAMELO BALL'S GAME BY GAME PAGE

        url_gbg = 'https://www.espn.com/nhl/player/gamelog/_/id/'
        html_gbg = requests.get(url_gbg + player_id)
        soup_gbg = bs4.BeautifulSoup(html_gbg.content, features='html.parser')

        new = []
        for elem in soup_gbg:
            if 'Regular Season' in str(elem):
                new.append(str(elem))
                
        statList = new[0]
        
        # print(statList)

        # game = meloBall.index('"groups":[{"name":"2021-22 Regular Season","tbls":[{"name":') # reg season
        game = statList.index('{"name":"Postseason","tbls":') # playoffs
        statList = statList[game:]
        # print(statList)
        preseason_index = statList.index('Regular Season Stats","data":[["Totals"')
        statList = statList[:preseason_index]
        x = statList.count('}],"totals":{"stats":["')
        i = 0
        # print('\n')
        # print('x = ' + str(x))     # ","events":[{"id":"
        # print('\n')
        stat_list = statList.split('"stats":[')
        while True:
            if i < x:
                if '}],"totals":{"stats":["' in statList:
                    ind = statList.index('}],"totals":{"stats":["')
                    ind_end = statList.index('","events":[{"id":"')
                    statList = statList[:ind] + statList[ind_end:]
                # stat_list = statList.split('"stats":[')
                i += 1
                continue
            else:
                break
                # print(meloBall[game:game + 700])
        # for elem in stat_list:
        #     print(elem)
            # print('\n')
        i = 0
        while True:
            if i < len(stat_list):
                if ']' in str(stat_list[i]):
                    if '"],"label":"' in str(stat_list[i]):
                        del stat_list[i]
                        continue
                    ind = stat_list[i].index(']')
                    stat_list[i] = stat_list[i][:ind]
                    stat_list[i] = stat_list[i].split(',')
                    if '.' in stat_list[i][0]:
                        del stat_list[i]
                        continue
                    lst = stat_list[i]
                    a = 0
                    while True:
                        if a < len(stat_list[i]):
                            stat_list[i][a] = stat_list[i][a][1:-1]
                            a += 1
                            continue
                        else:
                            break
                    i += 1
                    continue
                else:
                    del stat_list[i]
                    continue
            else:
                break
        
        # print('\n')
        # print('should be fixed')
        # for elem in stat_list:
        #     print(elem)
        # print('\n')
        
        
        player_stats = [['goals'],
                        ['assists'],
                        ['points'],
                        ['+/-'], 
                        ['penalty minutes'], 
                        ['shots'], 
                        ['shooting percentage'], 
                        ['power play goals'],
                        ['power play assists'],
                        ['short handed goals'],
                        ['short handed assists'], 
                        ['game winning goals'],
                        ['game tying goals'],
                        ['time on ice'],
                        ['production']
                        ]
        # print(len(player_stats))
        i = 0
        a = 0
        while True:
            if i < len(stat_list):
                if a < len(player_stats):
                    # if '-' in stat_list[i][a]:
                    #     ind = stat_list[i][a].index('-')
                    #     stat_list[i][a] = stat_list[i][a][:ind]
                    if player_stats[a][0] == 'shooting percentage':
                        stat_list[i][a] = float(stat_list[i][a])
                        player_stats[a].append(stat_list[i][a])
                        a += 1
                        continue
                    elif player_stats[a][0] == 'time on ice' or player_stats[a][0] == 'production':
                        stat_list[i][a] = str(stat_list[i][a])
                        player_stats[a].append(stat_list[i][a])
                        a += 1
                        continue
                    else: #if player_stats[a][0] != 'shooting percentage' and player_stats[a][0] != 'time on ice' and player_stats[a][0] != 'production':
                        # print(player_stats[a][0])
                        stat_list[i][a] = int(stat_list[i][a])
                        player_stats[a].append(stat_list[i][a])
                        a += 1
                        continue
                else:
                    a = 0
                    i += 1
                    continue
            else:
                break
        
        # for elem in player_stats:
        #     print(elem)
            
        dict_player_stats = {x[0]:x[1:] for x in player_stats}
        player_stats_keys = (dict_player_stats.keys())
        
        if bet_type == 1:    
            if stat in player_stats_keys:
                stat_list = dict_player_stats[stat]
            else:
                return('Wrong stat.')
            
            # print('\n')
            # print(stat_list)
            # print('\n')
            
            avg = statistics.mean(stat_list)
            std = statistics.pstdev(stat_list)
            # team, player, stat
            print('\n')
            print(str(player) + "'s average " + str(stat) + ' = ' + str(avg))
            print(str(player) + "'s " + str(stat) + ' standard deviation = ' + str(std))
            player_chance = scipy.stats.norm.cdf(value, avg, std)
            player_chance = round(1 - player_chance, 6)
            player_chance = round(player_chance * 100, 4)
            print(str(player) + ' has a ' + str(player_chance) + '% chance of ' + str(value) + '+ ' + str(stat) + '.')
            print('\n')
            return
        if bet_type == 2:
            ind = stat.index('+')
            stat0 = str(stat[:ind])
            stat1 = str(stat[ind + 1:])
            
            if stat0 in player_stats_keys:
                stat0_list = dict_player_stats[stat0]
            else:
                return('Wrong stat.')
            if stat1 in player_stats_keys:
                stat1_list = dict_player_stats[stat1]
            else:
                return('Wrong stat.')
            
            avg0 = statistics.mean(stat0_list)
            std0 = statistics.pstdev(stat0_list)
            avg1 = statistics.mean(stat1_list)
            std1 = statistics.pstdev(stat1_list)
            avg = avg0 + avg1
            std = std = math.sqrt(round((std0 * std0) + (std1 * std1), 6))
            # team, player, stat
            print('\n')
            # print(str(player) + "'s average " + str(stat) + ' = ' + str(avg))
            # print(str(player) + "'s " + str(stat) + ' standard deviation = ' + str(std))
            player_chance = scipy.stats.norm.cdf(value, avg, std)
            player_chance = round(1 - player_chance, 6)
            player_chance = round(player_chance * 100, 4)
            print(str(player) + ' has a ' + str(player_chance) + '% chance of ' + str(value) + '+ ' + str(stat0) + ' + ' + str(stat1) + '.')
            print('\n')
            return
        if bet_type == 3:
            ind = stat.index('+')
            stats = stat.split('+')
            stat0 = stats[0]
            stat1 = stats[1]
            stat2 = stats[2]
            
            if stat0 in player_stats_keys:
                stat0_list = dict_player_stats[stat0]
            else:
                return('Wrong stat0.')
            if stat1 in player_stats_keys:
                stat1_list = dict_player_stats[stat1]
            else:
                return('Wrong stat1.')
            if stat2 in player_stats_keys:
                stat2_list = dict_player_stats[stat2]
            else:
                return('Wrong stat2.')
            
            avg0 = statistics.mean(stat0_list)
            std0 = statistics.pstdev(stat0_list)
            avg1 = statistics.mean(stat1_list)
            std1 = statistics.pstdev(stat1_list)
            avg2 = statistics.mean(stat2_list)
            std2 = statistics.pstdev(stat2_list)
            avg = avg0 + avg1 + avg2
            std = std = math.sqrt(round((std0 * std0) + (std1 * std1) + (std2 * std2), 6))
            # team, player, stat
            print('\n')
            # print(str(player) + "'s average " + str(stat) + ' = ' + str(avg))
            # print(str(player) + "'s " + str(stat) + ' standard deviation = ' + str(std))
            player_chance = scipy.stats.norm.cdf(value, avg, std)
            player_chance = round(1 - player_chance, 6)
            player_chance = round(player_chance * 100, 4)
            print(str(player) + ' has a ' + str(player_chance) + '% chance of ' + str(value) + '+ ' + str(stat0) + ' + ' + str(stat1) + ' + ' + str(stat2) + '.')
            print('\n')
            return

# Current Leagues: NBA, NHL
# List teams by City Name except: Lakers = LAL, Clippers = LAC, Rangers = NYR, Islanders = NYI, Philadelphia = Philly
# Players by Full Name
# bet types: 1 = one stat, 2 = two stats combined (i.e. 40+ points+assists), 3 = three stats combined

def twoPlayers(league, team0, player0, stat0, value0, team1, player1, stat1, value1, bet_type):
    if league == 'NBA':
        if team0 == 'Boston':
            team0_url = 'bos/boston-celtics'
        if team0 == 'Brooklyn':
            team0_url = 'bkn/brooklyn-nets'
        if team0 == 'New York':
            team0_url = 'ny/new-york-knicks'
        if team0 == 'Philly':
            team0_url = 'phi/philadelphia-76ers'
        if team0 == 'Toronto':
            team0_url = 'tor/toronto-raptors'
        if team0 == 'Golden State':
            team0_url = 'gs/golden-state-warriors'
        if team0 == 'LAC':
            team0_url = 'lac/la-clippers'
        if team0 == 'LAL':
            team0_url = 'lal/los-angeles-lakers'
        if team0 == 'Phoenix':
            team0_url = 'phx/phoenix-suns'
        if team0 == 'Sacramento':
            team0_url = 'sac/sacramento-kings'
        if team0 == 'Chicago':
            team0_url = 'chi/chicago-bulls'
        if team0 == 'Cleveland':
            team0_url = 'cle/cleveland-cavaliers'
        if team0 == 'Detroit':
            team0_url = 'det/detroit-pistons'
        if team0 == 'Indiana':
            team0_url = 'ind/indiana-pacers'
        if team0 == 'Milwaukee':
            team0_url = 'mil/milwaukee-bucks'
        if team0 == 'Atlanta':
            team0_url = 'atl/atlanta-hawks'
        if team0 == 'Charlotte':
            team0_url = 'cha/charlotte-hornets'
        if team0 == 'Miami':
            team0_url = 'mia/miami-heat'
        if team0 == 'Orlando':
            team0_url = 'orl/orlando-magic'
        if team0 == 'Washington':
            team0_url = 'wsh/washington-wizards'
        if team0 == 'Denver':
            team0_url = 'den/denver-nuggets'
        if team0 == 'Minnesota':
            team0_url = 'min/minnesota-timberwolves'
        if team0 == 'OKC':
            team0_url = 'okc/oklahoma-city-thunder'
        if team0 == 'Portland':
            team0_url = 'por/portland-trail-blazers'
        if team0 == 'Utah':
            team0_url = 'utah/utah-jazz'
        if team0 == 'Dallas':
            team0_url = 'dal/dallas-mavericks'
        if team0 == 'Houston':
            team0_url = 'hou/houston-rockets'
        if team0 == 'Memphis':
            team0_url = 'mem/memphis-grizzlies'
        if team0 == 'New Orleans':
            team0_url = 'no/new-orleans-pelicans'
        if team0 == 'San Antonio':
            team0_url = 'sa/san-antonio-spurs'
        if team1 == 'Boston':
            team1_url = 'bos/boston-celtics'
        if team1 == 'Brooklyn':
            team1_url = 'bkn/brooklyn-nets'
        if team1 == 'New York':
            team1_url = 'ny/new-york-knicks'
        if team1 == 'Philly':
            team1_url = 'phi/philadelphia-76ers'
        if team1 == 'Toronto':
            team1_url = 'tor/toronto-raptors'
        if team1 == 'Golden State':
            team1_url = 'gs/golden-state-warriors'
        if team1 == 'LAC':
            team1_url = 'lac/la-clippers'
        if team1 == 'LAL':
            team1_url = 'lal/los-angeles-lakers'
        if team1 == 'Phoenix':
            team1_url = 'phx/phoenix-suns'
        if team1 == 'Sacramento':
            team1_url = 'sac/sacramento-kings'
        if team1 == 'Chicago':
            team1_url = 'chi/chicago-bulls'
        if team1 == 'Cleveland':
            team1_url = 'cle/cleveland-cavaliers'
        if team1 == 'Detroit':
            team1_url = 'det/detroit-pistons'
        if team1 == 'Indiana':
            team1_url = 'ind/indiana-pacers'
        if team1 == 'Milwaukee':
            team1_url = 'mil/milwaukee-bucks'
        if team1 == 'Atlanta':
            team1_url = 'atl/atlanta-hawks'
        if team1 == 'Charlotte':
            team1_url = 'cha/charlotte-hornets'
        if team1 == 'Miami':
            team1_url = 'mia/miami-heat'
        if team1 == 'Orlando':
            team1_url = 'orl/orlando-magic'
        if team1 == 'Washington':
            team1_url = 'wsh/washington-wizards'
        if team1 == 'Denver':
            team1_url = 'den/denver-nuggets'
        if team1 == 'Minnesota':
            team1_url = 'min/minnesota-timberwolves'
        if team1 == 'OKC':
            team1_url = 'okc/oklahoma-city-thunder'
        if team1 == 'Portland':
            team1_url = 'por/portland-trail-blazers'
        if team1 == 'Utah':
            team1_url = 'utah/utah-jazz'
        if team1 == 'Dallas':
            team1_url = 'dal/dallas-mavericks'
        if team1 == 'Houston':
            team1_url = 'hou/houston-rockets'
        if team1 == 'Memphis':
            team1_url = 'mem/memphis-grizzlies'
        if team1 == 'New Orleans':
            team1_url = 'no/new-orleans-pelicans'
        if team1 == 'San Antonio':
            team1_url = 'sa/san-antonio-spurs'
            
        # GET HTML SOUP CONTENT WITH BEAUTIFUL SOUP
        
        url_roster0 = 'https://www.espn.com/nba/team/roster/_/name/'
        # print(url_roster0 + team0_url)
        html_roster0 = requests.get(url_roster0 + team0_url)
        soup_roster0 = bs4.BeautifulSoup(html_roster0.content, features='html.parser')
        ids_roster0 = soup_roster0.find_all('a', {'class': 'AnchorLink'})
        
        url_roster1 = 'https://www.espn.com/nba/team/roster/_/name/'
        # print(url_roster1 + team1_url)
        html_roster1 = requests.get(url_roster1 + team1_url)
        soup_roster1 = bs4.BeautifulSoup(html_roster1.content, features='html.parser')
        ids_roster1 = soup_roster1.find_all('a', {'class': 'AnchorLink'})

        # CREATE LIST OF PLAYER IDS FROM TEAM

        roster0 = []
        for elem in ids_roster0:
            if 'div' not in str(elem):
                if '/player/_/id/' in str(elem):
                    roster0.append(str(elem))
        # print(roster0)    

        roster1 = []
        for elem in ids_roster1:
            if 'div' not in str(elem):
                if '/player/_/id/' in str(elem):
                    roster1.append(str(elem))

        team0_ids = []
        i = 0
        while True:
            if i < len(roster0):
                elem = roster0[i]
                name_index = elem.index('"0">')
                name_end_index = elem.index('</a>')
                id_index = elem.index('/id/')
                id_end_index = elem.index('" tabindex=')
                player0_name = elem[name_index + 4: name_end_index]
                player0_id = elem[id_index + 4: id_end_index]
                lst = [player0_name, player0_id]
                team0_ids.append(lst)
                i += 1
                continue
            else:
                break
        
        team1_ids = []
        i = 0
        while True:
            if i < len(roster1):
                elem = roster1[i]
                name_index = elem.index('"0">')
                name_end_index = elem.index('</a>')
                id_index = elem.index('/id/')
                id_end_index = elem.index('" tabindex=')
                player1_name = elem[name_index + 4: name_end_index]
                player1_id = elem[id_index + 4: id_end_index]
                lst = [player1_name, player1_id]
                team1_ids.append(lst)
                i += 1
                continue
            else:
                break
            
        dict_team0_ids = {x[0]:x[1:] for x in team0_ids}
        team0_ids_keys = (dict_team0_ids.keys())
        if player0 in team0_ids_keys:
            player0_id = dict_team0_ids[player0]
            player0_id = player0_id[0]
        else:
            return('Wrong player0 name.')
        # print(dict_team0_ids)
        
        dict_team1_ids = {x[0]:x[1:] for x in team1_ids}
        team1_ids_keys = (dict_team1_ids.keys())
        # print(player1)
        if player1 in team1_ids_keys:
            player1_id = dict_team1_ids[player1]
            player1_id = player1_id[0]
        else:
            return('Wrong player1 name.')
        # print(dict_team1_ids)
        
        
        
        ###
        
        # TESTING WIHT LAMELO BALL'S GAME BY GAME PAGE

        url_gbg0 = 'https://www.espn.com/nba/player/gamelog/_/id/'
        html_gbg0 = requests.get(url_gbg0 + player0_id)
        soup_gbg0 = bs4.BeautifulSoup(html_gbg0.content, features='html.parser')

        url_gbg1 = 'https://www.espn.com/nba/player/gamelog/_/id/'
        html_gbg1 = requests.get(url_gbg1 + player1_id)
        soup_gbg1 = bs4.BeautifulSoup(html_gbg1.content, features='html.parser')

        player0_gbg = []
        for elem in soup_gbg0:
            if 'Regular Season' in str(elem):
                player0_gbg.append(str(elem))
        
        player1_gbg = []
        for elem in soup_gbg1:
            if 'Regular Season' in str(elem):
                player1_gbg.append(str(elem))
        
        player0_gbg = player0_gbg[0]
        # game = player0_gbg.index('"groups":[{"name":"2021-22 Regular Season","tbls":[{"name":') # {"name":"Postseason","tbls":
        game = player0_gbg.index('{"name":"Postseason","tbls":')
        player0_gbg = player0_gbg[game:]
        preseason_index = player0_gbg.index(',["Totals","')
        player0_gbg = player0_gbg[:preseason_index]
        if '"allStar":"*"},' in player0_gbg:
            ind = player0_gbg.index('"allStar":"*"},')
            ind_end = player0_gbg.index('4th quarter untimed')
            player0_gbg = player0_gbg[:ind] + player0_gbg[ind_end:]
        player_0_gbg = player0_gbg.split('"stats":[')
        # print(player0_gbg[game:game + 700])
        
        player1_gbg = player1_gbg[0]
        # game = player1_gbg.index('"groups":[{"name":"2021-22 Regular Season","tbls":[{"name":')
        game = player1_gbg.index('{"name":"Postseason","tbls":')
        player1_gbg = player1_gbg[game:]
        # print(player1_gbg)
        preseason_index = player1_gbg.index(',["Totals","')
        player1_gbg = player1_gbg[:preseason_index]
        if '"allStar":"*"},' in player1_gbg:
            ind = player1_gbg.index('"allStar":"*"},')
            ind_end = player1_gbg.index('4th quarter untimed')
            player1_gbg = player1_gbg[:ind] + player1_gbg[ind_end:]
        player_1_gbg = player1_gbg.split('"stats":[')

        i = 0
        while True:
            if i < len(player_0_gbg):
                if ']' in str(player_0_gbg[i]):
                    ind = player_0_gbg[i].index(']')
                    player_0_gbg[i] = player_0_gbg[i][:ind]
                    player_0_gbg[i] = player_0_gbg[i].split(',')
                    if '.' in player_0_gbg[i][0]:
                        del player_0_gbg[i]
                        continue
                    lst = player_0_gbg[i]
                    a = 0
                    while True:
                        if a < len(player_0_gbg[i]):
                            player_0_gbg[i][a] = player_0_gbg[i][a][1:-1]
                            a += 1
                            continue
                        else:
                            break
                    i += 1
                    continue
                else:
                    del player_0_gbg[i]
                    continue
            else:
                break
        
        i = 0
        while True:
            if i < len(player_1_gbg):
                if ']' in str(player_1_gbg[i]):
                    ind = player_1_gbg[i].index(']')
                    player_1_gbg[i] = player_1_gbg[i][:ind]
                    player_1_gbg[i] = player_1_gbg[i].split(',')
                    if '.' in player_1_gbg[i][1]:
                        del player_1_gbg[i]
                        continue
                    lst = player_1_gbg[i]
                    a = 0
                    while True:
                        if a < len(player_1_gbg[i]):
                            player_1_gbg[i][a] = player_1_gbg[i][a][1:-1]
                            a += 1
                            continue
                        else:
                            break
                    i += 1
                    continue
                else:
                    del player_1_gbg[i]
                    continue
            else:
                break
            
        

        # for elem in melo_ball:
        #     print(elem)
        
        player0_stats = [['minutes'],
                        ['field goals'],
                        ['field goal percentage'],
                        ['threes'], 
                        ['three percentage'], 
                        ['free throws'], 
                        ['free throw percentage'], 
                        ['rebounds'],
                        ['assists'],
                        ['blocks'],
                        ['steals'], 
                        ['fouls'],
                        ['turn overs'],
                        ['points']
                        ]
        
        player1_stats = [['minutes'],
                        ['field goals'],
                        ['field goal percentage'],
                        ['threes'], 
                        ['three percentage'], 
                        ['free throws'], 
                        ['free throw percentage'], 
                        ['rebounds'],
                        ['assists'],
                        ['blocks'],
                        ['steals'], 
                        ['fouls'],
                        ['turn overs'],
                        ['points']
                        ]
        
        i = 0
        a = 0
        while True:
            if i < len(player_0_gbg):
                if a < len(player0_stats):
                    if '-' in player_0_gbg[i][a]:
                        ind = player_0_gbg[i][a].index('-')
                        player_0_gbg[i][a] = player_0_gbg[i][a][:ind]
                    if player0_stats[a][0] == 'free throw percentage' or player0_stats[a][0] == 'three percentage' or player0_stats[a][0] == 'field goal percentage':
                        player_0_gbg[i][a] = float(player_0_gbg[i][a])
                        player0_stats[a].append(player_0_gbg[i][a])
                    if player0_stats[a][0] != 'free throw percentage' and player0_stats[a][0] != 'three percentage' and player0_stats[a][0] != 'field goal percentage':
                        player_0_gbg[i][a] = int(player_0_gbg[i][a])
                        player0_stats[a].append(player_0_gbg[i][a])
                    a += 1
                    continue
                else:
                    a = 0
                    i += 1
                    continue
            else:
                break
            
        i = 0
        a = 0
        while True:
            if i < len(player_1_gbg):
                if a < len(player1_stats):
                    if '-' in player_1_gbg[i][a]:
                        ind = player_1_gbg[i][a].index('-')
                        player_1_gbg[i][a] = player_1_gbg[i][a][:ind]
                    if player1_stats[a][0] == 'free throw percentage' or player1_stats[a][0] == 'three percentage' or player1_stats[a][0] == 'field goal percentage':
                        player_1_gbg[i][a] = float(player_1_gbg[i][a])
                        player1_stats[a].append(player_1_gbg[i][a])
                    if player1_stats[a][0] != 'free throw percentage' and player1_stats[a][0] != 'three percentage' and player1_stats[a][0] != 'field goal percentage':
                        player_1_gbg[i][a] = int(player_1_gbg[i][a])
                        player1_stats[a].append(player_1_gbg[i][a])
                    a += 1
                    continue
                else:
                    a = 1
                    i += 1
                    continue
            else:
                break
        
        
        print('something')
        if bet_type == 1:
            if stat0 == stat1:
                # for elem in player0_stats:
                #     print(elem)
                dict_player0_stats = {x[0]:x[1:] for x in player0_stats}
                player0_stats_keys = (dict_player0_stats.keys())
                if stat0 in player0_stats_keys:
                    stat0_list = dict_player0_stats[stat0]
                # else:
                #     return('Wrong stat0.')
                dict_player1_stats = {x[0]:x[1:] for x in player1_stats}
                player1_stats_keys = (dict_player1_stats.keys())
                if stat1 in player1_stats_keys:
                    stat1_list = dict_player1_stats[stat0]
                # else:
                #     return('Wrong stat1.')
                avg0 = statistics.mean(stat0_list)
                std0 = statistics.pstdev(stat0_list)
                avg1 = statistics.mean(stat1_list)
                std1 = statistics.pstdev(stat1_list)
                print('\n')
                print(str(player0) + "'s average " + str(stat0) + ' = ' + str(avg0))
                print(str(player0) + "'s " + str(stat0) + ' standard deviation = ' + str(std0))
                player0_chance = scipy.stats.norm.cdf(value0, avg0, std0)
                player0_chance = round(1 - player0_chance, 6)
                player0_chance = round(player0_chance * 100, 4)
                print(str(player0) + ' has a ' + str(player0_chance) + '% chance of ' + str(value0) + '+ ' + str(stat0) + '.')
                print('\n')
                print(str(player1) + "'s average " + str(stat1) + ' = ' + str(avg1))
                print(str(player1) + "'s " + str(stat1) + ' standard deviation = ' + str(std1))
                player1_chance = scipy.stats.norm.cdf(value1, avg1, std1)
                player1_chance = round(1 - player1_chance, 6)
                player1_chance = round(player1_chance * 100, 4)
                print(str(player1) + ' has a ' + str(player1_chance) + '% chance of ' + str(value1) + '+ ' + str(stat1) + '.')
                print('\n')
                combo_chance = round((player0_chance / 100) * (player1_chance / 100) * 100, 5)
                print('There is a ' + str(combo_chance) + '% for both ' + str(player0) + ' and ' + str(player1) + ' to record '+ str(value0) + '+ ' + str(stat0) + '.')
                print('\n')
                return
            if stat0 != stat1:
                # for elem in player0_stats:
                #     print(elem)
                dict_player0_stats = {x[0]:x[1:] for x in player0_stats}
                player0_stats_keys = (dict_player0_stats.keys())
                if stat0 in player0_stats_keys:
                    stat0_list = dict_player0_stats[stat0]
                # else:
                #     return('Wrong stat0.')
                dict_player1_stats = {x[0]:x[1:] for x in player1_stats}
                player1_stats_keys = (dict_player1_stats.keys())
                if stat1 in player1_stats_keys:
                    stat1_list = dict_player1_stats[stat1]
                # else:
                #     return('Wrong stat1.')
                avg0 = statistics.mean(stat0_list)
                std0 = statistics.pstdev(stat0_list)
                avg1 = statistics.mean(stat1_list)
                std1 = statistics.pstdev(stat1_list)
                print('\n')
                print(str(player0) + "'s average " + str(stat0) + ' = ' + str(avg0))
                print(str(player0) + "'s " + str(stat0) + ' standard deviation = ' + str(std0))
                player0_chance = scipy.stats.norm.cdf(value0, avg0, std0)
                player0_chance = round(1 - player0_chance, 6)
                player0_chance = round(player0_chance * 100, 4)
                print(str(player0) + ' has a ' + str(player0_chance) + '% chance of ' + str(value0) + '+ ' + str(stat0) + '.')
                print('\n')
                print(str(player1) + "'s average " + str(stat1) + ' = ' + str(avg1))
                print(str(player1) + "'s " + str(stat1) + ' standard deviation = ' + str(std1))
                player1_chance = scipy.stats.norm.cdf(value1, avg1, std1)
                player1_chance = round(1 - player1_chance, 6)
                player1_chance = round(player1_chance * 100, 4)
                print(str(player1) + ' has a ' + str(player1_chance) + '% chance of ' + str(value1) + '+ ' + str(stat1) + '.')
                print('\n')
                combo_chance = round((player0_chance / 100) * (player1_chance / 100) * 100, 5)
                print('There is a ' + str(combo_chance) + '% for ' + str(player0) + ' to record '+ str(value0) + '+ ' + str(stat0) + ' and ' + str(player1) + ' to record ' + str(value1) + '+ ' + str(stat1) + '.')
                print('\n')
                return
        if bet_type == 2:
            print('Bet Type Worked')
            if stat0 == stat1:
                print('stat matching worked')
                # for elem in player0_stats:
                #     print(elem)
                dict_player0_stats = {x[0]:x[1:] for x in player0_stats}
                player0_stats_keys = (dict_player0_stats.keys())
                if stat0 in player0_stats_keys:
                    stat0_list = dict_player0_stats[stat0]
                # else:
                #     return('Wrong stat0.')
                dict_player1_stats = {x[0]:x[1:] for x in player1_stats}
                player1_stats_keys = (dict_player1_stats.keys())
                if stat1 in player1_stats_keys:
                    stat1_list = dict_player1_stats[stat0]
                # else:
                #     return('Wrong stat1.')
                avg0 = statistics.mean(stat0_list)
                std0 = statistics.pstdev(stat0_list)
                avg1 = statistics.mean(stat1_list)
                std1 = statistics.pstdev(stat1_list)
                combo_avg = avg0 + avg1
                print(combo_avg)
                combo_std = math.sqrt(round((std0 * std0) + (std1 * std1), 6))
                print(combo_std)
                combo_chance = scipy.stats.norm.cdf(value0, combo_avg, combo_std)
                combo_chance = round(1 - combo_chance, 6)
                combo_chance = round(combo_chance * 100, 4)
                str_combo_chance = str(combo_chance)
                print('\n')
                if str_combo_chance[0] != '8':
                    print('There is a ' + str(combo_chance) + '% chance of ' + str(player0) + ' and ' +str(player1) + ' combining for ' + str(value0) + '+ ' + str(stat0) + '.')
                if str_combo_chance[0] == '8':
                    print('There is an ' + str(combo_chance) + '% chance of ' + str(player0) + ' and ' +str(player1) + ' combining for ' + str(value0) + '+ ' + str(stat0) + '.')
                print('\n')
                return
            if stat0 != stat1:
                dict_player0_stats = {x[0]:x[1:] for x in player0_stats}
                player0_stats_keys = (dict_player0_stats.keys())
                if stat0 in player0_stats_keys:
                    stat00_list = dict_player0_stats[stat0]
                dict_player1_stats = {x[0]:x[1:] for x in player1_stats}
                player1_stats_keys = (dict_player1_stats.keys())
                if stat1 in player1_stats_keys:
                    stat10_list = dict_player1_stats[stat0]
                dict_player0_stats = {x[0]:x[1:] for x in player0_stats}
                player0_stats_keys = (dict_player0_stats.keys())
                if stat0 in player0_stats_keys:
                    stat01_list = dict_player0_stats[stat1]
                dict_player1_stats = {x[0]:x[1:] for x in player1_stats}
                player1_stats_keys = (dict_player1_stats.keys())
                if stat1 in player1_stats_keys:
                    stat11_list = dict_player1_stats[stat1]
                avg00 = statistics.mean(stat00_list)
                std00 = statistics.pstdev(stat00_list)
                avg10 = statistics.mean(stat10_list)
                std10 = statistics.pstdev(stat10_list)
                avg01 = statistics.mean(stat01_list)
                std01 = statistics.pstdev(stat01_list)
                avg11 = statistics.mean(stat11_list)
                std11 = statistics.pstdev(stat11_list)
                combo_avg = avg00 + avg10 + avg01 + avg11
                combo_std = math.sqrt(round((std00 * std00) + (std10 * std10) + (std01 * std01) + (std11 * std11), 6))
                combo_chance = scipy.stats.norm.cdf(value0, combo_avg, combo_std)
                combo_chance = round(1 - combo_chance, 6)
                combo_chance = round(combo_chance * 100, 4)
                str_combo_chance = str(combo_chance)
                print('\n')
                if str_combo_chance[0] != '8':
                    print('There is a ' + str(combo_chance) + '% chance of ' + str(player0) + ' and ' +str(player1) + ' combining for ' + str(value0) + '+ ' + str(stat0) + ' and ' + str(stat1) + '.')
                if str_combo_chance[0] == '8':
                    print('There is an ' + str(combo_chance) + '% chance of ' + str(player0) + ' and ' +str(player1) + ' combining for ' + str(value0) + '+ ' + str(stat0) + ' and ' + str(stat1) + '.')
                print('\n')
                return
                
            
    if league == 'NHL':
        if team0 == 'Boston':
            team0_url = 'bos/boston-bruins'
        if team0 == 'Buffalo':
            team0_url = 'buf/buffalo-sabres'
        if team0 == 'NYI':
            team0_url = 'nyi/new-york-islanders'
        if team0 == 'Philly':
            team0_url = 'phi/philadelphia-flyers'
        if team0 == 'Toronto':
            team0_url = 'tor/toronto-maple-leafs'
        if team0 == 'Montreal':
            team0_url = 'mtl/montreal-canadiens'
        if team0 == 'Ottawa':
            team0_url = 'ott/ottawa-senators'
        if team0 == 'LA':
            team0_url = 'la/los-angeles-kings'
        if team0 == 'Arizona':
            team0_url = 'ari/arizona-coyotes'
        if team0 == 'New Jersey':
            team0_url = 'nj/new-jersey-devils'
        if team0 == 'Chicago':
            team0_url = 'chi/chicago-blackhawks'
        if team0 == 'Seattle':
            team0_url = 'sea/seattle-kraken'
        if team0 == 'Vancouver':
            team0_url = 'van/vancouver-canucks'
        if team0 == 'Vegas':
            team0_url = 'vgk/vegas-golden-knights'
        if team0 == 'Colombus':
            team0_url = 'cbj/columbus-blue-jackets'
        if team0 == 'Detroit':
            team0_url = 'det/detroit-red-wings'
        if team0 == 'Pittsburgh':
            team0_url = 'pit/pittsburgh-penguins'
        if team0 == 'San Jose':
            team0_url = 'sj/san-jose-sharks'
        if team0 == 'Edmonton':
            team0_url = 'edm/edmonton-oilers'
        if team0 == 'Carolina':
            team0_url = 'car/carolina-hurricanes'
        if team0 == 'Florida':
            team0_url = 'fla/florida-panthers'
        if team0 == 'NYR':
            team0_url = 'nyr/new-york-rangers'
        if team0 == 'Washington':
            team0_url = 'wsh/washington-capitals'
        if team0 == 'Colorado':
            team0_url = 'col/colorado-avalanche'
        if team0 == 'Minnesota':
            team0_url = 'min/minnesota-wild'
        if team0 == 'Calgary':
            team0_url = 'cgy/calgary-flames'
        if team0 == 'Anaheim':
            team0_url = 'ana/anaheim-ducks'
        if team0 == 'Dallas':
            team0_url = 'dal/dallas-stars'
        if team0 == 'Winnipeg':
            team0_url = 'wpg/winnipeg-jets'
        if team0 == 'Tampa Bay':
            team0_url = 'tb/tampa-bay-lightning'
        if team0 == 'Nashville':
            team0_url = 'nsh/nashville-predators'
        if team0 == 'St. Louis':
            team0_url = 'stl/st-louis-blues'
        if team1 == 'Boston':
            team1_url = 'bos/boston-bruins'
        if team1 == 'Buffalo':
            team1_url = 'buf/buffalo-sabres'
        if team1 == 'NYI':
            team1_url = 'nyi/new-york-islanders'
        if team1 == 'Philly':
            team1_url = 'phi/philadelphia-flyers'
        if team1 == 'Toronto':
            team1_url = 'tor/toronto-maple-leafs'
        if team1 == 'Montreal':
            team1_url = 'mtl/montreal-canadiens'
        if team1 == 'Ottawa':
            team1_url = 'ott/ottawa-senators'
        if team1 == 'LA':
            team1_url = 'la/los-angeles-kings'
        if team1 == 'Arizona':
            team1_url = 'ari/arizona-coyotes'
        if team1 == 'New Jersey':
            team1_url = 'nj/new-jersey-devils'
        if team1 == 'Chicago':
            team1_url = 'chi/chicago-blackhawks'
        if team1 == 'Seattle':
            team1_url = 'sea/seattle-kraken'
        if team1 == 'Vancouver':
            team1_url = 'van/vancouver-canucks'
        if team1 == 'Vegas':
            team1_url = 'vgk/vegas-golden-knights'
        if team1 == 'Colombus':
            team1_url = 'cbj/columbus-blue-jackets'
        if team1 == 'Detroit':
            team1_url = 'det/detroit-red-wings'
        if team1 == 'Pittsburgh':
            team1_url = 'pit/pittsburgh-penguins'
        if team1 == 'San Jose':
            team1_url = 'sj/san-jose-sharks'
        if team1 == 'Edmonton':
            team1_url = 'edm/edmonton-oilers'
        if team1 == 'Carolina':
            team1_url = 'car/carolina-hurricanes'
        if team1 == 'Florida':
            team1_url = 'fla/florida-panthers'
        if team1 == 'NYR':
            team1_url = 'nyr/new-york-rangers'
        if team1 == 'Washington':
            team1_url = 'wsh/washington-capitals'
        if team1 == 'Colorado':
            team1_url = 'col/colorado-avalanche'
        if team1 == 'Minnesota':
            team1_url = 'min/minnesota-wild'
        if team1 == 'Calgary':
            team1_url = 'cgy/calgary-flames'
        if team1 == 'Anaheim':
            team1_url = 'ana/anaheim-ducks'
        if team1 == 'Dallas':
            team1_url = 'dal/dallas-stars'
        if team1 == 'Winnipeg':
            team1_url = 'wpg/winnipeg-jets'
        if team1 == 'Tampa Bay':
            team1_url = 'tb/tampa-bay-lightning'
        if team1 == 'Nashville':
            team1_url = 'nsh/nashville-predators'
        if team1 == 'St. Louis':
            team1_url = 'stl/st-louis-blues'
            
        ###
        
        url_roster0 = 'https://www.espn.com/nhl/team/roster/_/name/'
        html_roster0 = requests.get(url_roster0 + team0_url)
        soup_roster0 = bs4.BeautifulSoup(html_roster0.content, features='html.parser')
        ids_roster0 = soup_roster0.find_all('a', {'class': 'AnchorLink'})
        
        url_roster1 = 'https://www.espn.com/nhl/team/roster/_/name/'
        html_roster1 = requests.get(url_roster1 + team1_url)
        soup_roster1 = bs4.BeautifulSoup(html_roster1.content, features='html.parser')
        ids_roster1 = soup_roster1.find_all('a', {'class': 'AnchorLink'})

        roster0 = []
        for elem in ids_roster0:
            if 'div' not in str(elem):
                if '/player/_/id/' in str(elem):
                    roster0.append(str(elem))
        
        roster1 = []
        for elem in ids_roster1:
            if 'div' not in str(elem):
                if '/player/_/id/' in str(elem):
                    roster1.append(str(elem))

        # for elem in roster0:
        #     print(elem)
        #     print('\n')

        team0_ids = []
        i = 0
        while True:
            if i < len(roster0):
                elem = roster0[i]
                # print(elem)
                name_index = elem.index('"0">')
                name_end_index = elem.index('</a>')
                id_index = elem.index('/id/')
                id_end_index = elem.index('" tabindex=')
                player_name = elem[name_index + 4: name_end_index]
                player_id = elem[id_index + 4: id_end_index]
                lst = [player_name, player_id]
                team0_ids.append(lst)
                i += 1
                continue
            else:
                break
        
        team1_ids = []
        i = 0
        while True:
            if i < len(roster1):
                elem = roster1[i]
                # print(elem)
                name_index = elem.index('"0">')
                name_end_index = elem.index('</a>')
                id_index = elem.index('/id/')
                id_end_index = elem.index('" tabindex=')
                player_name = elem[name_index + 4: name_end_index]
                player_id = elem[id_index + 4: id_end_index]
                lst = [player_name, player_id]
                team1_ids.append(lst)
                i += 1
                continue
            else:
                break
            
        # for elem in team0_ids:
        #     print(elem)
            
        dict_team0_ids = {x[0]:x[1:] for x in team0_ids}
        team0_ids_keys = (dict_team0_ids.keys())
        if player0 in team0_ids_keys:
            player_id = dict_team0_ids[player0]
            player_id = player_id[0]
        else:
            return('Wrong player0 name.')
        
        dict_team1_ids = {x[0]:x[1:] for x in team1_ids}
        team1_ids_keys = (dict_team1_ids.keys())
        if player1 in team1_ids_keys:
            player1_id = dict_team1_ids[player1]
            player1_id = player_id[0]
        else:
            return('Wrong player1 name.')
        
        
        
        ###
        
        # TESTING WIHT LAMELO BALL'S GAME BY GAME PAGE

        url_gbg0 = 'https://www.espn.com/nhl/player/gamelog/_/id/'
        html_gbg0 = requests.get(url_gbg0 + player_id)
        soup_gbg0 = bs4.BeautifulSoup(html_gbg0.content, features='html.parser')
        
        url_gbg1 = 'https://www.espn.com/nhl/player/gamelog/_/id/'
        html_gbg1 = requests.get(url_gbg1 + player1_id)
        soup_gbg1 = bs4.BeautifulSoup(html_gbg1.content, features='html.parser')

        new0 = []
        for elem in soup_gbg0:
            if 'Regular Season' in str(elem):
                new0.append(str(elem))
        
        new1 = []
        for elem in soup_gbg1:
            if 'Regular Season' in str(elem):
                new1.append(str(elem))
                
        statList0 = new0[0]
        # print(statList)
        game = statList0.index('"groups":[{"name":"2021-22 Regular Season","tbls":[{"name":')
        statList0 = statList0[game:]
        # print(statList)
        preseason_index0 = statList0.index('Regular Season Stats","data":[["Totals"')
        statList0 = statList0[:preseason_index0]
        x = statList0.count('}],"totals":{"stats":["')
        
        statList1 = new1[0]
        # print(statList)
        game = statList1.index('"groups":[{"name":"2021-22 Regular Season","tbls":[{"name":')
        statList1 = statList1[game:]
        # print(statList)
        preseason_index1 = statList1.index('Regular Season Stats","data":[["Totals"')
        statList1 = statList1[:preseason_index1]
        x = statList1.count('}],"totals":{"stats":["')
        
        i = 0
        print('\n')
        print('x = ' + str(x))     # ","events":[{"id":"
        print('\n')
        stat_list0 = statList0.split('"stats":[')
        while True:
            if i < x:
                if '}],"totals":{"stats":["' in statList0:
                    ind = statList0.index('}],"totals":{"stats":["')
                    ind_end = statList0.index('","events":[{"id":"')
                    statList0 = statList0[:ind] + statList0[ind_end:]
                # stat_list = statList.split('"stats":[')
                i += 1
                continue
            else:
                break
                # print(meloBall[game:game + 700])
        # for elem in stat_list:
        #     print(elem)
            # print('\n')
        i = 0
        while True:
            if i < len(stat_list0):
                if ']' in str(stat_list0[i]):
                    if '"],"label":"' in str(stat_list0[i]):
                        del stat_list0[i]
                        continue
                    ind = stat_list0[i].index(']')
                    stat_list0[i] = stat_list0[i][:ind]
                    stat_list0[i] = stat_list0[i].split(',')
                    if '.' in stat_list0[i][0]:
                        del stat_list0[i]
                        continue
                    lst = stat_list0[i]
                    a = 0
                    while True:
                        if a < len(stat_list0[i]):
                            stat_list0[i][a] = stat_list0[i][a][1:-1]
                            a += 1
                            continue
                        else:
                            break
                    i += 1
                    continue
                else:
                    del stat_list0[i]
                    continue
            else:
                break
        
        i = 0
        print('\n')
        print('x = ' + str(x))     # ","events":[{"id":"
        print('\n')
        stat_list1 = statList1.split('"stats":[')
        while True:
            if i < x:
                if '}],"totals":{"stats":["' in statList1:
                    ind = statList1.index('}],"totals":{"stats":["')
                    ind_end = statList1.index('","events":[{"id":"')
                    statList1 = statList1[:ind] + statList1[ind_end:]
                # stat_list = statList.split('"stats":[')
                i += 1
                continue
            else:
                break
                # print(meloBall[game:game + 700])
        # for elem in stat_list1:
        #     print(elem)
            # print('\n')
        i = 0
        while True:
            if i < len(stat_list1):
                if ']' in str(stat_list1[i]):
                    if '"],"label":"' in str(stat_list1[i]):
                        del stat_list1[i]
                        continue
                    ind = stat_list1[i].index(']')
                    stat_list1[i] = stat_list1[i][:ind]
                    stat_list1[i] = stat_list1[i].split(',')
                    if '.' in stat_list1[i][0]:
                        del stat_list1[i]
                        continue
                    lst = stat_list1[i]
                    a = 0
                    while True:
                        if a < len(stat_list1[i]):
                            stat_list1[i][a] = stat_list1[i][a][1:-1]
                            a += 1
                            continue
                        else:
                            break
                    i += 1
                    continue
                else:
                    del stat_list1[i]
                    continue
            else:
                break
        
        # print('\n')
        # print('should be fixed')
        # for elem in stat_list0:
        #     print(elem)
        # print('\n')
        
        player0_stats = [['goals'],
                        ['assists'],
                        ['points'],
                        ['+/-'], 
                        ['penalty minutes'], 
                        ['shots'], 
                        ['shooting percentage'], 
                        ['power play goals'],
                        ['power play assists'],
                        ['short handed goals'],
                        ['short handed assists'], 
                        ['game winning goals'],
                        ['game tying goals'],
                        ['time on ice'],
                        ['production']
                        ]
        
        player1_stats = [['goals'],
                        ['assists'],
                        ['points'],
                        ['+/-'], 
                        ['penalty minutes'], 
                        ['shots'], 
                        ['shooting percentage'], 
                        ['power play goals'],
                        ['power play assists'],
                        ['short handed goals'],
                        ['short handed assists'], 
                        ['game winning goals'],
                        ['game tying goals'],
                        ['time on ice'],
                        ['production']
                        ]
        
        print(len(player0_stats))
        i = 0
        a = 0
        while True:
            if i < len(stat_list0):
                if a < len(player0_stats):
                    # if '-' in stat_list0[i][a]:
                    #     ind = stat_list0[i][a].index('-')
                    #     stat_list0[i][a] = stat_list0[i][a][:ind]
                    if player0_stats[a][0] == 'shooting percentage':
                        stat_list0[i][a] = float(stat_list0[i][a])
                        player0_stats[a].append(stat_list0[i][a])
                        a += 1
                        continue
                    elif player0_stats[a][0] == 'time on ice' or player0_stats[a][0] == 'production':
                        stat_list0[i][a] = str(stat_list0[i][a])
                        player0_stats[a].append(stat_list0[i][a])
                        a += 1
                        continue
                    else: #if player_stats0[a][0] != 'shooting percentage' and player_stats0[a][0] != 'time on ice' and player_stats0[a][0] != 'production':
                        # print(player_stats0[a][0])
                        stat_list0[i][a] = int(stat_list0[i][a])
                        player0_stats[a].append(stat_list0[i][a])
                        a += 1
                        continue
                else:
                    a = 0
                    i += 1
                    continue
            else:
                break
        
        print(len(player1_stats))
        i = 0
        a = 0
        while True:
            if i < len(stat_list1):
                if a < len(player1_stats):
                    # if '-' in stat_list1[i][a]:
                    #     ind = stat_list1[i][a].index('-')
                    #     stat_list1[i][a] = stat_list1[i][a][:ind]
                    if player1_stats[a][0] == 'shooting percentage':
                        stat_list1[i][a] = float(stat_list1[i][a])
                        player1_stats[a].append(stat_list1[i][a])
                        a += 1
                        continue
                    elif player1_stats[a][0] == 'time on ice' or player1_stats[a][0] == 'production':
                        stat_list1[i][a] = str(stat_list1[i][a])
                        player1_stats[a].append(stat_list1[i][a])
                        a += 1
                        continue
                    else: #if player_stats1[a][0] != 'shooting percentage' and player_stats1[a][0] != 'time on ice' and player_stats1[a][0] != 'production':
                        # print(player_stats1[a][0])
                        stat_list1[i][a] = int(stat_list1[i][a])
                        player1_stats[a].append(stat_list1[i][a])
                        a += 1
                        continue
                else:
                    a = 0
                    i += 1
                    continue
            else:
                break
        
        # for elem in player0_stats:
        #     print(elem)
            
        dict_player0_stats = {x[0]:x[1:] for x in player0_stats}
        player0_stats_keys = (dict_player0_stats.keys())
        if stat0 in player0_stats_keys:
            stat0_list = dict_player0_stats[stat0]
        else:
            return('Wrong stat.')
        
        dict_player1_stats = {x[0]:x[1:] for x in player1_stats}
        player1_stats_keys = (dict_player1_stats.keys())
        if stat1 in player1_stats_keys:
            stat1_list = dict_player1_stats[stat1]
        else:
            return('Wrong stat.')
        
        # print(dict_player0_stats)
        
        for elem in dict_player0_stats:
            print(elem)
            print(dict_player0_stats[elem])
            
        for elem in dict_player1_stats:
            print(elem)
            print(dict_player1_stats[elem])
        
        # EVERYTHING GOOD BELOW HERE
        
        avg0 = statistics.mean(stat0_list)
        std0 = statistics.pstdev(stat0_list)
        avg1 = statistics.mean(stat1_list)
        std1 = statistics.pstdev(stat1_list)
        
        if bet_type == 1:
            print('\n')
            print(str(player0) + "'s average " + str(stat0) + ' = ' + str(avg0))
            print(str(player0) + "'s " + str(stat0) + ' standard deviation = ' + str(std0))
            player0_chance = scipy.stats.norm.cdf(value0, avg0, std0)
            player0_chance = round(1 - player0_chance, 6)
            player0_chance = round(player0_chance * 100, 4)
            print(str(player0) + ' has a ' + str(player0_chance) + '% chance of ' + str(value0) + '+ ' + str(stat0) + '.')
            print('\n')
            print(str(player1) + "'s average " + str(stat1) + ' = ' + str(avg1))
            print(str(player1) + "'s " + str(stat1) + ' standard deviation = ' + str(std1))
            player1_chance = scipy.stats.norm.cdf(value1, avg1, std1)
            player1_chance = round(1 - player1_chance, 6)
            player1_chance = round(player1_chance * 100, 4)
            print(str(player1) + ' has a ' + str(player1_chance) + '% chance of ' + str(value1) + '+ ' + str(stat1) + '.')
            print('\n')
            combo_chance = round((player0_chance / 100) * (player1_chance / 100) * 100, 5)
            print('There is a ' + str(combo_chance) + '% for both ' + str(player0) + ' and ' + str(player1) + ' to record '+ str(value0) + '+ ' + str(stat0) + '.')
            print('\n')
        if bet_type == 2:
            combo_avg = avg0 + avg1
            combo_std = math.sqrt(round((std0 * std0) + (std1 * std1), 6))
            combo_chance = scipy.stats.norm.cdf(value0, combo_avg, combo_std)
            combo_chance = round(1 - combo_chance, 6)
            combo_chance = round(combo_chance * 100, 4)
            str_combo_chance = str(combo_chance)
            print('\n')
            if str_combo_chance[0] != '8':
                print('There is a ' + str(combo_chance) + '% chance of ' + str(player0) + ' and ' +str(player1) + ' combining for ' + str(value0) + '+ ' + str(stat0) + '.')
            if str_combo_chance[0] == '8':
                print('There is an ' + str(combo_chance) + '% chance of ' + str(player0) + ' and ' +str(player1) + ' combining for ' + str(value0) + '+ ' + str(stat0) + '.')
            print('\n')
        return

# Current Leagues: NBA, NHL
# List teams by City Name except: Lakers = LAL, Clippers = LAC, Rangers = NYR, Islanders = NYI, Philadelphia = Philly
# Players by Full Name
# bet types: 1 = separate, 2 = combined

def threePlayers(league, team0, player0, stat0, value0, team1, player1, stat1, value1, team2, player2, stat2, value2, bet_type):
    if league == 'NBA':
        if team0 == 'Boston':
            team0_url = 'bos/boston-celtics'
        if team0 == 'Brooklyn':
            team0_url = 'bkn/brooklyn-nets'
        if team0 == 'New York':
            team0_url = 'ny/new-york-knicks'
        if team0 == 'Philly':
            team0_url = 'phi/philadelphia-76ers'
        if team0 == 'Toronto':
            team0_url = 'tor/toronto-raptors'
        if team0 == 'Golden State':
            team0_url = 'gs/golden-state-warriors'
        if team0 == 'LAC':
            team0_url = 'lac/la-clippers'
        if team0 == 'LAL':
            team0_url = 'lal/los-angeles-lakers'
        if team0 == 'Phoenix':
            team0_url = 'phx/phoenix-suns'
        if team0 == 'Sacramento':
            team0_url = 'sac/sacramento-kings'
        if team0 == 'Chicago':
            team0_url = 'chi/chicago-bulls'
        if team0 == 'Cleveland':
            team0_url = 'cle/cleveland-cavaliers'
        if team0 == 'Detroit':
            team0_url = 'det/detroit-pistons'
        if team0 == 'Indiana':
            team0_url = 'ind/indiana-pacers'
        if team0 == 'Milwaukee':
            team0_url = 'mil/milwaukee-bucks'
        if team0 == 'Atlanta':
            team0_url = 'atl/atlanta-hawks'
        if team0 == 'Charlotte':
            team0_url = 'cha/charlotte-hornets'
        if team0 == 'Miami':
            team0_url = 'mia/miami-heat'
        if team0 == 'Orlando':
            team0_url = 'orl/orlando-magic'
        if team0 == 'Washington':
            team0_url = 'wsh/washington-wizards'
        if team0 == 'Denver':
            team0_url = 'den/denver-nuggets'
        if team0 == 'Minnesota':
            team0_url = 'min/minnesota-timberwolves'
        if team0 == 'OKC':
            team0_url = 'okc/oklahoma-city-thunder'
        if team0 == 'Portland':
            team0_url = 'por/portland-trail-blazers'
        if team0 == 'Utah':
            team0_url = 'utah/utah-jazz'
        if team0 == 'Dallas':
            team0_url = 'dal/dallas-mavericks'
        if team0 == 'Houston':
            team0_url = 'hou/houston-rockets'
        if team0 == 'Memphis':
            team0_url = 'mem/memphis-grizzlies'
        if team0 == 'New Orleans':
            team0_url = 'no/new-orleans-pelicans'
        if team0 == 'San Antonio':
            team0_url = 'sa/san-antonio-spurs'
        if team1 == 'Boston':
            team1_url = 'bos/boston-celtics'
        if team1 == 'Brooklyn':
            team1_url = 'bkn/brooklyn-nets'
        if team1 == 'New York':
            team1_url = 'ny/new-york-knicks'
        if team1 == 'Philly':
            team1_url = 'phi/philadelphia-76ers'
        if team1 == 'Toronto':
            team1_url = 'tor/toronto-raptors'
        if team1 == 'Golden State':
            team1_url = 'gs/golden-state-warriors'
        if team1 == 'LAC':
            team1_url = 'lac/la-clippers'
        if team1 == 'LAL':
            team1_url = 'lal/los-angeles-lakers'
        if team1 == 'Phoenix':
            team1_url = 'phx/phoenix-suns'
        if team1 == 'Sacramento':
            team1_url = 'sac/sacramento-kings'
        if team1 == 'Chicago':
            team1_url = 'chi/chicago-bulls'
        if team1 == 'Cleveland':
            team1_url = 'cle/cleveland-cavaliers'
        if team1 == 'Detroit':
            team1_url = 'det/detroit-pistons'
        if team1 == 'Indiana':
            team1_url = 'ind/indiana-pacers'
        if team1 == 'Milwaukee':
            team1_url = 'mil/milwaukee-bucks'
        if team1 == 'Atlanta':
            team1_url = 'atl/atlanta-hawks'
        if team1 == 'Charlotte':
            team1_url = 'cha/charlotte-hornets'
        if team1 == 'Miami':
            team1_url = 'mia/miami-heat'
        if team1 == 'Orlando':
            team1_url = 'orl/orlando-magic'
        if team1 == 'Washington':
            team1_url = 'wsh/washington-wizards'
        if team1 == 'Denver':
            team1_url = 'den/denver-nuggets'
        if team1 == 'Minnesota':
            team1_url = 'min/minnesota-timberwolves'
        if team1 == 'OKC':
            team1_url = 'okc/oklahoma-city-thunder'
        if team1 == 'Portland':
            team1_url = 'por/portland-trail-blazers'
        if team1 == 'Utah':
            team1_url = 'utah/utah-jazz'
        if team1 == 'Dallas':
            team1_url = 'dal/dallas-mavericks'
        if team1 == 'Houston':
            team1_url = 'hou/houston-rockets'
        if team1 == 'Memphis':
            team1_url = 'mem/memphis-grizzlies'
        if team1 == 'New Orleans':
            team1_url = 'no/new-orleans-pelicans'
        if team1 == 'San Antonio':
            team1_url = 'sa/san-antonio-spurs'
        if team2 == 'Boston':
            team2_url = 'bos/boston-celtics'
        if team2 == 'Brooklyn':
            team2_url = 'bkn/brooklyn-nets'
        if team2 == 'New York':
            team2_url = 'ny/new-york-knicks'
        if team2 == 'Philly':
            team2_url = 'phi/philadelphia-76ers'
        if team2 == 'Toronto':
            team2_url = 'tor/toronto-raptors'
        if team2 == 'Golden State':
            team2_url = 'gs/golden-state-warriors'
        if team2 == 'LAC':
            team2_url = 'lac/la-clippers'
        if team2 == 'LAL':
            team2_url = 'lal/los-angeles-lakers'
        if team2 == 'Phoenix':
            team2_url = 'phx/phoenix-suns'
        if team2 == 'Sacramento':
            team2_url = 'sac/sacramento-kings'
        if team2 == 'Chicago':
            team2_url = 'chi/chicago-bulls'
        if team2 == 'Cleveland':
            team2_url = 'cle/cleveland-cavaliers'
        if team2 == 'Detroit':
            team2_url = 'det/detroit-pistons'
        if team2 == 'Indiana':
            team2_url = 'ind/indiana-pacers'
        if team2 == 'Milwaukee':
            team2_url = 'mil/milwaukee-bucks'
        if team2 == 'Atlanta':
            team2_url = 'atl/atlanta-hawks'
        if team2 == 'Charlotte':
            team2_url = 'cha/charlotte-hornets'
        if team2 == 'Miami':
            team2_url = 'mia/miami-heat'
        if team2 == 'Orlando':
            team2_url = 'orl/orlando-magic'
        if team2 == 'Washington':
            team2_url = 'wsh/washington-wizards'
        if team2 == 'Denver':
            team2_url = 'den/denver-nuggets'
        if team2 == 'Minnesota':
            team2_url = 'min/minnesota-timberwolves'
        if team2 == 'OKC':
            team2_url = 'okc/oklahoma-city-thunder'
        if team2 == 'Portland':
            team2_url = 'por/portland-trail-blazers'
        if team2 == 'Utah':
            team2_url = 'utah/utah-jazz'
        if team2 == 'Dallas':
            team2_url = 'dal/dallas-mavericks'
        if team2 == 'Houston':
            team2_url = 'hou/houston-rockets'
        if team2 == 'Memphis':
            team2_url = 'mem/memphis-grizzlies'
        if team2 == 'New Orleans':
            team2_url = 'no/new-orleans-pelicans'
        if team2 == 'San Antonio':
            team2_url = 'sa/san-antonio-spurs'
            
        # GET HTML SOUP CONTENT WITH BEAUTIFUL SOUP
        
        url_roster0 = 'https://www.espn.com/nba/team/roster/_/name/'
        # print(url_roster0 + team0_url)
        html_roster0 = requests.get(url_roster0 + team0_url)
        soup_roster0 = bs4.BeautifulSoup(html_roster0.content, features='html.parser')
        ids_roster0 = soup_roster0.find_all('a', {'class': 'AnchorLink'})
        
        url_roster1 = 'https://www.espn.com/nba/team/roster/_/name/'
        # print(url_roster1 + team1_url)
        html_roster1 = requests.get(url_roster1 + team1_url)
        soup_roster1 = bs4.BeautifulSoup(html_roster1.content, features='html.parser')
        ids_roster1 = soup_roster1.find_all('a', {'class': 'AnchorLink'})
        
        url_roster2 = 'https://www.espn.com/nba/team/roster/_/name/'
        # print(url_roster2 + team2_url)
        html_roster2 = requests.get(url_roster2 + team2_url)
        soup_roster2 = bs4.BeautifulSoup(html_roster2.content, features='html.parser')
        ids_roster2 = soup_roster2.find_all('a', {'class': 'AnchorLink'})

        # CREATE LIST OF PLAYER IDS FROM TEAM

        roster0 = []
        for elem in ids_roster0:
            if 'div' not in str(elem):
                if '/player/_/id/' in str(elem):
                    roster0.append(str(elem))
        # print(roster0)    

        roster1 = []
        for elem in ids_roster1:
            if 'div' not in str(elem):
                if '/player/_/id/' in str(elem):
                    roster1.append(str(elem))
        
        roster2 = []
        for elem in ids_roster2:
            if 'div' not in str(elem):
                if '/player/_/id/' in str(elem):
                    roster2.append(str(elem))

        team0_ids = []
        i = 0
        while True:
            if i < len(roster0):
                elem = roster0[i]
                name_index = elem.index('"0">')
                name_end_index = elem.index('</a>')
                id_index = elem.index('/id/')
                id_end_index = elem.index('" tabindex=')
                player0_name = elem[name_index + 4: name_end_index]
                player0_id = elem[id_index + 4: id_end_index]
                lst = [player0_name, player0_id]
                team0_ids.append(lst)
                i += 1
                continue
            else:
                break
        
        team1_ids = []
        i = 0
        while True:
            if i < len(roster1):
                elem = roster1[i]
                name_index = elem.index('"0">')
                name_end_index = elem.index('</a>')
                id_index = elem.index('/id/')
                id_end_index = elem.index('" tabindex=')
                player1_name = elem[name_index + 4: name_end_index]
                player1_id = elem[id_index + 4: id_end_index]
                lst = [player1_name, player1_id]
                team1_ids.append(lst)
                i += 1
                continue
            else:
                break
        
        team2_ids = []
        i = 0
        while True:
            if i < len(roster2):
                elem = roster2[i]
                name_index = elem.index('"0">')
                name_end_index = elem.index('</a>')
                id_index = elem.index('/id/')
                id_end_index = elem.index('" tabindex=')
                player2_name = elem[name_index + 4: name_end_index]
                player2_id = elem[id_index + 4: id_end_index]
                lst = [player2_name, player2_id]
                team2_ids.append(lst)
                i += 1
                continue
            else:
                break
            
        dict_team0_ids = {x[0]:x[1:] for x in team0_ids}
        team0_ids_keys = (dict_team0_ids.keys())
        if player0 in team0_ids_keys:
            player0_id = dict_team0_ids[player0]
            player0_id = player0_id[0]
        else:
            return('Wrong player0 name.')
        # print(dict_team0_ids)
        
        dict_team1_ids = {x[0]:x[1:] for x in team1_ids}
        team1_ids_keys = (dict_team1_ids.keys())
        # print(player1)
        if player1 in team1_ids_keys:
            player1_id = dict_team1_ids[player1]
            player1_id = player1_id[0]
        else:
            return('Wrong player1 name.')
        # print(dict_team1_ids)
        
        dict_team2_ids = {x[0]:x[1:] for x in team2_ids}
        team2_ids_keys = (dict_team2_ids.keys())
        # print(player2)
        if player2 in team2_ids_keys:
            player2_id = dict_team2_ids[player2]
            player2_id = player2_id[0]
        else:
            return('Wrong player2 name.')
        # print(dict_team2_ids)
        
        
        
        ###
        
        # TESTING WIHT LAMELO BALL'S GAME BY GAME PAGE

        url_gbg0 = 'https://www.espn.com/nba/player/gamelog/_/id/'
        html_gbg0 = requests.get(url_gbg0 + player0_id)
        soup_gbg0 = bs4.BeautifulSoup(html_gbg0.content, features='html.parser')

        url_gbg1 = 'https://www.espn.com/nba/player/gamelog/_/id/'
        html_gbg1 = requests.get(url_gbg1 + player1_id)
        soup_gbg1 = bs4.BeautifulSoup(html_gbg1.content, features='html.parser')
        
        url_gbg2 = 'https://www.espn.com/nba/player/gamelog/_/id/'
        html_gbg2 = requests.get(url_gbg2 + player2_id)
        soup_gbg2 = bs4.BeautifulSoup(html_gbg2.content, features='html.parser')

        player0_gbg = []
        for elem in soup_gbg0:
            if 'Regular Season' in str(elem):
                player0_gbg.append(str(elem))
        
        player1_gbg = []
        for elem in soup_gbg1:
            if 'Regular Season' in str(elem):
                player1_gbg.append(str(elem))
                
        player2_gbg = []
        for elem in soup_gbg2:
            if 'Regular Season' in str(elem):
                player2_gbg.append(str(elem))
        
        player0_gbg = player0_gbg[0]
        game = player0_gbg.index('"groups":[{"name":"2021-22 Regular Season","tbls":[{"name":')
        player0_gbg = player0_gbg[game:]
        preseason_index = player0_gbg.index(',["Totals","')
        player0_gbg = player0_gbg[:preseason_index]
        if '"allStar":"*"},' in player0_gbg:
            ind = player0_gbg.index('"allStar":"*"},')
            ind_end = player0_gbg.index('4th quarter untimed')
            player0_gbg = player0_gbg[:ind] + player0_gbg[ind_end:]
        player_0_gbg = player0_gbg.split('"stats":[')
        # print(player0_gbg[game:game + 700])
        
        player1_gbg = player1_gbg[0]
        game = player1_gbg.index('"groups":[{"name":"2021-22 Regular Season","tbls":[{"name":')
        player1_gbg = player1_gbg[game:]
        # print(player1_gbg)
        preseason_index = player1_gbg.index(',["Totals","')
        player1_gbg = player1_gbg[:preseason_index]
        if '"allStar":"*"},' in player1_gbg:
            ind = player1_gbg.index('"allStar":"*"},')
            ind_end = player1_gbg.index('4th quarter untimed')
            player1_gbg = player1_gbg[:ind] + player1_gbg[ind_end:]
        player_1_gbg = player1_gbg.split('"stats":[')
        
        player2_gbg = player2_gbg[0]
        game = player2_gbg.index('"groups":[{"name":"2021-22 Regular Season","tbls":[{"name":')
        player2_gbg = player2_gbg[game:]
        # print(player2_gbg)
        preseason_index = player2_gbg.index(',["Totals","')
        player2_gbg = player2_gbg[:preseason_index]
        if '"allStar":"*"},' in player2_gbg:
            ind = player2_gbg.index('"allStar":"*"},')
            ind_end = player2_gbg.index('4th quarter untimed')
            player2_gbg = player2_gbg[:ind] + player2_gbg[ind_end:]
        player_2_gbg = player2_gbg.split('"stats":[')

        i = 0
        while True:
            if i < len(player_0_gbg):
                if ']' in str(player_0_gbg[i]):
                    ind = player_0_gbg[i].index(']')
                    player_0_gbg[i] = player_0_gbg[i][:ind]
                    player_0_gbg[i] = player_0_gbg[i].split(',')
                    if '.' in player_0_gbg[i][0]:
                        del player_0_gbg[i]
                        continue
                    lst = player_0_gbg[i]
                    a = 0
                    while True:
                        if a < len(player_0_gbg[i]):
                            player_0_gbg[i][a] = player_0_gbg[i][a][1:-1]
                            a += 1
                            continue
                        else:
                            break
                    i += 1
                    continue
                else:
                    del player_0_gbg[i]
                    continue
            else:
                break
        
        i = 0
        while True:
            if i < len(player_1_gbg):
                if ']' in str(player_1_gbg[i]):
                    ind = player_1_gbg[i].index(']')
                    player_1_gbg[i] = player_1_gbg[i][:ind]
                    player_1_gbg[i] = player_1_gbg[i].split(',')
                    if '.' in player_1_gbg[i][1]:
                        del player_1_gbg[i]
                        continue
                    lst = player_1_gbg[i]
                    a = 0
                    while True:
                        if a < len(player_1_gbg[i]):
                            player_1_gbg[i][a] = player_1_gbg[i][a][1:-1]
                            a += 1
                            continue
                        else:
                            break
                    i += 1
                    continue
                else:
                    del player_1_gbg[i]
                    continue
            else:
                break
            
        i = 0
        while True:
            if i < len(player_2_gbg):
                if ']' in str(player_2_gbg[i]):
                    ind = player_2_gbg[i].index(']')
                    player_2_gbg[i] = player_2_gbg[i][:ind]
                    player_2_gbg[i] = player_2_gbg[i].split(',')
                    if '.' in player_2_gbg[i][1]:
                        del player_2_gbg[i]
                        continue
                    lst = player_2_gbg[i]
                    a = 0
                    while True:
                        if a < len(player_2_gbg[i]):
                            player_2_gbg[i][a] = player_2_gbg[i][a][1:-1]
                            a += 1
                            continue
                        else:
                            break
                    i += 1
                    continue
                else:
                    del player_2_gbg[i]
                    continue
            else:
                break
        
        
        player0_stats = [['minutes'],
                        ['field goals'],
                        ['field goal percentage'],
                        ['threes'], 
                        ['three percentage'], 
                        ['free throws'], 
                        ['free throw percentage'], 
                        ['rebounds'],
                        ['assists'],
                        ['blocks'],
                        ['steals'], 
                        ['fouls'],
                        ['turn overs'],
                        ['points']
                        ]
        
        player1_stats = [['minutes'],
                        ['field goals'],
                        ['field goal percentage'],
                        ['threes'], 
                        ['three percentage'], 
                        ['free throws'], 
                        ['free throw percentage'], 
                        ['rebounds'],
                        ['assists'],
                        ['blocks'],
                        ['steals'], 
                        ['fouls'],
                        ['turn overs'],
                        ['points']
                        ]
        
        player2_stats = [['minutes'],
                        ['field goals'],
                        ['field goal percentage'],
                        ['threes'], 
                        ['three percentage'], 
                        ['free throws'], 
                        ['free throw percentage'], 
                        ['rebounds'],
                        ['assists'],
                        ['blocks'],
                        ['steals'], 
                        ['fouls'],
                        ['turn overs'],
                        ['points']
                        ]
        
        i = 0
        a = 0
        while True:
            if i < len(player_0_gbg):
                if a < len(player0_stats):
                    if '-' in player_0_gbg[i][a]:
                        ind = player_0_gbg[i][a].index('-')
                        player_0_gbg[i][a] = player_0_gbg[i][a][:ind]
                    if player0_stats[a][0] == 'free throw percentage' or player0_stats[a][0] == 'three percentage' or player0_stats[a][0] == 'field goal percentage':
                        player_0_gbg[i][a] = float(player_0_gbg[i][a])
                        player0_stats[a].append(player_0_gbg[i][a])
                    if player0_stats[a][0] != 'free throw percentage' and player0_stats[a][0] != 'three percentage' and player0_stats[a][0] != 'field goal percentage':
                        player_0_gbg[i][a] = int(player_0_gbg[i][a])
                        player0_stats[a].append(player_0_gbg[i][a])
                    a += 1
                    continue
                else:
                    a = 0
                    i += 1
                    continue
            else:
                break
            
        i = 0
        a = 0
        while True:
            if i < len(player_1_gbg):
                if a < len(player1_stats):
                    if '-' in player_1_gbg[i][a]:
                        ind = player_1_gbg[i][a].index('-')
                        player_1_gbg[i][a] = player_1_gbg[i][a][:ind]
                    if player1_stats[a][0] == 'free throw percentage' or player1_stats[a][0] == 'three percentage' or player1_stats[a][0] == 'field goal percentage':
                        player_1_gbg[i][a] = float(player_1_gbg[i][a])
                        player1_stats[a].append(player_1_gbg[i][a])
                    if player1_stats[a][0] != 'free throw percentage' and player1_stats[a][0] != 'three percentage' and player1_stats[a][0] != 'field goal percentage':
                        player_1_gbg[i][a] = int(player_1_gbg[i][a])
                        player1_stats[a].append(player_1_gbg[i][a])
                    a += 1
                    continue
                else:
                    a = 1
                    i += 1
                    continue
            else:
                break
        
        i = 0
        a = 0
        while True:
            if i < len(player_2_gbg):
                if a < len(player_2_gbg):
                    if '-' in player_2_gbg[i][a]:
                        ind = player_2_gbg[i][a].index('-')
                        player_2_gbg[i][a] = player_2_gbg[i][a][:ind]
                    if player2_stats[a][0] == 'free throw percentage' or player2_stats[a][0] == 'three percentage' or player2_stats[a][0] == 'field goal percentage':
                        player_2_gbg[i][a] = float(player_2_gbg[i][a])
                        player2_stats[a].append(player_2_gbg[i][a])
                    if player2_stats[a][0] != 'free throw percentage' and player2_stats[a][0] != 'three percentage' and player2_stats[a][0] != 'field goal percentage':
                        player_2_gbg[i][a] = int(player_2_gbg[i][a])
                        player2_stats[a].append(player_2_gbg[i][a])
                    a += 1
                    continue
                else:
                    a = 1
                    i += 1
                    continue
            else:
                break
        
        # bet_type 1 = 'both' and bet_type 2 = 'combined'
        if bet_type == 1:
            if stat0 == stat1 and stat1 == stat2:
                # for elem in player0_stats:
                #     print(elem)
                dict_player0_stats = {x[0]:x[1:] for x in player0_stats}
                player0_stats_keys = (dict_player0_stats.keys())
                if stat0 in player0_stats_keys:
                    stat0_list = dict_player0_stats[stat0]
                # else:
                #     return('Wrong stat0.')
                dict_player1_stats = {x[0]:x[1:] for x in player1_stats}
                player1_stats_keys = (dict_player1_stats.keys())
                if stat1 in player1_stats_keys:
                    stat1_list = dict_player1_stats[stat1]
                dict_player2_stats = {x[0]:x[1:] for x in player2_stats}
                player2_stats_keys = (dict_player2_stats.keys())
                if stat2 in player2_stats_keys:
                    stat2_list = dict_player2_stats[stat2]
                # else:
                #     return('Wrong stat1.')
                avg0 = statistics.mean(stat0_list)
                std0 = statistics.pstdev(stat0_list)
                avg1 = statistics.mean(stat1_list)
                std1 = statistics.pstdev(stat1_list)
                avg2 = statistics.mean(stat2_list)
                std2 = statistics.pstdev(stat2_list)
                print('\n')
                print(str(player0) + "'s average " + str(stat0) + ' = ' + str(avg0))
                print(str(player0) + "'s " + str(stat0) + ' standard deviation = ' + str(std0))
                player0_chance = scipy.stats.norm.cdf(value0, avg0, std0)
                player0_chance = round(1 - player0_chance, 6)
                player0_chance = round(player0_chance * 100, 4)
                print(str(player0) + ' has a ' + str(player0_chance) + '% chance of ' + str(value0) + '+ ' + str(stat0) + '.')
                # print('\n')
                print(str(player1) + "'s average " + str(stat1) + ' = ' + str(avg1))
                print(str(player1) + "'s " + str(stat1) + ' standard deviation = ' + str(std1))
                player1_chance = scipy.stats.norm.cdf(value1, avg1, std1)
                player1_chance = round(1 - player1_chance, 6)
                player1_chance = round(player1_chance * 100, 4)
                print(str(player1) + ' has a ' + str(player1_chance) + '% chance of ' + str(value1) + '+ ' + str(stat1) + '.')
                # print('\n')
                print(str(player2) + "'s average " + str(stat2) + ' = ' + str(avg2))
                print(str(player2) + "'s " + str(stat2) + ' standard deviation = ' + str(std2))
                player2_chance = scipy.stats.norm.cdf(value2, avg2, std2)
                player2_chance = round(1 - player1_chance, 6)
                player2_chance = round(player2_chance * 100, 4)
                print(str(player2) + ' has a ' + str(player2_chance) + '% chance of ' + str(value2) + '+ ' + str(stat2) + '.')
                print('\n')
                combo_chance = round((player0_chance / 100) * (player1_chance / 100) * (player2_chance / 100) * 100, 5)
                print('There is a ' + str(combo_chance) + '% for ' + str(player0) + ', ' + str(player1) + ', and ' + str(player2) + ' to record '+ str(value0) + '+ ' + str(stat0) + '.')
                print('\n')
                return
            if stat0 != stat1 or stat1 != stat2:
                # for elem in player0_stats:
                #     print(elem)
                dict_player0_stats = {x[0]:x[1:] for x in player0_stats}
                player0_stats_keys = (dict_player0_stats.keys())
                if stat0 in player0_stats_keys:
                    stat0_list = dict_player0_stats[stat0]
                # else:
                #     return('Wrong stat0.')
                dict_player1_stats = {x[0]:x[1:] for x in player1_stats}
                player1_stats_keys = (dict_player1_stats.keys())
                if stat1 in player1_stats_keys:
                    stat1_list = dict_player1_stats[stat1]
                dict_player2_stats = {x[0]:x[1:] for x in player2_stats}
                player2_stats_keys = (dict_player2_stats.keys())
                if stat2 in player2_stats_keys:
                    stat2_list = dict_player2_stats[stat2]
                # else:
                #     return('Wrong stat1.')
                avg0 = statistics.mean(stat0_list)
                std0 = statistics.pstdev(stat0_list)
                avg1 = statistics.mean(stat1_list)
                std1 = statistics.pstdev(stat1_list)
                avg2 = statistics.mean(stat2_list)
                std2 = statistics.pstdev(stat2_list)
                print('\n')
                print(str(player0) + "'s average " + str(stat0) + ' = ' + str(avg0))
                print(str(player0) + "'s " + str(stat0) + ' standard deviation = ' + str(std0))
                player0_chance = scipy.stats.norm.cdf(value0, avg0, std0)
                player0_chance = round(1 - player0_chance, 6)
                player0_chance = round(player0_chance * 100, 4)
                print(str(player0) + ' has a ' + str(player0_chance) + '% chance of ' + str(value0) + '+ ' + str(stat0) + '.')
                # print('\n')
                print(str(player1) + "'s average " + str(stat1) + ' = ' + str(avg1))
                print(str(player1) + "'s " + str(stat1) + ' standard deviation = ' + str(std1))
                player1_chance = scipy.stats.norm.cdf(value1, avg1, std1)
                player1_chance = round(1 - player1_chance, 6)
                player1_chance = round(player1_chance * 100, 4)
                print(str(player1) + ' has a ' + str(player1_chance) + '% chance of ' + str(value1) + '+ ' + str(stat1) + '.')
                print(str(player2) + "'s average " + str(stat2) + ' = ' + str(avg2))
                print(str(player2) + "'s " + str(stat2) + ' standard deviation = ' + str(std2))
                player2_chance = scipy.stats.norm.cdf(value2, avg2, std2)
                player2_chance = round(1 - player2_chance, 6)
                player2_chance = round(player2_chance * 100, 4)
                print(str(player2) + ' has a ' + str(player2_chance) + '% chance of ' + str(value2) + '+ ' + str(stat2) + '.')
                print('\n')
                combo_chance = round((player0_chance / 100) * (player1_chance / 100) * 100, 5)
                print('There is a ' + str(combo_chance) + '% chance for ' + str(player0) + ' to record '+ str(value0) + '+ ' + str(stat0) + ' and ' + str(player1) + ' to record ' + str(value1) + '+ ' + str(stat1) + ' and ' + str(player2) + ' to record '+ str(value2) + '+ ' + str(stat2) + '.')
                print('\n')
                return
        # bet_type 1 = 'both' and bet_type 2 = 'combined'
        if bet_type == 2:
            if stat0 == stat1 and stat1 == stat2:
                # for elem in player0_stats:
                #     print(elem)
                dict_player0_stats = {x[0]:x[1:] for x in player0_stats}
                player0_stats_keys = (dict_player0_stats.keys())
                if stat0 in player0_stats_keys:
                    stat0_list = dict_player0_stats[stat0]
                # else:
                #     return('Wrong stat0.')
                dict_player1_stats = {x[0]:x[1:] for x in player1_stats}
                player1_stats_keys = (dict_player1_stats.keys())
                if stat1 in player1_stats_keys:
                    stat1_list = dict_player1_stats[stat0]
                dict_player2_stats = {x[0]:x[1:] for x in player2_stats}
                player2_stats_keys = (dict_player2_stats.keys())
                if stat2 in player2_stats_keys:
                    stat2_list = dict_player2_stats[stat0]
                # else:
                #     return('Wrong stat1.')
                avg0 = statistics.mean(stat0_list)
                std0 = statistics.pstdev(stat0_list)
                avg1 = statistics.mean(stat1_list)
                std1 = statistics.pstdev(stat1_list)
                avg2 = statistics.mean(stat2_list)
                std2 = statistics.pstdev(stat2_list)
                combo_avg = avg0 + avg1 + avg2
                print(combo_avg)
                combo_std = math.sqrt(round((std0 * std0) + (std1 * std1) + (std2 * std2), 6))
                print(combo_std)
                combo_chance = scipy.stats.norm.cdf(value0, combo_avg, combo_std)
                combo_chance = round(1 - combo_chance, 6)
                combo_chance = round(combo_chance * 100, 4)
                str_combo_chance = str(combo_chance)
                print('\n')
                if str_combo_chance[0] != '8':
                    print('There is a ' + str(combo_chance) + '% chance of ' + str(player0) + ' and ' +str(player1) + ' combining for ' + str(value0) + '+ ' + str(stat0) + '.')
                if str_combo_chance[0] == '8':
                    print('There is an ' + str(combo_chance) + '% chance of ' + str(player0) + ' and ' +str(player1) + ' combining for ' + str(value0) + '+ ' + str(stat0) + '.')
                print('\n')
                return
            if stat0 != stat1:
                dict_player0_stats = {x[0]:x[1:] for x in player0_stats}
                player0_stats_keys = (dict_player0_stats.keys())
                if stat0 in player0_stats_keys:
                    stat00_list = dict_player0_stats[stat0]
                dict_player1_stats = {x[0]:x[1:] for x in player1_stats}
                player1_stats_keys = (dict_player1_stats.keys())
                if stat1 in player1_stats_keys:
                    stat10_list = dict_player1_stats[stat0]
                dict_player0_stats = {x[0]:x[1:] for x in player0_stats}
                player0_stats_keys = (dict_player0_stats.keys())
                if stat0 in player0_stats_keys:
                    stat01_list = dict_player0_stats[stat1]
                dict_player1_stats = {x[0]:x[1:] for x in player1_stats}
                player1_stats_keys = (dict_player1_stats.keys())
                if stat1 in player1_stats_keys:
                    stat11_list = dict_player1_stats[stat1]
                avg00 = statistics.mean(stat00_list)
                std00 = statistics.pstdev(stat00_list)
                avg10 = statistics.mean(stat10_list)
                std10 = statistics.pstdev(stat10_list)
                avg01 = statistics.mean(stat01_list)
                std01 = statistics.pstdev(stat01_list)
                avg11 = statistics.mean(stat11_list)
                std11 = statistics.pstdev(stat11_list)
                combo_avg = avg00 + avg10 + avg01 + avg11
                combo_std = math.sqrt(round((std00 * std00) + (std10 * std10) + (std01 * std01) + (std11 * std11), 6))
                combo_chance = scipy.stats.norm.cdf(value0, combo_avg, combo_std)
                combo_chance = round(1 - combo_chance, 6)
                combo_chance = round(combo_chance * 100, 4)
                str_combo_chance = str(combo_chance)
                print('\n')
                if str_combo_chance[0] != '8':
                    print('There is a ' + str(combo_chance) + '% chance of ' + str(player0) + ' and ' +str(player1) + ' combining for ' + str(value0) + '+ ' + str(stat0) + ' and ' + str(stat1) + '.')
                if str_combo_chance[0] == '8':
                    print('There is an ' + str(combo_chance) + '% chance of ' + str(player0) + ' and ' +str(player1) + ' combining for ' + str(value0) + '+ ' + str(stat0) + ' and ' + str(stat1) + '.')
                print('\n')
                return

# Current Leagues: NBA, NHL
# List teams by City Name except: Lakers = LAL, Clippers = LAC, Rangers = NYR, Islanders = NYI, Philadelphia = Philly
# Players by Full Name
# bet types:






# onePlayer('NBA', 'Dallas', 'Luka Doncic', 'points', 24.5, 1)
# onePlayer('NHL', 'NYR', 'Chris Kreider', 'goals', 0.5, 1)
# onePlayer('NHL', 'Calgary', 'Johnny Gaudreau', 'goals', 0.5, 1)
# onePlayer('NHL', 'Edmonton', 'Connor McDavid', 'goals', 0.5, 1)


onePlayer('NBA', 'Boston', 'Jayson Tatum', 'points', 0.5, 1)
onePlayer('NBA', 'Miami', 'Jimmy Butler', 'points', 0.5, 1)












# twoPlayers('NBA', 'Golden State', "Stephen Curry", 'threes', 7.5, 'Dallas', "Luka Doncic", 'threes', 7.5, 2)
# twoPlayers('NBA', 'Phoenix', "Deandre Ayton", 'points', 9.5, 'Phoenix', "Deandre Ayton", 'assists', 9.5, 1)
# twoPlayers('NBA', 'Phoenix', "Deandre Ayton", 'rebounds', 9.5, 'Phoenix', "Deandre Ayton", 'assists', 9.5, 1)


