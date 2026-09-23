import os
import pandas as pd
from data_validator import validate_data, get_data_summary
from analysis import run_analysis

def home():

    print("Student Performance Analytics")

    if not os.path.exists("student_data.csv"):
        print("Dataset is not present")
        return

    print("Dataset is present")

    file_size = os.path.getsize("student_data.csv") / (1024 * 1024)
    print(f"Dataset Size : {file_size:.2f} MB")

    df = pd.read_csv("student_data.csv")

    validate_data(df)

    data_summary = get_data_summary(df)

    print("\nData Summary")
    print(f"Total Students : {data_summary['Total_Students']}")
    print(f"Average Percentage : {data_summary['Average_Percentage']:.2f}")
    print(f"Top Grade Students : {data_summary['Top_Grade_Students']}")

    run_analysis()


home()