# Problem Statement:
# Given a class of students and their marks in different subjects:
# 1. Each student has marks in multiple subjects
# 2. Data is provided as a 2D list where:
#    - Each row represents a student
#    - Each column represents a subject
#    - marks[i][j] gives the marks of student i in subject j
# 3. Task: Calculate total marks for each student after removing the subject
#    that has the lowest average marks across all students
#
# Example:
# Input: marks = [
#     [80, 75, 90, 85],  # Student 1's marks in 4 subjects
#     [70, 80, 85, 90],  # Student 2's marks in 4 subjects
#     [85, 65, 95, 88]   # Student 3's marks in 4 subjects
# ]
# If Subject 2 has lowest average: (75 + 80 + 65)/3 = 73.33
# Output: [255, 245, 268]  # Total marks for each student after removing Subject 2

def calculate_student_totals(marks):
    """
    Calculate total marks for each student after removing the subject with lowest average.
    
    Args:
    marks: 2D list where marks[i][j] is the marks of student i in subject j
    
    Returns:
    list: Total marks for each student after removing the subject with lowest average
    """
    N = len(marks)        # number of students (rows)
    M = len(marks[0])     # number of subjects (columns)
    
    # Calculate average for each subject
    subject_averages = []
    for j in range(M):
        subject_total = 0
        for i in range(N):
            subject_total += marks[i][j]
        subject_averages.append(subject_total / N)
    
    # Find subject with lowest average
    min_avg_subject = subject_averages.index(min(subject_averages))
    
    # Calculate total for each student after removing that subject
    student_totals = []
    for i in range(N):
        # Sum all subjects then subtract the marks of lowest average subject
        total = sum(marks[i]) - marks[i][min_avg_subject]
        student_totals.append(total)
    
    return student_totals

# Test the function
if __name__ == "__main__":
    # Test data
    marks = [
        [80, 75, 90, 85],  # Student 1
        [70, 80, 85, 90],  # Student 2
        [85, 65, 95, 88]   # Student 3
    ]
    
    print("Original marks:")
    for i, student_marks in enumerate(marks):
        print(f"Student {i+1}: {student_marks}")
    
    # Calculate and print subject averages
    N = len(marks)
    M = len(marks[0])
    print("\nSubject averages:")
    for j in range(M):
        avg = sum(marks[i][j] for i in range(N)) / N
        print(f"Subject {j+1}: {avg:.2f}")
    
    # Get and print results
    result = calculate_student_totals(marks)
    print("\nTotal marks for each student after removing lowest average subject:")
    for i, total in enumerate(result):
        print(f"Student {i+1}: {total}")
