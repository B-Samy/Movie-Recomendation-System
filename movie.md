THIS IS ME SHAHEER RANGREJ : 
I BUILD THIS AI MOVIE RECOMMENDATION USING PYTHON , DATASCIENCE , MACHINE LEARNING AND NLP 



TMDB Dataset
      ↓
EDA
      ↓
Merge datasets
      ↓
Select useful columns
      ↓
AST preprocessing
      ↓
Extract genres / keywords / cast / director
      ↓
Create tags
      ↓
Text preprocessing
      ↓
Stemming
      ↓
CountVectorizer
      ↓
Movie vectors
      ↓
Cosine Similarity
      ↓
Top 5 similar movies
      ↓
TMDB API → Posters
      ↓
Streamlit App




User selects a movie → system analyzes its content → converts it into numerical vectors → calculates similarity → returns the 5 most similar movies.

# 🎬 CineMind — AI Movie Recommendation System

**Built by Shaheer Rangrej**

CineMind is an **AI-powered movie recommendation system** built using Python, Machine Learning, NLP, and Streamlit.

The user selects or searches for a movie they like, and the system recommends **5 similar movies** based on the movie's:

* 🎭 Genres
* 🔑 Keywords
* 🎬 Cast
* 👨‍💼 Director
* 📝 Movie Overview

### ⚙️ How It Works

```text
User selects a movie
        ↓
Movie features are extracted
        ↓
NLP preprocessing
        ↓
CountVectorizer
        ↓
Cosine Similarity
        ↓
Top 5 similar movies
        ↓
TMDB API → Movie Posters
```

### 🛠️ Technologies

* Python
* Pandas
* Scikit-learn
* NLTK
* Streamlit
* TMDB API
* Pickle

### 📊 Dataset

The project uses the **TMDB 5000 Movies** and **TMDB 5000 Credits** datasets.

### 🚀 Result

Select a movie you like and CineMind finds movies with similar characteristics using **content-based recommendation**.

> 🎬 **Discover your next favorite movie with AI.**



FOR THIS PROJECT I TOOK 2 DATA SETS FROM TMDB :
WHICH IS

TMDB_5000_CREDITS 
TMDB_5000_MOVIES

FOR THE PYTHON LIBRARY I USED MANY SUCH AS : 


import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

from sklearn.preprocessing import StandardScaler , LabelEncoder , OneHotEncoder , MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score , classification_report , precision_score , f1_score , mean_absolute_error , mean_squared_error , root_mean_squared_error
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer


PANDAS FOR DATA EDA PREPROCESSING 

MATPLOTLIB FOR GRAPHS 

SEABORN FOR GRAPH VISUALIZATIONS 

SKLEARN PREPROCESSING FOR CONVERTING TEXT INTO NUMBER LIKE STANDARD SCALER , LABELENCODER , ONEHOTENCODER , MINMAXSCALER

SKLERAN MODEL SELECTION FOR MACHINE LEARNING DATA TESTING AND TRAINING 80% FOR TRAINING THE DATA AND 20% TESTING THE DATA TO CHECK THE ACCURACY

SKLEARN METRICS FOR ACCURACY OF THE MODEL , REPORTS LIKE F1 SCORE , RECALL SCORE , METRICS ETC 

FEATURES EXTRACTION WHICH IS IMPORTANT , COUNTERVECTORIZER WHICH IS USED IN NLP , LIKE NLP USED TO DO PREPROCESSING AND MACHINE DOESNT UNDERSTAND TEXT SO AFTER I DID NLP THEN I USE COUNTERVECTORIZER TO CONVERT THOSE TEXT N PASS TO MACHINE LEARNING MODEL 




STRUCTURE : 

IMPORTED DATASET : 

credits_df = pd.read_csv('tmdb_5000_credits.csv')
movies_df = pd.read_csv('tmdb_5000_movies.csv')

PERFORM EDA :

LIKE CHECK HEAD
CHECK NULL VALUES (IF HAVE THEN DROP THE NULL VALUES )
CHECK DUPLICATED VALUES 
COLUMNS


NOW I MERGE THE DATA SET IN TERMS OF TITLE CUZ BOTH HAVE TITLE N OTHER COLUMSN AS WELL IN ANOTHER DATASET WHICH IS LEAST USEFUL

