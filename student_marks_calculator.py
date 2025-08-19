import numpy as np

class StudentMarks:
    @classmethod
    def total_marks_after_ignoring_subject(cls, marks, N, M):
        # Calculate average marks for each subject using loops
        subject_averages = []
        for j in range(M):  # for each subject
            subject_sum = 0
            for i in range(N):  # for each student
                subject_sum += marks[i][j]
            subject_averages.append(subject_sum / N)
        
        # Find subject with minimum average
        min_avg = subject_averages[0]
        min_avg_subject = 0
        for j in range(1, M):
            if subject_averages[j] < min_avg:
                min_avg = subject_averages[j]
                min_avg_subject = j
        
        # Calculate total marks for each student after ignoring the subject with lowest average
        total_marks = []
        for i in range(N):
            total_marks.append(sum(marks[i]) - marks[i][min_avg_subject])
        
        return total_marks

# Example usage
if __name__ == "__main__":
    # Example data: 3 students (N=3) with marks in 4 subjects (M=4)
    example_marks = [
        [80, 75, 90, 85],  # Student 1
        [70, 80, 85, 90],  # Student 2
        [85, 65, 95, 88]   # Student 3
    ]
    N = 3  # number of students
    M = 4  # number of subjects
    
    # Calculate total marks after ignoring the subject with lowest average
    result = StudentMarks.total_marks_after_ignoring_subject(example_marks, N, M)
    
    # Print the results
    print("Original marks for each student:")
    for i, marks in enumerate(example_marks, 1):
        print(f"Student {i}: {marks}")
    
    print("\nTotal marks after ignoring subject with lowest average:")
    for i, total in enumerate(result, 1):
        print(f"Student {i}: {total}")
