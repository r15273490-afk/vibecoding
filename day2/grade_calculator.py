def get_mark(prompt):
    while True:
        try:
            mark = float(input(prompt))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Error: Mark must be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid numerical value.")

def calculate_grade(average):
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "Fail"

def main():
    print("--- Grade Calculator (Type 'exit' as name to quit) ---")
    
    while True:
        # Step 0: Input Name
        name = input("\nEnter student's name: ").strip()
        
        # Exit condition
        if name.lower() == "exit":
            print("Exiting Grade Calculator. Goodbye!")
            break
            
        # Input 3 marks
        mark1 = get_mark(f"Enter mark 1 for {name}: ")
        mark2 = get_mark(f"Enter mark 2 for {name}: ")
        mark3 = get_mark(f"Enter mark 3 for {name}: ")
        
        # Calculate average
        average = (mark1 + mark2 + mark3) / 3
        
        # Determine grade
        grade = calculate_grade(average)
        
        # Display results in requested format
        print("-" * 30)
        print(f"Name   : {name}")
        print(f"Average: {average:.1f}")
        print(f"Grade  : {grade}")
        print("-" * 30)

if __name__ == "__main__":
    main()
