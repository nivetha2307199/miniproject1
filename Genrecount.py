import streamlit as st
import pandas as pd
import pymysql
def genre_visual():
    mydb = pymysql.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT COUNT(*)Title FROM finaldataset GROUP BY Genre")
    myresult = mycursor.fetchall()
    st.title("Genre Distribution")
    st.subheader("Count of the Movies for each Genre")
    data1=pd.DataFrame(myresult,index=["Action","Comedy","Drama","Romance","Documentary"],columns=['Count'])
    st.dataframe(data1)
    st.subheader("Ploting the movies count for each genre")
    st.bar_chart(data1)
genre_visual()