movies = movies_df.merge(credits_df , on='title')



NOW I HAVE TONS OF COLUMNS LIKE  : 

Index(['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language',
       'original_title', 'overview', 'popularity', 'production_companies',
       'production_countries', 'release_date', 'revenue', 'runtime',
       'spoken_languages', 'status', 'tagline', 'title', 'vote_average',
       'vote_count', 'movie_id', 'cast', 'crew'],
      dtype='str')


SO I CHOOSE ONLY USE FULL COLUMN FOR RECOMMNEDATION FOR MOVIE , LIKE :

ID ,
TITLE ,
OVERVIEW ,
GENRES,
KEYWORDS ,
CAST ,
CREW

movies =  movies[['id' , 'title' , 'overview' ,  'genres' , 'keywords'  , 'cast' , 'crew']]



I CHECKED AGAIN NULL VALUES N GOT IT :
SO TIME TO DROP :
movies.dropna(inplace=True)



NOW MAIN PREPROCESSING I USE AST 
import ast (ast.literal_eval() in Python is used to safely convert a string containing a Python literal into its actual Python data type.)


import ast

data = "['Avatar', 'Titanic', 'Inception']"

result = ast.literal_eval(data)

print(result)
print(type(result))

['Avatar', 'Titanic', 'Inception']




FIRST FUNCTION TO GET :
 
SUPPOSE OBJ CONTAIN :
"[{'id': 28, 'name': 'Action'}, {'id': 35, 'name': 'Comedy'}]"


ITS A DICTIONARY AND I WANT NAME : ACTION 
SO USING THIS CODE I WOULD GET ACTION , COMEDY ETC 

def convert(obj):
    L = []

    for name in ast.literal_eval(obj):
        L.append(name['name'])
    return L



I APPLIED THIS ON GENRES , KEYWORDS 

LET YOU KNOW , HOW I APPLIED : 
movies['genres'] = movies['genres'].apply(convert)
movie['keywords'] = move['keywords'].apply(convert)

FIRST IS LIKE THIS : 

[{"id": 28, "name": "Action"}, {"id": 12, "nam...	[{"id": 1463, "name": "culture clash"}, {"id":...

EXAMPLE I GOT THIS : 
GENRES: [Action, Adventure, Fantasy, Science Fiction]
KEYWORDS : [culture clash, future, space war, space colon]

SECOND FUNCTION : 

IMAGINE CONVERT CAST I MEAN GET THEIR NAME WHICH IS != 3 
movies['cast']
[Sam Worthington, Zoe Saldana, Sigourney Weave]



def convertCast(obj):
    L=[]
    counter=0
    for name in ast.literal_eval(obj):
        if counter !=3:
            L.append(name['name'])
    return L



FUNCTION 3 :

ITS FOR CREW AND INPUT IS 
([{"credit_id": "52fe48009251416c750aca23", "department": "Editing", "gender": 0, "id": 1721, "job": "Editor", "name": "Stephen E. Rivkin"},)


AFTER USING THIS FUNCTION IF JOB == DIRECTOR THEN GIVE ME THOSE NAME , BASICALLY THERE ARE MULTIPLE JOB LIKE EDITOR ETC BUT I WANT DIRECTOR NAMES ONLY ....



def fetchIt(obj):
    L=[]

    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])

    return L

I APPLIED 
movies['crew'] = movies['crew'].apply(fetchIt)


N GOT THIS : OUTPUT : [James Cameron]


NOW MAYBE NLP : FOR PREPROCESSING 

movies['overview'] = movies['overview'].apply(lambda x:x.split())

BASICALLY I HAVE INPUT LIKE : 

['THIS PROJECT MADE BY SHAHEER']

AFTER USING THIS WILL SPLIT THE TEXT INTO WORDS 

LIKE OUTPUT WILL BE : ['THIS' 'PROJECT' 'MADE' 'BY' 'SHAHEER']






MAIN FUNCTION WHIC IS NOT MAIN :

movies['genres'] = movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast'] = movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew'] = movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])

THERE ARE IN LIST LIKE NAMES ARE [SHAHEER RANGREJ]
BUT I WANT TO REPLACE THOSE SPACES WITH LIKE [SHAHEERRANGREJ]


