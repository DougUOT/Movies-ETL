# Movies-ETL
ETL (Extract, transform and load) is a essential process for a Data Analysis. In this project we will Create an ETL pipeline from raw data to a SQL database, extract data from disparate sources using Python and then clean and transform data using Pandas and load data with PostgreSQL.

A massive movie dataset called Movie Lens contains over 20 million ratings for 27,000 movies by 138,000 users.

## Overview of Project

Amazin Prime Video is a platform for streaming movies and TV shows on Amazing Prime, the world's largest retailer. The Amazing Prime video team would like to develop an algorithm to predict which low-budget films begin released will become popular so that they can buy the streaming rights at a bargain. The company decided to provide a clean data set of movie data, and we need to create the datasets. There are two data sources: a scrape of Wikipedia for all movies released since 1990 and rating data from the Movie Land's website. We will need to extract the data from the two sources, transform it into one clean data set, and finally load that data set into a SQL table. 
 

Follow below the goals for this project:

1) Objective 1: Write an ETL Function to Read Three Data Files
2) Objective 2: Extract and Transform the Wikipedia Data
3) Objective 3: Extract and Transform the Kaggle Data
4) Objective 4: Create the Movie Database

## Resources

* Data Files: [movies_metadata.csv](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/movies_metadata.csv) and [wikipedia.movies.json](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/wikipedia-movies.json)
* Data Output: Data Source: [ETL_function_test.ipynb](https://github.com/DougUOT/Movies-ETL/blob/main/ETL_function_test.ipynb), [ETL_clean_wiki_movies.ipynb](https://github.com/DougUOT/Movies-ETL/blob/main/ETL_clean_wiki_movies.ipynb), [ETL_clean_kaggle_data.ipynb](https://github.com/DougUOT/Movies-ETL/blob/main/ETL_clean_kaggle_data.ipynb) and [ETL_create_database.ipynb](https://github.com/DougUOT/Movies-ETL/blob/main/ETL_create_database.ipynb)
* Software: Python 3.8.8, Anaconda 4.11.0, Jupyter Notebook 6.4.6, Pandas 1.3.4, Numpy 1.20.3, sqlalchemy 1.3.19, psycopg2 3.8.6, PgAdmin 4, version 5.7, PostgreSQL X64 11

## Results

### Objective 1: Write an ETL Function to Read Three Data Files

Using your knowledge of Python, Pandas, the ETL process, and code refactoring, write a function that reads in the three data files and creates three separate DataFrames. The complete code is available on the file  [ETL_function_test.ipynb](https://github.com/DougUOT/Movies-ETL/blob/main/ETL_function_test.ipynb)

Read in the Kaggle metadata and MovieLens ratings CSV files as Pandas DataFrames:

![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del1_img_.PNG)

Open the Wikipedia JSON file and use the json.load() function to convert the JSON data to raw data:

![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del1_img1_.PNG)

Read in the raw Wikipedia movie data as a Pandas DataFrame:

![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del1_img2_.PNG)

Use the variables provided to create a path to the Wikipedia data, the Kaggle metadata, and the MovieLens rating data files:

![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del1_img3_.PNG)

Set the three variables (Dataframe):

![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del1_img4_.PNG)

wiki_movies DataFrame (First Data File):

![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del1_img5_.PNG)

kaggle_metadata (Second Data File):

![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del1_img6_.PNG)

ratings (Third Data File):

![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del1_img7_.PNG)

### Objective 2: Extract and Transform the Wikipedia Data

Using the knowledge of Python, Pandas, the ETL process, and code refactoring, extract and transform the Wikipedia data so we can merge it with the Kaggle metadata. While extracting the IMDb IDs using a regular expression string and dropping duplicates, use a try-except block to catch errors.

This deliverable consists of creating the clean movie function, cleaning the box office data, budget data, the release date, and the running time. Also, removing duplicates with regular expressions, columns with null values and Drop null values and converting data to string values.

Follow below of part of the code related to using the try-except blocks to catch errors. The complete code is available on the file [ETL_clean_wiki_movies.ipynb](https://github.com/DougUOT/Movies-ETL/blob/main/ETL_clean_wiki_movies.ipynb)

![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del2_img1_.PNG)
![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del2_img2_.PNG)

### Objective 3: Extract and Transform the Kaggle Data

Using your knowledge of Python, Pandas, the ETL process, and code refactoring, extract and transform the Kaggle metadata and MovieLens rating data, then convert the transformed data into separate DataFrames. Then, you’ll merge the Kaggle metadata DataFrame with the Wikipedia movies DataFrame to create the movies_df DataFrame. Finally, you’ll merge the MovieLens rating data DataFrame with the movies_df DataFrame to create the movies_with_ratings_df.

This deliverable consists of cleaning the budget data, the release date, running time and cleaning the Kaggle data. Merge Wikipedia and Kaggle DataFrames, also transform and merge the rating data.

Follow below of part of the code related to transforming and merging the rating DataFrame with the movies_df DataFrame, name the new DataFrame movies_with_ratings_df, and cleaning the movies_with_ratings_df DataFrame. The complete code is available on the file [ETL_clean_kaggle_data.ipynb](https://github.com/DougUOT/Movies-ETL/blob/main/ETL_clean_kaggle_data.ipynb)

![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del3_img1_.PNG)

### Objective 4: Create the Movie Database

Use the knowledge of Python, Pandas, the ETL process, code refactoring, and PostgreSQL to add the movies_df DataFrame and MovieLens rating CSV data to a SQL database.

The last deliverable consists of creating and connecting to the database, then importing data.

Follow below of part of the code related to adding the code to create the connection to the PostgreSQL database, then add the movies_df DataFrame to a SQL database. The complete code is available on the file [ETL_create_database.ipynb](https://github.com/DougUOT/Movies-ETL/blob/main/ETL_create_database.ipynb)

![](https://github.com/DougUOT/Movies-ETL/blob/main/Resources/ETL_Del4_img1_.PNG)

### Others consideration related to the process ETL (Extract, Transform and Load) 
  
According to the University of Toronto, the Data pipeline process, known as Extract, transform and load, is the workhorse for moving data between information bases. For instance, a few organizations, for example, Google and Amazon, are continually moving information around to various areas to improve performance. Still, according to the UOT, the ETL is a central idea in information designing, guaranteeing that information is steady and keeps up with its trustworthiness; also, An all-around planned ETL pipeline endeavours to robotize as much data wrangling as it can. The last, still according to the UOT, The ETL cycle can likewise make information stores that perform more effectively, lessening the time it takes to run analysis. 

We utilized Python and Pandas to play out our data wrangling and PostgresSQL to store our completed information for this task.
  
## Recommendations for future Analysis

To further improve this project, in the future, as a suggestion, other analyzes could be developed, comparing the ratings of different countries to understand the regional preferences for films. This information may be valuable for stakeholders and Amazing Prime Video to focus on buying future movie releases according to local priorities. 








