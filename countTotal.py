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


def countByTime(df):
    """Print "Hello World" and return None"""
    print("每天提交的次数折线图")
    df = df.loc[:,['stu_id','commit_time']]
    df.columns = ['id','time']
    df = df.dropna(axis=0, subset=['time'])
    a = np.arange(52404, dtype=int)
    for i in range(len(a)):
        a[i] = 1

    df['time'] = pd.to_datetime(df['time'],unit='ms')
    df['count'] = a
    print('转换后的数据：')
    print(df)

    print('数据统计')
    print(df['time'].describe())

    df = pd.DataFrame(df[['count']].values,index=df['time'])
    print('时间为索引')
    print(df)

    resD = df.resample('D').sum()
    print(resD)
    x1 = resD.index
    y1 = resD.values
    plt.plot(x1,y1,label='line',color='r')
    plt.xlabel('time')
    plt.ylabel('count')
    plt.title('Commit Times Total / Day ')

    # resW = df.resample('W').sum()
    # print(resW)
    # print(type(resW))
    # x2 = resW.index
    # y2 = resW.values
    # plt.plot(x2,y2,label='line2',color='b')
    # plt.xlabel('time')
    # plt.ylabel('count')
    # plt.title('提交次数折线图/周')
    # plt.legend()
    plt.show()







# main program starts here
if __name__ == '__main__':
    path = 'mydata\\stu_ass_exe_info.xlsx'
    df = readExcel(path)
    countByTime(df)