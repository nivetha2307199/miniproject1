import streamlit as st
import pandas as pd
import pymysql
def maxmin():
    mydb =pymysql.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Title,Duration FROM finaldataset")
    myresult = mycursor.fetchall()
    data1=pd.DataFrame(myresult)
    hrs = data1[1].str.split('h')
    mins=data1[1].str.split('m')
    hours=[]
    minutes=[]
    for i in hrs:
        val=i[0].replace(" ", "")
        if(len(val)>=2):
            val=val[0:2].replace(" ", "")
        hours.append(val)
    for i in mins:
        val=i[0].split('h')
        str1=str(val)
        str1=str1[7:len(str1)-2].replace(" ", "")
        if(len(str1)==0):
            minutes.append("0")
        else:
            minutes.append(str1)
    duration=[]
    for i in range(len(hours)):
        if(len(hours)==0 or len(minutes)==0):
            continue
        else:
            hh=(hours[i])
            mm=(minutes[i])
            dd=hh+mm
            h1=(int(dd[0])*60)+int(mm)
            duration.append(h1)
    movie=data1[0]
    dataset={"Movie":movie,"Duration":duration}
    df=pd.DataFrame(dataset)
    st.title("Shortest and Longest Duration of Movies")
    st.subheader("Shortest Duration of Movies")
    df1= df.sort_values(by="Duration", ascending=True)
    df1=df1.head(10)
    st.table(df1)
    st.subheader("Longest Duration of Movies")
    df2= df.sort_values(by="Duration", ascending=False)
    df2=df2.head(10)
    st.table(df2)
maxmin()
