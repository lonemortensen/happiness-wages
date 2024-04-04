# =======================================================================
# Project: Happiness and salary
# Description: Relationship between happiness and salary.
# The project uses Python's Pandas, Matplotlib, and Seaborn libraries. Data aggregation techniques are used to analyze the merged dataset. A bubbleplot of the merged dataset helps compare data and infer whether there’s a relationship between the annual salary and a country's happiness levels.
# Background: Coursework for Skillcrush's "Preparing & Displaying Data with Python" class.

# ==== *** ====Hap

# The main.py file contains code that:
# - reads data from csv files and stores data in Pandas dataframes.
# - merges two dataframes into a single dataframe for analysis.
# - groups the merged data based on the values in the "Country" column for
# further analysis and aggregation.
# - uses Seaborn to create a bubbleplot comparing annual salary and happiness.
# =======================================================================

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Standardizes currency to USD values so that we can better compare results
def format_currency(dataset):
  url = "https://api.exchangerate-api.com/v4/latest/USD"

  # Requests data from API
  response = requests.get(url)
  data = response.json()

  def convert_currency(row):
    rate = data["rates"][row["Unit Code"]]
    return row["Value"] / rate

  for index, row in dataset.iterrows():
    dataset.at[index, "Unit Code"] = "USD"
    dataset.at[index, "Value"] = convert_currency(row)
  return dataset


# Opens CSV file and retrieves data in the form of Pandas dataframes:
wage = pd.read_csv("wage.csv", delimiter=",")
happiness = pd.read_csv("happiness.csv", delimiter=",")

# Converts wage data into USD:
wage_usd = format_currency(wage)

# Merges wage and happiness dataframes:
wage_and_happiness = wage.merge(happiness)

### Groups and aggregates data in the merged dataset's Country column for analysis:

# Collects wage and happiness data in the merged dataframe's Country column:
wage_and_happiness_by_country = wage_and_happiness.groupby("Country")

# Calculates the mean wage (the "Value" series) and happiness score (the "Happiness score" series) per country:
wage_average_per_country = wage_and_happiness_by_country["Value"].mean()
happiness_average_per_country = wage_and_happiness_by_country[
  "Happiness score"].mean()

# Calculates the 10 countries with the largest and smallest average wages:
print(
  f"Countries with the largest average wages: {wage_average_per_country.nlargest(10)}"
)
print(
  f"Countries with the smallest average wages: {wage_average_per_country.nsmallest(10)}"
)

# Calculates the 10 countries with the largest and smallest average values for happiness:
print(
  f"Countries with the largest average happiness score: #{happiness_average_per_country.nlargest(10)}"
)
print(
  f"Countries with the smallest average happiness score: #{happiness_average_per_country.nsmallest(10)}"
)

### Creates bubbleplot:

# Create scatterplot with wage and happiness data:
fig = sns.scatterplot(x="Value",
                      y="Happiness score",
                      hue="Happiness score",
                      size="Happiness score",
                      sizes=(20, 180),
                      data=wage_and_happiness)

plt.title("Annual Salary and Happiness")
plt.xlabel("Annual Salary of Full-Time Workers (USD)")
plt.ylabel("Happiness Scores of All Citizens")
# Sets background color:
fig.set_facecolor("#E5E5E5")

plt.savefig("salary_and_happiness.png")
