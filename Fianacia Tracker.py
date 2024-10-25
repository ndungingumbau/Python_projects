# Financial Tracker
import json

class FinancialTracker:
    def __init__(self):
        self.salary = 0
        self.expenses = {}
        self.savings_goal = 0

    def set_salary(self, salary):
        self.salary = salary
        print(f"Salary set to: ${self.salary}")

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        print(f"Added ${amount} to {category} expenses.")

    def total_expenses(self):
        return sum(self.expenses.values())

    def calculate_savings_rate(self):
        savings = self.salary - self.total_expenses()
        savings_rate = (savings / self.salary) * 100 if self.salary > 0 else 0
        return savings, savings_rate

    def set_savings_goal(self, goal):
        self.savings_goal = goal
        print(f"Savings goal set to: ${self.savings_goal}")

    def financial_advice(self):
        savings, savings_rate = self.calculate_savings_rate()
        print(f"Total Expenses: ${self.total_expenses()}")
        print(f"Savings: ${savings} ({savings_rate:.2f}% of income)")

        advice = []
        if savings_rate < 20:
            advice.append("Consider increasing your savings rate to at least 20% by reducing non-essential expenses.")
        if savings < self.savings_goal:
            advice.append(f"You're ${self.savings_goal - savings} away from your savings goal.")
            advice.append("Try setting aside more each month to reach your goal.")
        else:
            advice.append("Great job! You've met or exceeded your savings goal.")
        
        emergency_fund = self.salary * 3
        if savings < emergency_fund:
            advice.append("Consider building an emergency fund worth 3 months of income for financial security.")
        
        print("\nFinancial Advice:")
        for item in advice:
            print(f"- {item}")

    def save_data(self, filename="financial_data.json"):
        data = {
            "salary": self.salary,
            "expenses": self.expenses,
            "savings_goal": self.savings_goal
        }
        with open(filename, "w") as file:
            json.dump(data, file)
        print("Data saved successfully.")

    def load_data(self, filename="financial_data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
            self.salary = data.get("salary", 0)
            self.expenses = data.get("expenses", {})
            self.savings_goal = data.get("savings_goal", 0)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")

# Example usage
tracker = FinancialTracker()
tracker.set_salary(5000)
tracker.add_expense("Rent", 1200)
tracker.add_expense("Groceries", 500)
tracker.add_expense("Utilities", 200)
tracker.set_savings_goal(1000)
tracker.financial_advice()
tracker.save_data()
