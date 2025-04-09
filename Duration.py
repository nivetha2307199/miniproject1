import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt 
def duration_visual():
    mydb = mysql.connector.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Title,Duration,Genre FROM finaldataset")
    myresult = mycursor.fetchall()
    data=pd.DataFrame(myresult)
    hrs = data[1].str.split('h')
    mins=data[1].str.split('m')
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
    movie=data[0]
    genre=data[2]
    dataset={"Movie":movie,"Duration":duration,"Genre":genre}
    df=pd.DataFrame(dataset)
    st.title("Average Duration by Genre")
    st.subheader("Dataset of the IMDB")
    genre_duration = df.groupby('Genre')['Duration'].mean().reset_index()
    st.table(genre_duration)
    st.title("Average values of the genre")
    st.subheader("Chart for the aveage value of the genre")
    fig, ax = plt.subplots(figsize=(10, 6))  # Set figure size here
    ax.bar(genre, duration, color='pink', alpha=0.7)
    ax.set_xlabel('Genre', fontsize=14)
    ax.set_ylabel('Duration', fontsize=14)
    plt.xticks(rotation=45, ha="right", fontsize=12)
    ax.grid(axis='y')
    st.pyplot(fig)
duration_visual()   