import streamlit as st
import pandas as pd
import pymysql
def genre():
    mydb = pymysql.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Title,Rating,Duration,Voting,Genre FROM finaldataset where Voting>=50000")
    myresult = mycursor.fetchall()
    data=pd.DataFrame(myresult,columns=['Movie','Rating','Duration','Voting','Genre'])
    st.title("Genre")
    st.subheader("Filter Genre based on their runtime")
    st.write("option1:Action")
    st.write("option2:Drama")
    st.write("option3:Comedy")
    st.write("option4:Romance")
    st.write("option5:Documentary")
    options = ['Selection','Action', 'Drama', 'Comedy','Romance','Documentary']
    selected_voting = st.selectbox("Choose your selection:", options)
    movie=data['Movie']
    duration=data['Duration']
    rating=data['Rating']
    voting=data['Voting']
    genre=data['Genre']
    if(selected_voting=='Action'):
        m=[]
        d=[]
        r=[]
        v=[]
        i=0
        for dt in movie:
            if(genre[i]=='Action'):
                m.append(dt)
                d.append(duration[i])
                r.append(rating[i])
                v.append(voting[i])
            i+=1
        data={"Movie":m,"Duration":d,"Rating":r,"Voting":v}
        st.dataframe(data)
    if(selected_voting=='Drama'):
        m=[]
        d=[]
        r=[]
        v=[]
        i=0
        for dt in movie:
            if(genre[i]=='Drama'):
                m.append(dt)
                d.append(duration[i])
                r.append(rating[i])
                v.append(voting[i])
            i+=1
        data={"Movie":m,"Duration":d,"Rating":r,"Voting":v}
        st.dataframe(data)
    if(selected_voting=='Comedy'):
        m=[]
        d=[]
        r=[]
        v=[]
        i=0
        for dt in movie:
            if(genre[i]=='Comedy'):
                m.append(dt)
                d.append(duration[i])
                r.append(rating[i])
                v.append(voting[i])
            i+=1
        data={"Movie":m,"Duration":d,"Rating":r,"Voting":v}
        st.dataframe(data)
    if(selected_voting=='Romance'):
        m=[]
        d=[]
        r=[]
        v=[]
        i=0
        for dt in movie:
            if(genre[i]=='Romance'):
                m.append(dt)
                d.append(duration[i])
                r.append(rating[i])
                v.append(voting[i])
            i+=1
        data={"Movie":m,"Duration":d,"Rating":r,"Voting":v}
        st.dataframe(data)
    if(selected_voting=='Documentary'):
        m=[]
        d=[]
        r=[]
        v=[]
        i=0
        for dt in movie:
            if(genre[i]=='Documentary'):
                m.append(dt)
                d.append(duration[i])
                r.append(rating[i])
                v.append(voting[i])
            i+=1
        data={"Movie":m,"Duration":d,"Rating":r,"Voting":v}
        st.dataframe(data)
genre()
