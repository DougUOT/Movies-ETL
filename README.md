# Movies-ETL
ETL (Extract, transform and load) is a essential process for a Data Analysis. In this project we will Create an ETL pipeline from raw data to a SQL database, extract data from disparate sources using Python and then clean and transform data using Pandas and load data with PostgreSQL.

A massive movie dataset called Movie Lens contains over 20 million ratings for 27,000 movies by 138,000 users.

## Overview of Project

Amazon Prime Video is a platform for streaming movies and TV shows on Amazing Prime, the world's largest retailer. The Amazing Prime video team would like to develop an algorithm to predict which low-budget films begin released will become popular so that they can buy the streaming rights at a bargain. The company decided to provide a clean data set of movie data, and we need to create the datasets. There are two data sources: a scrape of Wikipedia for all movies released since 1990 and rating data from the Movie Land's website. We will need to extract the data from the two sources, transform it into one clean data set, and finally load that data set into a SQL table. 

This assignment is related to the Bootcamp Data Analytics from the University of Toronto and comprises the goals below for this module: 

Follow below the goals for this module:

1) Objective 1: Write an ETL Function to Read Three Data Files
2) Objective 2: Extract and Transform the Wikipedia Data
3) Objective 3: Extract and Transform the Kaggle Data
4) Objective 4: Create the Movie Database

## Resources

* Data Files: [movies_metadata.csv](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/movies_metadata.csv) and [wikipedia.movies.json](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/wikipedia-movies.json)
* Data Output: Data Source: [ETL_function_test.ipynb](https://github.com/DougUOT/Movies-ETL/blob/main/ETL_function_test.ipynb), [ETL_clean_wiki_movies.ipynb](https://github.com/DougUOT/Movies-ETL/blob/main/ETL_clean_wiki_movies.ipynb), [ETL_clean_kaggle_data.ipynb] (https://github.com/DougUOT/Movies-ETL/blob/main/ETL_clean_kaggle_data.ipynb) and [ETL_create_database.ipynb](https://github.com/DougUOT/Movies-ETL/blob/main/ETL_create_database.ipynb)
* Software: Python 3.8.8, Anaconda 4.11.0, Jupyter Notebook 6.4.6, Pandas 1.3.4, Numpy 1.20.3, sqlalchemy 1.3.19, psycopg2 3.8.6, PgAdmin 4, version 5.7, PostgreSQL X64 11

## Results

### Objective 1: Write an ETL Function to Read Three Data Files

Using your knowledge of Python, Pandas, the ETL process, and code refactoring, write a function that reads in the three data files and creates three separate DataFrames.



