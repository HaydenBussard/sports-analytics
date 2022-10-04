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

url_tr = 'https://www.teamrankings.com/nba/stat/three-pointers-made-per-game'
df_tr = pd.read_html(url_tr)
tr_3s_table = df_tr[0].values.tolist()

for elem in tr_3s_table:
    del elem[0]
    del elem[2:4]
    del elem[-1]
    # print(str(type(elem[1])) + str(type(elem[2])) + str(type(elem[3])))
    print(elem)
    
