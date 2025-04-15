import streamlit as st
import pandas as pd
import pymysql
import matplotlib.pyplot as plt
import seaborn as sns
def rating():
    mydb = pymysql.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Genre,Rating FROM finaldataset")
    myresult = mycursor.fetchall()
    df=pd.DataFrame(myresult,columns=['genre','rating'])
    st.title("Average of rating by genre")
    genre_avg = df.groupby('genre')['rating'].mean().reset_index()
    st.dataframe(genre_avg)
    st.title("Average Ratings Heatmap by Genre")
    heatmap_data = genre_avg.pivot_table(index='genre', values='rating')
    fig, ax = plt.subplots()
    sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", fmt=".2f", linewidths=.5, ax=ax)
    ax.set_title("Average Rating by Genre")
    st.pyplot(fig)
rating()
