def subject_totals(marks):
    students = len(marks)     # rows = 3
    subjects = len(marks[0])  # columns = 4
    
    totals = []
    # i loops through subjects (columns 0 to 3)
    for i in range(subjects):
        total = 0
        # j loops through students (rows 0 to 2)
        for j in range(students):
            total += marks[j][i]
            # When i = 0 (First Subject):
            #   j = 0: marks[0][0] = 80 (Student 1's mark in Subject 1)
            #   j = 1: marks[1][0] = 70 (Student 2's mark in Subject 1)
            #   j = 2: marks[2][0] = 85 (Student 3's mark in Subject 1)
            #   total for Subject 1 = 235
            
            # When i = 1 (Second Subject):
            #   j = 0: marks[0][1] = 75 (Student 1's mark in Subject 2)
            #   j = 1: marks[1][1] = 80 (Student 2's mark in Subject 2)
            #   j = 2: marks[2][1] = 65 (Student 3's mark in Subject 2)
            #   total for Subject 2 = 220
            
            # When i = 2 (Third Subject):
            #   j = 0: marks[0][2] = 90 (Student 1's mark in Subject 3)
            #   j = 1: marks[1][2] = 85 (Student 2's mark in Subject 3)
            #   j = 2: marks[2][2] = 95 (Student 3's mark in Subject 3)
            #   total for Subject 3 = 270
            
            # When i = 3 (Fourth Subject):
            #   j = 0: marks[0][3] = 85 (Student 1's mark in Subject 4)
            #   j = 1: marks[1][3] = 90 (Student 2's mark in Subject 4)
            #   j = 2: marks[2][3] = 88 (Student 3's mark in Subject 4)
            #   total for Subject 4 = 263
            
        totals.append(total)  # Add the total for current subject to our list
    
    return totals

# Test with example data
if __name__ == "__main__":
    marks = [
        [80, 75, 90, 85],  # Student 1's marks in 4 subjects
        [70, 80, 85, 90],  # Student 2's marks in 4 subjects
        [85, 65, 95, 88]   # Student 3's marks in 4 subjects
    ]
    
    result = subject_totals(marks)
    
    # Print results
    for i, total in enumerate(result):
        print(f"Subject {i+1}: Total = {total}")
        # Output will be:
        # Subject 1: Total = 235 (80 + 70 + 85)
        # Subject 2: Total = 220 (75 + 80 + 65)
        # Subject 3: Total = 270 (90 + 85 + 95)
        # Subject 4: Total = 263 (85 + 90 + 88)
