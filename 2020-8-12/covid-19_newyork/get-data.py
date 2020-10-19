import re
import requests
import numpy as np
import json
import os
from collections import OrderedDict
import pandas as pd
import json
import datetime
import time
import csv
##############################################
#函数作用：写入数据到json文件
def write_list_to_json(list, json_file_name):
    with open(json_file_name, 'w') as  f:
        json.dump(list, f)
#############################################

#函数作用：获取世界疫情
#函数get_world_data参数说明{
#     url为目标数据的网页
#     headers为请求服务
#     entries为所要数据的位置，
#     date为数据开始的日期的位置
#     want_data_class为获取数据的类型（active，confirm，death，cover）
# }
def get_world_confirm_data(url,headers):

    res = requests.get(url,headers = headers)
    res.encoding = "UTF-8"
    pattern = re.compile('(\'\{"(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}\}\')',re.S)
    end = re.findall(pattern,res.text)
    print(end)
    a=str(end[0])
    data_relative_confirmed_json=[]
    pattern_1 = re.compile('(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}',re.S)
    end_1=re.findall(pattern_1,a)
    country=[]
    for i in range(len(end_1)):
        data={
            'Country':'',
        }
        data['Country']=end_1[i][0]
        #确诊人数
        country.append(end_1[i][0])
        care=end_1[i][7].replace('[','').replace(']','').split(',')
        try:
            time=end_1[i][8].replace('/',',').replace('/',',').replace('"','').split(',')
            print(time)
            time[2]='2020'
            date=[]
            in_date = time[2]+'-'+time[0]+'-'+time[1]
            dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
            for k in range(len(end_1[i][7].replace('[','').replace(']','').split(','))):
                out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
                date.append(out_date)
            print(date)
            time_care=OrderedDict(zip(date,care))
            print(time_care)
            date_json=OrderedDict(data,**time_care)
            data_relative_confirmed_json.append(date_json)
            
        except:
            pass
        
    with open(date[-1]+'-1point3acres-last_world_confirm_data.txt', 'w') as f:
        f.write(str(data_relative_confirmed_json))
    write_list_to_json(data_relative_confirmed_json,date[-1]+'-world-confirm-data.json')
    data_csv=pd.DataFrame(json.loads(open(date[-1]+'-world-confirm-data.json','r+').read()))
    print(end_1[36][0])
    care=end_1[36][7].replace('[','').replace(']','').split(',')
    try:
        time=end_1[36][8].replace('/',',').replace('/',',').replace('"','').split(',')
        print(time)
        time[2]='2020'
        date=[]
        in_date = time[2]+'-'+time[0]+'-'+time[1]
        dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
        for k in range(len(end_1[36][7].replace('[','').replace(']','').split(','))):
            out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
            date.append(out_date)
        print(date)
        time_care=OrderedDict(zip(date,care))
        print(time_care)
    except:
        pass
    with open(date[-1]+'-1point3acres-former_world-data.txt', 'w') as f:
        f.write(res.text)

    date.insert(0,'Country')
    cols=date
    data_csv=data_csv.loc[:,cols]
    data_csv.T
    data_csv.to_csv(date[-1]+'-1point3acres-world-confirm-data.json.csv')
    df=pd.read_csv(date[-1]+'-1point3acres-world-confirm-data.json.csv')
    new_csv=df.T
    new_csv.to_csv(date[-1]+'-1point3acres-world-confirm-data.json.csv')
    return date[-1]
