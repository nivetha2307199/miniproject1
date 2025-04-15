import streamlit as st
import pandas as pd
import pymysql
def voting():
    mydb = pymysql.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    st.title("Voting")
    st.subheader("Filter voting based on their runtime")
    st.write("option1:50000")
    st.write("option2:50000-100000")
    st.write("option3:1000000-500000")
    st.write("option4:500000-1000000")
    st.write("option5:>1000000")
    options = ['Selection','<50000', '50000-100000', '100000-500000','500000-1000000','>1000000']
    selected_voting= st.selectbox("Choose your selection:", options)
    if(selected_voting=='<50000'):
        mycursor.execute("SELECT Title,Rating,Duration,Voting,Genre FROM finaldataset where Voting<=50000")
        myresult = mycursor.fetchall()
        data=pd.DataFrame(myresult,columns=['Movie','Rating','Duration','Voting','Genre'])
        st.dataframe(data)
    if(selected_voting=='50000-100000'):
        mycursor.execute("SELECT Title,Rating,Duration,Voting,Genre FROM finaldataset where Voting>50000 and Voting<=100000")
        myresult = mycursor.fetchall()
        data=pd.DataFrame(myresult,columns=['Movie','Rating','Duration','Voting','Genre'])
        st.dataframe(data)
    if(selected_voting=='100000-500000'):
        mycursor.execute("SELECT Title,Rating,Duration,Voting,Genre FROM finaldataset where Voting>100000 and Voting<=500000")
        myresult = mycursor.fetchall()
        data=pd.DataFrame(myresult,columns=['Movie','Rating','Duration','Voting','Genre'])
        st.dataframe(data)
    if(selected_voting=='500000-1000000'):
        mycursor.execute("SELECT Title,Rating,Duration,Voting,Genre FROM finaldataset where Voting>500000 and Voting<=1000000")
        myresult = mycursor.fetchall()
        data=pd.DataFrame(myresult,columns=['Movie','Rating','Duration','Voting','Genre'])
        st.dataframe(data)
    if(selected_voting=='>1000000'):
        mycursor.execute("SELECT Title,Rating,Duration,Voting,Genre FROM finaldataset where Voting>=1000000")
        myresult = mycursor.fetchall()
        data=pd.DataFrame(myresult,columns=['Movie','Rating','Duration','Voting','Genre'])
        if(data.empty):
            st.write("No Record Found")
voting()
