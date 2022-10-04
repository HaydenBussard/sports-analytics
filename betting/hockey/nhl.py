from os import pipe
from typing import Match, Text
from urllib import request
import bs4
import pandas as pd
import urllib.request
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
from selenium.webdriver.chrome.options import Options
from webdriver_auto_update import check_driver
import copy


def nhl():
    def team_rename(team):
        if 'Anaheim' in team or 'Ducks' in team or team == 'ANA' or team == 'Buffalo Bills' or team == 'Bills':
            name = 'Anaheim Ducks'
            return name
        if 'Arizona' in team or 'Coyotes' in team or team == 'ARI' or team == 'Los Angeles Rams' or team == 'Rams':
            name = 'Arizona Coyotes'
            return name
        if 'Boston' in team or 'Bruins' in team or team == 'BOS' or team == 'Dallas Cowboys' or team == 'Cowboys':
            name = 'Boston Bruins'
            return name
        if 'Buffalo' in team or 'Sabres' in team or team == 'BUF' or team == 'Atlanta Falcons' or team == 'Falcons':
            name = 'Buffalo Sabres'
            return name
        if 'Calgary' in team or 'Flames' in team or team == 'CGY' or team == 'Washington Commanders' or team == 'Commanders':
            name = 'Calgary Flames'
            return name
        if 'Carolina' in team or 'Hurricanes' in team or team == 'CAR' or team == 'Pittsburgh Steelers' or team == 'Steelers':
            name = 'Carolina Hurricanes'
            return name
        if 'Chicago' in team or 'Blackhawks' in team or team == 'CHI' or team == 'New Orleans Saints' or team == 'Saints':
            name = 'Chicago Blackhawks'
            return name
        if 'Colorado' in team or 'Avalanche' in team or team == 'COL' or team == 'Las Vegas Raiders' or team == 'Raiders':
            name = 'Colorado Avalanche'
            return name
        if 'Columbus' in team or 'Jackets' in team or team == 'CBJ' or team == 'Detroit Lions' or team == 'Lions':
            name = 'Columbus Blue Jackets'
            return name
        if 'Dallas' in team or 'Stars' in team or team == 'DAL' or team == 'Chicago Bears' or team == 'Bears':
            name = 'Dallas Stars'
            return name
        if 'Detroit' in team or 'Wings' in team or team == 'DET' or team == 'Jacksonville Jaguars' or team == 'Jaguars':
            name = 'Detroit Red Wings'
            return name
        if 'Edmonton' in team or 'Oilers' in team or team == 'EDM' or team == 'San Francisco 49ers' or team == '49ers':
            name = 'Edmonton Oilers'
            return name
        if 'Florida' in team or 'Panthers' in team or team == 'FLA' or team == 'New York Jets' or team == 'Jets':
            name = 'Florida Panthers'
            return name
        if 'Los Angeles' in team or 'Kings' in team or team == 'LA' or team == 'Miami Dolphins' or team == 'Dolphins':
            name = 'Los Angeles Kings'
            return name
        if 'Minnesota' in team or 'Wild' in team or team == 'MIN' or team == 'Tennessee Titans' or team == 'Titans':
            name = 'Minnesota Wild'
            return name
        if 'Montreal' in team or 'Canadiens' in team or team == 'MTL' or team == 'Cleveland Browns' or team == 'Browns':
            name = 'Montreal Canadiens'
            return name
        if 'Nashville' in team or 'Predators' in team or team == 'NSH' or team == 'Houston Texans' or team == 'Texans':
            name = 'Nashville Predators'
            return name
        if 'New Jersey' in team or 'Devils' in team or team == 'NJ' or team == 'Tampa Bay Buccaneers' or team == 'Buccaneers':
            name = 'New Jersey Devils'
            return name
        if 'NY Islanders' in team or 'Islanders' in team or team == 'NYI' or team == 'Arizona Cardinals' or team == 'Cardinals':
            name = 'New York Islanders'
            return name
        if 'NY Rangers' in team or 'Rangers' in team or team == 'NYR' or team == 'New England Patriots' or team == 'Patriots':
            name = 'New York Rangers'
            return name
        if 'Ottawa' in team or 'Senators' in team or team == 'OTT' or team == 'Kansas City Chiefs' or team == 'Chiefs':
            name = 'Ottawa Senators'
            return name
        if 'Philadelphia' in team or 'Flyers' in team or team == 'PHI' or team == 'Denver Broncos' or team == 'Broncos':
            name = 'Philadelphia Flyers'
            return name
        if 'Pittsburgh' in team or 'Penguins' in team or team == 'PIT' or team == 'Carolina Panthers' or team == 'Panthers':
            name = 'Pittsburgh Penguins'
            return name
        if 'San Jose' in team or 'Sharks' in team or team == 'SJ' or team == 'Los Angeles Chargers' or team == 'Chargers':
            name = 'San Jose Sharks'
            return name
        if 'Seattle' in team or 'Kraken' in team or team == 'SEA' or team == 'New York Giants' or team == 'Giants':
            name = 'Seattle Kraken'
            return name
        if 'St. Louis' in team or 'Blues' in team or team == 'STL' or team == 'Green Bay Packers' or team == 'Packers':
            name = 'St. Louis Blues'
            return name
        if 'Tampa Bay' in team or 'Lightning' in team or team == 'TB' or team == 'Cincinnati Bengals' or team == 'Bengals':
            name = 'Tampa Bay Lightning'
            return name
        if 'Toronto' in team or 'Leafs' in team or team == 'TOR' or team == 'Baltimore Ravens' or team == 'Ravens':
            name = 'Toronto Maple Leafs'
            return name
        if 'Vancouver' in team or 'Canucks' in team or team == 'VAN' or team == 'Seattle Seahawks' or team == 'Seahawks':
            name = 'Vancouver Canucks'
            return name
        if 'Vegas' in team or 'Knights' in team or team == 'VGS' or team == 'Philadelphia Eagles' or team == 'Eagles':
            name = 'Vegas Golden Knights'
            return name
        if 'Washington' in team or 'Capitals' in team or team == 'WSH' or team == 'Minnesota Vikings' or team == 'Vikings':
            name = 'Washington Capitals'
            return name
        if 'Winnipeg' in team or 'Jets' in team or team == 'WPG' or team == 'Indianapolis Colts' or team == 'Colts':
            name = 'Winnipeg Jets'
            return name
        else:
            return team

    url_yahoo_ta = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=1&sortStatId=GOALS_AGAINST_AVERAGE&cutTypeIds='
    url_yahoo_tf = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=0&sortStatId=GOALS_FOR_AVERAGE&cutTypeIds='
    url_yahoo_ha = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=1&sortStatId=GOALS_AGAINST&cutTypeIds=HOME'
    url_yahoo_hf = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=0&sortStatId=GOALS_AGAINST&cutTypeIds=HOME'
    url_yahoo_aa = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=1&sortStatId=GOALS_AGAINST&cutTypeIds=AWAY'
    url_yahoo_af = 'https://sports.yahoo.com/nhl/stats/team/?selectedTable=0&sortStatId=GOALS_AGAINST&cutTypeIds=AWAY'
    df_ta_stats = pd.DataFrame(pd.read_html(url_yahoo_ta)[0])
    df_tf_stats = pd.DataFrame(pd.read_html(url_yahoo_tf)[0])
    df_ha_stats = pd.DataFrame(pd.read_html(url_yahoo_ha)[0])
    df_hf_stats = pd.DataFrame(pd.read_html(url_yahoo_hf)[0])
    df_aa_stats = pd.DataFrame(pd.read_html(url_yahoo_aa)[0])
    df_af_stats = pd.DataFrame(pd.read_html(url_yahoo_af)[0])
    new_cols_a = ['Team', 'GAA', 'GA/G']
    new_cols_f = ['Team', 'GFA', 'GF/G']
    df_ta_stats = df_ta_stats.reindex(columns=new_cols_a)
    df_tf_stats = df_tf_stats.reindex(columns=new_cols_f)
    df_ha_stats = df_ha_stats.reindex(columns=new_cols_a)
    df_hf_stats = df_hf_stats.reindex(columns=new_cols_f)
    df_aa_stats = df_aa_stats.reindex(columns=new_cols_a)
    df_af_stats = df_af_stats.reindex(columns=new_cols_f)
    df_ta_stats = df_ta_stats.rename(
        columns={'GAA': 'GAA_t', 'GA/G': 'GA/G_t'})
    df_tf_stats = df_tf_stats.rename(
        columns={'GFA': 'GFA_t', 'GF/G': 'GF/G_t'})
    df_ha_stats = df_ha_stats.rename(
        columns={'GAA': 'GAA_h', 'GA/G': 'GA/G_h'})
    df_hf_stats = df_hf_stats.rename(
        columns={'GFA': 'GFA_h', 'GF/G': 'GF/G_h'})
    df_aa_stats = df_aa_stats.rename(
        columns={'GAA': 'GAA_a', 'GA/G': 'GA/G_a'})
    df_af_stats = df_af_stats.rename(
        columns={'GFA': 'GFA_a', 'GF/G': 'GF/G_a'})

    df_stats = pd.merge(
        df_tf_stats, df_ta_stats, on=['Team']
    )

    df_stats = pd.merge(
        df_stats, df_hf_stats, on=['Team']
    )

    df_stats = pd.merge(
        df_stats, df_ha_stats, on=['Team']
    )

    df_stats = pd.merge(
        df_stats, df_af_stats, on=['Team']
    )

    df_stats = pd.merge(
        df_stats, df_aa_stats, on=['Team']
    )

    df_stats['Team'] = df_stats.apply(
        lambda x: team_rename(x['Team']), axis=1
    )

    # print('\n')
    # print(df_stats)

    df_stats = df_stats.replace('--', 0)
    # df_stats['Team']
    # print(df_stats)
    df_stats['GAA_t'] = pd.to_numeric(df_stats['GAA_t'])
    df_stats['GAA_h'] = pd.to_numeric(df_stats['GAA_h'])
    df_stats['GAA_a'] = pd.to_numeric(df_stats['GAA_a'])
    df_stats['GA/G_t'] = pd.to_numeric(df_stats['GA/G_t'])
    df_stats['GA/G_h'] = pd.to_numeric(df_stats['GA/G_h'])
    df_stats['GA/G_a'] = pd.to_numeric(df_stats['GA/G_a'])
    nhl_avg_against_total = df_stats['GAA_t'].mean()
    nhl_avg_against_home = df_stats['GAA_h'].mean()
    nhl_avg_against_away = df_stats['GAA_a'].mean()

    html_text = urllib.request.urlopen(
        "https://sportsbook.draftkings.com/leagues/hockey/nhl"
    )
    bs_obj = BeautifulSoup(html_text)
    tables = bs_obj.findAll('table', attrs={'class': 'sportsbook-table'})
    dfs = []
    for table in tables:
        df = pd.DataFrame(pd.read_html(str(table))[0])
        # print(df)
        df.columns.values.tolist()
        col_lst = list(df.columns)
        dat_e = col_lst[0]
        df = df.rename(
            columns={dat_e: 'Team'})
        df['date'] = df.apply(lambda x: dat_e, axis=1)
        dfs.append(df)

    # print(dfs)

    df_dk = pd.concat(dfs)
    df_dk = df_dk.reset_index(drop=True)

    df_dk['Team'] = df_dk.apply(
        lambda x: team_rename(x['Team']), axis=1
    )
    df_dk = df_dk.rename(
        columns={'PUCK LINE': 'pl', 'TOTAL': 'total', 'MONEYLINE': 'ml'}
    )
    print(df_dk)

    len_dk_df = len(df_dk.index)
    opponent_lst = []
    mtch = []
    home_away = []
    i = 0
    while True:
        if i < len_dk_df:
            if i % 2 == 0:
                o = i + 1
                team = df_dk['Team'][i]
                team = team_rename(team)
                opp = df_dk['Team'][o]
                opp = team_rename(opp)
                matchup = team + ' @ ' + opp
                opponent_lst.append(opp)
                mtch.append(matchup)
                home_away.append('away')
                i += 1
                continue
            else:
                o = i - 1
                team = df_dk['Team'][i]
                team = team_rename(team)
                opp = df_dk['Team'][o]
                opp = team_rename(opp)
                matchup = opp + ' @ ' + team
                opponent_lst.append(opp)
                mtch.append(matchup)
                home_away.append('home')
                i += 1
                continue
        else:
            break

    df_dk['Matchup'] = mtch
    df_dk['Opponent'] = opponent_lst
    df_dk['H/A'] = home_away

    df = pd.merge(
        df_dk, df_stats, on=['Team']
    )

    print('MERGED DRAFTKINGS AND TEAMRANKINGS DATAFRAMES')
    print(df)
    df = df.drop_duplicates(subset=['Team'])

    df = df.reset_index(drop=True)

    print('DROPPED ALL TEAM DUPLICATES AND RESET INDICES')
    print(df)
    print('\n')
    print('LENGTH OF SHORTENED DATAFRAME')
    print(len(df))

    # df = df['TOTAL'].replace('', np.nan, inplace=True)
    # print(df)
    # df = df.dropna(subset=['TOTAL'])

    today = date.today()
    day_lst = ['Today', 'Tomorrow']
    days = 8  # ADJUST DAYS INCLUDED IN ABBREVIATED SHEET HERE
    i = 1
    while True:
        if i < days:
            day = today + timedelta(i)
            day_lst.append(str(day))
            i += 1
            continue
        else:
            break

    def date_dig_to_words(lst):
        days = ['Today', 'Tomorrow']
        th = ['10', '11', '12', '13', '14', '15', '16', '17', '18',
              '19', '20', '24', '25', '26', '27', '28', '29', '30']
        st = ['21', '31']
        i = 0
        while True:
            if i < len(lst):
                if str(lst[i]) == 'Today' or str(lst[i]) == 'Tomorrow':
                    i += 1
                    continue
                else:
                    day = str(lst[i])
                    # print(day)
                    gd = day.split('-')
                    # print(day)
                    day = gd[2]
                    # print('day = ')
                    # print(gd[2])
                    # print('month = ')
                    m = gd[1]
                    if m == '08':
                        m = 'AUG'
                    if m == '09':
                        m = 'SEP'
                    if m == '10':
                        m = 'OCT'
                    if m == '11':
                        m = 'NOV'
                    if m == '12':
                        m = 'DEC'
                    if m == '01':
                        m = 'JAN'
                    if day == '01':
                        day = '1ST'
                    if day == '02':
                        day = '2ND'
                    if day == '03':
                        day = '3RD'
                    if day == '04':
                        day = '4TH'
                    if day == '05':
                        day = '5TH'
                    if day == '06':
                        day = '6TH'
                    if day == '07':
                        day = '7TH'
                    if day == '08':
                        day = '8TH'
                    if day == '09':
                        day = '9TH'
                    if day == '22':
                        day = '22ND'
                    if day == '23':
                        day = '23RD'
                    if day in th:
                        day = str(day) + 'TH'
                    if day in st:
                        day = str(day) + 'ST'
                    game_day = str(m) + ' ' + str(day)
                    days.append(game_day)
                    i += 1
                    continue
            else:
                break
        return days
    # print('Day search list for making abbreviated list of bets:')

    # print(day_lst)

    day_lst = date_dig_to_words(day_lst)

    # print(day_lst)

    def fix_date(mtch):
        day = df.loc[df['Matchup'] == mtch, 'date'].iloc[0]
        if day == 'Today':
            return day
        elif day == 'Tomorrow':
            return day
        else:
            ind = day.index(' ') + 1
            day = day[ind:]
            return day

    df['date'] = df.apply(
        lambda x: fix_date(x['Matchup']), axis=1
    )
    # print(df)
    # df = pd.DataFrame(df)
    df = df[~df['date'].isin([day_lst])]

    print('\n')
    print('DROPPED ALL GAMES WITHIN NEXT 8 DAYS & MERGED DRAFTKINGS AND TEAM STATS:')
    print(df)

    print(df_stats)

    def opponent_against(team):
        opponent = df.loc[df['Team'] == team, 'Opponent'].iloc[0]
        # print(opponent)
        home_away = df.loc[df['Team'] == team, 'H/A'].iloc[0]
        if home_away == 'home':
            # will need to change to 'GAA_a'
            opp_against = df_stats.loc[df_stats['Team']
                                       == opponent, 'GAA_t']
            # print(opp_against)
            # print(type(opp_against))
            opp_against = float(opp_against)
            return opp_against
        else:
            # will need to change to 'GAA_h'
            opp_against = df_stats.loc[df_stats['Team']
                                       == opponent, 'GAA_t']
            # print(opp_against)
            # print(type(opp_against))
            opp_against = float(opp_against)
            return opp_against

    df['opp_against'] = df.apply(
        lambda x: opponent_against(x['Team']), axis=1
    )
    print('opponent against added to df')
    print(df)

    def opponent_for(team):
        opponent = df.loc[df['Team'] == team, 'Opponent'].iloc[0]
        home_away = df.loc[df['Team'] == team, 'H/A'].iloc[0]
        if home_away == 'home':
            # will need to change to 'GFA_a'
            opp_for = df_stats.loc[df_stats['Team'] == opponent, 'GFA_t']
            opp_for = float(opp_for)
            return opp_for
        else:
            # will need to change to 'GFA_h'
            opp_for = df_stats.loc[df_stats['Team'] == opponent, 'GFA_t']
            opp_for = float(opp_for)
            return opp_for

    df['opp_for'] = df.apply(
        lambda x: opponent_for(x['Team']), axis=1
    )

    def team_total(team):
        home_away = df.loc[df['Team'] == team, 'H/A'].iloc[0]
        if home_away == 'home':
            # will need to change to 'GFA_h'
            team_for = df.loc[df['Team'] == team, 'GFA_t'].iloc[0]
            team_for = float(team_for)
            # does not need to change
            opp_against = df.loc[df['Team'] == team, 'opp_against'].iloc[0]
            # will need to change to 'nhl_avg_against_away'
            team_pts = round((team_for * opp_against) /
                             nhl_avg_against_total, 2)
            return team_pts
        else:
            # will need to change to 'GFA_a'
            team_for = df.loc[df['Team'] == team, 'GFA_t'].iloc[0]
            team_for = float(team_for)
            # does not need to change
            opp_against = df.loc[df['Team'] == team, 'opp_against'].iloc[0]
            # will need to change to 'nhl_avg_against_home'
            team_pts = round((team_for * opp_against) /
                             nhl_avg_against_total, 2)
            return team_pts

    df['team_total'] = df.apply(
        lambda x: team_total(x['Team']), axis=1
    )

    def opponent_total(team):
        home_away = df.loc[df['Team'] == team, 'H/A'].iloc[0]
        if home_away == 'home':
            opp_for = df.loc[df['Team'] == team, 'opp_for'].iloc[0]
            opp_for = float(opp_for)
            # will need to change to 'GAA_h'
            team_against = df.loc[df['Team'] == team, 'GAA_t'].iloc[0]
            team_against = float(team_against)
            opp_pts = round(((opp_for * team_against) /
                            nhl_avg_against_total), 2)  # will need to change to 'nhl_avg_against_home'
            return opp_pts
        else:
            opp_for = df.loc[df['Team'] == team, 'opp_for'].iloc[0]
            opp_for = float(opp_for)
            # will need to change to 'GAA_a'
            team_against = df.loc[df['Team'] == team, 'GAA_t'].iloc[0]
            team_against = float(team_against)
            opp_pts = round(((opp_for * team_against) /
                            nhl_avg_against_total), 2)  # will need to change to 'nhl_avg_against_away'
            return opp_pts

    df['opp_total'] = df.apply(
        lambda x: opponent_total(x['Team']), axis=1
    )

    def game_total(team):
        team_pts = df.loc[df['Team'] == team, 'team_total'].iloc[0]
        opp_pts = df.loc[df['Team'] == team, 'opp_total'].iloc[0]
        total = round(team_pts + opp_pts, 2)
        return total

    df['game_total'] = df.apply(
        lambda x: game_total(x['Team']), axis=1
    )

    possible_points = []
    p = 0
    while True:
        if p < 10:
            possible_points.append(int(p))
            p += 1
            continue
        else:
            break

    def team_poisson(team):
        team_poisson = []
        team_total = df.loc[df['Team'] == team, 'team_total'].iloc[0]
        i = 0
        while True:
            if i < len(possible_points):
                chance_of_total_team = ((team_total**(possible_points[i])) * (
                    math.exp(-team_total)) / math.factorial(possible_points[i]))
                team_poisson.append(chance_of_total_team)
                i += 1
                continue
            else:
                break
        return team_poisson

    def opp_poisson(team):
        opp_poisson = []
        opp_total = df.loc[df['Team'] == team, 'opp_total'].iloc[0]
        i = 0
        while True:
            if i < len(possible_points):
                chance_of_total_opp = ((opp_total**(possible_points[i])) * (
                    math.exp(-opp_total)) / math.factorial(possible_points[i]))
                opp_poisson.append(chance_of_total_opp)
                i += 1
                continue
            else:
                break
        return opp_poisson

    df['team_poisson'] = df.apply(
        lambda x: team_poisson(x['Team']), axis=1
    )
    df['opponent_poisson'] = df.apply(
        lambda x: opp_poisson(x['Team']), axis=1
    )

    no_chance = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def list_chance(team):
        print('Calculating ' + str(team) + "'s chance")
        t = 0
        o = 0
        team_poisson = df.loc[df['Team'] == team, 'team_poisson'].iloc[0]
        opp_poisson = df.loc[df['Team']
                             == team, 'opponent_poisson'].iloc[0]
        if team_poisson == no_chance or opp_poisson == no_chance or sum(team_poisson) < 0 or sum(opp_poisson) < 0:
            lst = [0, 0]
            return lst
        rg = 100000
        q = np.asarray(possible_points)
        team_array = np.asarray(team_poisson)
        opp_array = np.asarray(opp_poisson)
        # print(opp_array)
        for x in range(rg):
            chance = random.choices(q, team_array)
            opp_chance = random.choices(q, opp_array)
            if chance > opp_chance:
                t += 1
            elif opp_chance > chance:
                o += 1
        # print(t)
        # print(o)
        w = round(t + o, 2)
        t = round((t / w) * 100, 2)
        o = round((o / w) * 100, 2)
        lst = [t, o]
        return lst

    df['chance_list'] = df.apply(
        lambda x: list_chance(x['Team']), axis=1
    )

    def team_chance(team):
        lst = df.loc[df['Team'] == team, 'chance_list'].iloc[0]
        chance = lst[0]
        return chance

    def opponent_chance(team):
        lst = df.loc[df['Team'] == team, 'chance_list'].iloc[0]
        chance = lst[1]
        return chance

    df['calc_%'] = df.apply(
        lambda x: team_chance(x['Team']), axis=1
    )
    df['opp_%'] = df.apply(
        lambda x: opponent_chance(x['Team']), axis=1
    )

    def calc_chance_value(team):
        chance = df.loc[df['Team'] == team, 'calc_%'].iloc[0]
        odds = df.loc[df['Team'] == team, 'ml'].iloc[0]
        if odds == '':
            return 0
        else:
            chance = float(chance)
            odds = float(odds)
            if odds > 0:
                value = round(((odds / 10) + 10) * chance / 100, 3)
                return value
            else:
                value = round(chance / 100 * (10 + 10 /
                                              ((-1 * odds) / 10) * 10), 3)
                return value

    df['calc_v'] = df.apply(
        lambda x: calc_chance_value(x['Team']), axis=1
    )

    new_cols = ['Team', 'pl', 'total', 'ml', 'date',
                'team_total', 'game_total', 'calc_%', 'calc_v']

    df = df.reindex(columns=new_cols)

    df = df.sort_values(by=['calc_v'], ascending=False)

    print('\n')
    print(df)
    print('\n')

    with pd.ExcelWriter('/Users/Hayden/OneDrive/Sports Betting/Hockey/nhl_calc_only.xlsx') as writer:  # doctest: +SKIP
        df.to_excel(writer, sheet_name='main', index=False)
        df_dk.to_excel(writer, sheet_name='draftkings', index=False)
        df_stats.to_excel(writer, sheet_name='yahoo', index=False)
        # df_nf.to_excel(writer, sheet_name='numberfire', index=False)
        # df_espn.to_excel(writer, 'ESPN', index=False)

    # # NUMBERFIRE CHANCES
    # today = date.today()
    # tomorrow = today + timedelta(1)
    # twodays = today + timedelta(2)
    # threedays = today + timedelta(3)
    # fourdays = today + timedelta(4)
    # fivedays = today + timedelta(5)
    # day_lst = [today, tomorrow, twodays, threedays, fourdays, fivedays]

    # for elem in day_lst:
    #     print(str(elem))
    # no_nf_days_count = 0

    # url_nf_cfb = "https://www.numberfire.com/nhl/games/"

    # nf_matchups = []
    # nf_predictions = []
    # x = 0
    # i = 0
    # y = i + 1
    # while True:
    #     if x < len(day_lst):
    #         url_nf = str(url_nf_cfb) + str(day_lst[x])
    #         html_nf = requests.get(url_nf)
    #         soup_nf = bs4.BeautifulSoup(
    #             html_nf.content, features='html.parser')
    #         soup_str = str(soup_nf)
    #         if 'There are no games scheduled for today.' in soup_str:
    #             no_nf_days_count += 1
    #             x += 1
    #             continue
    #         else:
    #             scrape_nf = soup_nf.findAll(
    #                 'span', attrs={'class': 'abbrev'}
    #             )
    #             for el in scrape_nf:
    #                 print(el.text)
    #             if y < len(scrape_nf):
    #                 team = scrape_nf[i].text
    #                 team = team_rename(team)
    #                 opponent = scrape_nf[y].text
    #                 opponent = team_rename(opponent)
    #                 matchup = team + ' @ ' + opponent
    #                 lst0 = [team, opponent, matchup]
    #                 lst1 = [opponent, team, matchup]
    #                 nf_matchups.append(lst0)
    #                 nf_matchups.append(lst1)
    #                 i += 2
    #                 y = i + 1
    #                 continue
    #             else:
    #                 predictions = soup_nf.findAll(
    #                     'div', attrs={'class': 'win-probability-wrap'}
    #                 )
    #                 # nf_predictions = []
    #                 for elem in predictions:
    #                     name = str(elem).strip(' ')
    #                     ind_0 = name.index(
    #                         '<h4>'
    #                     )
    #                     ind_1 = name.index(
    #                         '<span class="win-probability'
    #                     )
    #                     name = name[ind_0:ind_1]
    #                     name = name.strip('<h4>')
    #                     name = name.replace(
    #                         ' ', ''
    #                     )
    #                     name = name.replace(
    #                         '\n', ''
    #                     )
    #                     ind_chance = name.index('<')
    #                     chance = name[:ind_chance]
    #                     chance = round(float(chance), 2)
    #                     opp_chance = round(100 - chance, 2)
    #                     ind_name = name.index('</h4>') + 5
    #                     name = name[ind_name:]
    #                     name = str(name)
    #                     name = team_rename(name)
    #                     print(str(name) + ' ' + str(chance))
    #                     # print(chance)
    #                     lst = [name, chance, opp_chance]
    #                     nf_predictions.append(lst)
    #                 i = 0
    #                 y = i + 1
    #                 x += 1
    #                 continue
    #     else:
    #         break

    # # print(nf_matchups)

    # if no_nf_days_count != 6:
    #     nf_matchups_headers = ['Team', 'Opponent', 'Matchup']
    #     df_nf_matchups = pd.DataFrame(nf_matchups, columns=nf_matchups_headers)
    #     print(df_nf_matchups)
    #     nf_prediction_headers = ['Team', 'nf_%', 'opp_chance']
    #     df_nf_predictions = pd.DataFrame(
    #         nf_predictions, columns=nf_prediction_headers)
    #     print(df_nf_predictions)
    #     df1 = pd.merge(
    #         df_nf_matchups, df_nf_predictions, on=['Team']
    #     )
    #     print(df1)
    #     df2 = df1.loc[:, df1.columns.drop(['Team', 'nf_%', 'Matchup'])]
    #     df1 = df1.loc[:, df1.columns.drop(
    #         ['Opponent', 'opp_chance', 'Matchup'])]
    #     df2 = df2.rename(columns={'Opponent': 'Team',
    #                      'opp_chance': 'nf_%'})
    #     df_nf = pd.concat([df, df2])
    #     df_nf = df_nf.reset_index(drop=True)
    #     # print(df)
    #     # df_nf['Team'] = df_nf.apply(
    #     #     lambda x: team_rename(x['Team']), axis=1
    #     # )
    #     # df_nf_matchups['Team'] = df_nf_matchups.apply(
    #     #     lambda x: team_rename(x['Team']), axis=1
    #     # )
    #     df_nf = pd.merge(
    #         df_nf, df_nf_matchups, on=['Team']
    #     )
    #     # df_nf['Opponent'] = df_nf.apply(
    #     #     lambda x: team_rename(x['Opponent']), axis=1
    #     # )
    #     print('NEW NUMBERFIRE DATAFRAME: MUST VERIFY CORRECT')
    #     print(df_nf)

    # def merge_both_nf(team):
    #     df_lst = df_nf_predictions['Team'].tolist()
    #     opponent = df_nf_matchups.loc[df_nf_matchups['Team']
    #                                   == team, 'Opponent'].iloc[0]
    #     if team in df_lst:
    #         chance = df_nf_predictions.loc[df_nf_predictions['Team']
    #                                        == team, 'nf_%'].iloc[0]
    #         chance = float(chance)
    #         return chance
    #     elif opponent in df_lst:
    #         chance = df_nf_predictions.loc[df_nf_predictions['Team']
    #                                        == opponent, 'opp_chance'].iloc[0]
    #         chance = float(chance)
    #         return chance
    #     else:
    #         return 0

    # df_nf_matchups['nf_%'] = df_nf_matchups.apply(
    #     lambda x: merge_both_nf(x['Team']), axis=1
    # )
    # df_nf = df_nf_matchups
    # print('\n')
    # print('\n')
    # print(df_nf)
    # print('\n')
    # print('\n')

    # def merge_dk_and_nf(team):
    #     df_lst = df['Team'].tolist()
    #     df_lst_nf = df_nf['Team'].tolist()
    #     if team in df_lst and team in df_lst_nf:
    #         opponent_dk = df.loc[df['Team']
    #                              == team, 'Matchup'].iloc[0]
    #         opponent_nf = df_nf.loc[df_nf['Team']
    #                                 == team, 'Matchup'].iloc[0]
    #         if opponent_dk == opponent_nf:
    #             nf_chance = df_nf.loc[df_nf['Team']
    #                                   == team, 'nf_%'].iloc[0]
    #             return nf_chance
    #         else:
    #             return 0
    #     else:
    #         return 0

    # df_espn = pd.DataFrame(columns=['Team', 'Matchup', 'espn_%'])
    # url_main = 'https://www.espn.com/nhl/scoreboard'
    # html_main = requests.get(url_main)  # urlopen
    # soup_main = bs4.BeautifulSoup(html_main.content, features="html.parser")
    # scrape_main = soup_main.findAll(
    #     'div', attrs={'class': 'react-swipe-container DateCarousel__List'}
    # )
    # str_main = str(soup_main)
    # splt_main = str_main.split(
    #     '"year":2022,"url":"/nhl/scoreboard')

    # del splt_main[0]

    # week_urls = []

    # for elem in splt_main:
    #     # print(elem)
    #     ind = elem.index('","isActive":')
    #     url = elem[:ind]
    #     url = 'https://www.espn.com/nhl/scoreboard' + url
    #     if url in week_urls:
    #         continue
    #     else:
    #         week_urls.append(url)

    # for elem in week_urls:
    #     print(elem)

    # # df_espn = pd.DataFrame(columns=['Team', 'Matchup', 'espn_%'])

    # for elem in week_urls:
    #     url_main = elem
    #     html_main = requests.get(url_main)  # urlopen
    #     soup_main = bs4.BeautifulSoup(
    #         html_main.content, features="html.parser")
    #     scrape_main = soup_main.findAll(
    #         'div', attrs={'class': 'ScoreCell__Time ScoreboardScoreCell__Time h9 clr-gray-01'}
    #     )

    #     str_main = str(soup_main)

    #     # str_main = str_main.split(
    #     #     '<div class="ScoreCell__Time ScoreboardScoreCell__Time h9 clr-gray-01"></div>')
    #     str_main = str_main.split(
    #         '"link":"/nhl/game/_/gameId/'
    #     )

    #     # last_completed = str_main[-1]
    #     # ind_last_comp = last_completed.index('</section') + 8
    #     # last_completed = last_completed[ind_last_comp:]
    #     # each_game = last_completed.split(
    #     #     'Scoreboard bg-clr-white flex flex-auto justify-between" id="')
    #     each_game = str_main
    #     i = 0
    #     while True:
    #         if i < len(each_game):
    #             print('Game ID = ' + str(each_game[i])[:9])
    #             each_game[i] = each_game[i][:9]
    #             i += 1
    #             continue
    #         else:
    #             break

    #     each_game = each_game[1:]
    #     print('\n')
    #     print('Each game ID list:')
    #     print(each_game)
    #     print('\n')

    #     weeks = soup_main.findAll(
    #         'div', attrs={'class': 'custom--week'}
    #     )

    #     for elem in weeks:
    #         print(elem.text)

    #     for el in each_game:
    #         url_games = 'https://www.espn.com/nhl/game/_/gameId/' + el
    #         html_games = requests.get(url_games)  # urlopen
    #         soup_games = bs4.BeautifulSoup(
    #             html_games.content, features="html.parser")
    #         scrape_games = soup_games.findAll(
    #             'div', attrs={'class': 'chart-container'}
    #         )
    #         # for e in scrape_games:
    #         #     print(e.text)
    #         teams = soup_games.findAll(
    #             # or 'long-name' but doesnt work with multi-team cities
    #             'span', attrs={'class': 'short-name'}
    #         )
    #         teams_lg = soup_games.findAll(
    #             'span', attrs={'class': 'long-name'}
    #         )
    #         # for e in teams:
    #         #     print(e.text)
    #         home_chance = soup_games.findAll(
    #             'span', attrs={'class': 'value-home'}
    #         )
    #         # for e in home_chance:
    #         #     print(e.text)
    #         away_chance = soup_games.findAll(
    #             'span', attrs={'class': 'value-away'}
    #         )
    #         # for e in away_chance:
    #         #     print(e.text)

    #         away_team = teams[0].text
    #         away_team = team_rename(away_team)
    #         home_team = teams[1].text
    #         home_team = team_rename(home_team)
    #         away_team_lg = teams_lg[0].text
    #         home_team_lg = teams_lg[1].text
    #         if away_team_lg == 'TBD' or home_team_lg == 'TBD':
    #             continue
    #         else:
    #             home = home_chance[0].text
    #             if ':' in home:
    #                 continue
    #             else:
    #                 home = float(home[:-1])
    #                 home = np.nan_to_num(home)
    #                 away = away_chance[0].text
    #                 away = float(away[:-1])
    #                 away = np.nan_to_num(away)
    #                 matchup = away_team + ' @ ' + home_team
    #                 away_chance_lst = [away_team, matchup, float(away)]
    #                 print(away_chance_lst)
    #                 home_chance_lst = [home_team, matchup, float(home)]
    #                 print(home_chance_lst)
    #                 df_espn_game = pd.DataFrame(np.array([away_chance_lst, home_chance_lst]), columns=[
    #                     'Team', 'Matchup', 'espn_%'])
    #                 df_espn = df_espn.append(df_espn_game, ignore_index=True)

    # def merge_df_and_espn(team):
    #     df_lst = df['Team'].tolist()
    #     df_lst_espn = df_espn['Team'].tolist()
    #     if team in df_lst and team in df_lst_espn:
    #         mtch_dk = df.loc[df['Team']
    #                          == team, 'Matchup'].iloc[0]
    #         mtch_espn = df_espn.loc[df_espn['Team']
    #                                 == team, 'Matchup'].iloc[0]
    #         if mtch_dk == mtch_espn:
    #             espn_chance = df_espn.loc[df_espn['Team']
    #                                       == team, 'espn_%'].iloc[0]
    #             return espn_chance
    #         else:
    #             return 0
    #     else:
    #         return 0

    # df['nf_%'] = df.apply(
    #     lambda x: merge_dk_and_nf(x['Team']), axis=1
    # )
    # df['espn_%'] = df.apply(
    #     lambda x: merge_df_and_espn(x['Team']), axis=1
    # )

    # fte_url = 'https://projects.fivethirtyeight.com/2022-nhl-predictions/games/'
    # html_text = urllib.request.urlopen(
    #     fte_url
    # )
    # bs_fte = BeautifulSoup(html_text)
    # tables = bs_fte.findAll('table', attrs={'class': 'game-body'})
    # dfs_fte = []
    # for table in tables:
    #     df_indiv = pd.DataFrame(pd.read_html(str(table))[0])
    #     df_indiv.columns.values.tolist()
    #     col_lst = list(df_indiv.columns)
    #     dat_e = col_lst[0]
    #     df_indiv = df_indiv.rename(
    #         columns={dat_e: 'Team'})
    #     df_home = df_indiv.iloc[[1]]
    #     df_home = df_home.reset_index()
    #     df_home = df_home.rename(
    #         columns={'index': 'index_1', 'Team': 'nothing_1', 1: 'home_team',
    #                  2: 'spread_1', 3: 'home_chance', 4: 'outcome_1'}
    #     )
    #     # print('df_home')
    #     # print(df_home)
    #     df_away = df_indiv.iloc[[0]]
    #     df_away = df_away.reset_index()
    #     df_away = df_away.rename(
    #         columns={'index': 'index_0', 'Team': 'nothing_0', 1: 'away_team',
    #                  2: 'spread_0', 3: 'away_chance', 4: 'outcome_0'}
    #     )
    #     # print('df_away')
    #     # print(df_away)
    #     df_home_away = pd.concat([df_home, df_away], axis=1)
    #     # print('df_home')
    #     # print(df_home_away)
    #     df_away_home = pd.concat([df_away, df_home], axis=1)
    #     # print('df_away')
    #     # print(df_away_home)
    #     home_team = df_home_away.at[0, 'home_team']
    #     home_team = team_rename(home_team)
    #     away_team = df_away_home.at[0, 'away_team']
    #     away_team = team_rename(away_team)
    #     matchup = str(away_team) + ' @ ' + str(home_team)
    #     df_home_away['Matchup'] = matchup
    #     df_away_home['Matchup'] = matchup
    #     df_indiv = pd.concat([df_home_away, df_away_home])
    #     # print(df_indiv)
    #     df_indiv = df_indiv.drop(['index_1', 'nothing_1', 'spread_1', 'outcome_1',
    #                              'index_0', 'nothing_0', 'spread_0'], axis=1)
    #     dfs_fte.append(df_indiv)

    # df_fte = pd.concat(dfs_fte)
    # df_fte = df_fte.reset_index(drop=True)
    # df_fte = df_fte[df_fte['outcome_0'].isnull()]
    # df_fte = df_fte.drop(['outcome_0'], axis=1)
    # df_fte['home_team'] = df_fte.apply(
    #     lambda x: team_rename(x['home_team']), axis=1
    # )
    # df_fte['away_team'] = df_fte.apply(
    #     lambda x: team_rename(x['away_team']), axis=1
    # )
    # df_fte = df_fte.drop_duplicates(subset=['Matchup'])
    # new_fte_cols = ['Matchup', 'home_team',
    #                 'home_chance', 'away_team', 'away_chance']
    # df_fte = df_fte.reindex(columns=new_fte_cols)
    # # print(df_fte)
    # print('MERGING DATAFRAME AND FIVETHIRTYEIGHT')

    # def merge_df_and_fte_lst(mtch):
    #     print('Matchup = ' + str(mtch))
    #     fte_matchups = df_fte['Matchup'].tolist()
    #     df_lst_espn = df_espn['Team'].tolist()
    #     home_chance = df_fte.loc[df_fte['Matchup']
    #                              == mtch, 'home_chance'].iloc[0]
    #     away_chance = df_fte.loc[df_fte['Matchup']
    #                              == mtch, 'away_chance'].iloc[0]
    #     lst = [home_chance, away_chance]
    #     return lst
    #     # if mtch in fte_matchups:
    #     #     home_away = df.loc[df['Matchup']
    #     #                        == mtch, 'H/A'].iloc[0]
    #     #     team = df.loc[df['Matchup'] == mtch, 'Team'].iloc[0]
    #     #     opp = df.loc[df['Matchup'] == mtch, 'Opponent'].iloc[0]
    #     #     if home_away == 'home':
    #     #         home_team =
    #     #         chance = df_fte.loc[df_fte['Matchup']
    #     #                             == mtch, 'home_chance'].iloc[0]
    #     #         chance = str(chance)
    #     #         chance = chance[:-1]
    #     #         chance = float(chance)
    #     #         print(chance)
    #     #         return chance
    #     #     else:
    #     #         chance = df_fte.loc[df_fte['Matchup']
    #     #                             == mtch, 'away_chance'].iloc[0]
    #     #         print(chance)
    #     #         chance = str(chance)
    #     #         chance = chance[:-1]
    #     #         chance = float(chance)
    #     #         return chance
    #     # else:
    #     #     return 0

    # df['fte_%_lst'] = df.apply(
    #     lambda x: merge_df_and_fte_lst(x['Matchup']), axis=1
    # )

    # def fte_chance(team):
    #     home_away = df.loc[df['Team'] == team, 'H/A'].iloc[0]
    #     lst = df.loc[df['Team'] == team, 'fte_%_lst'].iloc[0]
    #     if home_away == 'home':
    #         chance = lst[0]
    #         chance = str(chance)
    #         chance = chance[:-1]
    #         chance = float(chance)
    #         return chance
    #     else:
    #         chance = lst[1]
    #         chance = str(chance)
    #         chance = chance[:-1]
    #         chance = float(chance)
    #         return chance

    # df['fte_%'] = df.apply(
    #     lambda x: fte_chance(x['Team']), axis=1
    # )

    # print(df)

    # def avg_chance(team):
    #     calc = df.loc[df['Team'] == team, 'calc_%'].iloc[0]
    #     nf = df.loc[df['Team'] == team, 'nf_%'].iloc[0]
    #     espn = df.loc[df['Team'] == team, 'espn_%'].iloc[0]
    #     fte = df.loc[df['Team'] == team, 'fte_%'].iloc[0]
    #     if nf == '' or nf == 0:
    #         if espn == '' or espn == 0:
    #             if fte == '' or fte == 0:
    #                 return 0
    #             else:
    #                 return fte
    #         else:
    #             if fte == '' or fte == 0:
    #                 return espn
    #             else:
    #                 espn = float(espn)
    #                 fte = float(fte)
    #                 avg = round((espn + fte) / 2, 3)
    #                 return avg
    #     if espn == '' or espn == 0:
    #         if nf == '' or nf == 0:
    #             if fte == '' or fte == 0:
    #                 return 0
    #             else:
    #                 return fte
    #         else:
    #             if fte == '' or fte == 0:
    #                 return nf
    #             else:
    #                 nf = float(nf)
    #                 fte = float(fte)
    #                 avg = round((nf + fte) / 2, 3)
    #                 return avg
    #     if fte == '' or fte == 0:
    #         if espn == '' or espn == 0:
    #             if nf == '' or nf == 0:
    #                 return 0
    #             else:
    #                 return nf
    #         else:
    #             if nf == '' or nf == 0:
    #                 return espn
    #             else:
    #                 espn = float(espn)
    #                 nf = float(nf)
    #                 avg = round((espn + nf) / 2, 3)
    #                 return avg
    #     else:
    #         # calc = float(calc)
    #         nf = float(nf)
    #         espn = float(espn)
    #         fte = float(fte)
    #         avg_calc_nf = round((espn + nf + fte) / 3, 2)
    #         return avg_calc_nf

    # def espn_chance_value(team):
    #     chance = df.loc[df['Team'] == team, 'espn_%'].iloc[0]
    #     odds = df.loc[df['Team'] == team, 'ml'].iloc[0]
    #     if chance == '' or odds == '':
    #         return 0
    #     else:
    #         chance = float(chance)
    #         odds = float(odds)
    #         if odds > 0:
    #             value = round(((odds / 10) + 10) * chance / 100, 3)
    #             return value
    #         else:
    #             value = round(chance / 100 * (10 + 10 /
    #                                           ((-1 * odds) / 10) * 10), 3)
    #             return value

    # def nf_chance_value(team):
    #     chance = df.loc[df['Team'] == team, 'nf_%'].iloc[0]
    #     odds = df.loc[df['Team'] == team, 'ml'].iloc[0]
    #     if chance == '' or odds == '':
    #         return 0
    #     else:
    #         chance = float(chance)
    #         odds = float(odds)
    #         if odds > 0:
    #             value = round(((odds / 10) + 10) * chance / 100, 3)
    #             return value
    #         else:
    #             value = round(chance / 100 * (10 + 10 /
    #                                           ((-1 * odds) / 10) * 10), 3)
    #             return value

    # def fte_chance_value(team):
    #     chance = df.loc[df['Team'] == team, 'fte_%'].iloc[0]
    #     odds = df.loc[df['Team'] == team, 'ml'].iloc[0]
    #     if chance == '' or odds == '':
    #         return 0
    #     else:
    #         chance = float(chance)
    #         odds = float(odds)
    #         if odds > 0:
    #             value = round(((odds / 10) + 10) * chance / 100, 3)
    #             return value
    #         else:
    #             value = round(chance / 100 * (10 + 10 /
    #                                           ((-1 * odds) / 10) * 10), 3)
    #             return value

    # def avg_chance_value(team):
    #     chance = df.loc[df['Team'] == team, 'avg_%'].iloc[0]
    #     odds = df.loc[df['Team'] == team, 'ml'].iloc[0]
    #     if chance == '' or odds == '':
    #         return 0
    #     else:
    #         chance = float(chance)
    #         odds = float(odds)
    #         if odds > 0:
    #             value = round(((odds / 10) + 10) * chance / 100, 3)
    #             return value
    #         else:
    #             value = round(chance / 100 * (10 + 10 /
    #                           ((-1 * odds) / 10) * 10), 3)
    #             return value

    # df['avg_%'] = df.apply(
    #     lambda x: avg_chance(x['Team']), axis=1
    # )

    # df['nf_v'] = df.apply(
    #     lambda x: nf_chance_value(x['Team']), axis=1
    # )
    # df['espn_v'] = df.apply(
    #     lambda x: espn_chance_value(x['Team']), axis=1
    # )
    # df['fte_v'] = df.apply(
    #     lambda x: fte_chance_value(x['Team']), axis=1
    # )
    # df['avg_v'] = df.apply(
    #     lambda x: avg_chance_value(x['Team']), axis=1
    # )

    # df = df.sort_values(by=['avg_v'], ascending=False)

    # new_cols = ['Team', 'pl', 'total', 'ml', 'date', 'team_total', 'total', 'calc_%', 'nf_%', 'espn_%', 'fte_%', 'avg_%',
    #             'calc_v', 'nf_v', 'espn_v', 'fte_v', 'avg_v']

    # df = df.reindex(columns=new_cols)

    # # df = df['TOTAL'].replace('', np.nan, inplace=True)
    # # df = df.dropna(subset=['TOTAL'], inplace=True)

    # with pd.ExcelWriter('/Users/Hayden/OneDrive/Sports Betting/Football/nhl_ugh.xlsx') as writer:  # doctest: +SKIP
    #     df.to_excel(writer, sheet_name='main', index=False)
    #     df_dk.to_excel(writer, sheet_name='draftkings', index=False)
    #     df_stats.to_excel(writer, sheet_name='teamrankings', index=False)
    #     df_nf.to_excel(writer, sheet_name='numberfire', index=False)
    #     df_espn.to_excel(writer, 'ESPN', index=False)
    #     df_fte.to_excel(writer, 'fte', index=False)

    return


nhl()
