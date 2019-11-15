# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 21:34:13 2019

@author: Rishav

extracting different data variations from the text file dates.txt using Regular
Expression
    
"""

import pandas as pd

doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
df.head(10)


## (1) 04/20/2009; 04/20/09; 4/20/09; 4/3/09

a1_1 = df.str.extractall(r'(\d{1,2})[/-](\d{1,2})[/-](\d{2})\b')
a1_2 = df.str.extractall(r'(\d{1,2})[/-](\d{1,2})[/-](\d{4})\b')
a1 = pd.concat([a1_1,a1_2])


## (2)Mar-20-2009; Mar 20, 2009; March 20, 2009; Mar. 20, 2009; Mar 20 2009; (20 points)

a2_1 = df.str.extractall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[-]([\d]{1,2})[-]([\d]{4})')
a2_2 = df.str.extractall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\s]([\d]{1,2})[,][\s]([\d]{4})')
a2_3 = df.str.extractall(r'(January|February|March|April|May|June|July|August|September|October|November|December)[\s]([\d]{1,2})[,][\s]([\d]{4})')
a2_4 = df.str.extractall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[.][\s]([\d]{1,2})[,][\s]([\d]{4})')
a2_5 = df.str.extractall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\s]([\d]{1,2})[\s]([\d]{4})')
a2 = pd.concat([a2_1,a2_2,a2_3,a2_4,a2_5])


## (3) 20 Mar 2009; 20 March 2009; 20 Mar. 2009; 20 March, 2009 (20 points)

a3_1 = df.str.extractall(r'([\d]{1,2})[\s](Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\s]([\d]{4})')
a3_2 = df.str.extractall(r'([\d]{1,2})[\s](January|February|March|April|May|June|July|August|September|October|November|December)[\s]([\d]{4})')
a3_3 = df.str.extractall(r'([\d]{1,2})[\s](Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[.][\s]([\d]{4})')
a3_4 = df.str.extractall(r'([\d]{1,2})[\s](January|February|March|April|May|June|July|August|September|October|November|December)[,][\s]([\d]{4})')
a3 = pd.concat([a3_1,a3_2,a3_3,a3_4])

## (4) Mar 20th, 2009; Mar 21st, 2009; Mar 22nd, 2009 (20 points)

a4_1 = df.str.extractall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\s]([\d]{1,2})\Bth[,][\s]([\d]{4})')
a4_2 = df.str.extractall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\s]([\d]{1,2})\Bth[,][\s]([\d]{4})')
a4_3 = df.str.extractall(r'(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[\s]([\d]{1,2})\Bnd[,][\s]([\d]{4})')
a4 = pd.concat([a4_1,a4_2,a4_3])

## (5) 6/2008; 12/2009 (20 points)

a5_1 = df.str.extractall(r'(\d{1})[/](\d{4})\b')
a5_2 = df.str.extractall(r'(\d{1,2})[/](\d{4})\b')
a5 = pd.concat([a5_1,a5_2])

#concatinating all 5 parts together
final = pd.concat([a1,a2,a3,a5])