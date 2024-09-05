#!/usr/bin/env python
# coding: utf-8

# ## Level 3

# ## Task 1: Restaurant Reviews

# In[20]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[21]:


df=pd.read_csv("Dataset .csv")
df.head()


# In[22]:


df.info()


# In[23]:


df.describe()


# In[26]:


df.shape


# ### 1.1 Analyze the text reviews to identify the most common positive and negative keywords.

# In[27]:


review_data = df["Rating text"].value_counts()
print(review_data)
plt.pie(review_data.values,labels =review_data.index,autopct ="%1.1f%%" )
plt.show()


# In[28]:


review_data


# ### 1.2  Calculate the average length of reviews and explore if there is a relationship between review length                     and rating.

# In[38]:


reviews = df["Rating text"]
print(reviews)
total_reviews = len(reviews)
print(total_reviews)
total_reviews_length = 0


# In[44]:


for review in reviews:
    total_reviews_length += len(review.split())
avg_review_length = total_reviews_length / total_reviews
print("average length of rating:",round(avg_review_length,2))


# In[40]:


review_len_vs_rating ={}

for rating in df["Aggregate rating"].unique():
    filttered_reviews = df.loc[df["Aggregate rating"] == rating]["Rating text"]
    total_length = 0
    total_reviews = len(filttered_reviews)
    
    for review in filttered_reviews:
        total_length += len(review.split())
        
        
    average_length = total_length / total_reviews
    review_len_vs_rating[rating] = average_length
        
print("review_len_vs_rating")
print(review_len_vs_rating)


# In[41]:


#creating the Dataframe 
review_len_vs_rating = pd.DataFrame({
    "ratings": list(review_len_vs_rating.keys()),
    "avg_review_len": list(review_len_vs_rating.values())
})


# In[42]:


review_len_vs_rating


# In[43]:


plt.figure(figsize =(20,6))
sns.barplot(x ="ratings",y = "avg_review_len",data = review_len_vs_rating )
plt.title("ratings vs avg review length")
plt.show()


# ## Task 2: Votes Analysis

# ### 2.1 Identify the restaurants with the highest and lowest number of votes.

# In[45]:


#groupby restaurant Name with votes
resturant_votes = df.groupby("Restaurant Name")["Votes"].sum()
resturant_votes.sort_values(ascending =False)


# In[46]:


#finding min and max of resturant name and  votes
high_votes = resturant_votes.max()
high_resname =  resturant_votes.idxmax()
lowest_votes = resturant_votes.min()
lowest_resname =  resturant_votes.idxmin()


# In[47]:


#creating new dataframe for above value
res = pd.DataFrame({"resturant":[high_resname,lowest_resname],"votes":[high_votes,lowest_votes]})
res


# In[48]:


print( "the",high_resname,"has the highest vote of : ",high_votes)
print( "the",lowest_resname,"has the lowest vote of :",lowest_votes)


# ### 2.2 Analyze if there is a correlation between the number of votes and the rating of a restaurant.

# In[49]:


#checking the correlation  between the  2 columns like Votes and Aggregate rating
corr_col = df[["Votes","Aggregate rating"]]
corr_matrix = corr_col.corr()
corr_matrix


# In[50]:


#Correlation display with heatmap 
sns.heatmap(corr_matrix,annot= True,cmap="coolwarm")
plt.show()


# ## Task 3: Price Range vs. Online Delivery and Table Booking

# ### 1.1 Analyze if there is a relationship between the price range and the availability of online delivery and table booking.

# In[51]:


price_onlined = df.groupby("Price range")["Has Online delivery"].value_counts(normalize = True).unstack().fillna(0)
price_table = df.groupby("Price range")["Has Table booking"].value_counts(normalize = True).unstack().fillna(0)


# In[52]:


price_onlined


# In[53]:


price_table


# In[54]:


print("relation between price range and Has Online delivery")
print()
print(price_onlined)


# In[55]:


print("relation between price range and has table booking")
print()
print(price_table)


# ### 1.2 Determine if higher-priced restaurants are more likely to offer these services.

# In[56]:


max_rang = df["Price range"].max()
high_price_restaurant = df[df["Price range"] == max_rang]


# In[57]:


res_offer_table = high_price_restaurant["Has Table booking"].value_counts()
print(res_offer_table)
plt.bar(res_offer_table.index,res_offer_table,color="blue")
plt.xlabel("Has Table booking")
plt.ylabel("Frequency")
plt.title("High priced Restaurant")
plt.show()


# In[58]:


res_offer_online = high_price_restaurant["Has Online delivery"].value_counts()
print(res_offer_online)
plt.bar(res_offer_online.index,res_offer_online,color = "green")
plt.xlabel("Has Online order")
plt.ylabel("Frequency")
plt.title("High priced Restaurant")
plt.show()

