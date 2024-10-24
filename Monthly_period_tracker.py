import sqlite3
from datetime import datetime, timedelta

# Create SQLite connection
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('period_tracker.db')
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Create table for period tracking
def create_period_table(conn):
    query = '''CREATE TABLE IF NOT EXISTS period_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                start_date TEXT NOT NULL,
                cycle_length INTEGER NOT NULL,
                cramps_level INTEGER,
                mood TEXT,
                notes TEXT
            );'''
    conn.execute(query)
    conn.commit()

# Add period record
def add_period_record(conn, start_date, cycle_length, cramps_level, mood, notes):
    query = '''INSERT INTO period_data (start_date, cycle_length, cramps_level, mood, notes) 
               VALUES (?, ?, ?, ?, ?);'''
    conn.execute(query, (start_date, cycle_length, cramps_level, mood, notes))
    conn.commit()
    print("Period record added")

# Calculate next period based on cycle length
def calculate_next_period(last_start_date, cycle_length):
    last_start_date = datetime.strptime(last_start_date, '%Y-%m-%d')
    next_period_date = last_start_date + timedelta(days=cycle_length)
    return next_period_date.strftime('%Y-%m-%d')

# Get all period records
def get_period_records(conn):
    query = '''SELECT * FROM period_data;'''
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    return records

# Track cramps and other symptoms
def log_cramps_and_symptoms(conn):
    start_date = input("Enter the start date of your period (YYYY-MM-DD): ")
    cycle_length = int(input("Enter your average cycle length in days: "))
    cramps_level = int(input("Rate your cramps on a scale of 1 to 10: "))
    mood = input("Describe your mood (e.g., happy, irritable, sad): ")
    notes = input("Any additional notes or symptoms: ")
    
    add_period_record(conn, start_date, cycle_length, cramps_level, mood, notes)
    
    next_period = calculate_next_period(start_date, cycle_length)
    print(f"Based on your average cycle length, your next period is expected on: {next_period}")

# Display period history
def display_period_history(conn):
    records = get_period_records(conn)
    if not records:
        print("No period records found.")
    else:
        print(f"{'ID':<5} {'Start Date':<12} {'Cycle Length':<14} {'Cramps Level':<14} {'Mood':<12} {'Notes'}")
        for record in records:
            print(f"{record[0]:<5} {record[1]:<12} {record[2]:<14} {record[3]:<14} {record[4]:<12} {record[5]}")
    
# Main function
def main():
    conn = create_connection()
    if conn:
        create_period_table(conn)
        
        while True:
            print("\n--- Period Tracker Menu ---")
            print("1. Log a new period and symptoms")
            print("2. View period history")
            print("3. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                log_cramps_and_symptoms(conn)
            elif choice == '2':
                display_period_history(conn)
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

        conn.close()

if __name__ == "__main__":
    main()
