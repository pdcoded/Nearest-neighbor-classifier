# -*- coding: utf-8 -*-
"""
Created on Mon Feb 09 12:29:15 2015

@author: PRABHUDATTA
"""
from math import sqrt,pow
def training():
    f=open('D:/data mining/athletesTrainingSet.txt')
    lines = f.readlines()
    f.close()
    k= lines[0].strip().split('\t')
    training_data=[]
    for line in lines[1:]:
        a=''
        b=[]
        c=''
        x=line.strip().split('\t')
        for i in range(len(k)):
            if k[i]=='class':
                a=x[i]
            if k[i]=='num':
                b.append(int(x[i]))
            if k[i]=='comment':
                c=x[i]
        training_data.append((a,b,c))
    return training_data
def test():
    f=open('D:/data mining/athletesTestSet.txt')
    lines = f.readlines()
    f.close()
    k= lines[0].strip().split('\t')
    test_data=[]
    for line in lines[1:]:
        a=''
        b=[]
        c=''
        x=line.strip().split('\t')
        for i in range(len(k)):
            if k[i]=='class':
                a=x[i]
            if k[i]=='num':
                b.append(int(x[i]))
            if k[i]=='comment':
                c=x[i]
        test_data.append((a,b,c))
    return test_data

def Median(alist):
    if alist == []:
        return []
    blist = sorted(alist)
    length = len(alist)
    if length % 2 == 1:
        return blist[int(((length + 1) / 2) - 1)]
    else:
        v1 = blist[int(length / 2)]
        v2 =blist[(int(length / 2) - 1)]
        return (v1 + v2) / 2.0
def getAbsoluteStandardDeviation(alist, median):
    sum = 0
    for item in alist:
        sum += abs(item - median)
    return sum / len(alist)
def Normalized_TrainingSet():
    k=training()
    a=[]
    b=[]
    normal_list=[]
    for i in k:
        a.append(i[1][0])
        b.append(i[1][1])
    x=[(z-Median(a))/(getAbsoluteStandardDeviation(a,Median(a))) for z in a]
    y=[(z-Median(b))/(getAbsoluteStandardDeviation(b,Median(b))) for z in b]
    for i in range(len(x)):
        normal_list.append((k[i][0],[x[i],y[i]],k[i][2]))
    return normal_list
def Normalized_TestSet():
    k=test()
    a=[]
    b=[]
    normal_list2=[]
    for i in k:
        a.append(i[1][0])
        b.append(i[1][1])
    x=[(z-Median(a))/(getAbsoluteStandardDeviation(a,Median(a))) for z in a]
    y=[(z-Median(b))/(getAbsoluteStandardDeviation(b,Median(b))) for z in b]
    for i in range(len(x)):
        normal_list2.append((k[i][0],[x[i],y[i]],k[i][2]))
    return normal_list2
def Nearest_Neighborhood():
    test=Normalized_TestSet()
    train=Normalized_TrainingSet()
    classify=[]
    for i in test:
        k=[(sqrt(pow(i[1][0]-z[1][0],2)+pow(i[1][1]-z[1][1],2)),z[0]) for z in train]
        k.sort()
        classify.append(k[0][1])
    return classify
def accuracy(): 
    test_data=Normalized_TestSet()
    response_data=Nearest_Neighborhood()
    flag=0
    for i in range(len(test_data)):
        if response_data[i]==test_data[i][0]:
            flag+=1
    return (flag*100)/len(test_data)
    
    
    
    
    
    
        
        
        
        
        

    
    
    
    
                
            