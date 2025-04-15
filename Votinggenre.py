import streamlit as st
import pandas as pd
import pymysql
def voting_visual():
    mydb = pymysql.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Rating,Genre FROM finaldataset")
    myresult = mycursor.fetchall()
    dataset=pd.DataFrame(myresult)
    rating=[]
    genre=[]
    for v in dataset[0]:
        rating.append(v)
    for g in dataset[1]:
        genre.append(g)
    data={"Rating":rating,"Genre":genre}
    df=pd.DataFrame(data)
    st.title("Average values of rating for Each genre")
    avg_ratings = df.groupby('Genre')['Rating'].mean()
    st.dataframe(avg_ratings)
    st.title("Bar char for rating Average values for Each genre")
    st.line_chart(avg_ratings)
voting_visual()
