#Create a Dictionary of Student Marks

students_marks = {'Prash': 95, 'Pradeep': 85, 'Khushi': 99, 'Ayush': 99, 'Riyansh': 97}
a= input("Enter the Students name: ")

if a in students_marks:
    print(a,"'s marks: ", students_marks[a] )

else:
    print("Student not found")


