#!/usr/bin/env python
# coding: utf-8

# In[7]:


import json
import pandas as pd
import numpy as np

import re

from sqlalchemy import create_engine
import psycopg2

# from config import db_password

import time

# 1. Create a function that takes in three arguments;
# Wikipedia data, Kaggle metadata, and MovieLens rating data (from Kaggle)


def three_arguments_func(wiki_file, kaggle_file, ratings_file):
    # 2. Read in the kaggle metadata and MovieLens ratings CSV files as Pandas DataFrames.
    kaggle_metadata = pd.read_csv(f'{file_dir}movies_metadata.csv', low_memory=False)
    ratings = pd.read_csv(f'{file_dir}ratings.csv') 
    
    # 3. open the Wikipedia JSON file and use the json.load() function to convert the JSON data to raw data.
    f'{file_dir}wikipedia-movies.json'

    with open(f'{file_dir}wikipedia-movies.json', mode='r') as file:
        wiki_movies_raw = json.load(file)
                          
    # 4. Read in the raw wiki movie data as a Pandas DataFrame.
        wiki_movies_df = pd.DataFrame(wiki_movies_raw)
                          
                          
    # 5. Return the three DataFrames
    return wiki_movies_df, kaggle_metadata, ratings

# 6 Creating the path to your file directory and variables for the three files. 
file_dir = 'C:/Users/dougl/OneDrive/Documents/UOT Data Analytics Bootcamp/MODULES_STUDY CLASS/8_Module_ETL Extract Transform and Load/Movies-ETL/'
# Wikipedia data
wiki_file = f'{file_dir}/wikipedia.movies.json'
# Kaggle metadata
kaggle_file = f'{file_dir}/movies_metadata.csv'
# MovieLens rating data.
ratings_file = f'{file_dir}/ratings.csv'

# 7. Set the three variables in Step 6 equal to the function created in Step 1.
wiki_file, kaggle_file, ratings_file = three_arguments_func(wiki_file, kaggle_file, ratings_file)


# In[8]:


# 8. Set the DataFrames from the return statement equal to the file names in Step 6. 
# In this step, you are reassigning the variables created in Step 6 to the variables in the return statement.
wiki_movies_df = wiki_file
kaggle_metadata = kaggle_file
ratings = ratings_file


# In[9]:


# 9. Check the wiki_movies_df DataFrame.
wiki_movies_df.head()


# In[10]:


# 10. Check the kaggle_metadata DataFrame.
kaggle_metadata.head()


# In[11]:


# 11. Check the ratings DataFrame.
ratings.head()


# In[ ]:




