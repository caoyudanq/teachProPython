# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:00:11 2020

@author: Administrator
"""


# Demo file for Spyder Tutorial


# Hans Fangohr, University of Southampton, UK

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def readExcel(path):
    df = pd.read_excel(path)
    return df

def CountByExeId(df):
    """Print "Hello World" and return None"""
    print("Good Bye World")
    df = df.loc[:,['stu_id','exe_id','commit_time']]
    print(df)
    df.columns = ['id','exe_id','time']
    ids = df.groupby('exe_id')

    print(ids.size())

    x1 = ids.size().index
    y1 = ids.size().values
    plt.plot(x1,y1,label='line',color='r')
    plt.xlabel('exe_id')
    plt.ylabel('count')
    plt.title('exercise commit times')
    plt.show()


# main program starts here
if __name__ == '__main__':
    path = 'mydata\\stu_ass_exe_info.xlsx'
    df = readExcel(path)
    CountByExeId(df)
    # student(df)