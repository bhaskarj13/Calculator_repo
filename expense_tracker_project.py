import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT,
                    amount REAL,
                    description TEXT,
                    date TEXT
                )''')
conn.commit()

# Function to add an expense
def add_expense(category, amount, description, date):
    cursor.execute("INSERT INTO expenses (category, amount, description, date) VALUES (?, ?, ?, ?)",
                   (category, amount, description, date))
    conn.commit()
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    for expense in expenses:
        print(expense)

# Function to get total expenses
def total_expenses():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]
    print(f"Total Expenses: {total if total else 0}")

# Function to filter expenses by category
def filter_expenses_by_category(category):
    cursor.execute("SELECT * FROM expenses WHERE category = ?", (category,))
    expenses = cursor.fetchall()
    for expense in expenses:
        print(expense)

# Menu
def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Filter by Category")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(category, amount, description, date)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expenses()
        elif choice == '4':
            category = input("Enter category to filter: ")
            filter_expenses_by_category(category)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
    
# Close the database connection when done
conn.close()

