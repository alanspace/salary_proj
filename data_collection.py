# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 23:38:46 2020

@author: alan
"""
import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/alan/Downloads/Data_Science/salary_proj/chromedriver"
df = gs.get_jobs('data scientist', 100, False, path, 20)

