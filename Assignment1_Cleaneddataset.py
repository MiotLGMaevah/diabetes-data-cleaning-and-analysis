#assignment1


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score



file_path = "Cleaned_Diabetes_Data.csv"

dataset = pd.read_csv(file_path)

print("\nDataset loaded successfully!")

print("\nDataset shape:")
print(dataset.shape)

print("\nColumn names:")
print(dataset.columns.tolist())

print("\nFirst 5 rows:")
print(dataset.head())



missing_values = dataset.isnull().sum()
print(missing_values)

missing_percent = (dataset.isnull().sum()/len(dataset)) * 100
print(missing_percent.sort_values(ascending=False))

missing_only = missing_percent[missing_percent > 0]
print(missing_only.sort_values(ascending=False))


dataset = dataset.drop(columns=["weight", "max_glu_serum"])
print(dataset.shape)


print(dataset["A1Cresult"].value_counts(dropna=False))

columns_to_check = dataset.columns.drop("A1Cresult")
dataset = dataset.dropna(subset= columns_to_check)
print("Rows after removing rows missing other information:", len(dataset))

columns_to_normalize = ["num_lab_procedures", "num_medications", "num_procedures"]
for column in columns_to_normalize:
    dataset[column]= ((dataset[column] - dataset[column].min()) / (dataset[column].max() - dataset[column].min()))
print(dataset[columns_to_normalize].describe())

a1c_dummies = pd.get_dummies(
    dataset["A1Cresult"],
    prefix="A1C"
).astype(int)

dataset = pd.concat([dataset, a1c_dummies], axis=1)

print(a1c_dummies.head())
print(a1c_dummies.sum())

#descriptive analytics
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

#barchart
a1c_over8 = dataset[dataset["A1Cresult"] == ">8"]

a1c_by_race = a1c_over8["race"].value_counts()

print(a1c_by_race)

a1c_by_race.plot(kind="bar")

plt.title("Number of Patients with A1CResult >8 by Race")
plt.xlabel("Race")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#pie chart

print("\nReadmission categories:")
print(dataset["readmitted"].value_counts())


dataset["readmission_status"] = dataset["readmitted"].apply(
    lambda x: "Not Readmitted" if x == "NO" else "Readmitted"
)

readmitted_only = dataset[
    dataset["readmission_status"] == "Readmitted"
]

gender_readmitted = readmitted_only["gender"].value_counts()

print("\nNumber of Readmitted Patients by Gender:")
print(gender_readmitted)

gender_percent = (
    gender_readmitted / gender_readmitted.sum()
) * 100

print("\nPercentage of Readmitted Patients by Gender:")
print(gender_percent)

plt.figure(figsize=(7, 7))

plt.pie(
    gender_readmitted.values,
    labels=gender_readmitted.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Prevalence of Readmission by Gender")

plt.tight_layout()

plt.show()



#histogram
plt.hist(dataset["length-of-stay"], bins=7)

plt.title("Distribution of Length of Stay")
plt.xlabel("Length of Stay (Days)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()





print("\nFINAL DATASET SHAPE:")
print(dataset.shape)

print("\nMISSING VALUES:")
print(dataset.isnull().sum())

print("\nFIRST FIVE ROWS:")
print(dataset.head())

