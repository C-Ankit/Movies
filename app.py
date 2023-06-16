import pandas as pd
import requests
import streamlit as st
import pickle
import pandas
import requests



def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original/" + data['poster_path']


def recommend(movie):
    movie_index =movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    movies_new = [t[0] for t in movies_list]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_new:
        movie_id_n = movies.iloc[i].movie_id
        recommended_movies.append(movies.iloc[i].title)

        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id_n))
    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))


st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
'Enter a movie name that you liked',
movies['title'].values)
st.text("")

if st.button('Recommend'):
    st.text("")
    st.subheader("The Top Recommendations based on your previous experience are:")
    st.text("")
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.caption("Kaafi Mehnat lagi Deploy karne me")
