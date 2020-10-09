import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def readExcel(path):
    df = pd.read_excel(path)
    return df


def student(df):
    print("学生个人数据")
    df = pd.read_excel('mydata\\stu_ass_exe_info.xlsx').loc[:,['stu_id','exe_id','commit_time']]
    df.columns = ['id','exe_id','time']
    df['time'] = pd.to_datetime(df['time'],unit='ms')
    df['count'] = 1
    # print(df)
    idGroup = df.groupby('id')
    stuDf = pd.DataFrame(columns=['jiange_days', 'youxiao_days', 'first_day', 'last_day', 'counts'])
    print(stuDf)


    for id,group in idGroup:
        stu = pd.DataFrame(group[['count']].values, index=group['time'])
        res = stu.resample('D').sum()
        stuDf.loc[id] = [len(res.index), len(res[res[0] > 0]), res.index[0], res.index[len(res)-1], res.sum()[0]]

    print(stuDf)
    stuDf.to_excel('handle.xlsx')

# main program starts here
if __name__ == '__main__':
    path = 'mydata\\stu_ass_exe_info.xlsx'
    df = readExcel(path)
    student(df)