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
    print(df)
    return df

def countByDay(df):
    """Print "Hello World" and return None"""
    print("每天提交的次数折线图")
    df = df.loc[:,['stu_id','exe_id', 'commit_time']]
    df.columns = ['id', 'exe_id', 'time']
    df = df.dropna(axis=0, subset=['time'])
    df['time'] = pd.to_datetime(df['time'],unit='ms')
    df['count'] = 1
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

def countByHours(df):
    print('按时间段统计提交次数')
    df = df.loc[:, ['stu_id', 'commit_time']]
    df.columns = ['id', 'time']
    df = df.dropna(axis=0, subset=['time'])
    df['time'] = pd.to_datetime(df['time'],unit='ms')
    df['count'] = 1
    print('时间戳转换后的数据：')
    print(df)

    print('数据统计')
    print(df['time'].describe())

    df = pd.DataFrame(df[['count']].values,index=df['time'])
    print('时间为索引的数据')
    print(df)


    resDf = pd.DataFrame(columns=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23'])
    resD = df.resample('H')
    print(resD)
    print(type(resD))
    for name,group in resD:
        hour = name.hour
        print(hour)
        count = group.sum()
        print(count)
        resDf[count] = resDf[count] + count
        # break
    print(resDf)
# main program starts here
if __name__ == '__main__':
    path = 'mydata\\stu_ass_exe_info.xlsx'
    df = readExcel(path)
    countByHours(df)