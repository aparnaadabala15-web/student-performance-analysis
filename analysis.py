import pandas as pd
import matplotlib.pyplot as plt

def run_analysis():

    print("Loading Student Data...")

    df = pd.read_csv("student_data.csv")

    print(f"Loaded {len(df)} records\n")

    # ==============================
    # KEY METRICS
    # ==============================

    print("KEY METRICS")
    print("-" * 30)

    print(f"Total Students : {len(df)}")
    print(f"Average Percentage : {df['Percentage'].mean():.2f}")
    print(f"Highest Percentage : {df['Percentage'].max():.2f}")
    print(f"Lowest Percentage : {df['Percentage'].min():.2f}")
    print(f"Average Attendance : {df['Attendance'].mean():.2f}")

    # ==============================
    # SUBJECT AVERAGES
    # ==============================

    subjects = ["Maths", "Science", "English", "Social", "Computer"]

    averages = [df[sub].mean() for sub in subjects]

    # ==============================
    # DASHBOARD
    # ==============================

    fig, axes = plt.subplots(2,2,figsize=(12,8))

    # Bar Chart
    axes[0,0].bar(subjects, averages)
    axes[0,0].set_title("Average Subject Marks")

    # Pie Chart
    grade_counts = df["Grade"].value_counts()

    axes[0,1].pie(
        grade_counts.values,
        labels=grade_counts.index,
        autopct="%1.1f%%"
    )

    axes[0,1].set_title("Grade Distribution")

    # Histogram
    axes[1,0].hist(df["Percentage"], bins=10)
    axes[1,0].set_title("Percentage Distribution")

    # Scatter Plot
    axes[1,1].scatter(df["Attendance"], df["Percentage"])
    axes[1,1].set_title("Attendance vs Percentage")

    plt.tight_layout()

    plt.savefig("student_dashboard.png")

    plt.show()

    print("\nDashboard Created Successfully")