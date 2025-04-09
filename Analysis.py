import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns
def rating():
    mydb = mysql.connector.connect(host="localhost",user="root", password="root@2024",database='imdbmoviedata')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT Voting,Rating FROM finaldataset")
    myresult = mycursor.fetchall()
    df=pd.DataFrame(myresult,columns=['voting','rating'])
    st.title("Correlation Analysis: Voting vs Rating")
    df=df.head(20)
    st.dataframe(df)
    correlation = df[['voting', 'rating']].corr()
    st.subheader("Correlation Matrix")
    st.dataframe(correlation)
    st.subheader("Voting vs Rating Scatter Plot")
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df, x='voting', y='rating', ax=ax2)
    ax2.set_title('Voting vs Rating')
    st.pyplot(fig2)
rating()