# Diabetes Data Cleaning and Exploratory Analysis

**Author: Maevah Miot**  
**Tools: Python, Pandas, NumPy, Matplotlib, and Scikit-learn**

## Project Overview

In this project, I used Python to clean and explore a dataset containing information about hospital encounters for patients with diabetes. The dataset included hospital admissions, diagnoses, length of stay, laboratory procedures, and medications administered during encounters.

The goal was to prepare the data for future statistical analysis and predictive modeling, including length-of-stay prediction and readmission analysis. I also created visualizations to explore A1C results by race, the gender distribution of readmitted encounters, and hospital length of stay.

This project focuses on data cleaning, descriptive statistics, and exploratory visualization. Predictive models are not included in this script.

## Data Cleaning Process

### 1. Inspecting the Dataset

I loaded the dataset and reviewed its dimensions, column names, first five rows, and missing values.

The initial dataset contained **10,000 rows and 24 columns**.

### 2. Handling Missing Values

My analysis identified substantial missing information in two columns:

- **weight:** 96.75% missing
- **max_glu_serum:** 94.74% missing

I removed these columns because they contained insufficient information for meaningful analysis, as required by the assignment. This reduced the dataset from **10,000 rows and 24 columns** to **10,000 rows and 22 columns**.

Although **A1Cresult had 83.31% missing values**, I retained it because subsequent assignment tasks required A1C coding and analysis.

I then removed encounters with missing values in the other retained columns. The dataset decreased from **10,000 to 9,172 encounters**, removing **828 encounters**, or **8.28%** of the original dataset.

### 3. Normalizing Numerical Variables

I applied min-max normalization to:

- num_lab_procedures
- num_medications
- num_procedures

This places variables with different numerical ranges on the same **0–1 scale**. The smallest value becomes 0, and the largest becomes 1.

### 4. Encoding A1C Categories

I converted the recorded A1Cresult categories into binary dummy variables:

- **1:** The encounter belongs to that category.
- **0:** The encounter does not belong to that category.

Missing A1C values remain missing in the original column and receive zeros across the dummy columns. These zeros should not be interpreted as a normal A1C result.

## Descriptive Analysis

I calculated counts and percentages for age, gender, and race, along with summary statistics and medians for length of stay and previous inpatient visits.

```python
# Descriptive analytics
print("\nAGE")
print(dataset["age"].value_counts())
print(dataset["age"].value_counts(normalize=True) * 100)

print("\nGENDER")
print(dataset["gender"].value_counts())
print(dataset["gender"].value_counts(normalize=True) * 100)

print("\nRACE")
print(dataset["race"].value_counts())
print(dataset["race"].value_counts(normalize=True) * 100)

print("\nLENGTH OF STAY")
print(dataset["length-of-stay"].describe())
print("Median:", dataset["length-of-stay"].median())

print("\nNUMBER INPATIENT")
print(dataset["number_inpatient"].describe())
print("Median:", dataset["number_inpatient"].median())
```

## Visualizations

### A1C Results Greater Than 8 by Race

I created a bar chart showing the number of encounters with an A1Cresult category of `>8`, grouped by race.

This chart compares counts, rather than the percentage of encounters with high A1C within each racial group.

### Gender Distribution of Readmitted Encounters

I grouped readmission categories into “Readmitted” and “Not Readmitted,” selected the readmitted encounters, and calculated their gender distribution.

The pie chart shows each gender’s share of readmitted encounters. It does not measure the readmission rate within each gender.

### Distribution of Hospital Length of Stay

I created a histogram showing the distribution of hospital length of stay in days. This helps visualize common stay durations and the overall spread of the data.

## How to Run

1. Download the Python script.
2. Place `Cleaned_Diabetes_Data.csv` in the same folder.
3. Ensure the script uses:

   ```python
   file_path = "Cleaned_Diabetes_Data.csv"
   ```

4. Install the required libraries:

   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```

5. Run the script:

   ```bash
   python Assignment1_Cleaneddataset.py
   ```

The script prints descriptive statistics and displays three charts. It does not currently export the processed dataset to a new CSV file.

## Data Source

The dataset was provided for my HIM6682 Quality and Outcome Analytics coursework.

The original dataset citation and any redistribution terms should be confirmed before publicly sharing the CSV.

## Limitations

- Removing incomplete encounters may affect how representative the remaining data is.
- A1C results are missing for a large portion of the dataset.
- Encounter counts should not automatically be interpreted as counts of unique patients.
- The charts describe the dataset; they do not establish causes or clinical conclusions.

## Conclusion

This project strengthened my experience in cleaning healthcare data, handling missing values, normalizing numerical variables, encoding categorical information, and creating visualizations.

The cleaning process improved the dataset’s usability for exploratory analysis and future modeling. Additional preparation would be needed for predictive modeling, including splitting the data before fitting normalization to avoid data leakage.
