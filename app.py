import streamlit as st
import pickle
import requests

similarity = pickle.load(open('similarity.pkl','rb'))
moviedata = pickle.load(open('moviedata.pkl','rb'))
#print(type(moviedata))

def get_poster(id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=c96bd8d1109fb04c371d81a43408060d".format(id))
    posterpath=response.json()['poster_path']
    return "http://image.tmdb.org/t/p/w185"+posterpath

def get_details(id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=c96bd8d1109fb04c371d81a43408060d".format(id))
    d1 = response.json()['adult']
    if d1==False:
        d1='U'
    else:
        d1='A'
    d2 = response.json()['tagline']
    d3 = response.json()['release_date']
    d4 = response.json()['overview']
    return d1,d2,d3,d4

def Recommendation(movie):
    idx=moviedata[moviedata['title']==str(movie)].index[0]
    movie_list=sorted(list(enumerate(similarity[idx])),reverse=True,key=lambda x:x[1])[:7]
    recommended_movie=[]
    movie_poster=[]
    movietype=[]
    movieoverview=[]
    tagline=[]
    releasedate=[]
    for i in movie_list:
        recommended_movie.append(moviedata.iloc[i[0]].title)
        movie_poster.append(get_poster(moviedata.iloc[i[0]].id))
        movietype.append(get_details(moviedata.iloc[i[0]].id)[0])
        tagline.append(get_details(moviedata.iloc[i[0]].id)[1])
        releasedate.append(get_details(moviedata.iloc[i[0]].id)[2])
        movieoverview.append(get_details(moviedata.iloc[i[0]].id)[3])
    #print("poster",movie_poster)
    return recommended_movie,movie_poster,movietype,tagline,releasedate,movieoverview

mlst=list(moviedata['title'])
#print(mlst)

st.title('  Movie Recommendation System')

option = st.selectbox(
    'Select a movie name from dropdown',
    (mlst))

if st.button('Recommend'):
    name,poster,type,tag,date,overview = Recommendation(option)
    col1,col2,col3,col4,col5,col6,col7=st.columns(7)
    with col1:
        st.caption(name[0])
        st.image(poster[0])
        st.text('Movie Type :')
        st.caption(type[0])
        st.text('Movie Release Date :')
        st.caption(date[0])
        st.text('Movie Tagline :')
        st.caption(tag[0])
        st.text('Movie Overview :')
        st.caption(overview[0])


    with col2:
        st.caption(name[1])
        st.image(poster[1])
        st.text('Movie Type :')
        st.caption(type[1])
        st.text('Movie Release Date :')
        st.caption(date[1])
        st.text('Movie Tagline :')
        st.caption(tag[1])
        st.text('Movie Overview :')
        st.caption(overview[1])
    with col3:
        st.caption(name[2])
        st.image(poster[2])
        st.text('Movie Type :')
        st.caption(type[2])
        st.text('Movie Release Date :')
        st.caption(date[2])
        st.text('Movie Tagline :')
        st.caption(tag[2])
        st.text('Movie Overview :')
        st.caption(overview[2])
    with col4:
        st.caption(name[3])
        st.image(poster[3])
        st.text('Movie Type :')
        st.caption(type[3])
        st.text('Movie Release Date :')
        st.caption(date[3])
        st.text('Movie Tagline :')
        st.caption(tag[3])
        st.text('Movie Overview :')
        st.caption(overview[3])
    with col5:
        st.caption(name[4])
        st.image(poster[4])
        st.text('Movie Type :')
        st.caption(type[4])
        st.text('Movie Release Date :')
        st.caption(date[4])
        st.text('Movie Tagline :')
        st.caption(tag[4])
        st.text('Movie Overview :')
        st.caption(overview[4])
    with col6:
        st.caption(name[5])
        st.image(poster[5])
        st.text('Movie Type :')
        st.caption(type[5])
        st.text('Movie Release Date :')
        st.caption(date[5])
        st.text('Movie Tagline :')
        st.caption(tag[5])
        st.text('Movie Overview :')
        st.caption(overview[5])
    with col7:
        st.caption(name[6])
        st.image(poster[6])
        st.text('Movie Type :')
        st.caption(type[6])
        st.text('Movie Release Date :')
        st.caption(date[6])
        st.text('Movie Tagline :')
        st.caption(tag[6])
        st.text('Movie Overview :')
        st.caption(overview[6])