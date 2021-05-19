#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 12:29:38 2021

@author: denish
"""

import salary as s
import pandas as pd

path = '/Users/denish/Desktop/Completed Projects/DS_Salary/chromedriver'

df = s.get_jobs('data scientist',15,False,path,15)
