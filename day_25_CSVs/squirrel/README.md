# Squirrel Census Data Analysis

## Overview
This Python script analyzes data from the **2018 Central Park Squirrel Census** to count the number of squirrels with different fur colors and saves the results to a new CSV file. The program is a simple demonstration of using the `pandas` library for data manipulation and analysis.

---

## Features
- Reads squirrel census data from a CSV file.
- Filters and counts squirrels based on their fur colors: **Gray**, **Cinnamon**, and **Black**.
- Outputs the counts to the console.
- Creates a new CSV file summarizing the fur color counts.

---

## Code Explanation

### Reading the Data
```python
import pandas

data = pandas.read_csv("./day_25_CSVs/squirrel/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
