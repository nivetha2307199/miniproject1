import streamlit as st
from Main import main# type: ignore
from Moviebar import movie_visual # type: ignore
from Duration import duration_visual # type: ignore
from Genrecount import genre_visual # type: ignore
from Votinggenre import voting_visual # type: ignore
from Rating import rating_visual # type: ignore
from MaxMin import maxmin# type: ignore
from Ratinggenre import rating# type: ignore
from Populargenre import voting# type: ignore
from Analysis import rating #type:ignore
from DurationF import duration # type: ignore
from RatingF import rating #type:ignore
from VotingF import voting # type: ignore
from GenreF import genre #type:ignore
pages = {
    "🏠Home":
    [st.Page("Main.py",title="🗒️Main")],
    " 📊Main Category": 
    [
        st.Page("MovieBar.py", title="🗒️Top 10 Movies by Rating and voting"),
        st.Page("Duration.py", title="🗒️Average Duration by Genre"),
        st.Page("Genrecount.py",title="🗒️Genre Distribution"),
        st.Page("Votinggenre.py",title="🗒️Voting Trends by Genre"),
        st.Page("Rating.py",title="🗒️Rating Distribution"),
        st.Page("MaxMin.py",title="🗒️Duration Extremes"),
        st.Page("Ratinggenre.py",title="🗒️Rating by genre"),
        st.Page("Populargenre.py",title="🗒️Most Popular Genre by Voting"),
        st.Page("Analysis.py",title="🗒️Correlation Analysis")
    ],
    "🗂️Filtering":[st.Page("DurationF.py",title="🗒️Duration"),
                 st.Page("RatingF.py",title="🗒️Rating"),
                 st.Page("VotingF.py",title="🗒️Voting"),
                 st.Page("GenreF.py",title="🗒️Genre")]}
pg = st.navigation(pages)
pg.run()