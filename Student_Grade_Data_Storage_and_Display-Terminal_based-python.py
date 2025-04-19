class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
        
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("\nStudent Data:")
            print("-" * 40)
            print(f"{'ID':<10}{'Name':<20}{'Grade':<10}")
            print("-" * 40)
            temp_stack = Stack()
            
            while not self.is_empty():
                temp_stack.push(self.pop())
            
            while not temp_stack.is_empty():
                student = temp_stack.pop()
                student_id, name, grade = student
                print(f"{student_id:<10}{name:<20}{grade:<10}")
                self.push(student)
            
            print("-" * 40)

def main():
    student_stack = Stack()
    
    while True:
        print("\nStudent Data Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Remove Last Added Student")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            
            while True:
                try:
                    grade = float(input("Enter Student Grade: "))
                    break
                except ValueError:
                    print("Please enter a valid number for the grade.")
                    
            student_data = [student_id, name, grade]
            student_stack.push(student_data)
            print(f"\nStudent {name} added successfully!")
            
        elif choice == '2':
            student_stack.display()
            
        elif choice == '3':
            if not student_stack.is_empty():
                removed_student = student_stack.pop()
                print(f"\nRemoved student: {removed_student[1]}")
            else:
                print("\nNo students to remove. Stack is empty.")
                
        elif choice == '4':
            print("\nExiting program. Thank you!")
            break
            
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()