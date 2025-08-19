def calculate_student_totals(marks):
    """
    Example marks data:
    marks = [
        [80, 75, 90, 85],  # Student 1
        [70, 80, 85, 90],  # Student 2
        [85, 65, 95, 88]   # Student 3
    ]
    """
    N = len(marks)        # N = 3 students (rows)
    M = len(marks[0])     # M = 4 subjects (columns)
    
    # Part 1: Calculate average for each subject
    subject_averages = []
    for j in range(M):    # j goes from 0 to 3 (each subject)
        subject_total = 0
        for i in range(N):    # i goes from 0 to 2 (each student)
            subject_total += marks[i][j]
            
            # Iteration explanation for finding subject averages:
            # When j = 0 (First Subject):
            #   i = 0: subject_total += marks[0][0] = 80 (Student 1's mark)
            #   i = 1: subject_total += marks[1][0] = 70 (Student 2's mark)
            #   i = 2: subject_total += marks[2][0] = 85 (Student 3's mark)
            #   Average = 235/3 = 78.33
            
            # When j = 1 (Second Subject):
            #   i = 0: subject_total += marks[0][1] = 75 (Student 1's mark)
            #   i = 1: subject_total += marks[1][1] = 80 (Student 2's mark)
            #   i = 2: subject_total += marks[2][1] = 65 (Student 3's mark)
            #   Average = 220/3 = 73.33 (lowest average)
            
            # When j = 2 (Third Subject):
            #   i = 0: subject_total += marks[0][2] = 90 (Student 1's mark)
            #   i = 1: subject_total += marks[1][2] = 85 (Student 2's mark)
            #   i = 2: subject_total += marks[2][2] = 95 (Student 3's mark)
            #   Average = 270/3 = 90.00
            
            # When j = 3 (Fourth Subject):
            #   i = 0: subject_total += marks[0][3] = 85 (Student 1's mark)
            #   i = 1: subject_total += marks[1][3] = 90 (Student 2's mark)
            #   i = 2: subject_total += marks[2][3] = 88 (Student 3's mark)
            #   Average = 263/3 = 87.67
            
        subject_averages.append(subject_total / N)
    
    # Find subject with lowest average (Subject 1 in this case)
    min_avg_subject = subject_averages.index(min(subject_averages))
    
    # Part 2: Calculate total for each student after removing lowest average subject
    student_totals = []
    for i in range(N):    # i goes from 0 to 2 (each student)
        # For each student:
        # 1. sum(marks[i]) gets total of all subjects
        # 2. marks[i][min_avg_subject] gets their mark in the lowest average subject
        # 3. Subtract to get final total
        
        # When i = 0 (Student 1):
        #   All subjects = 80 + 75 + 90 + 85 = 330
        #   Remove Subject 2 mark = 75
        #   Final total = 330 - 75 = 255
        
        # When i = 1 (Student 2):
        #   All subjects = 70 + 80 + 85 + 90 = 325
        #   Remove Subject 2 mark = 80
        #   Final total = 325 - 80 = 245
        
        # When i = 2 (Student 3):
        #   All subjects = 85 + 65 + 95 + 88 = 333
        #   Remove Subject 2 mark = 65
        #   Final total = 333 - 65 = 268
        
        total = sum(marks[i]) - marks[i][min_avg_subject]
        student_totals.append(total)
    
    return student_totals

# Test the function
if __name__ == "__main__":
    marks = [
        [80, 75, 90, 85],  # Student 1
        [70, 80, 85, 90],  # Student 2
        [85, 65, 95, 88]   # Student 3
    ]
    
    print("Original marks:")
    for i, student_marks in enumerate(marks):
        print(f"Student {i+1}: {student_marks}")
    
    # Calculate and show subject averages
    N = len(marks)
    M = len(marks[0])
    print("\nSubject averages:")
    for j in range(M):
        avg = sum(marks[i][j] for i in range(N)) / N
        print(f"Subject {j+1}: {avg:.2f}")
    
    # Calculate and show final totals
    result = calculate_student_totals(marks)
    print("\nTotal marks after removing lowest average subject:")
    for i, total in enumerate(result):
        print(f"Student {i+1}: {total}")
