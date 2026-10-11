def calculate_grade(marks):
    """Calculates the grade based on predefined grading conditions."""
    if marks < 0 or marks > 100:
        return "Invalid Marks"
    elif marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

def main():
    # Suggested Dataset: Manually created student marks
    student_records = {
        "Avanish": 95,
        "Rahul": 82,
        "Priya": 74,
        "Sneha": 65,
        "Amit": 48,
        "InvalidTest": 105
    }

    print("--- Student Grade Calculator ---")
    for name, marks in student_records.items():
        grade = calculate_grade(marks)
        print(f"Student: {name} | Marks: {marks} | Grade: {grade}")

if _name_ == "_main_":
    main()
