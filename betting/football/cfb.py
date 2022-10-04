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
from selenium.webdriver.chrome.options import Options
from webdriver_auto_update import check_driver
import copy


def ncaaf():
    def team_rename(team):
        if 'Abilene Christian' in team:
            name = 'Abilene Christian'
            return name
        if 'Air Force' in team or 'AFA' == team:
            name = 'Air Force'
            return name
        if 'Akron' in team or 'AKR' == team:
            name = 'Akron'
            return name
        if 'S Alabama' in team or 'SOAL' == team or 'South Alabama' in team:
            name = 'South Alabama'
            return name
        if 'N Alabama' in team or 'NOAL' == team or 'North Alabama' in team:
            name = 'North Alabama'
            return name
        if 'Alabama A&M' in team:
            name = 'Alabama A&M'
            return name
        if 'Alabama St' in team or 'Alabama State' in team:
            name = 'Alabama State'
            return name
        if 'Alabama' in team or 'ALA' == team:
            name = 'Alabama'
            return name
        if 'Alcorn State' in team or 'ALCS' == team or 'Alcorn' in team:
            name = 'Alcorn State'
            return name
        if 'App State' in team or 'APP' == team or 'Appalachian State' in team:
            name = 'Appalachian State'
            return name
        if 'Arizona St' in team or 'AZST' == team:
            name = 'Arizona State'
            return name
        if 'Arizona' in team or 'ARIZ' == team:
            name = 'Arizona'
            return name
        if 'Arkansas St' in team or 'ARST' == team:
            name = 'Arkansas State'
            return name
        if 'Arkansas-Pine Bluff' in team or 'ARPB' == team:
            name = 'Arkansas-Pine Bluff'
            return name
        if 'Central Arkansas' in team:
            name = 'Central Arkansas'
            return name
        if 'Arkansas' in team or 'ARK' == team:
            name = 'Arkansas'
            return name
        if 'Austin Peay' in team:
            name = 'Austin Peay'
            return name
        if 'Army' in team or 'ARMY' == team:
            name = 'Army West Point'
            return name
        if 'Auburn' in team or 'AUB' == team:
            name = 'Auburn'
            return name
        if 'BYU' in team:
            name = 'BYU'
            return name
        if 'Ball State' in team or 'BALL' == team:
            name = 'Ball State'
            return name
        if 'Baylor' in team or 'BAY' == team:
            name = 'Baylor'
            return name
        if 'Boise State' in team or 'BSU' == team:
            name = 'Boise State'
            return name
        if 'Boston Col' in team or 'BC' == team:
            name = 'Boston College'
            return name
        if 'Bowling Grn' in team or 'BGSU' == team or 'Bowling Green' in team:
            name = 'Bowling Green'
            return name
        if 'Bucknell' in team or 'BUCK' == team:
            name = 'Bucknell'
            return name
        if 'Buffalo' in team or 'BUFF' == team:
            name = 'Buffalo'
            return name
        if 'California' in team or 'CAL' == team:
            name = 'California'
            return name
        if 'Campbell' in team:
            name = 'Campbell'
            return name
        if 'Central FL' in team or 'UCF' == team or 'UCF' in team:
            name = 'UCF'
            return name
        if 'Central Mich' in team or 'CMU' == team:
            name = 'Central Michigan'
            return name
        if 'Charlotte' in team or 'CHAR' == team:
            name = 'Charlotte'
            return name
        if 'Charleston Southern' in team:
            name = 'Charleston Southern'
            return name
        if 'Chattanooga' in team:
            name = 'Chattanooga'
            return name
        if 'Gardner-Webb' in team:
            name = 'Gardner-Webb'
            return name
        if 'Cincinnati' in team or 'CIN' == team:
            name = 'Cincinnati'
            return name
        if 'Clemson' in team or 'CLEM' == team:
            name = 'Clemson'
            return name
        if 'Coastal Car' in team or 'CCU' == team or 'Coastal Carolina' in team:
            name = 'Coastal Carolina'
            return name
        if 'Colorado St' in team or 'CSU' == team or 'Colorado State' in team:
            name = 'Colorado State'
            return name
        if 'Northern Colorado' in team or 'N Colorado' in team:
            name = 'Northern Colorado'
            return name
        if 'Colorado' in team or 'COLO' == team:
            name = 'Colorado'
            return name
        if 'Colgate' in team or 'COLG' == team:
            name = 'Colgate'
            return name
        if 'Connecticut' in team or 'CONN' == team or 'UConn' in team:
            name = 'UConn'
            return name
        if 'Duke' in team or 'DUKE' == team:
            name = 'Duke'
            return name
        if 'Duquesne' in team or team == 'DQNE':
            name = 'Duquesne'
            return name
        if 'E Carolina' in team or 'ECU' == team or 'East Carolina' in team:
            name = 'East Carolina'
            return name
        if 'East Tennessee State' in team:
            name = 'East Tennessee State'
            return name
        if 'Tennessee State' in team or 'Tennessee St' in team:
            name = 'Tennessee State'
            return name
        if 'Eastern Kentucky' in team or 'E Kentucky' in team or 'EKU' == team:
            name = 'Eastern Kentucky'
            return name
        if 'Eastern Washington' in team or 'E Washington' in team:
            name = 'Eastern Washington'
            return name
        if 'E Michigan' in team or 'EMU' == team or 'Eastern Michigan' in team:
            name = 'Eastern Michigan'
            return name
        if 'Fla Atlantic' in team or 'FAU' == team or 'Florida Atlantic' in team:
            name = 'Florida Atlantic'
            return name
        if 'S Florida' in team or 'USF' == team or 'South Florida' in team:
            name = 'South Florida'
            return name
        if 'Florida St' in team or 'FSU' == team or 'Florida State' in team:
            name = 'Florida State'
            return name
        if 'Florida Intl' in team or 'FIU' == team or 'FIU' in team or 'Florida International' in team:
            name = 'Florida International'
            return name
        if 'Florida' in team or 'FLA' == team:
            name = 'Florida'
            return name
        if 'Fordham' in team:
            name = 'Fordham'
            return name
        if 'Fresno St' in team or 'FRES' == team:
            name = 'Fresno State'
            return name
        if 'GA Southern' in team or 'GASO' == team or 'Georgia Southern' in team:
            name = 'Georgia Southern'
            return name
        if 'GA Tech' in team or 'GT' == team or 'Georgia Tech' in team:
            name = 'Georgia Tech'
            return name
        if 'Georgia State' in team or 'GSU' == team or 'Georgia St' in team:
            name = 'Georgia State'
            return name
        if 'Georgia' in team or 'UGA' == team:
            name = 'Georgia'
            return name
        if 'Hawaii' in team or 'HAW' == team or "Hawai'i" in team:
            name = 'Hawaii'
            return name
        if 'Holy Cross' in team:
            name = 'Holy Cross'
            return name
        if 'Idaho State' in team or 'Idaho St' in team:
            name = 'Idaho State'
            return name
        if 'Idaho' in team:
            name = 'Idaho'
            return name
        if 'Sam Houston' in team:
            name = 'Sam Houston'
            return name
        if 'Houston Baptist' in team:
            name = 'Houston Baptist'
            return name
        if 'Houston' in team or 'HOU' == team:
            name = 'Houston'
            return name
        if 'Howard' in team:
            name = 'Howard'
            return name
        if 'N Illinois' in team or 'NIU' == team or 'Northern Illinois' in team:  # NORTHERN ILLINOIS, NEEDS NF NAME
            name = 'Northern Illinois'
            return name
        if 'Southern Illinois' in team or 'S Illinois' in team or 'SIU' == team:
            name = 'Southern Illinois'
            return name
        if 'Western Illinois' in team or 'W Illinois' in team:
            name = 'Western Illinois'
            return name
        if 'Illinois' in team or 'ILL' == team:
            name = 'Illinois'
            return name
        if 'Indiana State' in team or 'IND' == team or 'Indiana St' in team:
            name = 'Indiana'
            return name
        if 'Indiana' in team or 'IND' == team:
            name = 'Indiana'
            return name
        if 'Iowa State' in team or 'ISU' == team:
            name = 'Iowa State'
            return name
        if 'Iowa' in team or 'IOWA' == team:
            name = 'Iowa'
            return name
        if 'Kansas St' in team or 'KSU' == team or 'Kansas State' in team:
            name = 'Kansas State'
            return name
        if 'Kansas' in team or 'KU' == team:
            name = 'Kansas'
            return name
        if 'Kennesaw State' in team:
            name = 'Kennesaw State'
            return name
        if 'Wofford' in team or 'WOFF' == team:
            name = 'Wofford'
            return name
        if 'Villanova' in team or 'NOVA' == team:
            name = 'Villanova'
            return name
        if 'Western Carolina' in team or 'W Carolina' in team:
            name = 'Western Carolina'
            return name
        if 'James Madison' in team or 'JMU' == team or 'JMU' in team or 'James Mad' in team:
            name = 'James Madison'
            return name
        if 'Kent State' in team or 'KENT' == team or 'Kent St' in team:
            name = 'Kent State'
            return name
        if 'W Kentucky' in team or 'WKU' == team or 'Western Kentucky' in team:
            name = 'Western Kentucky'
            return name
        if 'Kentucky' in team or 'UK' == team:
            name = 'Kentucky'
            return name
        if 'Incarnate Word' in team:
            name = 'Incarnate Word'
            return name
        if 'Lamar' in team:
            name = 'Lamar'
            return name
        if 'LIU' == team or 'Long Island' in team or 'LIU' in team:
            name = 'LIU'
            return name
        if 'SE Louisiana' in team:
            name = 'SE Louisiana'
            return name
        if 'LA Lafayette' == team or 'ULL' == team or 'Louisiana-Lafayette' == team or 'Louisiana' == team or 'Louisiana-Lafayette' in team:
            name = 'Louisiana-Lafayette'
            return name
        if 'Lafayette' in team:
            name = 'Lafayette'
            return name
        if 'LA Monroe' in team or 'ULM' == team or 'ULM' in team or 'UL Monroe' in team:
            name = 'ULM'
            return name
        if 'LA Tech' in team or 'LT' == team or 'Louisiana Tech' in team:
            name = 'Louisiana Tech'
            return name
        if 'LSU' in team:
            name = 'LSU'
            return name
        if 'Liberty' in team or 'LIB' == team:
            name = 'Liberty'
            return name
        if 'Jacksonville State' in team or 'Jacksonville St' in team:
            name = 'Jacksonville State'
            return name
        if 'Louisville' in team or 'LOU' == team:
            name = 'Louisville'
            return name
        if 'UMass' in team or 'Massachusetts' in team:
            name = 'Massachusetts'
            return name
        if 'Maine' in team:
            name = 'Maine'
            return name
        if 'Marshall' in team or 'MRSH' == team:
            name = 'Marshall'
            return name
        if 'McNeese' in team:
            name = 'McNeese'
            return name
        if 'Maryland' in team or 'MD' == team:
            name = 'Maryland'
            return name
        if 'Memphis' in team or 'MEM' == team:
            name = 'Memphis'
            return name
        if 'Miami (OH)' in team or 'M-OH' == team or 'Miami OH' in team:
            name = 'Miami OH'
            return name
        if 'Miami (FL)' in team or 'MIA' == team or 'Miami FL' in team or 'Miami' == team:
            name = 'Miami FL'
            return name
        if 'W Michigan' in team or 'WMU' == team or 'Western Michigan' in team:
            name = 'Western Michigan'
            return name
        if 'Michigan St' in team or 'MSU' == team or 'Michigan State' in team:
            name = 'Michigan State'
            return name
        if 'Michigan' in team or 'MICH' == team:
            name = 'Michigan'
            return name
        if 'Middle Tenn' in team or 'MTU' == team or 'Middle Tennessee' in team:
            name = 'Middle Tennessee'
            return name
        if 'Minnesota' in team or 'MINN' == team:
            name = 'Minnesota'
            return name
        if 'Miss State' in team or 'MSST' == team or 'Mississippi State' in team:
            name = 'Mississippi State'
            return name
        if 'S Mississippi' in team or 'USM' == team or 'Southern Mississippi' in team or 'Southern Miss' in team:
            name = 'Southern Mississippi'
            return name
        if 'Mississippi' in team or 'MISS' == team or 'Ole Miss' in team:
            name = 'Ole Miss'
            return name
        if 'Missouri' in team or 'MIZZ' == team:
            name = 'Missouri'
            return name
        if 'Missouri St' in team or 'MIZZ' == team or 'Missouri State' in team:
            name = 'Missouri State'
            return name
        if 'Montana St' in team or 'Montana St' in team:
            name = 'Montana State'
            return name
        if 'Murray State' in team or 'Murray St' in team:
            name = 'Murray State'
            return name
        if 'NC State' in team or 'NCST' == team or 'North Carolina State' in team:
            name = 'North Carolina State'
            return name
        if 'N Carolina' in team or 'UNC' == team or 'North Carolina' in team:
            name = 'North Carolina'
            return name
        if 'N Mex State' in team or 'NMSU' == team or 'New Mexico State' in team:
            name = 'New Mexico State'
            return name
        if 'Navy' in team or 'NAVY' == team:
            name = 'Navy'
            return name
        if 'Nebraska' in team or 'NEB' == team:
            name = 'Nebraska'
            return name
        if 'UT Martin' in team:
            name = 'UT Martin'
            return name
        if 'Nevada' in team or 'NEV' == team:
            name = 'Nevada'
            return name
        if 'New Hampshire' in team:
            name = 'New Hampshire'
            return name
        if 'Nicholls' in team or 'Nicholls State' in team or 'Nicholls St' in team:
            name = 'Nicholls State'
            return name
        if 'Norfolk State' in team or 'Norfolk St' in team:
            name = 'Norfolk State'
            return name
        if 'New Mexico' in team or 'UNM' == team:
            name = 'New Mexico'
            return name
        if 'North Texas' in team or 'UNT' == team:
            name = 'North Texas'
            return name
        if 'North Carolina A&T' in team:
            name = 'North Carolina A&T'
            return name
        if 'Northwestern State' in team or 'NW' == team or 'Northwestern St' in team:
            name = 'Northwestern State'
            return name
        if 'Northwestern' in team or 'NW' == team:
            name = 'Northwestern'
            return name
        if 'Notre Dame' in team or 'ND' == team:
            name = 'Notre Dame'
            return name
        if 'North Dakota State' in team or 'North Dakota St' in team:
            name = 'North Dakota State'
            return name
        if 'Ohio State' in team or 'OSU' == team:
            name = 'Ohio State'
            return name
        if 'Ohio' in team or 'OHIO' == team:
            name = 'Ohio'
            return name
        if 'Oklahoma St' in team or 'OKST' == team:
            name = 'Oklahoma State'
            return name
        if 'Oklahoma' in team or 'OKLA' == team:
            name = 'Oklahoma'
            return name
        if 'Old Dominion' in team or 'ODU' == team:
            name = 'Old Dominion'
            return name
        if 'Oregon St' in team or 'ORST' == team or 'Oregon State' in team:
            name = 'Oregon State'
            return name
        if 'Oregon' in team or 'ORE' == team:
            name = 'Oregon'
            return name
        if 'Penn State' in team or 'PSU' == team:
            name = 'Penn State'
            return name
        if 'Pittsburgh' in team or 'PITT' == team:
            name = 'Pittsburgh'
            return name
        if 'Portland State' in team or 'Portland St' in team:
            name = 'Portland State'
            return name
        if 'Purdue' in team or 'PUR' == team:
            name = 'Purdue'
            return name
        if 'Rhode Island' in team:
            name = 'Rhode Island'
            return name
        if 'Rice' in team or 'RICE' == team:
            name = 'Rice'
            return name
        if 'Rutgers' in team or 'RUTG' == team:
            name = 'Rutgers'
            return name
        if 'Robert Morris' in team or 'RMU' == team:
            name = 'Robert Morris'
            return name
        if 'Sacramento State' in team or 'Sacramento St' in team:
            name = 'Sacramento State'
            return name
        if 'South Carolina St' in team or 'SCST' == team or 'South Carolina State' in team:
            name = 'South Carolina State'
            return name
        if 'S Carolina' in team or 'SCAR' == team or 'South Carolina' in team:
            name = 'South Carolina'
            return name
        if 'S Methodist' in team or 'SMU' == team or 'SMU' in team:
            name = 'SMU'
            return name
        if 'Samford' in team:
            name = 'Samford'
            return name
        if 'San Diego St' in team or 'SDSU' == team or 'San Diego State' in team:
            name = 'San Diego State'
            return name
        if 'San Jose St' in team or 'SJSU' == team or 'San José State' in team or 'San Jose State' in team or 'San José St' in team:
            name = 'San Jose State'
            return name
        if 'Stanford' in team or 'STAN' == team:
            name = 'Stanford'
            return name
        if 'Syracuse' in team or 'SYR' == team:
            name = 'Syracuse'
            return name
        if 'Stephen F. Austin' in team or 'SFA' == team:
            name = 'Stephen F. Austin'
            return name
        if 'Stony Brook' in team:
            name = 'Stony Brook'
            return name
        if 'Tarleton' in team:
            name = 'Tarleton'
            return name
        if 'TX Christian' in team or 'TCU' == team or 'TCU' in team:
            name = 'TCU'
            return name
        if 'TX El Paso' in team or 'UTEP' == team or 'UTEP' in team:
            name = 'UTEP'
            return name
        if 'TX-San Ant' in team or 'UTSA' == team or 'UTSA' in team:
            name = 'UTSA'
            return name
        if 'Temple' in team or 'TEM' == team:
            name = 'Temple'
            return name
        if 'Tennessee' in team or 'TENN' == team:
            name = 'Tennessee'
            return name
        if 'Texas A&M' in team or 'TA&M' == team:
            name = 'Texas A&M'
            return name
        if 'Texas State' in team or 'TXST' == team or 'Texas St' in team:
            name = 'Texas State'
            return name
        if 'Texas Tech' in team or 'TTU' == team:
            name = 'Texas Tech'
            return name
        if 'Texas Southern' in team:
            name = 'Texas Southern'
            return name
        if 'Texas' in team or 'TEX' == team:
            name = 'Texas'
            return name
        if 'The Citadel' in team or 'Citadel' in team:
            name = 'The Citadel'
            return name
        if 'Toledo' in team or 'TOL' == team:
            name = 'Toledo'
            return name
        if 'Towson' in team:
            name = 'Towson'
            return name
        if 'Troy' in team or 'TROY' == team:
            name = 'Troy'
            return name
        if 'Tulane' in team or 'TULN' == team:
            name = 'Tulane'
            return name
        if 'Tulsa' in team or 'TLSA' == team:
            name = 'Tulsa'
            return name
        if 'U Mass' in team or 'MASS' == team or 'Massachusetts' in team:
            name = 'Massachusetts'
            return name
        if 'UAB' in team:
            name = 'UAB'
            return name
        if 'UCLA' in team:
            name = 'UCLA'
            return name
        if 'UNLV' in team:
            name = 'UNLV'
            return name
        if 'USC' in team:
            name = 'USC'
            return name
        if 'Southern Utah' in team or 'S Utah' in team:
            name = 'Southern Utah'
            return name
        if 'Utah Tech' in team:
            name = 'Utah Tech'
            return name
        if 'Utah State' in team or 'USU' == team or 'Utah St' in team:
            name = 'Utah State'
            return name
        if 'Utah' in team or 'UTAH' == team:
            name = 'Utah'
            return name
        if 'VA Tech' in team or 'VT' == team or 'Virginia Tech' in team:
            name = 'Virginia Tech'
            return name
        if 'Vanderbilt' in team or 'VAN' == team:
            name = 'Vanderbilt'
            return name
        if 'W Virginia' in team or 'WVU' == team or 'West Virginia' in team:
            name = 'West Virginia'
            return name
        if 'Virginia' in team or 'UVA' == team:
            name = 'Virginia'
            return name
        if 'Weber State' in team or 'Weber St' in team:
            name = 'Weber State'
            return name
        if 'Wake Forest' in team or 'WAKE' == team:
            name = 'Wake Forest'
            return name
        if 'Wagner' in team:
            name = 'Wagner'
            return name
        if 'Wash State' in team or 'WSU' == team or 'Washington State' in team:
            name = 'Washington State'
            return name
        if 'Washington' in team or 'WASH' == team:
            name = 'Washington'
            return name
        if 'Wisconsin' in team or 'WIS' == team:
            name = 'Wisconsin'
            return name
        if 'Wyoming' in team or 'WYO' == team:
            name = 'Wyoming'
            return name
        if 'Saint Francis PA' in team or 'SFPA' == team:
            name = 'Saint Francis PA'
            return name
        if 'Southern' in team:
            name = 'Southern'
            return name
        if 'Youngstown State' in team or 'Youngstown St' in team:
            name = 'Youngstown State'
            return name
        else:
            return team

    # teamrankings.com stats
    url_tr_pfa = 'https://www.teamrankings.com/college-football/stat/points-per-game'
    url_tr_paa = 'https://www.teamrankings.com/college-football/stat/opponent-points-per-game'
    df_f_stats = pd.DataFrame(pd.read_html(url_tr_pfa)[0])

    df_f_stats = df_f_stats.drop(df_f_stats.columns[[0, 3, 4]], axis=1)

    df_a_stats = pd.DataFrame(pd.read_html(url_tr_paa)[0])
    df_a_stats = df_a_stats.drop(df_a_stats.columns[[0, 3, 4]], axis=1)

    df_f_stats = df_f_stats.rename(
        columns={'2022': '2022_for', 'Home': 'home_for', 'Away': 'away_for', '2021': '2021_for'})
    df_a_stats = df_a_stats.rename(
        columns={'2022': '2022_against', 'Home': 'home_against', 'Away': 'away_against', '2021': '2021_against'})

    df_stats = pd.merge(
        df_f_stats, df_a_stats, on=['Team']
    )
    df_stats['Team'] = df_stats.apply(
        lambda x: team_rename(x['Team']), axis=1
    )
    df_stats = df_stats.replace('--', 0)
    df_stats['Team']
    print(df_stats)
    df_stats['2021_against'] = pd.to_numeric(df_stats['2021_against'])
    df_stats['home_against'] = pd.to_numeric(df_stats['home_against'])
    df_stats['away_against'] = pd.to_numeric(df_stats['away_against'])
    cfb_avg_against_2021 = df_stats['2021_against'].mean()
    cfb_avg_against_home = df_stats['home_against'].mean()
    cfb_avg_against_away = df_stats['away_against'].mean()

    url_dk = 'https://sportsbook.draftkings.com/leagues/football/ncaaf'
    df_dk = pd.DataFrame(pd.read_html(url_dk)[0])

    html_dk = requests.get(url_dk)  # urlopen
    soup_dk = bs4.BeautifulSoup(html_dk.content, features="html.parser")

    soup_dk = str(soup_dk)

    table_count = soup_dk.count(
        '<div class="parlay-card-10-a">')

    print(table_count)

    df_lst = []  # pd.read_html(url_dk)[:table_count]
    i = 0
    while True:
        if i < table_count:
            dk = pd.DataFrame(pd.read_html(url_dk)[i])
            col_lst = list(dk.columns)
            dat_e = col_lst[0]
            dk['date'] = dk.apply(lambda x: dat_e, axis=1)
            dk = dk.rename(columns={dat_e: 'Team'})
            df_lst.append(dk)
            i += 1
            continue
        else:
            break

    df_dk = pd.concat(df_lst)
    df_dk = df_dk.reset_index(drop=True)

    len_dk_df = len(df_dk.index)
    # print(df_dk.index)

    df_dk['Team'] = df_dk.apply(
        lambda x: team_rename(x['Team']), axis=1
    )

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

    dk_cols = list(df_dk.columns.values)
    pop_lst = []
    i = 0
    while True:
        if i < len(dk_cols):
            if 'Unnamed' in dk_cols[i]:
                pop_lst.append(i)
                i += 1
                continue
            else:
                i += 1
                continue
        else:
            break

    if len(pop_lst) != 0:
        df_dk = df_dk.drop(df_dk.columns[pop_lst], axis=1)

    # df_dk['Opponent'] = df_dk.apply(
    #     lambda x: team_rename(x['Opponent']), axis=1
    # )

    # NUMBERFIRE CHANCES
    today = date.today()
    tomorrow = today + timedelta(1)
    twodays = today + timedelta(2)
    threedays = today + timedelta(3)
    fourdays = today + timedelta(4)
    fivedays = today + timedelta(5)
    day_lst = [today, tomorrow, twodays, threedays, fourdays, fivedays]

    for elem in day_lst:
        print(str(elem))
    no_nf_days_count = 0

    url_nf_cfb = "https://www.numberfire.com/ncaaf/games/"

    nf_matchups = []
    nf_predictions = []
    x = 0
    i = 0
    y = i + 1
    while True:
        if x < len(day_lst):
            url_nf = str(url_nf_cfb) + str(day_lst[x])
            html_nf = requests.get(url_nf)
            soup_nf = bs4.BeautifulSoup(
                html_nf.content, features='html.parser')
            soup_str = str(soup_nf)
            if 'There are no games scheduled for today.' in soup_str:
                no_nf_days_count += 1
                x += 1
                continue
            else:
                scrape_nf = soup_nf.findAll(
                    'span', attrs={'class': 'abbrev'}
                )
                for el in scrape_nf:
                    print(el.text)
                if y < len(scrape_nf):
                    team = scrape_nf[i].text
                    team = team_rename(team)
                    opponent = scrape_nf[y].text
                    opponent = team_rename(opponent)
                    matchup = team + ' @ ' + opponent
                    lst0 = [team, opponent, matchup]
                    lst1 = [opponent, team, matchup]
                    nf_matchups.append(lst0)
                    nf_matchups.append(lst1)
                    i += 2
                    y = i + 1
                    continue
                else:
                    predictions = soup_nf.findAll(
                        'div', attrs={'class': 'win-probability-wrap'}
                    )
                    # nf_predictions = []
                    for elem in predictions:
                        name = str(elem).strip(' ')
                        ind_0 = name.index(
                            '<h4>'
                        )
                        ind_1 = name.index(
                            '<span class="win-probability'
                        )
                        name = name[ind_0:ind_1]
                        name = name.strip('<h4>')
                        name = name.replace(
                            ' ', ''
                        )
                        name = name.replace(
                            '\n', ''
                        )
                        ind_chance = name.index('<')
                        chance = name[:ind_chance]
                        chance = round(float(chance), 2)
                        opp_chance = round(100 - chance, 2)
                        ind_name = name.index('</h4>') + 5
                        name = name[ind_name:]
                        name = str(name)
                        name = team_rename(name)
                        print(str(name) + ' ' + str(chance))
                        # print(chance)
                        lst = [name, chance, opp_chance]
                        nf_predictions.append(lst)
                    i = 0
                    y = i + 1
                    x += 1
                    continue
        else:
            break

    # print(nf_matchups)

    if no_nf_days_count != 6:
        nf_matchups_headers = ['Team', 'Opponent', 'Matchup']
        df_nf_matchups = pd.DataFrame(nf_matchups, columns=nf_matchups_headers)
        print(df_nf_matchups)
        nf_prediction_headers = ['Team', 'nf_%', 'opp_chance']
        df_nf_predictions = pd.DataFrame(
            nf_predictions, columns=nf_prediction_headers)
        print(df_nf_predictions)
        df = pd.merge(
            df_nf_matchups, df_nf_predictions, on=['Team']
        )
        print(df)
        df2 = df.loc[:, df.columns.drop(['Team', 'nf_%', 'Matchup'])]
        df = df.loc[:, df.columns.drop(['Opponent', 'opp_chance', 'Matchup'])]
        df2 = df2.rename(columns={'Opponent': 'Team',
                         'opp_chance': 'nf_%'})
        df_nf = pd.concat([df, df2])
        df_nf = df_nf.reset_index(drop=True)
        # print(df)
        # df_nf['Team'] = df_nf.apply(
        #     lambda x: team_rename(x['Team']), axis=1
        # )
        # df_nf_matchups['Team'] = df_nf_matchups.apply(
        #     lambda x: team_rename(x['Team']), axis=1
        # )
        df_nf = pd.merge(
            df_nf, df_nf_matchups, on=['Team']
        )
        # df_nf['Opponent'] = df_nf.apply(
        #     lambda x: team_rename(x['Opponent']), axis=1
        # )
        print('NEW NUMBERFIRE DATAFRAME: MUST VERIFY CORRECT')
        print(df_nf)

    def merge_both_nf(team):
        df_lst = df_nf_predictions['Team'].tolist()
        opponent = df_nf_matchups.loc[df_nf_matchups['Team']
                                      == team, 'Opponent'].iloc[0]
        if team in df_lst:
            chance = df_nf_predictions.loc[df_nf_predictions['Team']
                                           == team, 'nf_%'].iloc[0]
            chance = float(chance)
            return chance
        elif opponent in df_lst:
            chance = df_nf_predictions.loc[df_nf_predictions['Team']
                                           == opponent, 'opp_chance'].iloc[0]
            chance = float(chance)
            return chance
        else:
            return 0

    df_nf_matchups['nf_%'] = df_nf_matchups.apply(
        lambda x: merge_both_nf(x['Team']), axis=1
    )
    df_nf = df_nf_matchups
    print('\n')
    print('\n')
    print(df_nf)
    print('\n')
    print('\n')

    def merge_dk_and_nf(team):
        df_lst = df['Team'].tolist()
        df_lst_nf = df_nf['Team'].tolist()
        if team in df_lst and team in df_lst_nf:
            opponent_dk = df.loc[df['Team']
                                 == team, 'Matchup'].iloc[0]
            opponent_nf = df_nf.loc[df_nf['Team']
                                    == team, 'Matchup'].iloc[0]
            if opponent_dk == opponent_nf:
                nf_chance = df_nf.loc[df_nf['Team']
                                      == team, 'nf_%'].iloc[0]
                return nf_chance
            else:
                return 0
        else:
            return 0

    # df_dk['nf_%'] = df_dk.apply(
    #     lambda x: merge_dk_and_nf(x['Team']), axis=1                                               ########### where NF chance was
    # )

    print(df_dk)

    df_dk = df_dk.drop_duplicates(subset=['Team'])

    df = pd.merge(
        df_dk, df_stats, on=['Team'], how='left'
    )
    print(
        'NEW DATAFRAME: ADDED NF CHANCES VIA NEW MATCHUP COLUMN'
    )
    print(df)

    df.to_excel(
        '/Users/Hayden/OneDrive/Sports Betting/Football/ignore/cfb_keepunmatchedrows.xlsx', index=False, sheet_name='penis'
    )

    # return

    def team_total(team):
        print('team = ' + str(team))
        home_away = df.loc[df['Team'] == team, 'H/A'].iloc[0]
        opponent = df.loc[df['Team'] == team, 'Opponent'].iloc[0]
        opp_stat_lst = df_stats['Team'].tolist()
        team_stat_lst = df_stats['Team'].tolist()
        print('opponent = ' + str(opponent))
        if team not in team_stat_lst or opponent not in opp_stat_lst:
            return 0
        elif home_away == 'home':
            # = df.loc[df['Team'] == team, 'home_for'].iloc[0]
            team_pts_for = df.loc[df['Team'] == team, '2021_for'].iloc[0]
            # = df.loc[df['Team'] == opponent, 'away_against'].iloc[0] | cfb_avg_against_away
            opponent_pts_against = df_stats.loc[df_stats['Team']
                                                == opponent, '2021_against'].iloc[0]
            total = round(float(
                team_pts_for) * float(opponent_pts_against) / float(cfb_avg_against_2021), 3)
            return total
        else:
            # = df.loc[df['Team'] == team, 'away_for'].iloc[0]
            team_pts_for = df.loc[df['Team'] == team, '2021_for'].iloc[0]
            # = df.loc[df['Team'] == opponent, 'home_against'].iloc[0] | cfb_avg_against_home
            opponent_pts_against = df_stats.loc[df_stats['Team']
                                                == opponent, '2021_against'].iloc[0]
            total = round(float(
                team_pts_for) * float(opponent_pts_against) / float(cfb_avg_against_2021), 3
            )
            return total

    def opponent_total(team):
        # print('\n')
        home_away = df.loc[df['Team'] == team, 'H/A'].iloc[0]
        opponent = df.loc[df['Team'] == team, 'Opponent'].iloc[0]
        opp_stat_lst = df_stats['Team'].tolist()
        team_stat_lst = df_stats['Team'].tolist()
        # print('opponent = ' + str(opponent))
        if team not in team_stat_lst or opponent not in opp_stat_lst:
            return 0
        if home_away == 'home':
            # = df.loc[df['Team'] == opponent, 'away_for'].iloc[0]
            opponent_pts_for = df.loc[df['Team']
                                      == opponent, '2021_for'].iloc[0]
            # = df.loc[df['Team'] == team, 'home_against'].iloc[0] | cfb_avg_against_home
            team_pts_against = df.loc[df['Team']
                                      == team, '2021_against'].iloc[0]
            opponent_total = round(float(
                opponent_pts_for) * float(team_pts_against) / float(cfb_avg_against_2021), 3)
            return opponent_total
        else:
            # = df.loc[df['Team'] == opponent, 'home_for'].iloc[0]
            opponent_pts_for = df.loc[df['Team']
                                      == opponent, '2021_for'].iloc[0]
            # = df.loc[df['Team'] == team, 'away_against'].iloc[0] | cfb_avg_against_away
            team_pts_against = df.loc[df['Team']
                                      == team, '2021_against'].iloc[0]
            opponent_total = round(float(
                opponent_pts_for) * float(team_pts_against) / float(cfb_avg_against_2021), 3)
            return opponent_total

    df['team_total'] = df.apply(
        lambda x: team_total(x['Team']), axis=1
    )
    # df_dk['nf_%'] = df_dk.apply(
    #     lambda x: merge_dk_and_nf(x['Team']), axis=1
    # )
    df['nf_%'] = df.apply(
        lambda x: merge_dk_and_nf(x['Team']), axis=1
    )
    df['opponent_total'] = df.apply(
        lambda x: opponent_total(x['Team']), axis=1
    )
    possible_points = []
    p = 0
    while True:
        if p < 100:
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
        opponent = df.loc[df['Team'] == team, 'Opponent'].iloc[0]
        opp_poisson = []
        opp_total = df.loc[df['Team'] == team, 'opponent_total'].iloc[0]
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

    no_chance = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0]

    def list_chance(team):
        t = 0
        o = 0
        team_poisson = df.loc[df['Team'] == team, 'team_poisson'].iloc[0]
        # print(team_poisson)
        opp_poisson = df.loc[df['Team']
                             == team, 'opponent_poisson'].iloc[0]
        # print(opp_poisson)
        if team_poisson == no_chance or opp_poisson == no_chance:
            lst = [0, 0]
            return lst
        rg = 100000
        q = np.asarray(possible_points)
        print(possible_points)
        team_array = np.asarray(team_poisson)
        print(team_array)
        opp_array = np.asarray(opp_poisson)
        print(opp_array)
        for x in range(rg):
            chance = random.choices(q, team_array)
            opp_chance = random.choices(q, opp_array)
            if chance > opp_chance:
                t += 1
            elif opp_chance > chance:
                o += 1
        print(t)
        print(o)
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
    df['opp_calc_%'] = df.apply(
        lambda x: opponent_chance(x['Team']), axis=1
    )

    df_espn = pd.DataFrame(columns=['Team', 'Matchup', 'espn_%'])
    url_main = 'https://www.espn.com/college-football/scoreboard/_/group/80'
    html_main = requests.get(url_main)  # urlopen
    soup_main = bs4.BeautifulSoup(html_main.content, features="html.parser")
    scrape_main = soup_main.findAll(
        'div', attrs={'class': 'react-swipe-container DateCarousel__List'}
    )
    str_main = str(soup_main)
    splt_main = str_main.split(
        '"year":2022,"url":"/college-football/scoreboard')

    del splt_main[0]

    week_urls = []

    for elem in splt_main:
        # print(elem)
        ind = elem.index('","isActive":')
        url = elem[:ind]
        url = 'https://www.espn.com/college-football/scoreboard' + url
        if url in week_urls:
            continue
        else:
            week_urls.append(url)

    for elem in week_urls:
        print(elem)

    # df_espn = pd.DataFrame(columns=['Team', 'Matchup', 'espn_%'])

    for elem in week_urls:
        url_main = elem
        html_main = requests.get(url_main)  # urlopen
        soup_main = bs4.BeautifulSoup(
            html_main.content, features="html.parser")
        scrape_main = soup_main.findAll(
            'div', attrs={'class': 'ScoreCell__Time ScoreboardScoreCell__Time h9 clr-gray-01'}
        )

        str_main = str(soup_main)

        # str_main = str_main.split(
        #     '<div class="ScoreCell__Time ScoreboardScoreCell__Time h9 clr-gray-01"></div>')
        str_main = str_main.split(
            '"link":"/college-football/game/_/gameId/'
        )

        # last_completed = str_main[-1]
        # ind_last_comp = last_completed.index('</section') + 8
        # last_completed = last_completed[ind_last_comp:]
        # each_game = last_completed.split(
        #     'Scoreboard bg-clr-white flex flex-auto justify-between" id="')
        each_game = str_main
        i = 0
        while True:
            if i < len(each_game):
                print('Game ID = ' + str(each_game[i])[:9])
                each_game[i] = each_game[i][:9]
                i += 1
                continue
            else:
                break

        each_game = each_game[1:]
        print('\n')
        print('Each game ID list:')
        print(each_game)
        print('\n')

        weeks = soup_main.findAll(
            'div', attrs={'class': 'custom--week'}
        )

        for elem in weeks:
            print(elem.text)

        for el in each_game:
            url_games = 'https://www.espn.com/college-football/game/_/gameId/' + el
            html_games = requests.get(url_games)  # urlopen
            soup_games = bs4.BeautifulSoup(
                html_games.content, features="html.parser")
            scrape_games = soup_games.findAll(
                'div', attrs={'class': 'chart-container'}
            )
            # for e in scrape_games:
            #     print(e.text)
            teams = soup_games.findAll(
                'span', attrs={'class': 'long-name'}
            )
            # for e in teams:
            #     print(e.text)
            home_chance = soup_games.findAll(
                'span', attrs={'class': 'value-home'}
            )
            # for e in home_chance:
            #     print(e.text)
            away_chance = soup_games.findAll(
                'span', attrs={'class': 'value-away'}
            )
            # for e in away_chance:
            #     print(e.text)

            away_team = teams[0].text
            away_team = team_rename(away_team)
            home_team = teams[1].text
            home_team = team_rename(home_team)
            if away_team == 'TBD' or home_team == 'TBD':
                continue
            else:
                home = home_chance[0].text
                if ':' in home:
                    continue
                else:
                    home = float(home[:-1])
                    home = np.nan_to_num(home)
                    away = away_chance[0].text
                    away = float(away[:-1])
                    away = np.nan_to_num(away)
                    matchup = away_team + ' @ ' + home_team
                    away_chance_lst = [away_team, matchup, float(away)]
                    print(away_chance_lst)
                    home_chance_lst = [home_team, matchup, float(home)]
                    print(home_chance_lst)
                    df_espn_game = pd.DataFrame(np.array([away_chance_lst, home_chance_lst]), columns=[
                        'Team', 'Matchup', 'espn_%'])
                    df_espn = df_espn.append(df_espn_game, ignore_index=True)

    def merge_df_and_espn(team):
        df_lst = df_espn['Team'].tolist()
        if team in df_lst:
            matchup_df = df.loc[df['Team']
                                == team, 'Matchup'].iloc[0]
            matchup_espn = df_espn.loc[df_espn['Team']
                                       == team, 'Matchup'].iloc[0]
            if matchup_df == matchup_espn:
                espn_chance = df_espn.loc[df_espn['Team']
                                          == team, 'espn_%'].iloc[0]
                return espn_chance
            else:
                return 0
        else:
            return 0

    df['espn_%'] = df.apply(
        lambda x: merge_df_and_espn(x['Team']), axis=1
    )

    print(df)

    def calc_chance_value(team):
        chance = df.loc[df['Team'] == team, 'calc_%'].iloc[0]
        odds = df.loc[df['Team'] == team, 'MONEYLINE'].iloc[0]
        if odds == '':
            return 0
        else:
            odds = str(odds)
            if odds[0] == '−':
                odds = odds[1:]
                odds = float(odds)
                odds = round(-1 * odds, 2)
            chance = float(chance)
            odds = float(odds)
            if odds > 0:
                value = round(((odds / 10) + 10) * chance / 100, 3)
                return value
            else:
                value = round(chance / 100 * (10 + 10 /
                                              ((-1 * odds) / 10) * 10), 3)
                return value

    def avg_chance(team):
        calc = df.loc[df['Team'] == team, 'calc_%'].iloc[0]
        nf = df.loc[df['Team'] == team, 'nf_%'].iloc[0]
        espn = df.loc[df['Team'] == team, 'espn_%'].iloc[0]
        if nf == '' or nf == 0:
            if espn == '' or espn == 0:
                return 0
            else:
                return espn
        if espn == '' or espn == 0:
            if nf == '' or nf == 0:
                return 0
            else:
                return nf
        else:
            # calc = float(calc)
            nf = float(nf)
            espn = float(espn)
            avg_calc_nf = round((espn + nf) / 2, 2)
            return avg_calc_nf

    def espn_chance_value(team):
        chance = df.loc[df['Team'] == team, 'espn_%'].iloc[0]
        odds = df.loc[df['Team'] == team, 'MONEYLINE'].iloc[0]
        if chance == '' or odds == '':
            return 0
        else:
            odds = str(odds)
            if odds[0] == '−':
                odds = odds[1:]
                odds = float(odds)
                odds = round(-1 * odds, 2)
            chance = float(chance)
            odds = float(odds)
            if odds > 0:
                value = round(((odds / 10) + 10) * chance / 100, 3)
                return value
            else:
                value = round(chance / 100 * (10 + 10 /
                                              ((-1 * odds) / 10) * 10), 3)
                return value

    def nf_chance_value(team):
        chance = df.loc[df['Team'] == team, 'nf_%'].iloc[0]
        odds = df.loc[df['Team'] == team, 'MONEYLINE'].iloc[0]
        if chance == '' or odds == '':
            return 0
        else:
            odds = str(odds)
            if odds[0] == '−':
                odds = odds[1:]
                odds = float(odds)
                odds = round(-1 * odds, 2)
            chance = float(chance)
            odds = float(odds)
            if odds > 0:
                value = round(((odds / 10) + 10) * chance / 100, 3)
                return value
            else:
                value = round(chance / 100 * (10 + 10 /
                                              ((-1 * odds) / 10) * 10), 3)
                return value

    def avg_chance_value(team):
        chance = df.loc[df['Team'] == team, 'nf_espn_%'].iloc[0]
        odds = df.loc[df['Team'] == team, 'MONEYLINE'].iloc[0]
        if chance == '' or odds == '':
            return 0
        else:
            odds = str(odds)
            if odds[0] == '−':
                odds = odds[1:]
                odds = float(odds)
                odds = round(-1 * odds, 2)
            chance = float(chance)
            odds = float(odds)
            if odds > 0:
                value = round(((odds / 10) + 10) * chance / 100, 3)
                return value
            else:
                value = round(chance / 100 * (10 + 10 /
                              ((-1 * odds) / 10) * 10), 3)
                return value

    df['nf_espn_%'] = df.apply(
        lambda x: avg_chance(x['Team']), axis=1
    )
    df['calc_v'] = df.apply(
        lambda x: calc_chance_value(x['Team']), axis=1
    )
    df['nf_v'] = df.apply(
        lambda x: nf_chance_value(x['Team']), axis=1
    )
    df['espn_v'] = df.apply(
        lambda x: espn_chance_value(x['Team']), axis=1
    )
    df['avg_v'] = df.apply(
        lambda x: avg_chance_value(x['Team']), axis=1
    )

    print(df)

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
                    print(day)
                    gd = day.split('-')
                    print(day)
                    day = gd[2]
                    print('day = ')
                    print(gd[2])
                    print('month = ')
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
    print('Day search list for making abbreviated list of bets:')

    print(day_lst)

    day_lst = date_dig_to_words(day_lst)

    print(day_lst)

    def fix_date(team):
        day = df.loc[df['Team'] == team, 'date'].iloc[0]
        if day == 'Today':
            return day
        elif day == 'Tomorrow':
            return day
        else:
            ind = day.index(' ') + 1
            day = day[ind:]
            return day

    df['date'] = df.apply(
        lambda x: fix_date(x['Team']), axis=1
    )

    df_short = df.drop(
        df.columns[[5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20, 21, 23]], axis=1)

    print(df_short)

    # df_short = df_short[~df_short['date'].isin(day_lst)]
    df_short = pd.DataFrame(df_short)
    df_short = df_short[~df_short['date'].isin([day_lst])]

    def blank_nf_chance(chance):
        chance = str(chance)
        if chance == 'NaN' or chance == '' or chance == ' ':
            chance = 0
            return chance
        else:
            chance = float(chance)
            return chance

    def blank_avg_chance(chance):
        chance = str(chance)
        if chance == 'NaN' or chance == '' or chance == ' ':
            chance = 0
            return chance
        else:
            chance = float(chance)
            return chance

    def blank_calc_value(val):
        val = str(val)
        if val == 'NaN' or val == '' or val == ' ':
            val = 0
            return val
        else:
            val = float(val)
            return val

    def blank_nf_value(val):
        val = str(val)
        if val == 'NaN' or val == '' or val == ' ':
            val = 0
            return val
        else:
            val = float(val)
            return val

    def blank_avg_value(val):
        val = str(val)
        if val == 'NaN' or val == '' or val == ' ':
            val = 0
            return val
        else:
            val = float(val)
            return val

    df_short['nf_%'] = df_short.apply(
        lambda x: blank_nf_chance(x['nf_%']), axis=1
    )
    df_short['nf_espn_%'] = df_short.apply(
        lambda x: blank_avg_chance(x['nf_espn_%']), axis=1
    )
    df_short['calc_v'] = df_short.apply(
        lambda x: blank_calc_value(x['calc_v']), axis=1
    )
    df_short['nf_v'] = df_short.apply(
        lambda x: blank_nf_value(x['nf_v']), axis=1
    )
    df_short['avg_v'] = df_short.apply(
        lambda x: blank_avg_value(x['avg_v']), axis=1
    )

    def print_column_nfc(team):
        val = df.loc[df['Team'] == team, 'nf_%'].iloc[0]
        print('.' + str(val) + '.')
        print(str(val))
        print(type(val))
        print('\n')
        return

    def print_column_avgc(team):
        val = df.loc[df['Team'] == team, 'avg_%'].iloc[0]
        print(val)
        print(str(val))
        print(type(val))
        print('\n')
        return

    def print_column_calcval(team):
        val = df.loc[df['Team'] == team, 'calc_v'].iloc[0]
        print(val)
        print(str(val))
        print(type(val))
        print('\n')
        return

    def print_column_nfcval(team):
        val = df.loc[df['Team'] == team, 'nf_v'].iloc[0]
        print(val)
        print(str(val))
        print(type(val))
        print('\n')
        return

    def print_column_nfval(team):
        val = df.loc[df['Team'] == team, 'nf_v'].iloc[0]
        print(val)
        print(str(val))
        print(type(val))
        print('\n')
        return

    def print_column_avgval(team):
        val = df.loc[df['Team'] == team, 'avg_v'].iloc[0]
        print(val)
        print(str(val))
        print(type(val))
        print('\n')
        return

    df_short.apply(
        lambda x: print_column_nfc(x['Team']), axis=1
    )

    print(df_short)
    # df_short = df_short.sort_values(by=['nf_v'], ascending=False)
    # df = df.sort_values(by=['nf_v'], ascending=False)

    # df.to_excel(
    #     '/Users/Hayden/OneDrive/Sports Betting/Football/cfb.xlsx', index=False, sheet_name='penis'
    # )

    new_cols = ['Team', 'SPREAD', 'TOTAL', 'MONEYLINE', 'date', 'team_total', 'calc_%', 'nf_%', 'espn_%', 'nf_espn_%', 'calc_v',
                'nf_v', 'espn_v', 'avg_v']

    df_short = df_short.reindex(columns=new_cols)

    df_short = df_short.sort_values(by=['avg_v'], ascending=False)

    # with pd.ExcelWriter('/Users/Hayden/OneDrive/Sports Betting/Football/ignore/isaidignore/urabitch/cfb_.xlsx') as writer:  # doctest: +SKIP
    #     df_short.to_excel(writer, 'Within Next Week', index=False)
    #     df.to_excel(writer, 'All', index=False)
    #     df_espn.to_excel(writer, 'ESPN', index=False)

    with pd.ExcelWriter('/Users/Hayden/OneDrive/Sports Betting/Football/cfb.xlsx') as writer:  # doctest: +SKIP
        df_short.to_excel(writer, 'Within Next Week', index=False)
        df_dk.to_excel(writer, sheet_name='draftkings', index=False)
        df.to_excel(writer, 'All', index=False)
        df_espn.to_excel(writer, 'ESPN', index=False)
        df_nf.to_excel(writer, sheet_name='nf', index=False)
        df_stats.to_excel(writer, sheet_name='teamrankings stats', index=False)
    return


ncaaf()
