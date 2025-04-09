import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
def rating_visual():
    mydb = mysql.connector.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Title,Rating FROM finaldataset where rating>=7.0 and rating<=9.0")
    myresult = mycursor.fetchall()
    data1=pd.DataFrame(myresult)
    data1=data1.head(10) 
    title=[]
    rating=[]
    for v in data1[0]:
        title.append(v)
    for g in data1[1]:
        rating.append(g)
    data={"Title":title,"Rating":rating}
    st.title("Top 10 Movie Rating Visualization")
    st.subheader("TOP 10 Movie Data's by Rating ")
    st.table(data)
    st.subheader("Data Visualization for top 10 movies data's by rating")
    plt.figure(figsize=(8, 5)) 
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(title,rating, color='green', alpha=0.7)
    ax.set_xlabel('Movie Title', fontsize=14)
    ax.set_ylabel('Rating', fontsize=14)
    ax.set_title('Top 10 Rating', fontsize=16)
    plt.xticks(rotation=45, ha="right", fontsize=12)
    ax.grid(axis='y')
    st.pyplot(fig)
rating_visual()