Def_init_(self,name,roll_number,cgpa):
self.name=name
self.roll_number=roll_number
self.cgpa=cgpa
Def sort_student(student_list):
#sort the list of students in desending order of cgpa
sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
#syntax_lambda arg:exp
return sorted_students
#example usage:
students=[
  student("stephen","A123",7.8),
  student("harini","A124",8.9),
  student("ragavi","A125",8.9),
  student("deepa","A126",9.9),
]
sorted_students=sort_student(students)
#print the sorted list of students
for students in sorted sorted_students:
print("Nmae:{},roll number:{}.cgpa{}".format(students.name,students.roll_number,students.cgpa))