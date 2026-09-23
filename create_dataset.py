import pandas as pd
import random

# Number of students
num_students = 1000

# Student names
names = [
    "Aparna", "Rahul", "Sneha", "Arjun", "Priya",
    "Kiran", "Sai", "Anjali", "Rohit", "Divya"
]

# Cities
cities = [
    "Hyderabad",
    "Vizag",
    "Vijayawada",
    "Guntur",
    "Rajahmundry"
]

print("Dataset generator started...")

students = []

for i in range(1, num_students + 1):

    student_id = 1000 + i
    name = random.choice(names)
    gender = random.choice(["Male", "Female"])
    age = random.randint(15, 18)
    student_class = random.choice([8, 9, 10])
    section = random.choice(["A", "B", "C"])

    maths = random.randint(35, 100)
    science = random.randint(35, 100)
    english = random.randint(35, 100)
    social = random.randint(35, 100)
    computer = random.randint(35, 100)

    attendance = random.randint(75, 100)
    city = random.choice(cities)

    total_marks = maths + science + english + social + computer
    percentage = round(total_marks / 5, 2)

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    students.append({
        "Student_ID": student_id,
        "Student_Name": name,
        "Gender": gender,
        "Age": age,
        "Class": student_class,
        "Section": section,
        "Maths": maths,
        "Science": science,
        "English": english,
        "Social": social,
        "Computer": computer,
        "Total_Marks": total_marks,
        "Percentage": percentage,
        "Grade": grade,
        "Attendance": attendance,
        "City": city
    })

df = pd.DataFrame(students)

df.to_csv("student_data.csv", index=False)

print("Student dataset created successfully!")
print(f"Total Records: {len(df)}")
print("File saved as student_data.csv")