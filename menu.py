# from services import StudentManager
# from models import Person, Student
# print("------------------------------Student Management System----------------------------------------------")
       
# student_manager = StudentManager()
# while True:
#     print("-------------------------------Menu----------------------------------------------")
#     print("1. Add Student")
#     print("2. Update Student")
#     print("3. Delete Student")
#     print("4. Search Student")
#     print("5. Show All Students")
#     print("6. Exit")

#     choice = input("Enter your choice: ")
#     try:
#         if choice == '1':
#             first = input("Enter first name: ")
#             last = input("Enter last name: ")
#             grade = input("Enter grade: ")
#             rollno = (input("Enter roll number: "))
#             marks = int(input("Enter marks: "))
#             first = first.strip()
#             last = last.strip()
#             grade = grade.strip()
#             if 0 <= marks <= 100:
#                 student = Student(first, last, grade, rollno, marks)
#                 student_manager.add_student(student)
#             else:
#                 print("Marks must be in between 0 & 100")
            
#     except ValueError:
#         print("Invalid input. Please enter the correct data type.")
#     except ValueError:
#         print("An error occurred.")

#     try:
#         if choice == '2':
#             rollno = (input("Enter rollno of student to update  marks/name: "))
#             ask = input("Do you to update student  name or marks ? yes/no: ")
#             if ask.lower() == "yes":
#                 new_name_first  = input("Enter new first name or press enter to keep current: ")
#                 new_name_last  = input("Enter new last name or press enter to keep current: ")
#                 marks_input = input("enter new marks to update or press enter to keep current: ")
#                 new_marks = int(marks_input) if marks_input else None
#                 student_manager.update_student(rollno,new_marks,new_name_first if new_name_first else None,new_name_last if new_name_last else None)   
#             elif ask.lower() == "no":
#                 print("Cancel operations")
#             else:
#                 print("Invaild input")
#     except ValueError:
#         print("Invalid input. Please enter the correct data type.")
#     except:
#         print("An error occurred.")
#     try:
#         if choice == '3':
#             rollno = (input("Enter roll number to delete: "))
#             student_manager.delete_student(rollno)
#     except ValueError:
#         print("Invalid input. Please enter the correct data type.")
#     try:
#         if choice == '4':
#             rollno = (input("Enter roll number to search: "))
#             student_manager.search_student(rollno)
#     except ValueError:
#         print("Invalid input. Please enter the correct data type.")
#     try:
#         if choice == '5':
#             student_manager.show_student()
#     except ValueError:
#         print("An error occurred.")
    
#     if choice == '6':
#         print("Exiting...")
#         break