#############################################################################
def get_world_death_data(url,headers):
    res = requests.get(url,headers = headers)
    res.encoding = "UTF-8"
    pattern = re.compile('(\'\{"(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}\}\')',re.S)
    end = re.findall(pattern,res.text)
    a=str(end[0])
    data_relative_confirmed_json=[]
    pattern_1 = re.compile('(\w+)":{"active":(.*?),"confirmed":(.*?),"deaths":(.*?),"recovered":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"relative_recovered":(.*?),"relative_recovered_start_date":(.*?)}',re.S)
    end_1=re.findall(pattern_1,a)
    country=[]
    for i in range(len(end_1)):
        data={
            'Country':'',
        }
        data['Country']=end_1[i][0]
        #确诊人数
        country.append(end_1[i][0])
        care=end_1[i][9].replace('[','').replace(']','').split(',')
        try:
            time=end_1[i][10].replace('/',',').replace('/',',').replace('"','').split(',')
            print(time)
            time[2]='2020'
            date=[]
            in_date = time[2]+'-'+time[0]+'-'+time[1]
            dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
            for k in range(len(end_1[i][9].replace('[','').replace(']','').split(','))):
                out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
                date.append(out_date)
            print(date)
            time_care=OrderedDict(zip(date,care))
            print(time_care)
            date_json=OrderedDict(data,**time_care)
            data_relative_confirmed_json.append(date_json)
            
        except:
            pass
    with open(date[-1]+'-1point3acres-last_world_death-data.txt', 'w') as f:
        f.write(str(data_relative_confirmed_json))


    write_list_to_json(data_relative_confirmed_json,date[-1]+'-world-death-data.json',)
    data_csv=pd.DataFrame(json.loads(open(date[-1]+'-world-death-data.json','r+').read()))
    print(end_1[36][0])
    care=end_1[36][9].replace('[','').replace(']','').split(',')
    try:
        time=end_1[36][10].replace('/',',').replace('/',',').replace('"','').split(',')
        print(time)
        time[2]='2020'
        date=[]
        in_date = time[2]+'-'+time[0]+'-'+time[1]
        dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
        for k in range(len(end_1[36][9].replace('[','').replace(']','').split(','))):
            out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            dt=datetime.datetime.strptime(out_date, "%Y-%m-%d")
            date.append(out_date)
        print(date)
        time_care=OrderedDict(zip(date,care))
        print(time_care)
    except:
        pass


    date.insert(0,'Country')
    cols=date
    data_csv=data_csv.loc[:,cols]
    data_csv.T
    data_csv.to_csv(date[-1]+'-1point3acres-world-death-data.json.csv')
    df=pd.read_csv(date[-1]+'-1point3acres-world-death-data.json.csv')
    new_csv=df.T
    new_csv.to_csv(date[-1]+'-1point3acres-world-death-data.json.csv')
    
    return date[-1]

####################################################################################

#函数作用：获取世界疫情
#函数get_state_data参数说明{
#     url为目标数据的网页
#     headers为请求服务
# }
def get_state_data(url,headers,csv_date):
    res = requests.get(url,headers = headers)
    res.encoding = "UTF-8"
    pattern = re.compile('state_name":(.*?),"county":(.*?),"entries":(.*?)}',re.S)
    end = list(re.findall(pattern,res.text))
    state_name='state_name'
    county='county'
    entries='entries'
    a=[]
    with open('1point3acres-former_us-state_data.txt','w') as f:
        f.write(res.text)
    #过滤出州和区的名字组成字典
    for i in range(len(end)):  
        data={
            "state_name:":[],
            "county:":[],
            
        } 
        data['state_name:'].append(end[i][0])
        data["county:"].append(end[i][1])
        
        data['state_name:']=','.join(data['state_name:'])
        data["county:"]=','.join(data["county:"])
        
        data['state_name:']=list(data['state_name:'])
        data["county:"]=list(data["county:"])
        
        #过滤出日期和确诊数，通过zip拉取起来
        date=re.findall(pattern,res.text)
        date_new=date[i][2].replace('[[',',[').replace(']]','],')
        re_compile = re.compile('"(.*?)",(.*?)]')
        date_care=re.findall(re_compile,date_new)
        time=[]
        care=[]
        for i in range(len(date_care)):
            time.append(date_care[i][0])
            care.append(date_care[i][1])

        time_care=OrderedDict(zip(time,care))
    #数据清洗
        for i in range(len(data['state_name:'])):
            data['state_name:'][i]=data['state_name:'][i].replace('\"','').replace('[','').replace(']','')
        for i in range(len(data["county:"])):
            data["county:"][i]=data["county:"][i].replace('\"','').replace('[','').replace(']','')
        
        data['state_name:']=''.join(data['state_name:'])
        data["county:"]=''.join(data["county:"])
        
        b={
            "state_name:":'',
            "county:":'',
            "entries:":''
        } 
        b["state_name:"]=data['state_name:']
        b["county:"]=data["county:"]
        
        b=OrderedDict(b,**time_care)
        time.insert(0,'state_name:')
        time.insert(1,"county:")
        a.append(b)
    with open(csv_date+'-1point3acres-last_us-state_data.txt','w') as f:
        f.write(str(a))
    write_list_to_json(a,csv_date+'-data.json')
    data_csv=pd.DataFrame(json.loads(open(csv_date+'-data.json','r+').read()))
    cols=time
    data_csv=data_csv.loc[:,cols]
    data_csv.to_csv(csv_date+'-1point3acres-data.json.csv')
    
