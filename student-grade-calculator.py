# Function to calculate the grade based on the score
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Main function to input scores and calculate grades
def main():
    print("Student Grade Calculator")

    # Input the number of students
    num_students = int(input("Enter the number of students: "))

    # Initialize an empty dictionary to store student names and scores
    student_scores = {}

    # Input student names and scores
    for i in range(num_students):
        student_name = input(f"Enter the name of Student {i+1}: ")
        student_score = float(input(f"Enter the score for {student_name} (out of 100): "))
        student_scores[student_name] = student_score

    # Display grades for each student
    print("\nGrades:")
    for student_name, student_score in student_scores.items():
        grade = calculate_grade(student_score)
        print(f"{student_name}: {grade}")

if __name__ == "__main__":
    main()
