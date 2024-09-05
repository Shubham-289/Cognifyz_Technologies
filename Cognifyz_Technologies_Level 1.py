#!/usr/bin/env python
# coding: utf-8

# # Level 1  

# ## Task: Top Cuisines

# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[12]:


df=pd.read_csv("Dataset .csv")
df.head()


# In[13]:


df.shape


# Task 1

# ### 1.1 Determine the top three most common cusines.

# In[16]:


print(df['Cuisines'])


# In[24]:


cuisine_count= df['Cuisines'].str.split(', ').explode('Cuisines').value_counts()
print(cuisine_count)
top_cuisine=cuisine_count.head(3)
print("The Top 3 Cuisines are : ",top_cuisine)


# In[25]:


colours = ['green', 'orange', 'red']
plt.bar(top_cuisine.index, top_cuisine.values, color=colours)
plt.xlabel('Cuisine')
plt.ylabel('Count')
plt.title('Top Three Cuisines')
plt.show()


# ### 1.2 Calculate the percentage of restaurants that serve each of the top cuisines.

# In[28]:


total_resturant = len(df)
print(total_resturant)
top_cuisine10=cuisine_count.head()
percentages = (top_cuisine / total_resturant) * 100
print("The Market Share of Top 5 Cuisines are :",percentages)


# In[38]:


print('percentage of resturant for top three cuisines')
percentages


# In[43]:


fig,ax=plt.subplots(figsize=(10,6))
ab=sns.barplot(x=percentages.index,y=percentages.values)
for bar in ab.containers[0]:
    height=bar.get_height()
    ab.annotate(f'{height:.2f})%',xy=(bar.get_x()+bar.get_width()/2,height),xytext=(0,3),textcoords='offset points',ha='center',va='bottom')
plt.title('percentage of resturant serving top 3 cuisines')              


# ## Task 2: City Analysis

# ## 2.1 Identify the city with the highest number of restaurants in the dataset

# In[44]:


print(df['City'].value_counts()[[0]].index[0])


# ### 2.2 Calculate the average rating for restaurants in each city.

# In[45]:


rating_by_each_city= df.groupby('City')['Aggregate rating'].mean()
print("The average of Rating of each city : ",rating_by_each_city)


# ### 2.3 Determine the city with the highest average rating.

# In[46]:


top_rated_city=rating_by_each_city.idxmax()
value=rating_by_each_city.max()
print("The city with Highest Avg. Rating is : ",top_rated_city,",","Rating -",value)


# ## Task 3: Price Range Distribution

# ### 3.1 Create A Histogram or Bar Chart To Visualize The Distribution Of Price Ranges Among The Restaurants.

# In[47]:


price_range=df['Price range'].value_counts()
h1=price_range.keys()
h2=price_range.values
h3=pd.DataFrame(zip(h1,h2),columns=['Price Range','Restaurants'])
h3


# In[48]:


plt.bar(price_range.index,price_range,color=['black','blue','red','orange'])
plt.title('Bar Plot')
plt.xlabel('Price Range')
plt.ylabel('Restaurants')
plt.show()


# In[49]:


plt.hist(df["Price range"],bins=40)
plt.show()


# ### 3.2 Calculate The Percentage Of Restaurants In Each Price Range Category.

# In[50]:


price_range= df['Price range'].value_counts()
cc=len(df['Price range'])
percentage_of_restarant=round(((price_range/cc)*100),2)
pd.DataFrame(percentage_of_restarant)


# ## Task 4: Online Delivery

# ### 4.1 Determine the percentage of restaurants that offer online delivery.

# In[51]:


df[df["Has Online delivery"]=="Yes"]["Restaurant Name"].value_counts()


# In[52]:


(df[df["Has Online delivery"]=="Yes"]["Restaurant Name"].value_counts()/len(df[df["Has Online delivery"]=="Yes"]))*100


# In[53]:


percentage2=(len(df[df["Has Online delivery"]=="Yes"])/len(df))*100
percentage2


# In[54]:


percentage2=(len(df[df["Has Online delivery"]=="No"])/len(df))*100
percentage2


# ### 4.2 Compare The Average Ratings Of Restaurants With and Without Online Delivery.

# In[55]:


aa=df[df['Has Online delivery']=='Yes']
bb=df[df['Has Online delivery']=='No']

dd = df.groupby('Has Online delivery')['Aggregate rating'].mean().round(2)
pd.DataFrame(dd)
plt.bar(dd.index,dd,color=['red','black'])
plt.xlabel('Restaurants with or without online delivery')
plt.ylabel('Average Ratings')
plt.show()

