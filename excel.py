import pandas as pd
import numpy as np
import openpyxl
import xlwt
from openpyxl import load_workbook
import subprocess
import time

#subprocess.run([r"C:\Users\ukt430\Documents\GitHub\automation-IBM-Cognos-Analytics\p.bat"])

df = pd.read_excel("Réception Management Rapport - Mois (33).xlsx",header=None)
dff = pd.read_csv('file_list - Copy - Copy.csv',header=None)

def data_processing(data,column,name,number,cols):
    a = data.rename(columns = {column:name})# renaming the columns
    rows = a.drop(range(number),axis = 0,inplace = True)# dropping rows
    col = a.drop(cols,axis=1,inplace = True)# dropping columns 
    df = a 
    return df
df = data_processing(df,0,"ASN",14,[1,2,3,4,5,6,7,8,9,10])

def processing_data(data,column,name,cols):
    a = data[0].str.split('_',expand=True)
    b = a.rename(columns = {column:name})# renaming the columns
    #rows = b.drop(range(number),axis = 0,inplace = True)# dropping rows
    col = b.drop(cols,axis=1,inplace = True)# dropping columns 
    
    return b 
dff = processing_data(dff,2,"ASN",[0,1,3,4,5,6,7,8])

def uncommon_values(set1,set2):
    df_asn = set1['ASN'].values.tolist()
    df_monitor =set2["ASN"].values.tolist()
    asn = set(df_asn)
    monitor = set(df_monitor)
    temp1 = []
    for i in asn:
        if i not in monitor:
            temp1.append(i)
    with open("file.txt","w") as output:
        output.write(str(temp1))
    print(f"The ASNs that have not been retriggered :"+ str(temp1))
uncommon_values(df,dff)
