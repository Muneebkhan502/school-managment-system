# STUDENT MANAGMENT SYSTEM
# Using json file to store student record
# main menu
# add students
# update marks
# delete student
# display students with complete details
# search student by rollno


import json
import os
FILENAME = 'student.json'
def load_data():
    if not os.path.exists(FILENAME):
        # if file not exist then it  return empty list
        return [] 
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, ValueError):
        return [] # if file name or somthing is wrong then it return empty list and program will not crash

def save_data():
    #Save the global students list to JSON.
    with open(FILENAME, 'w') as f:
        json.dump(students, f, indent=4)
    
students = load_data()



def add_students():
    try:
        name = (input("Enter student name: "))                  # we write all risky code in try block and if any error occur then it will handle by except block
        rollno = (int(input("Enter student rollno: ")))
        marks = (int(input("Enter student marks: ")))

        
    
        for std in students:
            if std["rollno"] == rollno:
                print("student already exist")
                return

        std_dict = {
            "name" : name,
            "rollno" : rollno,
            "marks" : marks
        }

        students.append(std_dict)
        print("Student added successfully.")
        save_data() # after changes it convert students list to json and save in file
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return
  


def update_std():
    try:
        rollno = int(input("Enter student rollno to update: "))
        marks = int(input("Enter student new marks to update: "))
        update_name = input("do you want to update name? (yes/no): ")

        for std in students:
            if std["rollno"] == rollno:
                std["marks"] = marks
                if update_name.lower() == "yes":
                    name = input("Enter student new name to update: ")
                    std["name"] = name
                    print("Student details updated successfully.")
                else:
                    print("Marks updated successfully.")
                    save_data()
                return
            
        print("Not exist")
        

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return



def display_std():
    if not students:
        print("No students to display")
        return
    print("----Students List----")
    print(f"{'Name':<15} {'Roll.No':<10} {'Marks':<10}")
    print("-"*30)
    for std in students:     
        print(f"{std['name']:<15} {std['rollno']:<10} {std['marks']:<10}")
    print("-"*30)

    # Display topper
    marks_list = []
    for std in students:
        marks_list.append(std['marks'])
        max_marks = max(marks_list)
    for std in students:
        if std["marks"] == max_marks:
            print(f"Topper:\t {std['name']} with marks {std['marks']}")

    # Display total number of students
    count = len(students)
    print(f"Total students:\t {count}")

    # Display Pass and Fail students
    # for std in students:
    #     if std['marks'] >= 50:
    #         print(f"{std['name']} is Pass")
    #     else:
    #         print(f"{std['name']} is Fail")

    pass_count = 0
    fail_count = 0
    for std in students:
        if std["marks"] >= 50:
            pass_count += 1
        else:
            fail_count += 1
    print(f"Pass Students:\t {pass_count}")
    print(f"Fail Students:\t {fail_count}")
    print("----- END -----")
    return
def delete_std():
    rollno = int(input("enter rollno to delete: "))
    for std in students:
        if std['rollno']  == rollno:
            print("----Student Detail----")
            print(f"Name: {std['name']} | Marks: {std['marks']}")
            confirm = input("Are you sure you want to delete this student? (yes/no): ")
            if confirm.lower() == "yes":
                students.remove(std)
                print("Student deleted successfully.")
                save_data()
                return
            else:
                print("Deletion cancelled.")
                return      
    print("Student not found! ")       
    

def get_cgpa(marks):
    # Aik dictionary banayein jo marks ki range ko CGPA se map kare
    # Hum search ulta shuru karein ge (highest to lowest)
    
    if marks >= 85: return 4.0
    if marks >= 80: 
        # 80 se 84 tak har marks par 0.1 ka izafa
        return 3.5 + (marks - 80) * 0.1
    if marks >= 75: return 3.0
    if marks >= 70: return 2.5
    if marks >= 60: return 2.0
    if marks >= 51: return 1.5
    return 0.0 # Fail case


def search_std():
    try:
        rollno = int(input("Enter student roll no: "))
        for std in students:
            if std["rollno"] == rollno:
                print("----Student Detail----")
                print(f"Name: {std['name']} | Marks: {std['marks']}")
                
                cgpa = get_cgpa(std['marks'])
                print(f"CGPA:\t {cgpa:.1f}") # .1f se decimal point control hoga
                
                if cgpa == 0.0:
                    print("Status:\t Fail")
                return
        print(f"Student {rollno} not found.")
    except ValueError:
        print("Invalid input.")

# MAIN MENU
print("1: Show all students")    
print("2: Add new students")
print("3: Update students")
print("4: Delete students")
print("5: Search students")
print("6: Exit")


while True:
    try:
        choice = int(input("choose option: "))
        if choice == 1:
            display_std()
        elif choice == 2:
            add_students()
        elif choice == 3:
            update_std()
        elif choice == 4:
            delete_std()
        elif choice == 5:   
            search_std()
        elif choice == 6:
            print("---Exit---")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")