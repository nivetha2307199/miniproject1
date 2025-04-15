import streamlit as st
import pandas as pd
import pymysql
def rating():
    mydb = pymysql.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Title,Rating,Duration,Voting,Genre FROM finaldataset")
    myresult = mycursor.fetchall()
    data=pd.DataFrame(myresult)
    st.title("Rating")
    st.subheader("Filter movies based on their runtime")
    st.write("option1:<7.0")
    st.write("option2:7.0-8.0")
    st.write("option3:8.0-9.0")
    st.write("option4:>9.0")
    options = ['Selection','<7.0', '7.0-8.0', '8.0-9.0','9.0']
    selected_rating = st.selectbox("Choose your selection:", options)
    movies=data[0]
    rating=data[1]
    duration=data[2]
    voting=data[3]
    genre=data[4]
    if(selected_rating=='<7.0'):
        m=[]
        r=[]
        d=[]
        v=[]
        g=[]
        i=0
        for val in movies:
            if(rating[i]<=7.0):
                r.append(rating[i])
                d.append(duration[i])
                v.append(voting[i])
                g.append(genre[i])
                m.append(val)
            i+=1
        dd={"Movie":m,"Duration":d,"Rating":r,"Voting":v,"Genre":g}
        df=pd.DataFrame(dd)
        st.dataframe(df)
    if(selected_rating=='7.0-8.0'):
        m=[]
        r=[]
        d=[]
        v=[]
        g=[]
        i=0
        for val in movies:
            if(rating[i]>=7.0 and rating[i]<=8.0):
                r.append(rating[i])
                d.append(duration[i])
                v.append(voting[i])
                g.append(genre[i])
                m.append(val)
            i+=1
        dd={"Movie":m,"Duration":d,"Rating":r,"Voting":v,"Genre":g}
        df=pd.DataFrame(dd)
        st.dataframe(df)
    if(selected_rating=='8.0-9.0'):
        m=[]
        r=[]
        d=[]
        v=[]
        g=[]
        i=0
        for val in movies:
            if(rating[i]>=8.0 and rating[i]<=9.0):
                r.append(rating[i])
                d.append(duration[i])
                v.append(voting[i])
                g.append(genre[i])
                m.append(val)
            i+=1
        dd={"Movie":m,"Duration":d,"Rating":r,"Voting":v,"Genre":g}
        df=pd.DataFrame(dd)
        df=df.dropna()
        st.dataframe(df)
    if(selected_rating=='9.0'):
        m=[]
        r=[]
        d=[]
        v=[]
        g=[]
        i=0
        for val in movies:
            if(rating[i]>9.0):
                r.append(rating[i])
                d.append(duration[i])
                v.append(voting[i])
                g.append(genre[i])
                m.append(val)
            i+=1
        dd={"Movie":m,"Duration":d,"Rating":r,"Voting":v,"Genre":g}
        df=pd.DataFrame(dd)
        st.dataframe(df)
rating()
