class StudentMarksAnalysis:
    def __init__(self, marks):
        """
        Initialize with marks data
        marks: 2D list where each row is a student and each column is a subject
        """
        self.marks = marks
        self.students = len(marks)  # number of rows
        self.subjects = len(marks[0])  # number of columns
    
    def get_subject_totals(self):
        """Calculate total marks for each subject"""
        subject_totals = []
        # Loop through each subject (column)
        for i in range(self.subjects):
            total = 0
            # Add marks of all students for this subject
            for j in range(self.students):
                total += self.marks[j][i]
            subject_totals.append(total)
        return subject_totals
    
    def get_subject_averages(self):
        """Calculate average marks for each subject"""
        totals = self.get_subject_totals()
        return [total/self.students for total in totals]
    
    def find_lowest_average_subject(self):
        """Find the subject with lowest average marks"""
        averages = self.get_subject_averages()
        return averages.index(min(averages))
    
    def get_student_totals_after_removing_subject(self):
        """
        Calculate total marks for each student after removing 
        the subject with lowest average
        """
        min_avg_subject = self.find_lowest_average_subject()
        student_totals = []
        
        for i in range(self.students):
            # Calculate total for student i after removing the subject
            total = sum(self.marks[i]) - self.marks[i][min_avg_subject]
            student_totals.append(total)
        
        return student_totals, min_avg_subject
    
    def print_detailed_analysis(self):
        """Print complete analysis of marks"""
        # 1. Subject-wise totals
        subject_totals = self.get_subject_totals()
        print("\nSubject-wise Total Marks:")
        for i, total in enumerate(subject_totals):
            print(f"Subject {i+1}: {total}")
        
        # 2. Subject-wise averages
        averages = self.get_subject_averages()
        print("\nSubject-wise Averages:")
        for i, avg in enumerate(averages):
            print(f"Subject {i+1}: {avg:.2f}")
        
        # 3. Student totals after removing lowest average subject
        student_totals, removed_subject = self.get_student_totals_after_removing_subject()
        print(f"\nAfter removing Subject {removed_subject + 1} (lowest average):")
        for i, total in enumerate(student_totals):
            print(f"Student {i+1} Total: {total}")

def main():
    # Example marks data: 3 students, 4 subjects
    marks = [
        [80, 75, 90, 85],  # Student 1's marks
        [70, 80, 85, 90],  # Student 2's marks
        [85, 65, 95, 88]   # Student 3's marks
    ]
    
    print("Original Marks:")
    for i, student_marks in enumerate(marks):
        print(f"Student {i+1}: {student_marks}")
    
    # Create analyzer object and run analysis
    analyzer = StudentMarksAnalysis(marks)
    analyzer.print_detailed_analysis()

if __name__ == "__main__":
    main()
