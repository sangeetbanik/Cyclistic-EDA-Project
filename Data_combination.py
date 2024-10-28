-- Combine data from Jan to Dec 2023 into a single table named cyclistic_data on Python.

-- Import all necessary libraries.
import pandas as pd # type: ignore
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats 

--combining all the 12 csv iles into a single csv file.
csv_files = [r"file_path\01-2023.csv" ,r"file_path\02-2023.csv",r"file_path\03-2023.csv",r"file_path\04-2023.csv",r"file_path\05-2023.csv",r"file_path\06-2023.csv",r"file_path\07-2023.csv",r"file_path\08-2023.csv",r"ṅ\09-2023.csv",r"file_path\10-2023.csv",r"file_path\11-2023.csv",r"file_path\12-2023.csv"]
cyclistic_data = pd.concat([pd.read_csv(file) for file in csv_files])
cyclistic_data.reset_index(drop=True, inplace=True)

--saving the new table.
cyclistic_data_path = r"C:\Users\Pratik Banik\Downloads\GDA_Project_1\2023-08 to 2024-08\clean files.csv"
cyclistic_data.to_csv('cyclistic_data_path' ,index=False)
print("CSV files have been successfully combined!")


