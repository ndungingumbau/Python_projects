import sqlite3
import pandas as pd

# Create SQLite connection
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('inventory.db')
        print("Connection established")
        return conn
    except sqlite3.Error as e:
        print(e)
    return conn

# Create table for inventory
def create_inventory_table(conn):
    query = '''CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sku TEXT NOT NULL,
                name TEXT NOT NULL,
                category TEXT,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL,
                warehouse_location TEXT
            );'''
    conn.execute(query)
    conn.commit()
    print("Inventory table created")

# Add new item to inventory
def add_item(conn, sku, name, category, quantity, price, warehouse_location):
    query = '''INSERT INTO inventory (sku, name, category, quantity, price, warehouse_location) 
               VALUES (?, ?, ?, ?, ?, ?);'''
    conn.execute(query, (sku, name, category, quantity, price, warehouse_location))
    conn.commit()
    print(f"Item {name} added to inventory")

# Update item in inventory
def update_item(conn, sku, quantity):
    query = '''UPDATE inventory SET quantity = ? WHERE sku = ?;'''
    conn.execute(query, (quantity, sku))
    conn.commit()
    print(f"Item {sku} updated with new quantity {quantity}")

# Delete an item from inventory
def delete_item(conn, sku):
    query = '''DELETE FROM inventory WHERE sku = ?;'''
    conn.execute(query, (sku,))
    conn.commit()
    print(f"Item {sku} deleted from inventory")

# Search for an item
def search_item(conn, search_term):
    query = '''SELECT * FROM inventory WHERE name LIKE ? OR sku LIKE ?;'''
    df = pd.read_sql_query(query, conn, params=(f'%{search_term}%', f'%{search_term}%'))
    return df

# Generate a low stock report
def low_stock_report(conn, threshold=10):
    query = '''SELECT * FROM inventory WHERE quantity < ?;'''
    df = pd.read_sql_query(query, conn, params=(threshold,))
    return df

# Main function to handle operations
def main():
    conn = create_connection()
    if conn:
        create_inventory_table(conn)
        
        # Add items to inventory
        add_item(conn, 'SKU123', 'Laptop', 'Electronics', 50, 999.99, 'Aisle 5')
        add_item(conn, 'SKU456', 'Monitor', 'Electronics', 75, 199.99, 'Aisle 3')
        add_item(conn, 'SKU789', 'Keyboard', 'Accessories', 200, 29.99, 'Aisle 7')
        
        # Update an item
        update_item(conn, 'SKU123', 40)
        
        # Search for an item
        search_result = search_item(conn, 'Laptop')
        print("Search Result:\n", search_result)
        
        # Generate low stock report
        low_stock = low_stock_report(conn, 50)
        print("Low Stock Report:\n", low_stock)
        
        # Delete an item
        delete_item(conn, 'SKU789')

        conn.close()

if __name__ == "__main__":
    main()
