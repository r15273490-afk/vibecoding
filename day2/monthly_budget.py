def get_number(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.lower() == 'done':
            return 'done'
        try:
            val = float(user_input)
            if val < 0:
                print("Error: Value cannot be negative. Please enter a positive number.")
                continue
            return val
        except ValueError:
            print("Error: Please enter a valid number or 'done' to exit.")

def main():
    print("--- Monthly Budget Program ---")
    
    while True:
        # Step 1: Get Total Budget
        total_budget = get_number("\nEnter total monthly budget (or type 'done' to exit): ")
        if total_budget == 'done':
            print("Exiting Budget Program. Goodbye!")
            break
            
        # Step 2: Get 3 Expenses
        expenses = []
        for i in range(1, 4):
            exp = get_number(f"Enter expense {i}: ")
            if exp == 'done':
                print("Exiting Budget Program. Goodbye!")
                return
            expenses.append(exp)
            
        # Step 3: Calculate remaining balance
        total_expenses = sum(expenses)
        balance = total_budget - total_expenses
        
        # Step 4: Display Results
        print("-" * 30)
        print(f"Total Budget: {total_budget:.2f} LKR")
        print(f"Total Expenses: {total_expenses:.2f} LKR")
        
        if balance < 0:
            print(f"Remaining Balance: 0.00 LKR")
            print(f"Warning: You are in debt! (Exceeded by {abs(balance):.2f} LKR)")
        else:
            print(f"Remaining Balance: {balance:.2f} LKR")
            if balance < 500:
                print("Warning: Low funds!")
        print("-" * 30)

if __name__ == "__main__":
    main()
