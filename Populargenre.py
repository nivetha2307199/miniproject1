import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
def voting():
    mydb = mysql.connector.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Genre,Voting FROM finaldataset")
    myresult = mycursor.fetchall()
    df=pd.DataFrame(myresult,columns=['genre','voting'])
    st.title("Total voting count of genre")
    genre_avg = df.groupby('genre')['voting'].sum().reset_index()
    st.dataframe(genre_avg)
    st.title("Pie Chart for Total voting count of each genre")
    fig = px.pie(df, names='genre', values='voting', title='Voting Count by Genre')
    st.plotly_chart(fig)
voting()