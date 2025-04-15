import streamlit as st
import pandas as pd
import pymysql
def movie_visual():
    mydb = pymysql.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Title,Duration,Rating,Voting,Genre FROM finaldataset where rating>=7 and voting>=15000")
    myresult = mycursor.fetchall()
    data1=pd.DataFrame(myresult,columns=['Title', 'Duration','Rating','Voting','Genre'])
    result=data1.head(10) 
    st.title("IMDB 2024 MOVIE DATA")
    st.subheader("TOP 10 Movie Data's by Rating and Voting")
    st.dataframe(result)
movie_visual()
