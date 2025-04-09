import streamlit as st
import pandas as pd
import mysql.connector
def duration():
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
    st.title("Duration Hrs")
    st.subheader("Filter movies based on their runtime")
    st.write("option1:<2hrs")
    st.write("option2:2-3hrs")
    st.write("option3:>3hrs")
    options = ['Selection','<2hrs', '2-3hrs', '>3hrs']
    selected_Movie = st.selectbox("Choose your selection:", options)
    movies=data[0]
    if(selected_Movie=='<2hrs'):
        two=[]
        i=0
        movie=[]
        for val in movies:
            if(duration[i]<=120):
                two.append(duration[i])
                movie.append(val)
            i+=1
        dd={"Movie":movie,"Duration":two}
        df=pd.DataFrame(dd)
        st.dataframe(df)
    elif(selected_Movie=='2-3hrs'):
        two=[]
        i=0
        movie=[]
        for val in movies:
            if(duration[i]>120 and duration[i]<=180):
                two.append(duration[i])
                movie.append(val)
            i+=1
        dd={"Movie":movie,"Duration":two}
        df=pd.DataFrame(dd)
        st.dataframe(df)
    elif(selected_Movie=='>3hrs'):
        two=[]
        i=0
        movie=[]
        for val in movies:
            if(duration[i]>180):
                two.append(duration[i])
                movie.append(val)
            i+=1
        dd={"Movie":movie,"Duration":two}
        df=pd.DataFrame(dd)
        st.dataframe(df)
duration()