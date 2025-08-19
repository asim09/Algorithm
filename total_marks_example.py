def calculate_total_marks(marks, min_avg_subject):
    N = len(marks)  # number of students
    
    print("Step by step calculation:")
    total_marks = []
    for i in range(N):
        all_subjects_total = sum(marks[i])
        mark_to_remove = marks[i][min_avg_subject]
        final_total = all_subjects_total - mark_to_remove
        
        print(f"\nStudent {i+1}:")
        print(f"All subjects total = {all_subjects_total} {marks[i]}")
        print(f"Mark removed (Subject {min_avg_subject + 1}) = {mark_to_remove}")
        print(f"Final total = {final_total}")
        
        total_marks.append(final_total)
    
    return total_marks

# Test data
marks = [
    [80, 75, 90, 85],  # Student 1's marks
    [70, 80, 85, 90],  # Student 2's marks
    [85, 65, 95, 88]   # Student 3's marks
]

min_avg_subject = 1  # Subject 2 has lowest average

print("Original marks:")
for i, student_marks in enumerate(marks):
    print(f"Student {i+1}: {student_marks}")

print("\nCalculating totals after removing subject", min_avg_subject + 1)
result = calculate_total_marks(marks, min_avg_subject)

print("\nFinal results:")
for i, total in enumerate(result):
    print(f"Student {i+1} total (after removing Subject {min_avg_subject + 1}) = {total}")