#########################################################################################
def get_us_state_data(url_us_state,headers,data,date,data_class,csv_date):
    res = requests.get(url_us_state, headers=headers)
    res.encoding = "UTF-8"
    with open(csv_date+'-1point3acres-former_us_state_data.txt', 'w') as f:
        f.write(res.text)

    with open(csv_date+'-1point3acres-former_us_state_data.txt', 'r') as b:
        a=b.read()
    data_relative_confirmed_json = []
    pattern_1 = re.compile('"(\w+)":{"active":(.*?),"confirmed":(.*?),"cured":(.*?),"deaths":(.*?),"end_date":(.*?),"relative_active":(.*?),"relative_active_start_date":(.*?),"relative_confirmed":(.*?),"relative_confirmed_start_date":(.*?),"relative_cured":(.*?),"relative_cured_start_date":(.*?),"relative_deaths":(.*?),"relative_deaths_start_date":(.*?),"start_date":(.*?)',re.S)
    end_1 = re.findall(pattern_1, a)
    country = []
    for i in range(14,len(end_1)):
        data_dict = {
            'Country': '',
        }
        data_dict['Country'] = end_1[i][0]
        # 确诊人数
        country.append(end_1[i][0])
        care = end_1[i][data].replace('[', '').replace(']', '').split(',')
        try:
            time = end_1[i][date].replace('/', ',').replace('"', '').split(',')
            time.append('NULL')
            time[2]='2020'
            date_number = []
            in_date = time[2] + '-' + time[0] + '-' + time[1]
            dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
            for k in range(len(end_1[i][data].replace('[', '').replace(']', '').split(','))):
                out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                dt = datetime.datetime.strptime(out_date, "%Y-%m-%d")
                date_number.append(out_date)

            time_care = OrderedDict(zip(date_number, care))
            date_json = OrderedDict(data_dict,**time_care)
            data_relative_confirmed_json.append(date_json)
        except:
            date_number = []
            today=datetime.date.today()
            dt = datetime.datetime.strptime(str(today), "%Y-%m-%d")
            for k in range(len(end_1[i][data].replace('[', '').replace(']', '').split(','))):
                out_date = (dt + datetime.timedelta(days=-1)).strftime("%Y-%m-%d")
                dt = datetime.datetime.strptime(out_date, "%Y-%m-%d")
                date_number.append(out_date)
            time_care = OrderedDict(zip(date_number[::-1], care))
            print(time_care)
            date_json = OrderedDict(data_dict, **time_care)
            data_relative_confirmed_json.append(date_json)
       
        write_list_to_json(data_relative_confirmed_json, '20200529.json')
        data_csv = pd.DataFrame(json.loads(open('20200529.json', 'r+').read()))

        care = end_1[53][data].replace('[', '').replace(']', '').split(',')
        try:
            time = end_1[53][date].replace('/', ',').replace('/', ',').replace('"', '').split(',')
            time.append('2020')
            date_number = []
            in_date = time[2] + '-' + time[0] + '-' + time[1]
            dt = datetime.datetime.strptime(in_date, "%Y-%m-%d")
            for k in range(len(end_1[53][data].replace('[', '').replace(']', '').split(','))):
                out_date = (dt + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
                dt = datetime.datetime.strptime(out_date, "%Y-%m-%d")
                date_number.append(out_date)
            time_care = OrderedDict(zip(date_number, care))
        except:
            pass

    os.remove('20200529.json')
    date_number.insert(0, 'Country')
    cols = date_number
    data_csv = data_csv.loc[:, cols]
    data_csv.T
    data_csv.to_csv(date_number[-1]+'-1point3acres-us_state-'+data_class+'-data.json.csv')
    df = pd.read_csv(date_number[-1]+'-1point3acres-us_state-'+data_class+'-data.json.csv')
    new_csv = df.T
    new_csv.to_csv(date_number[-1]+'-1point3acres-us_state-'+data_class+'-data.json.csv')
    with open(date_number[-1]+'-1point3acres-last-us_state-'+data_class+'-data.txt', 'w') as f:
        f.write(str(data_relative_confirmed_json))
#########################################################################################
def get_GA_data(csv_date):
    a=[]
    with open(csv_date+'-1point3acres-data.json.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        rows=[row for row in reader]
    a.append(rows[0][1:-1])
    print(rows)
    for i in range(len(rows)):
        if rows[i][1]=='GA':
            a.append(rows[i][1:-1])
    with open(csv_date+"-1point3acres-GA.json.csv","w",newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        #先写入columns_name
        #写入多行用writerows
        writer.writerows(a)
    with open(csv_date+"-1point3acres-GA.txt","w") as f: 
        f.write(str(a))
############################################################################################
#函数作用获取纽约市的数据
def get_NY_data(csv_date):
    a=[]
    with open(csv_date+'-1point3acres-data.json.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        rows=[row for row in reader]
    a.append(rows[0][1:-1])
    print(rows)
    for i in range(len(rows)):
        if rows[i][1]=='NY':
            a.append(rows[i][1:-1])
    with open(csv_date+"-1point3acres-NY.json.csv","w",newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        #先写入columns_name
        #写入多行用writerows
        writer.writerows(a)
    with open(csv_date+"-1point3acres-NY.txt","w") as f: 
        f.write(str(a))
######################################################################
#主函数#
url_us_state = 'https://coronavirus.1point3acres.com/_next/static/chunks/6229c4eae07ef0da4efb4e4efd0fcda01b4e963b.56bd7d585ed2db7ef8ac.js'
url_world = 'https://coronavirus.1point3acres.com/_next/static/chunks/7abc78da28f210ee742522915e43dec308bc0666.81f6c243e98f7d828403.js'

headers = {
    'User-Agent':'Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11',
}
#获取确诊人数数据
csv_date=get_world_confirm_data(url_world,headers)
#获取世界死亡人数
#get_world_death_data(url_world,headers)
#print('请等待程序还在运行！！！！！！！！')
#获取州数据，加上GA的数据
#get_state_data(url_world,headers,csv_date)
#get_GA_data(csv_date)
get_NY_data(csv_date)
#获取州的汇总数据
#get_us_state_data(url_us_state,headers,8,9,'confirmed',csv_date)
#get_us_state_data(url_us_state,headers,12,13,'death',csv_date)
#os.remove('1point3acres-former_us-state_data.txt')
#os.remove(csv_date+'-1point3acres-data.json.csv')
#os.remove(csv_date+'-1point3acres-last_us-state_data.txt')
###########################################################################