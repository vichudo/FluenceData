import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('Database fields - RecommendationMatrix.csv')

df.index = df['Unnamed: 0']
df = df.drop(columns ='Unnamed: 0')
df = df.fillna(0)


def Standarize(row):
  new_row = (row - row.mean())/(row.max() - row.min())
  return new_row

df_std = df.apply(Standarize)

#Calculating similarity row wise 
similarity = cosine_similarity(df_std.T)
similarity_df = pd.DataFrame(similarity, columns=df.columns, index = df.columns)



def get_similar_influencers(influencer,rating):
  similar_score = similarity_df[influencer]*(rating-2.5)
  similar_score = similar_score.sort_values(ascending = False)

  return similar_score

def collect_tastes():
  taste = []
  for i in range(3):
    value = input("Influencer name")
    score = input("score")

    taste.append(tuple([value,int(score)]))

  return taste

def recommend(store_likes):
    recommended_influencers = pd.DataFrame()

    for influencer,rating in store_likes:
        recommended_influencers = recommended_influencers.append(get_similar_influencers(influencer,rating),ignore_index = True)

    #return recommended_influencers.sum().sort_values(ascending = False)
    return pd.DataFrame(recommended_influencers.sum().sort_values(ascending = False).index.tolist(),columns=["Influencer Ranking"]).head(10)








