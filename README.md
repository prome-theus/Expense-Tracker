# 💰 Expense Tracker

A beginner-friendly command-line Expense Tracker built with Python.  
The application lets you record, view, search, summarize, and delete expenses, with automatic JSON data storage.

## ✨ Features

- Add expenses with name, amount, category, and date
- View all recorded expenses
- Calculate total spending
- Search expenses by category
- View spending totals by category
- Delete expenses
- Automatically save data to `expenses.json`
- Input validation for amounts and menu choices
- Uses only Python's standard library

## 🛠️ Technologies

- Python 3
- JSON
- File handling
- Functions
- Lists and dictionaries
- `datetime`
- Command-line interface (CLI)

## 📁 Project Structure

```text
expense-tracker/
├── main.py
├── expenses.json
├── README.md
├── requirements.txt
└── .gitignore
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/expense-tracker.git
```

### 2. Open the project

```bash
cd expense-tracker
```

### 3. Run the application

```bash
python main.py
```

On some Windows systems, you can also use:

```bash
py main.py
```

## 🧪 Example

```text
==========================================
           EXPENSE TRACKER
==========================================
1. Add Expense
2. View Expenses
3. Show Total Spending
4. Search by Category
5. Spending by Category
6. Delete Expense
7. Exit
==========================================
Enter your choice: 1

--- Add Expense ---
Enter expense name: Coffee
Enter amount: ₹120
Enter category: food
Expense added successfully!
```

## 💾 Data Storage

Expenses are stored locally in `expenses.json`.  
The program loads this file when it starts and saves it whenever an expense is added or deleted.

## 🚀 Future Improvements

- Monthly and yearly spending reports
- Budget limits and alerts
- Export data to CSV
- Graphs and charts
- GUI using Tkinter
- SQLite database
- Unit tests

## 👨‍💻 Author

**Your Name**

Replace `Your Name` with your name before publishing the project.
