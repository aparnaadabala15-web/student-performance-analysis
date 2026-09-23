import pandas as pd

def validate_data(df):

    validation_results = {
        "Total_Students": len(df),
        "Missing_Values": df.isnull().sum().sum(),
        "Duplicate_Students": df["Student_ID"].duplicated().sum(),
        "Invalid_Marks": (
            (df["Maths"] < 0).sum() +
            (df["Science"] < 0).sum() +
            (df["English"] < 0).sum() +
            (df["Social"] < 0).sum() +
            (df["Computer"] < 0).sum()
        ),
        "Data_Types_Valid": True
    }

    expected_types = {
        "Student_ID": "int64",
        "Student_Name": "object",
        "Gender": "object",
        "Age": "int64",
        "Class": "int64",
        "Section": "object",
        "Maths": "int64",
        "Science": "int64",
        "English": "int64",
        "Social": "int64",
        "Computer": "int64",
        "Total_Marks": "int64",
        "Percentage": "float64",
        "Grade": "object",
        "Attendance": "int64",
        "City": "object"
    }

    for col, expected_type in expected_types.items():
        if col in df.columns:
            if str(df[col].dtype) != expected_type:
                validation_results["Data_Types_Valid"] = False
                print(f"Column '{col}' has type {df[col].dtype}, expected {expected_type}")

    issues = (
        validation_results["Missing_Values"] +
        validation_results["Duplicate_Students"] +
        validation_results["Invalid_Marks"]
    )

    if issues == 0 and validation_results["Data_Types_Valid"]:
        print("All validations passed")
    else:
        print(f"{issues} issues found")

    return validation_results


def get_data_summary(df):

    summary = {
        "Total_Students": len(df),
        "Average_Percentage": df["Percentage"].mean(),
        "Highest_Percentage": df["Percentage"].max(),
        "Lowest_Percentage": df["Percentage"].min(),
        "Top_Grade_Students": (df["Grade"] == "A+").sum(),
        "Average_Attendance": df["Attendance"].mean()
    }

    return summary