NOW IMPORTANT PREPROCESSING IS THIS : 
IN I CREATED TAGS COLUMN N ADD THOSE IMPORTANT COLUMNS WHICH IS KINDA FEATURE ENGINEERING 

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']


NOW WHEN I CALL MOVIE['TAGS']

NOW I CREATED NEW DATAFRAME :
new_df = movies[['id' , 'title' , 'tags']]

<!-- id	title	tags
0	19995	Avatar	[In, the, 22nd, century,, a, paraplegic, Marin...
1	285	Pirates of the Caribbean: At World's End	[Captain, Barbossa,, long, believed, to, be, d...
2	206647	Spectre	[A, cryptic, message, from, Bond’s, past, send... -->


WHAT I DID BELOW IS :

IN TAGS COLUMNS I USED TO ADD ALL THOSE COLUMNS LIKE OVERVIEW , GENERES TILL CREW USING " ".JOIN(X)

new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))


NOW I DID TEXT LOWER WHICH IS PART OF NLP PREPROCESSING :
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())


I USED NLTK LIBRARY 
IMPORT NLTK
from nltk.stem import PorterStemmer


CALL THE OBJECT 
ps = PorterStemmer()



THIS FUNCTION WHAT DO : LIKE IT WILL APPLY STEMMING ON MY THOSE TAGS COLUMNS LIKE STEMMING REMOVE UNNECESSARY WORDS WHICH IS USEFUL CHATBOT TO UNDERSTAND THOSE TEXXT 



def stem(text):
    y = []

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)


EXAMPLE OUTPUT :
in the 22nd century, a parapleg marin is dispa...
1       captain barbossa, long believ to be dead, ha c...
2       a cryptic messag from bond’ past send him on a...
3       follow the death of district attorney harvey d...
4       john carter is a war-weary, former militari ca...




MAIN THING : VECTORIZER 

DID U SAW ABOVE THAT THOSE TEXT ...
I MEAN HOW CAN MACHINE UNDERSTAND THOSE TEXT 

GUESS HOW ? 

SO WE HAVE TO CONVERT TO VECTOR SO MACHINE CAN UNDERSTAND 

cv = CountVectorizer(max_features=500 , stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()


THATS WHY COUNVECTORIZER IS USEFULL : 
vectors[0]

<!-- array([1, 0, 1, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
       0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, -->


cv.get_feature_names_out()
array(['3d', 'accident', 'action', 'adventur', 'aftercreditssting', 'age',
       'agent', 'alcohol', 'alien', 'alway', 'america', 'american',






NOW COSINE SIMILARITY : 
Cosine similarity measures how similar two movies are based on their feature vectors.


In your movie recommendation system, it is used to answer:

"How similar is this movie to every other movie?"


simalirity[1]
GIVES ME VECTOR NOT MOVIE NAME ,  IMEAN IT WILL GIVE MOVIE NAME BUT AFTER PREPROCESSING :

array([0.17320508, 1.        , 0.11846978, ..., 0.04714045, 0.        ,
       0.05923489], shape=(4806,))




def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = simalirity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    for i in movie_list:
        print(new_df.iloc[i[0]].title)


NOW CONVERT MOVIE TITLE == MOVIE GIVES ME SIMILAR MOVIES 
IF I CALL FUCNTION 

recommend('superman)

GIVES ME : 

Iron Man 2
Ant-Man
X-Men: Apocalypse
The Wolverine
Spider-Man 2





DONE : 


BTW STREAMLIT NOW WE HVE TO USE THOSE FEATURE LIKE STANDARDSCALER , SIMILARITY ETC MANY MORE , SO WE HAVE TO DUMP USING PICKLE N LOAD INTO STREAMLIT L


LOOKS HOW ITS DONE : 
import pickle

pickle.dump(new_df.to_dict(),open('movie_dict.pkl','wb'))


pickle.dump(simalirity , open('simalirity.pkl' , 'wb'))


NOW I USED IN STREAMLIT THOSE TMDB API KEY , THEN ALL UI DONE BY ME AND AI 



This README is also my personal documentation, so I can return to the project later and understand what I did, why I did it, and how each step connects to the final recommendation system.

Built with Python, Machine Learning, NLP & Streamlit.
— Shaheer Rangrej