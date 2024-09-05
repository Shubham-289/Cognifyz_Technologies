#!/usr/bin/env python
# coding: utf-8

# ## Level 2 

# ### Task1: Restaurant Ratings

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("Dataset .csv")
df.head()


# In[3]:


cat=df.select_dtypes(include=['object']).columns
num=df.select_dtypes(exclude=['object']).columns
print('cat:',cat)
print('num:',num)


# In[5]:


df['Cuisines']=df['Cuisines'].fillna(df['Cuisines'].mode()[0])
df.isnull().sum()


# ### 1.1: Analyze the distribution of aggregate ratings and determine the most common rating range.

# In[6]:


rating=df['Aggregate rating'].head()
rating


# In[7]:


plt.figure(figsize=(5,5))
plt.hist(rating,bins=5)
plt.xlabel("Rating Range")
plt.ylabel("Number of Restaurants")
plt.title("Distribution of Aggregate Rating Among The Restaurants")
plt.show()


# In[8]:


rr=pd.cut(df['Aggregate rating'],bins=[0,1,2,3,4,5], labels=['0-1','1-2','2-3','3-4','4-5'])
rr


# ### 1.2:  Calculate the average number of votes received by restaurants.

# In[10]:


Average_vote=round(df['Votes'].mean(),2)
print('The Average Vote Recived By Restaurants is :',Average_vote)


# ## Task 2: Cuisine Combination

# ### 2.1 Identify the most common combinations of cuisines in the dataset.

# In[11]:


df["Cuisines"].value_counts()


# In[12]:


df['Cuisines'].unique()


# In[14]:


import itertools

df['Cuisines'] = df['Cuisines'].astype(str)
df['Cuisines'] = df['Cuisines'].str.split(',')
unique_combinations = []
for i in df['Cuisines']:
    unique_combinations.extend(set(combo) 
                               for combo in itertools.combinations(i, 2))
combination_counts = pd.Series(unique_combinations).value_counts()
print(combination_counts.head())


# ### 2.2 Determine if certain cuisine combinations tend to have higher ratings.

# In[16]:


df=df.dropna(subset=['Cuisines','Aggregate rating'])
df.head()


# In[17]:


rat=df['Cuisines']
rat


# In[19]:


df['Cuisines']=df['Cuisines'].apply(lambda x:','.join(x) if isinstance(x,list)else x)
print(df['Cuisines'])


# In[20]:


average_rating=df.groupby('Cuisines')['Aggregate rating'].mean()
average_rating


# In[21]:


average_rating=average_rating.sort_values(ascending=False)
average_rating


# In[22]:


print('The Cuisines Combination That Have Higher Ratings:')
print(average_rating.head())


# ### Task 3: Geographic Analysis

# ### 3.1 Plot the locations of restaurants on a map using longitude and latitude coordinates.

# In[25]:


import plotly.express as px

fig = px.scatter_mapbox(df,
     lat='Latitude',
     lon='Longitude',
     hover_name='Restaurant Name',
     hover_data=['Cuisines'],
     color_discrete_sequence=['green'],
    zoom=10,)


# In[26]:


fig.update_layout(
    mapbox_style="open-street-map",
    margin={"r": 0, "t": 0, "l": 0, "b": 0}
)


# ### 3.2 Identify any patterns or clusters of restaurants in specific areas.

# In[27]:


import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

x = df[['Latitude', 'Longitude']]

num_clusters = 5

kmeans = KMeans(n_clusters=num_clusters,n_init=10, random_state=42)
df['Cluster'] = kmeans.fit_predict(x)

# Plottinf The Clusters

plt.scatter(df['Longitude'], df['Latitude'], c=df['Cluster'],cmap='rainbow')
plt.title('Restaurant Clusters')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()


# ### Task 4: Restaurant Chains

# ### 4.1 Identify if there are any restaurant chains present in the dataset.

# In[28]:


res_count=df['Restaurant Name'].value_counts()
potential_chains=res_count[res_count > 1].index
print("Potential restaurant chains:")
for chain in potential_chains:
    print(f"-{chain}")


# ### 4.2 Analyze the ratings and popularity of different restaurant chains.

# In[33]:


df=df[df['Aggregate rating'].notnull()]


# In[34]:


chain_stats=df.groupby('Restaurant Name').agg({
    'Aggregate rating':'mean',
    'Votes':'sum','Cuisines':'count'}).reset_index()


# In[35]:


chain_stats.columns=['Restaurant Name','Average ratings','Total Votes','Number of Location']


# In[36]:


chain_stats=chain_stats.sort_values(by='Total Votes',ascending=False)


# In[37]:


print("Restaurant Chain Rating and Popularity Analysis (Sorted by Total Votes):")
print(chain_stats.to_string(index=False,justify='center'))

