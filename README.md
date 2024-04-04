# Happiness and Wages Datasets: Merging and Visualizing Data
Merging, aggregating, and visualizing datasets with Python's Pandas, Matplotlib, and Seaborn libraries.

## About
This project uses Python's Pandas, Matplotlib, and Seaborn libraries to compare two datasets - the World Happiness Report data from the United Nations and the Average Annual Wage data from the Organisation for Economic Co-Operation and Development (OECD). The two datasets are combined to help infer whether there’s a relationship between wages and happiness.

The Pandas library is used to create dataframes to hold each dataset which are subsequently combined into a single dataframe. Data aggregation techniques are used to examine the data, and the Matplotlib and Seaborn libraries are used to create a bubbleplot to visualize the data.   

## Project Background
The project was built as part of the coursework for Skillcrush's "Preparing & Displaying Data with Python" class.

During this project, I practiced: 

- Reading CSV files and retrieving and storing the data in two Pandas dataframes. 

- Merging the two Pandas dataframes into one dataframe for analysis and visualization, using the merge() function.

- Grouping the merged dataframe into sets, using the groupby() function, and applying aggregation techniques, incl. the mean(), nlargest() and nsmallest() functions, on select series in the grouped data to determine whether there is a relationship between the data.     

- Using the Matplotlib and Seaborn libraries to create a bubbleplot with multi-colored, multi-sized bubbles based on the merged dataset.   

## Built With 
- Python
- Pandas
- Matplotlib
- Seaborn

## Launch
[See the project here.](https://replit.com/@lonemortensen/skillcrush-py-cl03-ls07-happy-bubblepl-pandas-seaborn-final#main.py)

## Acknowledgements

**Skillcrush** - I coded the project's main.py file with support and guidance from Skillcrush. 